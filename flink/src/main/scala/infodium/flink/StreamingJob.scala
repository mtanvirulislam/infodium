package infodium.flink

import infodium.flink.FlinkDDL._
import infodium.flink.FlinkDML._
import org.apache.flink.streaming.api.scala._
import org.apache.flink.table.api._
import org.apache.flink.table.api.bridge.scala.tableConversions
import org.apache.flink.types.Row

object StreamingJob {
  def main(args: Array[String]) {

    // environment configuration
    val settings = EnvironmentSettings
      .newInstance()
      .inStreamingMode()
      .build()

    val tEnv = TableEnvironment.create(settings)
    /**
      * Execute queries
      */
    // Create inpute table
    tEnv.executeSql(kafkaTable)
    tEnv.executeSql(eventTypeTable)
    tEnv.executeSql(gameInfoTable)

    // Create output table
    tEnv.executeSql(eventsTable)
    tEnv.executeSql(eventsOccureciesTable)
    tEnv.executeSql(mostOffensiveTeamsTable)
    tEnv.executeSql(mostOffensivePlayersTable)

    // Insert data to output table
    tEnv.executeSql(eventsInfoInsert)
    tEnv.executeSql(eventsOccureciesInsert)
    tEnv.executeSql(mostOffensiveTeamsInsert)
    tEnv.executeSql(mostOffensivePlayersInsert)


  }
}
