import random
from math import sqrt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def is_prime(p):
    flag = 0
    if(p>1):
        for i in range(2, int(sqrt(p)+1)):
            if(p%i == 0):
                flag=1
                break
        if flag==0:
            return True
        else:
            return False
    return False
        
            
def key_gen(win, name, p, q):
  if (not is_prime(p) or not is_prime(q)):
    print("Wrong choice of primes")
  else:
    n=p*q
    g=n+1
    f=open('publicKeys.txt', 'a')
    if name not in getNames():
        f.write(name+","+str(n)+","+str(g)+"\n")
        f.close()
        messagebox.showinfo('UserName Added', 'Keys Added for '+name+' Sucessfully')

    else:
        messagebox.showerror('Name Already Exists', 'Keys already exist for '+name)
    win.destroy()
    
def getNames():
    f=open('publicKeys.txt', 'r')
    nameList=[]
    while True:
        line=f.readline()
        if not line:
            break
        line=line.split(',')
        nameList.append(line[0])
    f.close()
    return nameList

def fastExponentiation(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r
    

def modInverse(A, M):
    m0 = M
    y = 0
    x = 1
    if (M == 1):
        return 0
    while (A > 1):
        q = A // M
        t = M
        M = A % M
        A = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x

def encrypt(message, reciever):
    n, g = getPublicKeys(reciever)
    n=int(n)
    g=int(g)
    r=random.randint(0,n-1)
    while(gcd(r, n)!=1):
        r=random.randint(0,n-1)
    cipher=(fastExponentiation(g, message, n*n)*fastExponentiation(r, n, n*n))%(n*n)
    return cipher

def getPublicKeys(rec):
    f=open('publicKeys.txt', 'r')
    while True:
        line=f.readline()
        if not line:
            f.close()
            return -1, -1
        line=line.split(',')
        if rec==line[0]:
            f.close()
            return line[1], line[2]

def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

def decrypt(cipher, p, q):
    n=p*q
    phi=(p-1)*(q-1)
    z=fastExponentiation(cipher, phi, n*n)
    z-=1
    z/=n
    plain = z*modInverse(phi, n)
    plain %= n
    return int(plain)

def windowKG():
    
    def getCred():
        #global E1
        name = E1.get()
        p = E2.get()
        q = E3.get()
        key_gen(kgWin, name, int(p), int(q))
    
       
    kgWin = Tk()
    kgWin.geometry('500x600')
    kgL = Label(kgWin, text = "Key Generation", font="Roboto").place(x=190, y= 60)
    L1 = Label(kgWin, text="User Name").place(x=90, y= 100)
    E1 = Entry(kgWin, bd =5)
    E1.place(x=200, y = 100)
    
    L2 = Label(kgWin, text="Enter Prime 'p' ").place(x=90, y= 200)
    E2 = Entry(kgWin, bd =5)
    E2.place(x=200, y = 200)
    
    L3 = Label(kgWin, text="Enter Prime 'q' ").place(x=90, y= 300)
    E3 = Entry(kgWin, bd =5)
    E3.place(x=200, y = 300)
    okbtn = Button(kgWin, text = 'Ok', bd = '5', command = getCred ).place(x=250, y=400)
    kgWin.mainloop()

def windowEncrypt():
    def getCred():
        name = cb.get()
        msg = E2.get()
        cipher=encrypt(int(msg), name)
        messagebox.showinfo('Cipher Text', 'Cipher Text is '+str(cipher))
        eWin.destroy()
        
    eWin = Tk()
    eWin.title("Encrypt a Message ")
    eWin.geometry('500x600')
    kgL = Label(eWin, text = "Message Encryption ", font="Roboto").place(x=190, y= 60)
    
    L1 = Label(eWin, text="Choose Receiver : ").place(x=90, y= 100)
    var=StringVar()
    var.set("rethika")
    nameList=tuple(getNames())
    cb=ttk.Combobox(eWin ,values=nameList, width=30)
    cb.place(x = 200, y = 100)
    
    L2 = Label(eWin, text="Enter Message: ").place(x=90, y= 200)
    E2 = Entry(eWin, bd =5)
    E2.place(x=200, y = 200)
    
    okbtn = Button(eWin, text = 'Ok', bd = '5', command = getCred ).place(x=250, y=400)
    eWin.mainloop()
    
def windowDecrypt():
    def getCred():
        p = E2.get()
        q = E3.get()
        cipher = E4.get()
        plaintext = decrypt(int(cipher), int(p), int(q))
        messagebox.showinfo('Plain Text', 'Plain Text is '+str(plaintext))
        dWin.destroy()
    
       
    dWin = Tk()
    dWin.geometry('500x600')
    dWin.title("Decrypt a Message")
    dL = Label(dWin, text = "Decryption ", font="Roboto").place(x=190, y= 60)
    
    L2 = Label(dWin, text="Enter private key 'p' ").place(x=90, y= 200)
    E2 = Entry(dWin, bd =5)
    E2.place(x=200, y = 200)
    
    L3 = Label(dWin, text="Enter private key 'q' ").place(x=90, y= 300)
    E3 = Entry(dWin, bd =5)
    E3.place(x=200, y = 300)
    
    L4 = Label(dWin, text="Enter Message: ").place(x=90, y= 400)
    E4 = Entry(dWin, bd =5)
    E4.place(x=200, y = 400)
    
    okbtn = Button(dWin, text = 'Ok', bd = '5', command = getCred ).place(x=250, y=450)
    dWin.mainloop()

root = Tk()              
root.title("Paillier")
root.geometry('500x600')
paillier = Label(root, text = "Paillier CryptoSystem", font="Roboto").place(x=190, y= 60)
kgb = Button(root, text = 'Key Generation', bd = '5', command = windowKG)
kgb.place(x=50, y=100)

encb = Button(root, text = 'Encrypt', bd = '5', command = windowEncrypt)
encb.place(x=210, y=100)

decb = Button(root, text = 'Decrypt', bd = '5', command = windowDecrypt)
decb.place(x=350, y=100)
 
btn = Button(root, text = 'Click me !', bd = '5', command = root.destroy)
btn.pack(side = 'top')    
root.mainloop()
