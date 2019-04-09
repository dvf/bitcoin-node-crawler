# Bitcoin Node Crawler [WIP]

1. Install the dependencies
    ```bash
    poetry install
    ```
2. Run the crawler
    ```bash
    poetry shell
    python example.py
    ```

```bash
 ◰³ bitcoin-node-crawler-py3.7  ~/P/bitcoin-node-crawler  python example.py                                                                                                                                  2.6m  Tue Apr  9 01:37:24 2019


███████╗██╗   ██╗███╗   ██╗ █████╗ ██████╗ ███████╗███████╗
██╔════╝╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗ ╚████╔╝ ██╔██╗ ██║███████║██████╔╝███████╗█████╗
╚════██║  ╚██╔╝  ██║╚██╗██║██╔══██║██╔═══╝ ╚════██║██╔══╝
███████║   ██║   ██║ ╚████║██║  ██║██║     ███████║███████╗
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝

⚡ synapse 0.1.3

Listening on 127.0.0.1:9999

Registered Endpoints:

Background Tasks:
- get_dns_hosts (3600s)
- report_total_hosts (60s)


2019-04-09 01:37:25.238 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:18 - Populating hosts from DNS seeds
2019-04-09 01:37:25.240 | INFO     | __main__:report_total_hosts:35 - Total hosts: 0
2019-04-09 01:37:25.254 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:24 - Found 25 hosts from seed.bitcoin.sipa.be
2019-04-09 01:37:25.293 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:24 - Found 21 hosts from dnsseed.bluematt.me
2019-04-09 01:37:25.296 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:24 - Found 24 hosts from dnsseed.bitcoin.dashjr.org
2019-04-09 01:37:25.417 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:24 - Found 25 hosts from seed.bitcoinstats.com
2019-04-09 01:37:25.420 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:24 - Found 24 hosts from seed.bitcoin.jonasschnelli.ch
2019-04-09 01:37:25.423 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:24 - Found 23 hosts from seed.btc.petertodd.org
2019-04-09 01:37:25.423 | INFO     | bitcoin_node_crawler.crawler:get_dns_hosts:29 - Known hosts: 141
2019-04-09 01:38:25.239 | INFO     | __main__:report_total_hosts:35 - Total hosts: 141
```
