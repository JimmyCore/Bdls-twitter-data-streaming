from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'twitter_twt',
    bootstrap_servers=['10.177.17.31:9092'])

for message in consumer:
    print(message.value)
