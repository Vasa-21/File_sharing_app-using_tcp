# This file is used for sending the file over socket
import os
import socket
import time
##from security import encrypt
from compressor import *
from hashing import *
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
formate="utf-8"
class server():
    def __init__(self,parent):
        self.parent=parent
        self.transfer()
        self.window=Toplevel()
        self.window.geometry('300x300')
        self.display()
    def trans(self):
        name=compress([self.file_name])
        self.file_size = os.path.getsize(name)
       
        # Sending file_name and detail.
        print(hash_file(self.file_name))
        self.client.send(self.file_name.encode(formate))
        self.client.recv(100).decode(formate)
        
        self.client.send(str(self.file_size).encode(formate))
        self.client.recv(100).decode(formate)
        
        self.client.send(hash_file(self.file_name).encode(formate))
        self.client.recv(100).decode(formate)
        
        with open(name, "rb") as file:
            c = 0
            # Starting the time capture.
            start_time = time.time()

            # Running loop while c != file_size.
            while c <= self.file_size:
                data = file.read(1024)
                
                if not data:
                    self.client.send(data)
                    break
                enc_data =data
                
                self.client.send(enc_data)
                c += len(data)

            # Ending the time capture.
            end_time = time.time()
        self.tt=end_time - start_time
        print("File Transfer Complete.Total time: ", end_time - start_time)
        
    # Creating a socket.
    def transfer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 22222))
        sock.listen(1)
        print("Host Name: ", sock.getsockname())
        n,p=sock.getsockname()
        showinfo("",f"Host Name\n{n}")

        # Accepting the connection.
        self.client, addr = sock.accept()

        # Getting file details.
        self.file_name =askstring('', 'enter the file name')
        # Opening file and sending data.
        self.trans()
        # Cloasing the socket.
        sock.close()
    def display(self):
        Label(self.window,text=f"File Name:{self.file_name }\n").pack()
        Label(self.window,text=f"File Size:{self.file_size}\n").pack()
        Label(self.window,text=f"File Transfer Completed.\n\nTotal time taken: {self.tt}").pack()
def sender():
    win=Tk()
    win.withdraw()
    c=server(win)
    win.mainloop()
sender()
