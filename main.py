import sys,pdb
from Lista_Patrones import Lista_Patrones as lista_patrones
from Lista_Cuadro_Piso import Lista_Cuadro_Piso as lista_

from colorama import init, Fore
from tkinter import Tk,ttk
from tkinter import filedialog as Archivero
from tkinter.messagebox import showinfo
from xml.dom import minidom



Listado_Patrones = lista_patrones()
patron = ''
dentro = True
Filas = []
class principal():
    



    def menu(self):
        global dentro
        while dentro==True:
            print('menu')
            print('1. Cargar Archivo')
            print('2. Seleccionar Patron')
            print('3. Salir')
            print('4. op 1')
            print('5. op 1')
            op=input('Selecione una opcion')
            if(op == '1'):
                #nitido
                print('1.')
                principal.lectura(self,'s')
            elif(op == '2'):
                principal.ver_patron(self)
                print('2.')
            elif(op == '3'):
                dentro=False
            
    def ver_patron(self):
        global patron
        patron = ''
        Filas = [] 
        print('ingrese el codigo del patron que desea manipular: ')
        codigo = input('')
        print(codigo)
        if(patron == ''): 
            patron = lista_(codigo)
        else:
            patron.eliminar_todo()
            patron._nuevo_codigo(codigo)
        finder = principal.bucar(self, codigo)
        print(finder.patron_mater)
        dimensiones = int(finder.columnas)*int(finder.filas)
        #validando los espacios que coincidan con los cuadros
        #if(int(finder.patron_mater(len))==dimensiones):
        agg_fila = ''
        for x in finder.patron_mater:
            agg_fila += str(x)
            
            if (((len(agg_fila))%int(finder.columnas))==0):
                Filas.append(agg_fila)
                agg_fila = ''
        for y in Filas:
            print(y)

            

        print('nel')
        return 'c'

    #digrafh{
    #   label = "\n struct ListNide";
    #   node[shape]
    # }
    # )





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
        #Listado_Patrones.insertar_siguiente_patron(codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater)
        return 'si'

    def lectura(self, nombre_archivo):
        print('hola')
        nombre_archivo = 'info.xml'
        try:
            print('analizando  '+nombre_archivo)
            mydoc = minidom.parse(nombre_archivo)
            #print(mydoc)
            Listas_Titulares = mydoc.getElementsByTagName("pisosArtesanales")
            for Lista in Listas_Titulares:
                Lista_Pisos = (Lista.getElementsByTagName("piso"))
                for Piso in Lista_Pisos:
                    nombre_piso = str (Piso.getAttribute("nombre"))
                    #print(nombre_piso)
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
                        #print(codigo_patron)
                        #print(patron)
                        
                        self.agg_patron(self,codigo_patron, nombre_piso, filas, columnas, precio_volteo, precio_intercambio, patron)
                        #agg_patron(codigo_patron,nombre_piso, filas, columnas, precio_volteo, precio_intercambio, patron)
            print('-------------------------------------------------')
            #Listado_Patrones.print_lista_patrones()
            print('          Archivo Cargado Correctamente')
            print('-------------------------------------------------')
            #self.menu(self)
        except ValueError:
             print(ValueError) #vista de errores al intentar leer archivos en consola

    def bucar(self, codigo):
        find = Listado_Patrones.busqueda(codigo)
        return find

    def crear_pat(self, nodo):
        columnas = nodo.columnas
        filas = nodo.filas
        patron  = nodo.patron_mater


             
if __name__ == "__main__":
   principal.menu(principal)
