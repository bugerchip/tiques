import os
import pprint



rol=['Ejecutivo_mesa','Ejecutivo_area','Jefe_mesa','Administrador','Cliente']

tiques= [ {
        "nombre_cliente":'El',
        "apellido_cliente":'Fasher',
        "rut_cliente":'1564514-6',
        "fono_cliente":'56454842',
        "email_cliente":'fgrhg@gmail.com',
        "tipo":'Felicitacion',
        "prioridad":'Alta',
        "detalle1":"detalle1",
        "detalle2":"detalle2",
        "area":'area',
        "creador":'creador'
    }]

usuarios=[
    {
        "usr":"uzumaki",
        "passw":"1234",
        "rol":rol[0]},
    {
        "usr":"naruto",
        "passw":"1234", 
        "rol":rol[1]},
    {
        "usr":"ramen",
        "passw":"1234",
        "rol":rol[2]},
    {
        "usr":"bee",
        "passw":"1234",
        "rol":rol[3]},
        {
        "usr":"lee",
        "passw":"1234",
        "rol":rol[4]}
]


class Usuario():
    def __init__(self, usr,passw,rol):
        self.usr=usr
        self.passw=passw
        self.rol=rol

    def crearUsr():
        def default():
            print('No existe esa opcion')

        print('*************************************')
        print('***       Creador de Usuarios     ***')
        print('*************************************')
        print('*    Datos requeridos:              *')
        print('*    1:  Nombre de usuario          *')
        print('*    2:  Contrasena                 *')
        print('*    3:  Permisos                   *')
        print('*************************************')
        print('')
        print('*    1:  Nombre de usuario          *')
        print('___________________')
        print('Ingresa nombre de usuario: ')
        usr=input('>: ')
        print('Nombre de usuario: ' + usr)
        print('*    2:  Contrasena                 *')
        print('___________________')
        print('Ingresa contrasena: ')
        passw=input('>: ')
        print('Contrasena ok')
        print('*    3:  Permisos                   *')
        print('___________________')
        print('Opciones: ')


        tipo={1:'Ejecutivo de mesa',2:'Ejecutivo de area',3:'Jefe de mesa',4:'Administrador',5:'Cliente'}
        pprint.pprint(tipo, sort_dicts=False, width=1)
        print('___________________')
        print('(!): Ingresa el numero')
        def ejecutivo_mesa():
            return('Ejecutivo_mesa ')
 
        def ejecutivo_area():
            return('Ejecutivo_area ')

        def jefe_mesa():
            return('Jefe_mesa')

        def administrador():
            return('Administrador')

        def cliente():
            return('Cliente')
	        
        tipo={1:ejecutivo_mesa,2:ejecutivo_area, 2:jefe_mesa, 3:administrador, 4:cliente}
        rol=int(input('>: '))
        
        rol= tipo.get(rol,default)()
        print('Permisos : '+ rol)
        pass
    def verUsr():
        lista=usuarios 
        pprint.pprint(lista, sort_dicts=False, width=1)
    def editUsr():
        print('Aqui va la funcion para editar usuarios')

    def eliminarUsr():
        print('Aqui va la funcion para eliminar usuarios')

class Tique():
    def __init__(self, nombre_cliente,apellido_cliente,rut_cliente,fono_cliente,email_cliente, tipo, prioridad, detalle1, detalle2, area, creador):
        self.nombre_cliente=nombre_cliente
        self.apellido_cliente=apellido_cliente
        self.rut_cliente=rut_cliente
        self.fono_cliente=fono_cliente
        self.email_cliente=email_cliente
        self.tipo=tipo
        self.prioridad=prioridad
        self.detalle1=detalle1
        self.detalle2=detalle2
        self.area=area
        self.creador=creador
    
    def tiqueIn(usuario):
        tiques=[]
        os.system('cls')

        def default():
            print('No existe esa opcion')

        print('*************************************')
        print('***       Creador de tiques       ***')
        print('*************************************')
        print('*    Datos requeridos:              *')
        print('*    1:  Nombre cliente             *')
        print('*    2:  Apellido cliente           *')
        print('*    3:  RUT cliente                *')
        print('*    4:  Fono cliente               *')
        print('*    5:  Email cliente              *')
        print('*    6:  Tipo de tique              *')
        print('*    7:  Prioridad del tique        *')
        print('*    8:  Detalle del servicio       *')
        print('*    9:  Detalle del problema       *')
        print('*   10:  Area de destino            *')
        print('*************************************')
    
        print('_____________________________________')
        print('*    1:  Nombre cliente             *')
        print('')
        nombre_cliente=input('>: ')
        print('_____________________________________')
        print('*    2:  Apellido cliente             *')
        print('')
        apellido_cliente=input('>: ')
        print('')
        print('_____________________________________')
        print('*      3:  RUT cliente              *')
        print('')
        rut_cliente=input('>: ')
        print('_____________________________________')
        print('*    4:  Fono cliente             *')
        print('')
        fono_cliente=input('>: ')
        print('_____________________________________')
        print('*     5:  Email cliente             *')
        print('')
        email_cliente=input('>: ')

        print('_____________________________________')
        print('*    6:  Tipo de tique              *')
        print('')

        tipo={1:'Felicitacion', 2:'Consulta', 3:'Reclamo', 4:'Problema'}
        print('Opciones:')
        pprint.pprint(tipo, sort_dicts=False, width=8)

        def Felicitacion():
            return('felicitación')
	        
        def Consulta():
            return('Consulta')
 
        def Reclamo():
            return('Reclamo')

        def Problema():
            return('Problema')
	        
        tipo={1:Felicitacion, 2:Consulta, 3:Reclamo, 4:Problema}

        tipo_tique=int(input('>: '))
        tip= tipo.get(tipo_tique,default)()
        print('Tipo de tique: '+ tip)
        print('_____________________________________')
        prioridad={1:'Alta', 2:'Media',3:'Baja'}
        print('***    3:  Prioridad del tique    ***')
        print('Opciones:')
        print(prioridad)
        #pprint.pprint(prioridad,sort_dicts=False,width=1)
        print('')
        def Alta():
            return('Alta')

        def Media():
            return('Media')  

        def Baja():
            return('Baja')
        prioridad={1:Alta, 2:Media,3:Baja}
        prio=int(input('>: '))
        p= prioridad.get(prio,default)()
        print('Prioridad: '+ p)

        print('_____________________________________')
        print('****    4:  Area de destino      ****')
        area={1:'Ventas', 2:'Postventa',3:'Ayuda'}
        print('Opciones: ')
        pprint.pprint(area)
        def Ventas():
            return('Ventas')

        def Postventa():
            return('Postventa')

        def Ayuda():
            return('Ayuda') 
	           
        area={1:Ventas, 2:Postventa,3:Ayuda}
        print('')
        ar=int(input('>: '))
        a= area.get(ar,default)()
        print('Area: '+ a)
        det1='abc'
        det2='abc'
        print('_____________________________________')
        print('********* VISTA PRELIMINAR  *********')
        print('')

        tique=[{
            'Nombre Cliente: ':nombre_cliente,
            'Apellido Cliente: ':apellido_cliente,
            'Rut Cliente: ':rut_cliente,
            'Fono Cliente: ':fono_cliente,
            'Email Cliente: ':email_cliente,
            'Tipo Tique: ':tip,
            'Prioridad: ':p, 
            'Area: ':a,
            'Creado por: ':usuario
            }]
        pprint.pprint(tique, sort_dicts=False)
        
        print('____________________________________')
        print('************************************')
        print(' Desea guardar este Tique?  Si/No:\n')
        respuesta=input('>: ')

        if respuesta=='si' or respuesta=='Si' or respuesta=='Si' or respuesta=='SI' or respuesta=='sI' or respuesta=='s':

            tiques.append(tique)
            print('Guardado')
            return tiques

        if respuesta == 'no' or respuesta =='NO' or respuesta =='No' or respuesta =='nO' or respuesta =='n' or respuesta =='N':
            print('*************************************')
            print('\n No guardado') 

    def verTiques():
        lista=tiques
        pprint.pprint(lista, sort_dicts=False, width=1)

    def actualizarTique():
        print('Aqui va la funcion que actualiza el tique')

    def filtrarTique():
        print('Aqui va la funcion que filtra los tiques')
    
    def borrarTique():
        print('Aqui va la funcion que elimina un tique')

class Main(Tique,Usuario):
    
    def main(nombre,x):
        
        def default():
            print('No existe esa opcion')
        respuesta='si'
        if x=='Ejecutivo_mesa':
           
            switch={1: lambda :Tique.tiqueIn(nombre), 2:Tique.verTiques, 3:Tique.actualizarTique, 4:Tique.filtrarTique}
            while respuesta=='si' or respuesta=='Si' or respuesta=='Si' or respuesta=='SI' or respuesta=='sI' or respuesta=='s':
                print('*************************************')
                print('***       Ejecutivo de Mesa       ***')
                print('*************************************')
                print('*    opcion 1:  Agregar tique       *')
                print('*    opcion 2:  Ver tiques          *')
                print('*    opcion 3:  Actualizar tique    *')
                print('*    opcion 4:  Filtrar             *')
                print('*************************************')
                
                print('Selecciona una opcion: \t')
                x=int(input('>: '))

                switch.get(x,default)()

                print('___________________')
                respuesta=input('Desea continuar? Si/No:\n')
                os.system('cls')
                if respuesta == 'no' or respuesta =='NO' or respuesta =='No' or respuesta =='nO' or respuesta =='n' or respuesta =='N':
                    os.system('cls')
                    print('*************************************')
                    print('\n Programa finalizado por el usuario')
        if x=='Ejecutivo_area':
           
            switch={1: lambda :Tique.tiqueIn(nombre), 2:Tique.verTiques, 3:Tique.actualizarTique, 4:Tique.filtrarTique}
            while respuesta=='si' or respuesta=='Si' or respuesta=='Si' or respuesta=='SI' or respuesta=='sI' or respuesta=='s':
                print('*************************************')
                print('***      Ejecutivo de Area        ***')
                print('*************************************')
                print('*    opcion 1:  Agregar tique       *')
                print('*    opcion 2:  Ver tiques          *')
                print('*    opcion 3:  Actualizar tique    *')
                print('*    opcion 4:  Filtrar             *')
                print('*************************************')
                
                print('Selecciona una opcion: \t')
                x=int(input('>: '))

                switch.get(x,default)()

                print('___________________')
                respuesta=input('Desea continuar? Si/No:\n')
                os.system('cls')
                if respuesta == 'no' or respuesta =='NO' or respuesta =='No' or respuesta =='nO' or respuesta =='n' or respuesta =='N':
                    os.system('cls')
                    print('*************************************')
                    print('\n Programa finalizado por el usuario')
        if x=='Jefe_mesa':
            switch={1:Tique.verTiques, 2:lambda :Tique.tiqueIn(nombre), 3:Tique.actualizarTique, 4:Tique.borrarTique, 5:Tique.filtrarTique }

            while respuesta=='si' or respuesta=='Si' or respuesta=='Si' or respuesta=='SI' or respuesta=='sI' or respuesta=='s':
                print('***************************************')
                print('***          Jefe de Mesa           ***')
                print('***************************************')
                print('*   opcion 1: Ver listado de tiques  **')
                print('*   opcion 2: Agregar tiques         **')
                print('*   opcion 3: Actualizar tique       **')
                print('*   opcion 4: Borrar                 **')
                print('*   opcion 5: Filtrar tiques         **')
                print('***************************************')

                print('Selecciona una opcion: \t')
                x=int(input('>: '))
                switch.get(x,default)()
                print('___________________')
                respuesta=input('Desea continuar? Si/No:\n')
                os.system('cls')
                if respuesta == 'no' or respuesta =='NO' or respuesta =='No' or respuesta =='nO' or respuesta =='n' or respuesta =='N':
                    os.system('cls')
                    print('*************************************')
                    print('\n Programa finalizado por el usuario')

        if x=='Administrador':
            switch={1:Tique.verTiques, 2:lambda :Tique.tiqueIn(nombre),3:Tique.actualizarTique, 4:Tique.borrarTique, 5:Tique.filtrarTique, 6:Usuario.crearUsr, 7:Usuario.verUsr, 8:Usuario.editUsr, 9:Usuario.eliminarUsr }

            while respuesta=='si' or respuesta=='Si' or respuesta=='Si' or respuesta=='SI' or respuesta=='sI' or respuesta=='s':
                print('*************************************')
                print('***         Administrador         ***')
                print('*************************************')
                print('*    opcion 1: Ver listado          *')
                print('*    opcion 2: Agregar tiques       *')
                print('*    opcion 3: Actualizar tique     *')
                print('*    opcion 4: Borrar tique         *')
                print('*    opcion 5: Filtrar tiques       *')
                print('*    opcion 6: Agregar usuario      *')
                print('*    opcion 7: Ver usuarios         *')
                print('*    opcion 8: Editar usuario       *')
                print('*    opcion 9: ELiminar usuario     *')
                print('*************************************')

                print('Selecciona una opcion: \t')
                x=int(input('>: '))
                switch.get(x,default)()
                print('___________________')
                respuesta=input('Desea continuar? Si/No:\n')
                os.system('cls')
                if respuesta == 'no' or respuesta =='NO' or respuesta =='No' or respuesta =='nO' or respuesta =='n' or respuesta =='N':
                    os.system('cls')
                    print('*************************************')
                    print('\n Programa finalizado por el usuario')

        if x=='Cliente':
            switch={1:Tique.verTiques }

            while respuesta=='si' or respuesta=='Si' or respuesta=='Si' or respuesta=='SI' or respuesta=='sI' or respuesta=='s':
                print('*************************************')
                print('***           Cliente             ***')
                print('*************************************')
                print('*    opcion 1: Ver tiques           *')
                print('*************************************')

                print('Selecciona una opcion: \t')
                x=int(input('>: '))
                switch.get(x,default)()
                print('___________________')
                respuesta=input('Desea continuar? Si/No:\n')
                os.system('cls')
                if respuesta == 'no' or respuesta =='NO' or respuesta =='No' or respuesta =='nO' or respuesta =='n' or respuesta =='N':
                    os.system('cls')
                    print('*************************************')
                    print('\n Programa finalizado por el usuario')         

    def login():
        upass=[]
        ulevel=[]
        for usr in usuarios:
            usuariopassw={usr['usr']:usr['passw']}
            usuarionivel={usr['usr']:usr['rol']}
            upass.append(usuariopassw)
            ulevel.append(usuarionivel)
        print('***************************************')
        print('*****    VERSION DE PRUEBA #1      ****')
        print('***************************************')   
        print('** Utiliza alguno de estos usuarios: **')  
        print('_______________________________________')
        print(upass)
        print('')
        print('Usuario:')
        nombre=input(">: ")
        print('Passw: ')
        passw=input('>: ')
        usuario={nombre:passw}
    
        #validador de usuario y contrasena
        if usuario in upass:
        
        
            if {nombre:'Ejecutivo_mesa'} in ulevel:
                os.system('cls')
                print('Welcome '+ nombre)
    
                Main.main(nombre,'Ejecutivo_mesa')

            if {nombre:'Ejecutivo_area'} in ulevel:
                os.system('cls')
                print('Welcome '+ nombre)
    
                Main.main(nombre,'Ejecutivo_area')
                
    
            if {nombre:'Jefe_mesa'} in ulevel:
                os.system('cls')
                print('Welcome '+ nombre)
    
                Main.main(nombre,'Jefe_mesa')
    
            if {nombre:'Administrador'} in ulevel:
                os.system('cls')
                print('Welcome '+ nombre)
    
                Main.main(nombre,'Administrador')

            if {nombre:'Cliente'} in ulevel:
                os.system('cls')
                print('Welcome '+ nombre)
    
                Main.main(nombre,'Cliente')
    
        else:
                print('(!) Error') 
                pass


Main.login()