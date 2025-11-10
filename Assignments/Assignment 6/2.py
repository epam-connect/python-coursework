# Create a sender and receiver methods and show the communication using Pipes
from multiprocessing import Process, Pipe
import time

def send(conn):
    time.sleep(2)
    conn.send("Hello from sender")
    conn.close()

def recieve(conn):
    print("Reciever waiting for messages..")
    print(conn.recv())
    print("Message received")
    conn.close()

if __name__ == "__main__":
    sender_con, reciever_con = Pipe()
    sender_con.send
    reciever_con.recv
    sender = Process(target=send, args=(sender_con,))
    reciever = Process(target=recieve, args=(reciever_con,))
    
    sender.start()
    reciever.start()
