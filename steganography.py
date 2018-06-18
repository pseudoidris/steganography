import tkinter as tk
from tkinter import *
from tkinter import filedialog,Text,messagebox
from functools import partial
import encode
import decode
import pickle
import os

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label3= Label(self.frame,text="STEGANOGRAPHY" ,font = "David 24 bold",fg="blue")
        self.label3.pack()
        self.label4= Label(self.frame,text="Click Here to : " ,font = "Calibri 14")
        self.label4.pack()
        self.button1 = tk.Button(self.frame, text = 'ENCRYPT', width = 50,height = 2, command = self.new_window,bg="#868b78")
        self.button1.pack()
        self.label5= Label(self.frame,text="Click Here to : " ,font = "Calibri 14")
        self.label5.pack()
        self.button2 = tk.Button(self.frame, text = 'DECRYPT', width = 50,height = 2, command = self.new_window2,bg="#868b78")
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    def new_window2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo3(self.newWindow)
class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1= Label(self.frame,text="Please Select the image file which you have to encrypt :     " ,font = "David 16 bold",fg="#6383b7")
        self.label1.pack()

        #browse button
        self.browsebutton = Button(self.frame,text="Browse", width = 30,command=self.browsefunc,bg="#868b78")
        self.browsebutton.pack()
        self.pathlabel = Label(self.frame)
        self.pathlabel.pack()


        #uploadbutton
        self.uploadbutton = Button(self.frame,text="Upload", width = 30,command=self.upload,bg="#868b78")
        self.uploadbutton.pack()


        self.L1 = Label(self.frame, text="Message")
        self.L1.pack()
        self.E1 = Text(self.frame, bd =2,height=7,width=30)
        self.E1.pack()

        #savetxtbutton
        self.savetxtbutton = Button(self.frame,text="Save Text", width = 30, command= self.save_message,bg="#868b78")
        self.savetxtbutton.pack()


        #Encryptbutton
        self.encryptbutton = Button(self.frame,text="Encrypt", width = 30,height=2, command=self.encrypt,bg="#868b78")
        self.encryptbutton.pack(pady=20)

        self.frame.pack(pady=40,padx=10)

    global valid_extensions
    valid_extensions=["jpg","jpeg","png"]

    def browsefunc(self):
        filename = filedialog.askopenfilename()
        f = open("tmppath.txt","w")
        f.write(filename)
        f.close()
        self.pathlabel.config(text=filename)

    def upload(self):
        filename = open("tmppath.txt").read()
        fileext = filename.split(".")[-1].lower()
        if (fileext in valid_extensions):
            messagebox.showinfo("Status","Input recieved..!")
            #pathlabel.config(text=filename)
        else:
            messagebox.showinfo("Warning","File should be in valid format.")
            self.master.mainloop()

    def save_message(self):
        msgtext = None
        inputValue=self.E1.get("1.0","end-1c")
        msgtext=open("Encryptedmsg.txt","w")
        msgtext.write(inputValue)
        msgtext.close()

    def encrypt(self):
        self.E1.delete("1.0","end-1c")
        encode.main()
        messagebox.showinfo("Congrats","Encryption Done")
        os.remove("Encryptedmsg.txt")


class Demo3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label1= Label(self.frame,text="Please Select the image file which you have to decrypt :   " ,font = "David 16 bold",fg="#6383b7")
        self.label1.pack()

        #browse button
        self.browsebutton = Button(self.frame,text="Browse", width = 30,command=self.browsefunc,bg="#868b78")
        self.browsebutton.pack()
        self.pathlabel = Label(self.frame)
        self.pathlabel.pack()

        #uploadbutton
        self.uploadbutton = Button(self.frame,text="Upload", width = 30,command=self.upload,bg="#868b78")
        self.uploadbutton.pack()

        #Decryptbutton
        self.decryptbutton = Button(self.frame,text="Decrypt", width = 30,height=2, command=self.decrypt,bg="#868b78")
        self.decryptbutton.pack(pady=20)

        self.frame.pack(pady=30)

    global valid_extensions
    valid_extensions=["jpg","jpeg","png","bmp","tiff"]

    def browsefunc(self):
        filename = filedialog.askopenfilename()
        f = open("tmppath.txt","w")
        f.write(filename)
        f.close()
        self.pathlabel.config(text=filename)

    def upload(self):
        filename = open("tmppath.txt").read()
        fileext = filename.split(".")[-1].lower()
        if (fileext in valid_extensions):
            messagebox.showinfo("Status","Input recieved..!")
            #pathlabel.config(text=filename)
        else:
            messagebox.showinfo("Warning","File should be in valid format.")
            self.master.mainloop()

    def decrypt(self):
        decode.main()
        finalres=open("res.txt").read().strip()
        messagebox.showinfo("Decrypted Message :",finalres)
        os.remove("res.txt")

def main():
    root = tk.Tk()
    root.title("Steganography")
    root.geometry('600x400')
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
