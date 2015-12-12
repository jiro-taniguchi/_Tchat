__author__ = 'kinkazma'
import socket
import select
import time
import tkinter
from threading import Thread





class Serveur(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.boucle = 1
        self.data=0
        self.envoi=0

    def run(self):
        PORT = 8090
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[-]Creation du socket")
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", PORT))
        print("[-]Bindage du socket")
        s.listen(5)
        print("[-]Mise a l'écoute")
        client_conecter=[]

        


        while self.boucle:
            time.sleep(0.01)


            client_demande, wlist, xlist = select.select([s],[],[],0.1)

            for client in client_demande:

                client_conect,info = client.accept()

                print("[+] Client reçus :{0}".format(info))
                client_conecter.append(client_conect)
                self.envoi=client_conect



            client_a_lire, wilist, xelist= select.select(client_conecter, [], [], 0.1)


            for client in client_a_lire:

                self.data=client.recv(1024)
                if self.data == b'fin':
                    client.close()
                    client_conecter.remove(client)

                if self.data != "\n" and self.data!= "":
                    for pigeon in client_conecter:
                        if pigeon != client:
                            pigeon.send(self.data)
                    print("[+] Message : {0}".format(self.data.decode()))





        s.close()

def ChargeOther(box,message,who="Client"):
    if message != "" and message != "\n" and message != 0:
        box.config(state=tkinter.NORMAL)
        texte = "{0} :> {1}".format(who,message)
        box.insert(tkinter.END, texte)
        box.config(state=tkinter.DISABLED)
        box.yview('end')

class ReloadEntry(Thread):
        def __init__(self,box,serv):
            Thread.__init__(self)
            self.message=""
            self.box=box
            self.server=serv

        def run(self):
            while self.server.boucle:
                time.sleep(0.5)
                if self.message!=self.server.con :
                    self.message=self.server.con
                    ChargeOther(self.box,self.message)












