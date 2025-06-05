import time

tabuada=int(input("Qual tabuada você deseja? :"))    

def mostrar_tabuada(numero):
    for i in range(0, 11):
        print(f"{i} x {tabuada} = {i*tabuada}")
        time.sleep(1)

mostrar_tabuada(tabuada)