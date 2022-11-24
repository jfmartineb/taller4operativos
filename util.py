def imprimirMatriz(matriz):
    hor = "+---+"
    for i in range(len(matriz[0])):
        hor += "---+"

    string = hor + "\n| - | 0 "

    for i in range(1, len(matriz[0])):
        string += f"| {i} "
    string += "|"

    string += "\n" + hor

    for i in range(len(matriz)):
        string += f"\n| {i} | {matriz[i][0]} "
        for j in range(1, len(matriz[i])):
            string += f'| {matriz[i][j]} '
        string += "|"
    
    string += "\n" + hor
    return string

def matrizToString(matriz):
    string = ""
    string += str(matriz[0])
    for i in range(1, len(matriz)):
        string += str(matriz[i]) 
    return string

def stringToMatriz(string):
    matriz = string.split('[')
    matriz.pop(0)
    for i in range(len(matriz)):
        matriz[i] = matriz[i][0:-1].split(',')
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz