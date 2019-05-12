import pytest
from core.kafka_server import KafkaServer


class TestKafkaServer:

    @pytest.fixture
    def server(self):
        return KafkaServer()

    def test_publish_message_exception(self, server):
        with pytest.raises(Exception) as e:
            server.publish_message(producer='dummy_producer', topic='dummy_topic', value='dummy_value')

    def test_publish_message(self, server, mocker):
        mock_producer = mocker.patch('core.kafka_server.KafkaProducer')
        server.publish_message(producer=mock_producer, topic='dummy_topic', value='dummy_value')
        mock_producer.send.called
