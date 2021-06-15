package infodium.flink

object FlinkDDL {
  val kafkaTable =
    s"""
       |CREATE TABLE raw_events (
       |    id_odsp       STRING,
       |    id_event      STRING,
       |    sort_order    STRING,
       |    `time`        STRING,
       |    text          STRING,
       |    event_type    BIGINT,
       |    event_type2   STRING,
       |    side          STRING,
       |    event_team    STRING,
       |    opponent      STRING,
       |    player        STRING,
       |    player2       STRING,
       |    player_in     STRING,
       |    player_out    STRING,
       |    shot_place    STRING,
       |    shot_outcome  STRING,
       |    is_goal       STRING,
       |    location      STRING,
       |    bodypart      STRING,
       |    assist_method STRING,
       |    situation     STRING,
       |    fast_break    STRING,
       |    event_time    TIMESTAMP(3),
       |    proctime AS   PROCTIME(),
       |    WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
       |) WITH (
       |    'connector' = 'kafka',  -- using kafka connector
       |    'topic' = 'football',  -- kafka topic
       |    'scan.startup.mode' = 'earliest-offset',  -- reading from the beginning
       |    'properties.bootstrap.servers' = 'kafka:29092',  -- kafka broker address
       |    'format' = 'json'  -- the data format is json
       |)
      """.stripMargin

  // MySql Event type table
  val eventTypeTable: String =
    s"""
       |CREATE TABLE event_type (
       |    id BIGINT,
       |    event_type STRING
       |) WITH (
       |    'connector' = 'jdbc',
       |    'url' = 'jdbc:mysql://mysql:3306/football',
       |    'table-name' = 'event_type',
       |    'username' = 'root',
       |    'password' = '123456',
       |    'lookup.cache.max-rows' = '5000',
       |    'lookup.cache.ttl' = '60min'
       |)
      """.stripMargin

  // MySql game information table
  val gameInfoTable: String =
    Predef.augmentString(
      s"""
         |CREATE TABLE game_info (
         |    id_odsp   STRING,
         |    link_odsp STRING,
         |    adv_stats BIGINT,
         |    `date`    STRING,
         |    league    STRING,
         |    season    BIGINT,
         |    country   STRING,
         |    ht        STRING,
         |    `at`      STRING,
         |    fthg      BIGINT,
         |    ftag      BIGINT,
         |    odd_h     DOUBLE,
         |    odd_d     DOUBLE,
         |    odd_a     DOUBLE,
         |    odd_over  DOUBLE,
         |    odd_under DOUBLE,
         |    odd_bts   DOUBLE,
         |    odd_bts_n DOUBLE
         |) WITH (
         |    'connector' = 'jdbc',
         |    'url' = 'jdbc:mysql://mysql:3306/football',
         |    'table-name' = 'game_info',
         |    'username' = 'root',
         |    'password' = '123456',
         |    'lookup.cache.max-rows' = '5000',
         |    'lookup.cache.ttl' = '60min'
         |)
      """).stripMargin

  // Events Elasticsearch index
  val eventsTable: String =
    Predef.augmentString(
      s"""
         |CREATE TABLE events (
         |    country  STRING,
         |    league   STRING,
         |    `match`  STRING,
         |    text     STRING,
         |    `time`   STRING,
         |    proctime TIMESTAMP_LTZ(3)
         |) with (
         |    'connector' = 'elasticsearch-7', -- using elasticsearch connector
         |    'hosts' = 'http://elasticsearch:9200',  -- elasticsearch address
         |    'index' = 'events'
         |)
      """).stripMargin

  // Count of events occurecies Elasticsearch index
  val eventsOccureciesTable: String =
    Predef.augmentString(
      s"""
         |CREATE TABLE events_occurecies (
         |    event_type  STRING,
         |    `time`      STRING,
         |    event_count BIGINT
         |) with (
         |    'connector' = 'elasticsearch-7', -- using elasticsearch connector
         |    'hosts' = 'http://elasticsearch:9200',  -- elasticsearch address
         |    'index' = 'events_occurecies'
         |)
      """).stripMargin

  // Most offensive teams Elasticsearch index
  val mostOffensiveTeamsTable: String =
    Predef.augmentString(
      s"""
         |CREATE TABLE most_offensive_teams (
         |    team    STRING,
         |    goal    BIGINT
         |) with (
         |    'connector' = 'elasticsearch-7', -- using elasticsearch connector
         |    'hosts' = 'http://elasticsearch:9200',  -- elasticsearch address
         |    'index' = 'most_offensive_teams'
         |)
      """).stripMargin

  // Most offensive players Elasticsearch index
  val mostOffensivePlayersTable: String =
    Predef.augmentString(
      s"""
         |CREATE TABLE most_offensive_players (
         |    player  STRING,
         |    goal    BIGINT
         |) with (
         |    'connector' = 'elasticsearch-7', -- using elasticsearch connector
         |    'hosts' = 'http://elasticsearch:9200',  -- elasticsearch address
         |    'index' = 'most_offensive_players'
         |)
      """).stripMargin

}
