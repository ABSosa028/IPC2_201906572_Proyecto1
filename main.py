import sys,pdb

from django.forms import PasswordInput
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
        patron = lista_()
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
                principal.cambiar_patron(self,codigo)
            elif(op == '3'):
                
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

    def ver_patron2(self,codigo_patron):
        patron2 = lista_()
        patron_actual = Listado_Patrones.busqueda(codigo_patron)
        print('patron seleccionado:'+str(patron_actual.patron_mater))
        patron2.CrearMatriz(int(patron_actual.filas), int(patron_actual.columnas), patron_actual.patron_mater)
        print('-----------')
        patron2.MostrarMat()
        patron2.imagen(codigo_patron)
        return


    def cambiar_patron(self, codigo_patron):
        global Listado_Patrones, patron
        patron_actual = Listado_Patrones.busqueda(codigo_patron)
        print("Estos son los patrones a los cuales puede optar, escoja el patron que mas le convenza")
        opciones = Listado_Patrones.busqueda2(patron_actual.nombre_piso)
        it = 1
        for op in opciones:
            print(str(it)+'. codigo patron: ' + str(op.codigo)+' diseño del patron: '+op.patron_mater)
            it+=1
        print('Ingrese el numero del nuevo patron que desea')
        print('*si desea ver el grafico del nuevo piso ingrese la opcion 689 seguido de un punto y el codigo del patron que desea ver')
        opc = input()
        print(opc)
        validar= opc.split(".")
        if(validar[0]=='689'):
            principal.ver_patron2(self,validar[1])
            principal.cambiar_patron(self,codigo_patron)
        else:
            print(validar[0])
            codNuev=opciones[int(validar[0])-1].codigo
            principal.kambio(self,codNuev, codigo_patron)
        return 

    def kambio(self,codigo_nuevo, codigo_viejo):
        global Listado_Patrones, patron
        patron_nuevo = Listado_Patrones.busqueda(codigo_nuevo)
        patron_viejo = Listado_Patrones.busqueda(codigo_viejo)
        patron2 = lista_()
        patron.CrearMatriz(int(patron_viejo.filas), int(patron_viejo.columnas), patron_viejo.patron_mater)
        patron2.CrearMatriz(int(patron_nuevo.filas), int(patron_nuevo.columnas), patron_nuevo.patron_mater)
        print(patron_viejo.patron_mater)
        
        comparacion = patron.comparar(patron2)
        cambios_nec_w = patron2.cambios(patron)

        dif = 0
        for i in comparacion:
            if(i == False):
                dif += 1
        print('El patron seleccionado tiene '+str(dif)+' cuadros distintos en su patron')
        print('Es necesario cambiar '+str(cambios_nec_w)+' de color negro')
        for i in range(0, len(comparacion)):
            if(comparacion[i]==False and cambios_nec_w!=0):
                if(cambios_nec_w<0):
                    to = patron.cambiando_a_blanco(i)
                else:
                    to = patron.cambiando_a_negro(i)
                if(to ==True):
                    if(cambios_nec_w>0):
                        cambios_nec_w -= 1
                    else:
                        cambios_nec_w += 1
        comparacion2 = patron.comparar(patron2)
        cambios_nec_w2 = patron2.cambios(patron)
        tt=0
        for i in range(0, len(comparacion2)):
            if(comparacion2[i]==False):
                tt+=1
                if(tt==2):    
                    patron.nodos_intercambiar(patron_nuevo.patron_mater)
                    tt=0
        patron.MostrarMat()
        patron.imagen2(patron_viejo.codigo)                





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
