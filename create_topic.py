# copied from here https://github.com/googleapis/python-pubsub/blob/master/samples/snippets/publisher.py#L43

def create_topic(project_id, topic_id):
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    topic = publisher.create_topic(request={"name": topic_path})

if __name__ == "__main__":
    import os

    project_id = os.environ["PUBSUB_PROJECT_ID"]
    # topics should be ':' separated
    topics = os.environ["PUBSUB_TOPICS"]

    for topic in topic.split(":"):
        create_topic(project_id, topic)
