from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer("numbertest", bootstrap_servers=['10.177.17.31:9092'])
consumer = KafkaConsumer(
    'numtest',
    bootstrap_servers=['10.177.17.31:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print(message)
