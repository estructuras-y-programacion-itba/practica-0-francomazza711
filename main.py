# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"

from random import randint
def tirar_dados(cantidad):
    return[randint(1,6) for i in range (cantidad)]



def es_escalera(lista):
    if isinstance(lista,list):
        for i in range(len(lista)):
            if (1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista) or (2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista):
                print('Es escalera')
                return True
    print ('No es escalera')
    return False


def es_full(lista):
    d=sorted(lista)
    trio_inicial = (d[0]==d[1]==d[2]) and (d[3]==d[4]) 
    trio_final = (d[2]==d[3]==d[4]) and (d[0]== d[1])
    son_distintos=d[0]!=d[4]
    if (trio_final or trio_inicial) and son_distintos:
        print('Es full')
        return True
    print('No es full')
    return False


def es_poker(lista):
    d=sorted(lista)
    poker_inicial = (d[0]==d[1]==d[2]==d[3]==d[4])
    poker_final = (d[1]==d[2]==d[3]==d[4])
    generala = (d[0]==d[1]==d[2]==d[3]==d[4]==d[5])
    son_distintos=d[0]!=d[4]
    if (poker_inicial or poker_final or generala) and son_distintos:
        print('Es poker')
        return True
    print('No es Poker')
    return False


lista=[2, 2, 2, 1, 1]
escalera=es_escalera(lista)
poker=es_poker(lista)
full=es_full(lista)


def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
