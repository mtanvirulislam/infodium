spark-submit --master spark://spark-master:7077 --deploy-mode client \
--driver-java-options -Dconfig.resource=application.conf \
--conf spark.driver.host=spark-master \
--conf spark.driver.bindAddress=0.0.0.0 \
--conf "spark.driver.extraJavaOptions=-Dlog4j.configuration=log4j.properties" \
--conf "spark.executor.extraJavaOptions=-Dlog4j.configuration=log4j.properties" \
--conf "spark.driver.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true" \
--conf "spark.executor.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true" \
--class infodium.spark.InfodiumSpark  \
/opt/infodium-spark-job-1.0-jar-with-dependencies.jar