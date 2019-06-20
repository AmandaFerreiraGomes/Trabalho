class Carro(object):

     combustivel = 0

     def  __init__(self, consumo):
        self.consumo = consumo
        
     def adicionarGasolina(self, combustivel):
        self.combustivel = combustivel
        print("-> COMBUSTIVEL ADICIONADO: ", self.combustivel)
        return self.combustivel  

     def andar(self,dist):
        self.dist = dist
        print("-> DISTANCIA PERCORRIDA: ", self.dist)
        self.consumo = ((self.dist/self.consumo)-(self.combustivel))
        return self.consumo

     def obterGasolina(self):
       resto =self.consumo

       if resto<=-1:
           resto = resto*(-1)
       else:
           resto

       print("-> COMBUSTIVEL RESTANTE: ", resto)

     def __str__(self):
        pass
