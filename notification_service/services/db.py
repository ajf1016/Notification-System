# services/db.py
from cassandra.cluster import Cluster
from sqlalchemy.orm import Session
from models import engine, SessionLocal

# PostgreSQL Connection


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Cassandra Connection
CASSANDRA_HOSTS = ["cassandra_db"]
CASSANDRA_KEYSPACE = "notifications"


def get_cassandra_session():
    """ Get a Cassandra session """
    cluster = Cluster(CASSANDRA_HOSTS)
    session = cluster.connect()
    session.set_keyspace("my_keyspace")  # Replace with your actual keyspace
    return session
