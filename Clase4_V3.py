class Paciente: #se crea la clase pacientes
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    #se crea la clase sistema que hereda informacion y metodos de la clase pacientes
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self,cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, c):
        if self.verificarPaciente(c) == False:
            return None
        for p in self.__lista_pacientes:
            #retorne la cedula y la comparo con la ingresada por teclado
            if c == p.verCedula():
                return p #si encuentro el paciente lo retorno
    def verPacientePorNombre(self, nombre):
        pacientes_por_nombre=[]
        for p in self.__lista_pacientes:
            if p.verNombre().lower().startswith(nombre.lower()):
                pacientes_por_nombre.append()
        return pacientes_por_nombre      
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como1
                #  el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            menu2 = int(input("¿Como desea buscar el paciente?: \n1. Por cédula, \n2 Por nombre ")) 
            if menu2 == 1:
                cedula = int(input("Ingrese la cedula: "))
                p = sis.verDatosPaciente(cedula)
                if Paciente != None:
                    print("Nombre: " + p.verNombre()) 
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio()) 
                else:
                    print("No existe un paciente con esa cedula")
            elif menu2 == 2: 
                nombre = input("Ingrese el nombre: ")
                Paciente = sis.verPacientePorNombre(nombre)
                if Paciente:
                    for p in Paciente:
                      print("Nombre: " + p.verNombre()) 
                      print("Cedula: " + str(p.verCedula())) 
                      print("Genero: " + p.verGenero()) 
                      print("Servicio: " + p.verServicio()) 
                else: 
                    print("No existe un paciente con ese nombre")  
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
