class Nodo_Cuadro_Piso():

    def __init__(self, color):
        self.color = color
        self.left = None
        self.down = None
        self.up = None
        self.right = None
        

    def setDato(self,dato):
        self.dato = dato

    def getDato(self):
        return self.dato

    def Mostrar(self):
        print(str(self.color), end = "")
        