import os

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings


def main():
    # Create streaming environment
    env = StreamExecutionEnvironment.get_execution_environment()

    settings = EnvironmentSettings.new_instance() \
        .in_streaming_mode() \
        .use_blink_planner() \
        .build()

    # create table environment
    tbl_env = StreamTableEnvironment.create(stream_execution_environment=env,
                                            environment_settings=settings)

    # add kafka connector dependency
    kafka_jar = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             'flink-sql-connector-kafka_2.11-1.13.0.jar')

    tbl_env.get_config() \
        .get_configuration() \
        .set_string("pipeline.jars", "file://{}".format(kafka_jar))

    #######################################################################
    # Create Kafka Source Table with DDL
    #######################################################################
    src_ddl = """
        CREATE TABLE tweets (
            tweet_id BIGINT,
            text VARCHAR(4000),
            proctime AS PROCTIME()
        ) WITH (
            'connector' = 'kafka',
            'topic' = 'twitter_twt',
            'properties.bootstrap.servers' = 'localhost:9092',
            'properties.group.id' = 'twitter_twt',
            'format' = 'json'
        )
    """

    tbl_env.execute_sql(src_ddl)

    # create and initiate loading of source Table
    tbl = tbl_env.from_path('tweets')

    print('\nSource Schema')
    tbl.print_schema()

    #####################################################################
    # Define Tumbling Window Aggregate Calculation (Seller Sales Per Minute)
    #####################################################################
    sql = """
        SELECT * FROM tweets
    """
    revenue_tbl = tbl_env.sql_query(sql)

if __name__ == '__main__':
    main()
