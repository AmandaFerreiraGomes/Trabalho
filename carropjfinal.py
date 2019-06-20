from Carro import Carro

def main():
        print(" \t OLA, SEJA BEM-VINDO(A)!\n")
        c_m = float(input("CONSUMO MEDIO: "))
        q_g = float(input("QUANTIDADE DE GASOLINA(EM LITROS): "))
        d_p = float(input("DISTANCIA PERCORRIDA: "))
        meuFusca = Carro(c_m)
        meuFusca.adicionarGasolina(q_g)
        meuFusca.andar(d_p)
        meuFusca.obterGasolina()
main()
