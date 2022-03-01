class Nodo_Cuadro_Piso():

    def __init__(self, color):
        self.color = color
        self.cuadro_izquierda = None
        self.cuadro_arriba = None
        self.cuadro_derecha = None
        self.cuadro_abajo = None

    def setDato(self,dato):
        self.dato = dato

    def getDato(self):
        return self.dato

    def Mostrar(self):
        print(str(self.color), end = "")
        