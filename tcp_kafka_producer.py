from core.tcp_kafka_handler import SimpleTcpServer, KafkaTCPHandler
import logging.config
import click

logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)


@click.command()
@click.option('-k', '--kafka', default='localhost:9092', help='Kafka host:ip to forward to.')
@click.option('-t', '--topic', help='Topic for messages.', required=True)
@click.option('-i', '--interface', help='Listen on this interface.', required=True)
@click.option('-p', '--port', type=int, help='Listen for client connections on this port.', required=True)
def run(kafka, topic, interface, port):
    """
    Entry point for the Kafka TCP Stream Forwarder.

    """
    conf = {
        'bootstrap_servers': [kafka]
    }

    server = SimpleTcpServer((interface, port), KafkaTCPHandler)
    server.conf = conf
    server.topic = topic
    server.serve_forever()


if __name__ == "__main__":
    run()
