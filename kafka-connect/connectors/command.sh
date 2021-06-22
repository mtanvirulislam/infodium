echo -e "\n--\n+> Creating Data Generator source"
curl -s -X PUT -H  "Content-Type:application/json" http://localhost:8083/connectors/s3-sink/config \
    -d '{
    "connector.class":"io.confluent.connect.s3.S3SinkConnector",
    "tasks.max":"1",
    "topics":"football",
    "store.url": "http://s3-storage:4566",
    "s3.bucket.name":"raw-data",
    "s3.region":"us-east-1",
    "s3.part.size":"5242880",
    "flush.size":"100000",
    "key.converter":"org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable":"false",
    "value.converter":"org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable":"false",
    "storage.class":"io.confluent.connect.s3.storage.S3Storage",
    "format.class":"io.confluent.connect.s3.format.json.JsonFormat",
    "schema.compatibility":"NONE",
    "partitioner.class":"io.confluent.connect.storage.partitioner.DailyPartitioner",
    "locale":"en",
    "timezone":"UTC",
    "path.format":"'year'=YYYY/'month'=MM/'day'=dd",
    "partition.duration.ms":"3600000",
    "rotate.interval.ms":"60000",
    "timestamp.extractor":"Record"
}'