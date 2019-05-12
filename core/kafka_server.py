import logging
from kafka import KafkaProducer


class KafkaServer:
    """
    This class is generic class for instantiating producer and publishing messages.
    """

    def __init__(self, conf=None):
        self.logger = logging.getLogger(__name__)
        self.conf = conf

    def get_producer(self):
        """
        Instantiate a producer.

        :return: obj
        """
        # set the default bootstrap server if none is defined
        if self.conf is None:
            self.conf = {
                'bootstrap_servers': ['localhost:9092']
            }

        return KafkaProducer(**self.conf)

    def publish_message(self, producer, topic, value):
        """
        Publishes messages to the specified topic.

        :param producer: kafka producer
        :type producer: object
        :param topic: kafka topic
        :type topic: str
        :param value: message to be published.
        :type value: str
        :return: none
        """
        try:
            value_bytes = bytes(value, encoding='utf-8')
            producer.send(topic=topic, value=value_bytes)
            producer.flush()
            self.logger.info('Message published successfully.')
        except Exception as ex:
            self.logger.error(ex)
            raise Exception
