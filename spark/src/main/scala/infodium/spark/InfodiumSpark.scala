package infodium.spark

import com.typesafe.config.ConfigFactory
import org.apache.spark.sql.{SaveMode, SparkSession}
import org.apache.spark.sql.functions.{avg, count, lit}
// import org.elasticsearch.spark.sql
 import org.elasticsearch.spark.sql.sparkDatasetFunctions

import java.util.Properties

object InfodiumSpark {

  def main(args: Array[String]): Unit = {

    /**
      * Get configuration
      */
    val rootConfig = ConfigFactory.load("application.conf").getConfig("app")
    // S3
    val s3AccessKey = rootConfig.getString("s3.access_key")
    val s3SecretKey = rootConfig.getString("s3.secret_key")
    val s3Endpoint = rootConfig.getString("s3.endpoint")
    // MySql
    val mysqlEndpoint = rootConfig.getString("mysql.endpoint")
    val mysqlUser = rootConfig.getString("mysql.user")
    val mysqlPassword = rootConfig.getString("mysql.password")

    val mysqlProperties = new Properties()
    mysqlProperties.put("user", mysqlUser)
    mysqlProperties.put("password", mysqlPassword)


    val spark: SparkSession = SparkSession.builder()
      //.master("local[1]")
      .appName("SparkByExamples.com")
      .getOrCreate()

    import spark.implicits._

    // Set s3 configuration
    spark.conf.set("fs.s3a.endpoint", s3Endpoint)
    spark.conf.set("fs.s3a.access.key", s3AccessKey)
    spark.conf.set("fs.s3a.secret.key", s3SecretKey)
    spark.conf.set("spark.es.nodes", "elasticsearch")
    spark.conf.set("es.port", "9200")
    spark.conf.set("es.index.auto.create", "true")
    spark.conf.set("es.nodes.wan.only", "true" )

    val events = spark.read.json("s3a://raw-data/topics/football/")
/*
    val events =
      spark.read
        .format("org.apache.spark.sql.execution.datasources.v2.json.JsonDataSourceV2")
        .load("s3a://raw-data/topics/football/")


 */
    val shotEvents = events.filter($"event_type" === 1)

    // MySql info
    val database = "football"
    val shotPlaceTable = "shot_place"
    val gameInfoTable = "game_info"

    val shotPlace = spark.read.option("driver", "com.mysql.jdbc.Driver").jdbc(mysqlEndpoint, s"$database.$shotPlaceTable", mysqlProperties)
    val gameInfo = spark.read.option("driver", "com.mysql.jdbc.Driver").jdbc(mysqlEndpoint, s"$database.$gameInfoTable", mysqlProperties)

    val shotPlaceGrouped =
      shotEvents.join(
        shotPlace,
        events("shot_place") === shotPlace("id")
      ).select(shotPlace("shot_place")).groupBy("shot_place").count()

    //shotPlaceGrouped.show()

    val goalNoGoal =
      shotEvents.join(
       gameInfo,
        shotEvents("id_odsp") === gameInfo("id_odsp")
      ).withColumn("hola", lit(1)
      ).groupBy("is_goal", "country")count()

    goalNoGoal.show()
/*
    goalNoGoal.coalesce(1).write
      .mode(SaveMode.Overwrite)
      .format("org.apache.spark.sql.execution.datasources.v2.json.JsonDataSourceV2")
      .save("s3a://processed-data/goal-no-goal")
*/
    goalNoGoal.coalesce(1).write.mode(SaveMode.Overwrite).json("s3a://processed-data/goal-no-goal")
    goalNoGoal.saveToEs("goal_no_goal")

  }
}
