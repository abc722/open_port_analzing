from tkinter import*

import socket

pen = Tk()

pen.geometry("330x550")

pen.title("Acik Port Tarama")

pen.resizable(FALSE, FALSE)

arkaplanresmi = PhotoImage(file="unnamed.png")

lblarkaplan = Label(pen, image=arkaplanresmi)

lblarkaplan.place(x=0, y=0)

def tarama():

    s1 = str(enturl.get())
    liste = [21, 22, 23, 25, 80, 139, 443, 445, 3389]
    try:
        for port in liste:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((s1, port))
            if result == 0:
                listsonuc.insert(1, "Port {} Acik.".format(port))
            else:
                listsonuc.insert(1, "Port {} Kapali.".format(port))
                sock.close()

    except socket.error:
        print("Bu Allahin Belasi Bilgisayara Ulasilamiyor.")

lblurl = Label(pen, text="URL veya IP adresi giriniz.", font="Verdana 12 bold", fg="white", bg="black")

lblurl.place(x=60, y=20)

listsonuc = Listbox(pen, font="Verdana 12 bold", width="25", height="17", fg="white", bg="black")

listsonuc.place(x=27, y=140)

enturl = Entry(pen, font="Verdana 12 bold", fg="blue")

enturl.place(x=50, y=50)

btntara = Button(pen, text="Portlari Tara", font="Verdana 12 bold", fg="white", bg="black", command=tarama)

btntara.place(x=80, y=90)

pen.mainloop()
