
# A Solution to the TCP Kafka Producer Challenge

## How to Run
- Install the packages in the requirement.txt
- Run tcp_kafka_producer

```
Usage: tcp_kafka_producer.py [OPTIONS]

  Entry point for the Kafka TCP Stream Forwarder.

Options:
  -k, --kafka TEXT      Kafka host:ip to forward to.
  -t, --topic TEXT      Topic for messages.  [required]
  -i, --interface TEXT  Listen on this interface.  [required]
  -p, --port INTEGER    Listen for client connections on this port.
                        [required]
  --help                Show this message and exit.
  ```




