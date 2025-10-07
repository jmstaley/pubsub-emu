# Migrated to codeberg

This is now archived here and moved to codeberg

https://codeberg.org/jmstaley/pubsub-emu

---

Simple container to run gcloud pubsub emulator and automatically create topic for a single project

env vars needed:

 - `PUBSUB_EMULATOR_HOST=0.0.0.0:8432` - host and port of the running emulator
 - `PUBSUB_PROJECT_ID=test-project` - project id
 - `PUBSUB_TOPICS=test:testing` - list of topics ":" separated
