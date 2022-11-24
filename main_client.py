from requests import get
import sys
from colorama import Style, Fore
from util import *

class Client:
    def __init__(self, host, port):
        self.host = "http://" +  str(host) + ":" + str(port)
        self.secs = 5
        self.connect()

    def connect(self):
        response = get(self.host+"/infoService")
        if (str(response)[11:-2] == "404" or str(response)[11:-2] == "200"):
            print(response.text)
            while True:
                user = input("Ingrese un nombre de usuario: ")
                resp = self.iniciarSesion(user)
                if (resp == "1"):
                    break
                else:
                    print("Ingrese un usuario válido")

            mns = user + " -> "

            while True:
                peticion = input(Fore.GREEN + mns + Style.RESET_ALL)

                lista_peticion = peticion.split(" ")
                lista_peticion[0].lower()

                if (lista_peticion[0] == "out"):
                    self.logout(user)
                    break
                elif (lista_peticion[0].lower() == "sillas"):
                    self.solicitarInfo()
                elif (lista_peticion[0].lower() == "reservar"):
                    self.reservar(lista_peticion[1], lista_peticion[2], user)
                elif (lista_peticion[0].lower() == "pagar"):
                    self.pagarReserva(user)
                elif (lista_peticion[0].lower() == "cancelar"):
                    self.cancelarReserva(user)
                else:
                    print("Please enter a valid command")

        else:
            print ("Couldn't connect to the server")

    def iniciarSesion(self, user):
        string = self.host + f"/inicioSesion?user={user}"
        response = get(string)
        return response.text

    def logout(self, user):
        string = self.host + f"/logout?user={user}"
        response = get(string)
        return response.text

    def solicitarInfo(self):
        string = self.host + "/seats"
        response = get(string)
        print(imprimirMatriz(stringToMatriz((response.text[1:-1]))))

    def reservar(self, fila, col, user):
        string = self.host + f"/reservar?fila={fila}&col={col}&user={user}"
        response = get(string)
        if (response.text[1] == "1"):
            print(f"Reserva conservada para el asiento {fila}, {col}. Tiene 10 segundos para realizar el pago.")
        else:
            print(f"Asientos {fila}, {col} ocupados, intente nuevamente")
            print(imprimirMatriz(stringToMatriz((response.text[2:-1]))))

    def pagarReserva(self, user):
        string =self.host + f"/pagar?user={user}"
        response = get(string)
        if (response.text == "2"):
            print("Pago ya se había realizado")
        elif (response.text == "1"):
            print("Pago exitoso")
        else:
            print(f"No hay reserva a nombre de {user}.")

    def cancelarReserva(self, user):
        string =self.host + f"/cancelar?user={user}"
        response = get(string)
        if (response.text == "1"):
            print("Cancelación exitosa")
        else:
            print(f"No hay reserva a nombre de {user}.")





# ------------------------------------------------------------------------------------------------------------

def main(argv):
    if ("-p" in argv):
        port = argv[argv.index("-p")+1]
        host = "localhost"
        print("PORT: ",port)
        print("HOST: ",host)

        c = Client(host, port)
    else:
        print("Please indicate the desire port with -p #")

if __name__ == "__main__":
    main(sys.argv)