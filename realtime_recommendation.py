# -*- coding: utf-8 -*-
"""realtime_recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ckBug9892fprbFSgshFfZJqMOBji6eaX
"""

from kafka import KafkaProducer, KafkaConsumer
import json
import time

def generate_recommendations():
    """
    Generates recommendations based on user activity and sends them to a Kafka topic.
    """
    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    # Simulate user activity
    while True:
        # Assume user activity data is received from the web application
        user_activity = {
            'user_id': 123,
            'action': 'play',  # Example action, can be 'play', 'like', 'skip', etc.
            'track_id': 456
        }

        # Send user activity data to Kafka topic
        producer.send('user_activity', value=user_activity)
        print("User activity sent to Kafka:", user_activity)

        # Sleep for a while before generating next recommendation
        time.sleep(10)  # Adjust sleep time as needed

def main():
    # Generate recommendations
    generate_recommendations()

if __name__ == '__main__':
    main()