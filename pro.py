from time import sleep  
from json import dumps  
from kafka import KafkaProducer  
import pandas as pd 

# initializing the Kafka producer  
producer = KafkaProducer(bootstrap_servers=['3.8.91.110:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

producer.send('topic-stock', value= "{'name':'tato'}")
