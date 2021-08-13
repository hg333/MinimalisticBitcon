# MinimalisticBitcon
Minimalistic Bitcoin is a very small implementation of Bitcoin. 

I wrote it to have a better understanding of the Bitcoin protocol at low-level

## Quick Start
* Clone the repository. ```git clone https://github.com/hg333/MinimalisticBitcon.git```
* Execute connection.py file ```python3 connection.py```

That's it, you have a very tiny, very limited bitcoin-node working at port 8333 of your machine.

## P2P-Network

![image](https://user-images.githubusercontent.com/44291592/129307527-927dc17c-4022-4466-bf14-c9d68cd5eb0b.png)

The network between two nodes is estavlished via handshake demonstrated above.

* The Version Message
* The Verack Message

## Other Messages Used
* Addr
* Ping
* Pong
* Inv

For more refer [Messages](https://en.bitcoin.it/wiki/Protocol_documentation#Message_types)
## Configurations
### Version
Default version is set to ***70002***, can be changed by editing the respective variable in connection.py

```
version = struct.pack("i", 70002)
```

### Host
By defalt the application tries connecting to the node at address ***24.64.72.164:8333***.

```
HOST = "24.64.72.174"
PORT = 8333
```

For connecting to other nodes find a stable node at [bitnodes](https://bitnodes.io/)

## References
* [Mastering Bitcoin](https://www.oreilly.com/library/view/mastering-bitcoin/9781491902639/ch06.html)
* [Protocol Documentation](https://en.bitcoin.it/wiki/Protocol_documentation)
* [Developer Guides](https://developer.bitcoin.org/devguide/index.html)
* [Bitcoins the hard way](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)
* [Mybitcoin](https://github.com/zeltsi/Mybitcoin)
