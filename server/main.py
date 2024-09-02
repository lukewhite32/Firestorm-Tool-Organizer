import os.path
import socket
from request import Request

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(("127.0.0.1", 8080))

data = ""
while 1:
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    data = conn.recv(4096)
    req = Request(data)
    req.parseType()
    req.parseFileDirectory()
    if req.type == "GET":
        print("Ye")
        if not os.path.exists(req.fileDirectory[1:]):
            conn.send(bytes("HTTP/1.1 404 Not Found\r\nServer: webserver-c\r\nContent-type: text/html\r\nContent-Length: 109\r\n\r\n<!DOCTYPE html><html><head><title>404 not found</title></head><body><h1>404 Not Found</h1><p>404 Not Found</p></body></html>\r\n", "utf-8"))
        else:
            file = open(req.fileDirectory[1:], "r")
            lines = file.readlines()
            allLines = ""
            for l in lines:
                allLines += l
            contentType = "text/html"
            send = "HTTP/1.1 200 OK\r\nContent-type:" + contentType + "\r\nContent-Length: " + str(len(allLines)) + "\r\n\r\n" + allLines
            conn.send(bytes(send, "utf-8"))
