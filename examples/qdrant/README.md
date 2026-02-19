# Qdrant Load Testing with Locust

Simple example demonstrating load testing for Qdrant vector database operations.

## Prerequisites

Install Locust with Qdrant support:

```bash
# Using pip
pip install locust[qdrant]

# Using uv
uv add locust[qdrant]
# or
uv sync --extra qdrant
```

This installs the required dependencies:

- [`qdrant-client`](https://github.com/qdrant/qdrant-client) - Official Qdrant Python SDK

## Usage

```bash
# Navigate to this directory
cd examples/qdrant
```

```bash
# Run Qdrant
docker run -p 6333:6333 -d qdrant/qdrant
```

```bash
# Run headless
locust -f locustfile.py --host=http://localhost:6333 --headless --users=10 --spawn-rate=2 --run-time=60s

# Run with web UI
locust -f locustfile.py --host=http://localhost:6333
```

## Operations Tested

- Upsert points
- Search points
- Scroll points
- Delete points

For more advanced usage, see the [Locust documentation](https://docs.locust.io/).
