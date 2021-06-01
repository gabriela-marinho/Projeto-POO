import CasaModulo
import random


class Personagem(CasaModulo.Casa):
    def __init__(self,aluguel):
        super().__init__(aluguel)
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.acordado = False
        self.atrasado = False
        self.demitido = False
        self.dinheiro = 50
        self.salario = 100
        self.HP = 10
        self.elogio = 0
        self.advertencia = 0
        self.nome = 'Josefino'
        self.genero = "Homem"
        self.idade = 25
        self.cor = "Branco"
        self.altura = 1.85
        self.peso = "Magro"
        self.rosto = "Bonito"
        self.cabelo = "Liso"
        self.cor_cabelo = "Loiro"

    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta.\nTem "+str(self.comida)+" de comida na geladeira e "+str(self.remedios)+" de remedio em estoque.\nAdvertências = "+str(self.advertencia)+" Elogios = "+str(self.elogio)+" HP = "+str(self.HP)
    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.acordado = False
        self.atrasado = False
        self.dinheiro -= self.aluguel
        print(f"R${self.aluguel} descontados de sua conta para pagar o aluguel!")
        aumentar_aluguel = random.randint(1,15)
        if aumentar_aluguel <= 2:
            self.aluguel += 5
            print("5 reais acrescentados ao aluguel! A patroa tá brava!")

    def montar_personagem(self):
        self.genero = input("Para começar, você é Homem, Mulher ou outro? ")
        self.idade = int(input("Ótimo, e qual sua idade? "))
        self.nome = input("Bacana, e qual o seu nome? ")
        self.cor = input("E sua cor, por gentileza: ")
        self.altura = float(input("Qual sua altura? ").replace(',','.'))
        self.peso = input("Você gostaria de ser gordo ou magro? ")
        self.cabelo = input("Qual o estilo do seu cabelo? ")
        if self.cabelo.upper() == "CARECA":
            print("KKKKKKKKKKKKKKKKKKK OLHA AÍ A CABECINHA DE GUIDÃO!")
        else:
            self.cor_cabelo = input("E a cor dele? ")
        self.rosto = input("Você é feio ou bonito? ")

