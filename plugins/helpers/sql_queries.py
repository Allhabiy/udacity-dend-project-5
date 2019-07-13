class SqlQueries:
    # MODIFIED SQL queries:
    songplay_table_insert = ("""
        SELECT DISTINCT TIMESTAMP 'epoch' + se.ts/1000 * INTERVAL '1 second'   AS start_time,
            se.userId                   AS user_id,
            se.level                    AS level,
            ss.song_id                  AS song_id,
            ss.artist_id                AS artist_id,
            se.sessionId                AS session_id,
            se.location                 AS location,
            se.userAgent                AS user_agent
        FROM staging_events AS se
        JOIN staging_songs AS ss
        ON (se.artist = ss.artist_name
            AND se.artist = ss.artist_name
            AND se.length = ss.duration)
        WHERE se.page = 'NextSong';
    """)

    songplay_table_insert_not_working = ("""
        SELECT DISTINCT TIMESTAMP 'epoch' + se.ts/1000 * INTERVAL '1 second'   AS start_time,
            md5(se.sessionid)           AS songplay_id,
            se.userId                   AS user_id,
            se.level                    AS level,
            ss.song_id                  AS song_id,
            ss.artist_id                AS artist_id,
            se.sessionId                AS session_id,
            se.location                 AS location,
            se.userAgent                AS user_agent
        FROM staging_events AS se
        JOIN staging_songs AS ss
        ON (se.artist = ss.artist_name
            AND se.artist = ss.artist_name
            AND se.length = ss.duration)
        WHERE se.page = 'NextSong';
    """)

    user_table_insert = ("""
        SELECT  DISTINCT se.userId      AS user_id,
            se.firstName                AS first_name,
            se.lastName                 AS last_name,
            se.gender                   AS gender,
            se.level                    AS level
        FROM staging_events AS se
        WHERE se.page = 'NextSong';
    """)

    song_table_insert = ("""
        SELECT  DISTINCT ss.song_id     AS song_id,
            ss.title                    AS title,
            ss.artist_id                AS artist_id,
            ss.year                     AS year,
            ss.duration                 AS duration
        FROM staging_songs AS ss;
    """)

    artist_table_insert = ("""
        SELECT  DISTINCT ss.artist_id   AS artist_id,
            ss.artist_name              AS name,
            ss.artist_location          AS location,
            ss.artist_latitude          AS latitude,
            ss.artist_longitude         AS longitude
        FROM staging_songs AS ss;
    """)

    time_table_insert = ("""
        SELECT  DISTINCT TIMESTAMP 'epoch' + se.ts/1000 * INTERVAL '1 second'        AS start_time,
            EXTRACT(hour FROM start_time)    AS hour,
            EXTRACT(day FROM start_time)     AS day,
            EXTRACT(week FROM start_time)    AS week,
            EXTRACT(month FROM start_time)   AS month,
            EXTRACT(year FROM start_time)    AS year,
            EXTRACT(week FROM start_time)    AS weekday
        FROM    staging_events               AS se
        WHERE se.page = 'NextSong';
    """)
    # -------------------------------------------------------
    # ORIGINAL SQL Queries:
    songplay_table_insert_orig = ("""
        SELECT
            md5(events.sessionid || events.start_time) songplay_id,
            events.start_time,
            events.userid,
            events.level,
            songs.song_id,
            songs.artist_id,
            events.sessionid,
            events.location,
            events.useragent
            FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
        FROM staging_events
        WHERE page='NextSong') events
        LEFT JOIN staging_songs songs
        ON events.song = songs.title
            AND events.artist = songs.artist_name
            AND events.length = songs.duration
    """)

    user_table_insert_orig = ("""
        SELECT distinct userid, firstname, lastname, gender, level
        FROM staging_events
        WHERE page='NextSong'
    """)

    song_table_insert_orig = ("""
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_insert_orig = ("""
        SELECT distinct artist_id, artist_name, artist_location, artist_latitude, artist_longitude
        FROM staging_songs
    """)

    time_table_insert_orig = ("""
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time),
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM songplays
    """)
