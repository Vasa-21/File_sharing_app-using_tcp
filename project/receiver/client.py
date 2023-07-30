# This file will be used for recieving files over socket connection.

import socket
import time
from compressor import *
from hashing import *
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
formate="utf-8"
class client():
    def __init__(self,parent):
        self.error=0
        self.parent=parent
        self.receive()
        self.window=Toplevel()
        self.window.geometry('300x300')
        self.display()
    def rec(self):
        # Send file details.
        self.filename =self.sock.recv(100).decode(formate)
        self.sock.send("y".encode(formate))
        
        self.file_size = self.sock.recv(100).decode(formate)
        self.sock.send("y".encode(formate))
        
        self.file_hash = self.sock.recv(100).decode(formate)
        self.sock.send("y".encode(formate))
        
        with open("./rec/compressed.tar.gz", "wb") as file:  
            c = 0
            start_time = time.time()    # Starting the time capture.
            
            
            while c != int(self.file_size):  # Running the loop while file is recieved.
        
                data = self.sock.recv(1024)
                dec_data = data
                file.write(dec_data)
                c += len(dec_data)

            # Ending the time capture.
        end_time = time.time()
        
        self.tt=end_time - start_time
        decompress('rec/folder')
        print(self.filename)
        a='rec/folder/'+str(self.filename)
        if hash_file(a)==self.file_hash:
            self.error=1
            print("no error detected")
        else:
            print("error detected")
    def receive(self):
        host = askstring('get input', 'HOST Name')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:         # Trying to connect to socket.
            self.sock.connect((host, 22222))
            print("Connected Successfully")
        except:
            print("Unable to connect")
            exit(0)
            
        self.rec()
       
        self.sock.close()     # Closing the socket.
    def display(self):
        Label(self.window,text=f"File Name:{self.filename }\n").pack()
        Label(self.window,text=f"File Size:{self.file_size}\n").pack()
        Label(self.window,text=f"File Transfer Completed.\n\nTotal time taken: {self.tt}").pack()
        if self.error==1:
            Label(self.window,text="No Error detected").pack()
        else:
            Label(self.window,text="Error detected").pack()
def receiver():
    win=Tk()
    win.withdraw()
    c=client(win)
    win.mainloop()
