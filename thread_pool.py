from multiprocessing.pool import ThreadPool
from multiprocessing import Value
from random import randint
from time import sleep

class Teste():

    def __init__(self) -> None:
        pass

    def calcular_dobro(self, numero):
        #adicionado um sleep para simular um processamento
        sleep(randint(0, 2))
        return f'O dobro de {numero} é {numero * 2}'


if __name__ == '__main__':
    robo = Teste()
    
    #lista de robos
    lista_robos = []
    #pool de threads onde definimos quantos processos deve estar rodando ao mesmo tempo
    pool = ThreadPool(processes=2)

    for i in range(50):
        async_result = pool.apply_async(Teste().calcular_dobro, (i,))
        print(async_result.get())
        lista_robos.append(async_result)

    recupera_fim_robos = [result.get() for result in lista_robos]
    