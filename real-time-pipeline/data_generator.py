from faker import Faker
import json
import time
import random
import boto3

# Faker & Kinesis setup
fake = Faker()
kinesis = boto3.client("kinesis", region_name="us-east-1")

while True:
    order = {
        "order_id": fake.uuid4(),
        "product": random.choice(["Laptop", "Mobile", "Shoes", "Watch"]),
        "price": round(random.uniform(100, 2000), 2),
        "quantity": random.randint(1, 5),
        "city": fake.city(),
        "timestamp": fake.iso8601()
    }

    # Send to Kinesis
    kinesis.put_record(
        StreamName="orders-stream",
        Data=json.dumps(order),
        PartitionKey="1"
    )

    print("Sent:", order)
    time.sleep(1)