import sys,pdb
from Lista_Patrones import Lista_Patrones as lista_patrones
from Lista_Cuadro_Piso import Lista_Cuadro_Piso as lista_

from colorama import init, Fore
from tkinter import Tk,ttk
from tkinter import filedialog as Archivero
from tkinter.messagebox import showinfo
from xml.dom import minidom



Listado_Patrones = lista_patrones()
patron = lista_()
dentro = True
Filas = []
class principal():

    def menu(self):
        global dentro
        while dentro==True:
            print('-------------------------')
            print('          Menu')
            print('-------------------------')
            print('1.  Cargar Archivo')
            print('2.  Seleccionar Patron')
            print('3.  Salir')
            print('Selecione una opcion')
            op=input()
            if(op == '1'):
                #nitido
                print('1.')
                principal.lectura(self,'s')
            elif(op == '2'):
                principal.menu_patron(self)
                print('2.')
            elif(op == '3'):
                dentro=False
            
    def menu_patron(self):
        global patron
        Filas = [] 
        print('ingrese el codigo del patron que desea manipular: ')
        codigo = input('')
        tt=False
        while(tt==False):
            print('-------------------------------')
            print("          Menu Patron")
            print('-------------------------------')
            print('1. Ver el patron graficamente')
            print('2. Cambiar el patron ')
            print('3. Seleccionar otro patron')
            print('seleccione una opcion')
            print('')
            op = input('')
            if(op == '1'):
                principal.ver_patron(self,codigo)
            elif(op == '2'):
                principal.cambiar_patron()
            elif(op == '3'):
                patron.LimpiarMat()
                principal.menu_patron(self)
            else:
                print(Fore.RED+'opcion no valida, intente de nuevo')
                tt=False
        return 'c'

    def ver_patron(self,codigo_patron):
        global Listado_Patrones, patron
        patron_actual = Listado_Patrones.busqueda(codigo_patron)
        print('patron seleccionado:'+str(patron_actual.patron_mater))
        patron.CrearMatriz(int(patron_actual.filas), int(patron_actual.columnas), patron_actual.patron_mater)
        print('-----------')
        patron.MostrarMat()
        patron.imagen(codigo_patron)
        return

    def select_file_XML(self):
    #filtros de extension de archivos
        filetypes = (
            ('xml text','*.xml'),
            ('All files', '*.*')
        )
        #obtencion de la direccion del archivo seleccionado
        filename = Archivero.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
            )
        #info de el archivo seleccionado
        showinfo(
            title='Selected File',
            message=filename
        )
        #return seleccionado
        if(filename==''):
            return('nonearchivo.nada')

        return filename

    def agg_patron(self,codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater):
        Listado_Patrones.insertar_siguiente_patron(codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater)
        return 'si'

    def lectura(self, nombre_archivo):
        print('hola')
        nombre_archivo = 'info.xml'
        try:
            print('analizando  '+nombre_archivo)
            mydoc = minidom.parse(nombre_archivo)
            Listas_Titulares = mydoc.getElementsByTagName("pisosArtesanales")
            for Lista in Listas_Titulares:
                Lista_Pisos = (Lista.getElementsByTagName("piso"))
                for Piso in Lista_Pisos:
                    nombre_piso = str (Piso.getAttribute("nombre"))
                    R_elementos = Piso.getElementsByTagName("R")
                    filas = int(R_elementos[0].childNodes[0].data)
                    C_elementos = Piso.getElementsByTagName("C")
                    columnas = C_elementos[0].childNodes[0].data
                    F_elementos = Piso.getElementsByTagName("F")
                    precio_volteo = F_elementos[0].childNodes[0].data
                    S_elementos = Piso.getElementsByTagName("S")
                    precio_intercambio = S_elementos[0].childNodes[0].data
                    Patrones_Elementos = Piso.getElementsByTagName("patrones")
                    Patrones = Patrones_Elementos[0].getElementsByTagName("patron")
                    for Patron in Patrones:
                        codigo_patron = Patron.getAttribute("codigo")
                        patron= Patron.childNodes[0].data
                        self.agg_patron(self,codigo_patron, nombre_piso, filas, columnas, precio_volteo, precio_intercambio, patron)
            print('-------------------------------------------------')
            print('          Archivo Cargado Correctamente')
            print('-------------------------------------------------')
        except ValueError:
             print(ValueError) #vista de errores al intentar leer archivos en consola

    def bucar(self, codigo):
        find = Listado_Patrones.busqueda(codigo)
        return find

    
             
if __name__ == "__main__":
   principal.menu(principal)
