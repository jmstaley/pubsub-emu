import os
import time
import socket
# copied from here https://github.com/googleapis/python-pubsub/blob/master/samples/snippets/publisher.py#L43


def create_topic(project_id, topic_id):
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    topic = publisher.create_topic(request={"name": topic_path})


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


if __name__ == "__main__":
    project_id = os.environ["PUBSUB_PROJECT_ID"]
    # topics should be ':' separated
    topics = os.environ["PUBSUB_TOPICS"]

    host, port = os.environ["PUBSUB_EMULATOR_HOST"].split(":")

    while not is_open(host, port):
        print("Waiting for pubsub ...")
        time.sleep(1)

    for topic in topics.split(":"):
        create_topic(project_id, topic)
        print(f"created topic: {topic}")
