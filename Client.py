__author__ = 'kinkazma'
import tkinter
import Threadclient
global ip, port
Clients = Threadclient.Client("127.0.0.1")
Clients.start()

def toot():
    print(" Bonjoure")
def Action(*args):
    saisie = Entrybox.get("0.0", tkinter.END)

    ChargeMesEntre(saisie)
    saisie=saisie.encode()
    Clients.soc.send(saisie)


    Entrybox.delete("0.0", tkinter.END)
def ChargeMesEntre(texte):
    if texte != "" and texte != "\n":
        chatlog.config(state=tkinter.NORMAL)
        texte = "kinkazma :> {0}".format(texte)
        chatlog.insert(tkinter.END, texte)
        chatlog.config(state=tkinter.DISABLED)
        chatlog.yview('end')
#Bloque d'etat entrybox
def Blockstate(event):
    Entrybox.config(state=tkinter.DISABLED)
def Leasestate(event):
    Entrybox.config(state=tkinter.NORMAL)
    Action()
#Onglet de configuration IP
def second():
    top = tkinter.Toplevel(main)
    var = tkinter.IntVar(top)
    top.title("Configuration IP")
    top.geometry("280x120+500+200")
    top.resizable(width=False, height=False)
    iplabel = tkinter.Label(top, text="IP :")
    portlabel = tkinter.Label(top, text="PORT :")
    I = tkinter.Text(top, height=1, width=15, font="Arial")
    P = tkinter.Text(top, height=1, width=5, font="Arial")
    S = tkinter.Checkbutton(top, text="Avec SSL", variable=var)

    iplabel.grid(row=1, column=1)
    portlabel.grid(row=2, column=1)
    I.grid(row=1, column=2)
    P.grid(row=2, column=2)
    S.grid(row=3, column=1)


    OK = tkinter.Button(top, text="OK", command=toot)
    OK.grid(row=4, column=3)





# Creation de la fenetre main
main = tkinter.Tk()
main.geometry("400x500+450+250")
main.resizable(width=False, height=False)
main.title("Chat-Kinkazma Client v0.1")

# Creation du menu
menubar = tkinter.Menu(main)
menu1 = tkinter.Menu(menubar, tearoff=0)
menu1.add_command(label="Connection", command=second)
menu1.add_command(label="Actualiser", command=toot)
menu1.add_command(label="Quitter", command=toot)
menubar.add_cascade(label="Session", menu=menu1)
menu2 = tkinter.Menu(menubar, tearoff=0)
menu2.add_command(label="Aide", command=toot)
menubar.add_cascade(label="A propos", menu=menu2)




# Creation de la zone de texte console
chatlog = tkinter.Text(main, bd=0, bg="grey", height="8", width="50", font="Arial")
chatlog.insert(tkinter.END, "Setup connection !\n")
chatlog.config(state=tkinter.DISABLED)

Actuchatlog = Threadclient.ReloadEntry(chatlog,Clients)
Actuchatlog.start()

# Creation des widget button et saisie
Entrybox = tkinter.Text(main, bd=0, bg="white", height="8", width="9", font="Arial")
ButtonE = tkinter.Button(main, bd=0, bg="yellow", fg="red", height="4", width="5", font="Arial", text="Envoi",
                         command=Action)
Entrybox.bind("<Return>", Blockstate)  # Bindage de Action() sur la touche return
Entrybox.bind("<KeyRelease-Return>", Leasestate)

# Bar de scrolling
scrollbar = tkinter.Scrollbar(main, command=chatlog.yview, cursor="arrow")
chatlog['yscrollcommand'] = scrollbar.set
# Positionment
scrollbar.place(x=378, y=6, height=380, width=20)
Entrybox.place(x=6, y=400, height=70, width=270)
chatlog.place(x=6, y=6, height=380, width=370)
ButtonE.place(x=300, y=400, height=70, width=76)







main.config(menu=menubar)
main.mainloop()
Actuchatlog.clients.running=0
Actuchatlog.join()
Clients.soc.close()
Clients.join()
