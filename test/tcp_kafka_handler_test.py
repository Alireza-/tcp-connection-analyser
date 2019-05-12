from core.tcp_kafka_handler import SimpleTcpServer


class TestTcpKafkaHandler:
    HOST = '127.0.0.1'
    PORT = 12345

    def test_server_handler_interface(self, mocker):
        mocker_kafka_tcp_handler = mocker.patch('core.tcp_kafka_handler.KafkaTCPHandler')
        server = SimpleTcpServer((self.HOST, self.PORT), mocker_kafka_tcp_handler)
        assert server.server_address[0] == '127.0.0.1'
        assert server.server_address[1] == 12345
