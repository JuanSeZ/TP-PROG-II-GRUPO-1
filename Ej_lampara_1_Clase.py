class Lampara:
    def __init__(self,marca):
        self.foco = False
        self.marca = marca

    def getFoco(self):
        return self.foco

    def getMarca(self):
        return self.marca

    def prender(self):
        if self.foco == False:
            self.foco = True

    def apagar(self):
        if self.foco == True:
            self.foco = False

marca = 'Phillips'
lampara_1_living = Lampara(marca)
print('la marca del foco es: ',lampara_1_living.getMarca())
lampara_1_living.prender()
#lampara_1_living.apagar()
print("Hola")
#aver


if lampara_1_living.getFoco() == True:
    print('Foco encendido')
else:
    print('Foco Apagado')
# Edit
# Prog
