import abc
import queue
import threading
import socket
import logging
import BSGPythonSDK.models.redemption as redemption_model


class BSGPythonSDK(abc.ABC):
    LOG_HANDLE = "BSGPythonSDK"

    def __init__(self, host: str = "127.0.0.1", port: int = 29175):
        self._host = host
        self._port = port
        self._listen_thread: threading.Thread = None
        self._running = False

        self.logger = logging.getLogger(self.LOG_HANDLE)

        self._event_queue = queue.Queue()

        self.start()

    def start(self):
        self._running = True
        self._listen_thread = threading.Thread(target=self._listen_process, name="BSGProxyListener", daemon=True)
        self._listen_thread.start()

    def get_port(self) -> int:
        return self._port

    def get_host(self) -> str:
        return self._host

    def is_running(self) -> bool:
        return self._running

    def kill(self):
        self._running = False

    def _listen_process(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self._host, self._port))
        sock.listen()

        self.logger.info("Listening for TCP/IP Connections On {}:{}".format(self._host, self._port))

        while self._running:
            s, addr = sock.accept()

            threading.Thread(
                target=self.new_connection, args=(s, addr), daemon=True, name="TCP Listen {}".format(addr)
            ).start()

            self.logger.info("Received TCP/IP Connection From {}:{}".format(*addr))

    def new_connection(self, sock, addr):
        while self._running:
            try:
                request: bytes = sock.recv(1024)
                if request.replace(b" ", b"") != b"":
                    r = redemption_model.Redemption.from_json(request.decode("UTF-8"))
                    self._event_queue.put(r)

                    self.logger.debug("Received redemption request for command '{}' from '{}'".format(
                        r.get_command(), r.get_guest()
                    ))

                sock.send("null\n".encode("utf8"))

            except ConnectionError:
                self.logger.warning("Lost TCP/IP Connection From {}:{}".format(*addr))
                break

    def poll(self, *args, **kwargs):
        if not self._event_queue.empty():
            redemption = self._event_queue.get()
            self.on_redemption_received(redemption, *args, **kwargs)
            self.get_event(redemption).execute(*args, **kwargs)

    def on_redemption_received(self, redemption, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_event(self, redemption):
        pass
