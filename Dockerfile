FROM google/cloud-sdk:latest

COPY start-pubsub .

EXPOSE 8432

ENTRYPOINT ["./start-pubsub"]
