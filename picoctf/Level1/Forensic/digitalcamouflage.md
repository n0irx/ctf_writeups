# Digital Camouflage

1. Open data.pcap with wireshark
2. Because it's connected to login system, so it may be a http post request
3. Search for HTTP in the search bar
4. Identify all the logs, we have a username and a password in there
5. The password is based on base64, convert it using terminal

```bash
echo "hrKQSSLWvG" | base64 -D
```
