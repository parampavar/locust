"""
Minimal example demonstrating Qdrant load testing with Locust.
"""

from locust import between, task
from locust.contrib.qdrant import QdrantUser

import random

from qdrant_client.models import Distance, PointStruct, VectorParams


class SimpleQdrantUser(QdrantUser):
    """Minimal Qdrant user for load testing."""

    wait_time = between(1, 3)

    def on_start(self):
        self.dimension = 128
        self.test_vectors = [[random.random() for _ in range(self.dimension)] for _ in range(10)]

    collection_name = "load_test_collection"
    vectors_config = VectorParams(
        size=128,
        distance=Distance.COSINE,
    )

    def __init__(self, environment):
        self.url = environment.host
        super().__init__(environment)

    @task(3)
    def upsert_data(self):
        points = [
            PointStruct(
                id=random.randint(1, 10000),
                vector=[random.random() for _ in range(self.dimension)],
                payload={"name": f"item_{random.randint(1, 1000)}"},
            )
        ]
        self.upsert(points)

    @task(5)
    def search_vectors(self):
        search_vector = random.choice(self.test_vectors)
        self.search(query=search_vector, limit=5)

    @task(2)
    def scroll_data(self):
        self.scroll(limit=5)

    @task(1)
    def delete_data(self):
        delete_id = random.randint(1, 10000)
        self.delete(points_selector=[delete_id])
