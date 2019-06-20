from Carro import Carro

def main():
        print(" \t OLA, SEJA BEM-VINDO(A)!\n")
        #caso queira usar outros valores, remova os "#" das 3 linhas abaixo e apague as atribuiçoes das respectivas variaveis
        #c_m = float(input("CONSUMO MEDIO: "))
        #q_g = float(input("QUANTIDADE DE GASOLINA(EM LITROS): "))
        #d_p = float(input("DISTANCIA PERCORRIDA: "))
        c_m = 15
        q_g = 20
        d_p = 100
        meuFusca = Carro(c_m)
        meuFusca.adicionarGasolina(q_g)
        meuFusca.andar(d_p)
        meuFusca.obterGasolina()
main()
