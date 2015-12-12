__author__ = 'kinkazma'
import socket
import tkinter
import select
import time
from threading import Thread

class Client(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip
        self.running = 1
        self.soc=0


    def run(self):

        PORT = 8090
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("[-]Etape socket conection")
        try:
            self.soc.connect((self.ip, PORT))
        except:
            print("[-]Connection Impossible")
            self.running=0

def ChargeOther(box,message,who="Server"):
    if message != "" and message != "\n" and message != 0:
        box.config(state=tkinter.NORMAL)
        texte = "{0} :> {1}".format(who,message)
        box.insert(tkinter.END, texte)
        box.config(state=tkinter.DISABLED)
        box.yview('end')

class ReloadEntry(Thread):
        def __init__(self,box,clien):
            Thread.__init__(self)
            self.message=""
            self.box=box
            self.clients=clien
            self.data=""



        def run(self):
            while self.clients.running:
                time.sleep(0.5)
                self.clients.soc.setblocking(0)
                pret=select.select([self.clients.soc],[],[],0.4)
                if pret[0]:
                    self.data=self.clients.soc.recv(1024).decode()
                print("[-] Message:",self.data)
                if self.message!=self.data :
                    self.message=self.data
                    ChargeOther(self.box,self.message)













