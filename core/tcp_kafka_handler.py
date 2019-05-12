import socketserver
import logging
from kafka_server import KafkaServer

logger = logging.getLogger(__name__)


class KafkaTCPHandler(socketserver.BaseRequestHandler):
    """
    This class extends BaseRequestHandler and override and customise the handle method.
    """

    def handle(self):
        """
        Override the handel method and send the message to kafka.

        :return: none
        """
        # self.request is the client connection
        data = self.request.recv(1024)
        text = data.decode('utf-8')
        kafka_server = KafkaServer(self.server.conf)
        kafka_server.publish_message(producer=kafka_server.get_producer(), topic=self.server.topic, value=text)
        self.request.send('OK'.encode('utf-8'))
        self.request.close()


class SimpleTcpServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    Simple TCP Server.
    """
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
