import socket
import threading

from loguru import logger


class TCP:
    host = "localhost"
    port = 1235

    def __init__(self, host, port):
        """
        Example:
        >>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        >>> s.connect((socket.gethostname(), 1235))
        >>> s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        >>> msg = s.recv(1024)
        >>> print(msg.decode("utf-8"))
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        thread = threading.Thread(target=self.c2s, daemon=True)

        self.host = host
        self.port = port
        self.sock = s
        self.thread = thread

    def launce_server(self):
        logger.info("[ Launching server ]")

        self.sock.bind((self.host, self.port))
        # self.sock.listen()

        self.thread.start()
        while self.thread.is_alive():
            try:
                self.thread.join()
            except KeyboardInterrupt:
                logger.info("keyboard interrupt")
                break
            except Exception as err:
                logger.error(err)
                break

    def close(self):
        try:
            self.sock.close()
            logger.info("socket was closed")
        except Exception as err:
            logger.error(err)
        finally:
            logger.info("[ Close server ]")

    def c2s(self):
        """called with threading"""

        try:
            while True:
                clientsocket, address = self.sock.recvfrom(1024)
                logger.info(f"Connection from {address} has been established!")
                self.sock.sendto(bytes("Welcome to the UDP server!", "utf-8"), address)
        except ConnectionAbortedError:
            ...
        except OSError:
            ...
        except Exception as err:
            logger.error(err)
            logger.error(type(err))


def main():
    p2p = TCP("localhost", 1235)
    try:
        p2p.launce_server()
    finally:
        p2p.close()


if __name__ == '__main__':
    main()
