from cryptography.fernet import Fernet


pwd = input("What is the master password? ")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file= open("key.key","rb")
    key = file .read()
    file.close()
    return key

key= load_key()
fer = Fernet(key)

def view():
    with open("pass.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip().split("|")
            print("Usuario: "+data[0]+" Pass: "+ fer.decrypt(data[1].encode()).decode())


def add():
    name = input("Nombre de cuenta: ")
    pwd = input("Contraseña: ")

    with open("pass.txt","a") as f:      #a es append
        f.write(name + "|"+fer.encrypt(pwd.encode()).decode()+"\n")



while True:
    mode = input("Añadir contraseña(1), Ver contraseña(2), Salir(q) ")
    if mode == "q":
        break
    if mode == "1":
        add()
    elif mode == "2":
        view()
    else:
        print("Modo invalido")