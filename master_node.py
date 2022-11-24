from fastapi import FastAPI, Response
from pydantic import BaseModel
import threading
import time

from util import *

app = FastAPI()

global storage
storage = [[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],]

global reservas
reservas = {}

global users
users = []

class Item(BaseModel):
    key: str
    value: str

# Función que se invocará luego de un tiempo
def demoraPago(user):
    if (reservas[user][0] == 1):
        reservas[user][0] = 0
        print(f'storage[{reservas[user][1][0]}][{reservas[user][1][1]}]')
        storage[reservas[user][1][0]][reservas[user][1][1]] = 1
        print(storage[reservas[user][1][0]][reservas[user][1][1]])

@app.get("/inicioSesion", status_code=200)
async def get_kv(user: str, response: Response):
    if (user not in users):
        users.append(user)
        reservas[user] = [0, [-1, -1]]
        return 1
    return 0

@app.get("/logout", status_code=200)
async def get_kv(user: str, response: Response):
    if (user in users):
        users.remove(user)
        storage[reservas[user][1][0]][reservas[user][1][1]] = 1
        del reservas[user]
        return 1
    return 0

@app.get("/infoService", status_code=200)
async def get_kv():
    string = "Bienvenidos a la reserva de asientos para películas más sencillo del mundo! A continuación verás una matriz que indicará las sillas."
    string = string + "Si la posición que desea está en 1 es porque la silla está disponible, si está en 0 significa que está ocupada"
    return string.encode('utf-8')

@app.get("/seats", status_code=200)
async def get_kv():
    string = matrizToString(storage)
    return string.encode('utf-8')

@app.get("/reservar", status_code=200)
async def get_kv(fila: int, col:int, user:str, response: Response):
    if (storage[fila][col] == 1):
        reservas[user][0] = 1
        reservas[user][1][0] = fila
        reservas[user][1][1] = col
        storage[fila][col] = 0
        t = threading.Timer(10,demoraPago,[user])
        t.start()
        return "1"
    return "0" + matrizToString(storage)

@app.get("/reservar", status_code=200)
async def get_kv(fila: int, col:int, user:str, response: Response):
    if (reservas[user][0] == 1):
        reservas[user][0] = 2
        return 1
    elif (reservas[user][0] == 2):
        return 2
    return 0

@app.get("/pagar", status_code=200)
async def get_kv(user:str, response: Response):
    if (reservas[user][0] == 1):
        reservas[user][0] = 2
        return 1
    elif (reservas[user][0] == 2):
        return 2
    return 0

@app.get("/cancelar", status_code=200)
async def get_kv(user:str, response: Response):
    if (reservas[user][0] == 1 or reservas[user][0] == 2):
        reservas[user][0] = 0
        storage[reservas[user][1][0]][reservas[user][1][1]] = 1
        return 1
    return 0