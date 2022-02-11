import pandas as pd
import matplotlib.pyplot as plt
import json

from kafka import KafkaConsumer
from matplotlib.animation import FuncAnimation


consumer = KafkaConsumer(
    'twitter_twt',
    bootstrap_servers=['localhost:9092'])

dataFrame = pd.DataFrame(columns=['id', 'text', 'timestamp'])

for msg in consumer:
    m = json.loads(msg.value)
    dataFrame = dataFrame.append(m, ignore_index=True)
    print(m)
    break



    print(m)
