package infodium.flink

object FlinkDML {
  // Events info
  val eventsInfoInsert: String =
    s"""
       |INSERT INTO events
       |SELECT
       |    gi.country,
       |    gi.league,
       |    CONCAT(gi.ht, ' vs ', gi.`at`) `match`,
       |    re.text,
       |    re.`time`,
       |    proctime
       |FROM raw_events AS re
       |INNER JOIN game_info AS gi ON re.id_odsp = gi.id_odsp
      """.stripMargin

  // Count of events occurecies
  val eventsOccureciesInsert: String =
    s"""
       |INSERT INTO events_occurecies
       |SELECT
       |    event_type.event_type,
       |    raw_events.`time`,
       |    COUNT(*) event_count
       |FROM raw_events
       |INNER JOIN event_type ON raw_events.event_type = event_type.id
       |GROUP BY event_type.event_type, raw_events.`time`
      """.stripMargin

  // Most offensive teams
  val mostOffensiveTeamsInsert: String =
    s"""
       |INSERT INTO most_offensive_teams
       |SELECT
       |    event_team AS team,
       |    COUNT(*) goal
       |FROM raw_events
       |WHERE is_goal = '1'
       |GROUP BY event_team
      """.stripMargin

  // Most offensive players
  val mostOffensivePlayersInsert: String =
    s"""
       |INSERT INTO most_offensive_players
       |SELECT
       |    player,
       |    COUNT(*) goal
       |FROM raw_events
       |WHERE is_goal = '1'
       |GROUP BY player
      """.stripMargin
}
