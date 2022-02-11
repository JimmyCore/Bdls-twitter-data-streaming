from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'twitter_twt',
    bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(message.value)
