FROM google/cloud-sdk:latest

RUN pip3 install google-cloud-pubsub pytz

COPY start-pubsub .
COPY create_topic.py .

EXPOSE 8432

ENTRYPOINT ["./start-pubsub"]
