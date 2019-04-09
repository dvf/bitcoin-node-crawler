import asyncio
import socket
from collections import deque

from loguru import logger


class Crawler:
    def __init__(self):
        self.all_hosts = set()
        self.ordered_hosts = deque()

    async def get_dns_hosts(self, dns_seeds):
        """
        Fetches Bitcoin DNS seeds and adds them to the host set
        """
        logger.info("Populating hosts from DNS seeds")
        loop = asyncio.get_event_loop()

        for dns_seed in dns_seeds:
            hosts = await loop.getaddrinfo(*dns_seed, proto=socket.IPPROTO_TCP)

            logger.info(f"Found {len(hosts)} hosts from {dns_seed[0]}")

            for host in hosts:
                self.all_hosts.add(host[4][0])

        logger.info(f"Known hosts: {len(self.all_hosts)}")

    async def contact_host(self, host, port):
        pass

    @staticmethod
    async def tcp_client(host, port, message):
        reader, writer = await asyncio.open_connection(host, port)
        writer.write(message.encode())

        # Tweak the MTU to your connection to make this faster
        data = await reader.read(128)
        if data:
            logger.info(f"Data received from {host}:{port}: {data.decode()}")
        else:
            logger.info(f"Nothing received from {host}:{port}, closing...")
            writer.close()
            return
