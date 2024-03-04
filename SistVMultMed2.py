class Medicamento: #se contruye una clase medicamentos
    def __init__(self):
        #Todos los atributos de la clase son privados
        self.__nombre = "" #
        self.__dosis = 0 
    #definimos los setters y getters de la clase para asignar y ver datos
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota: #se crea la clase mascota 
    #Todos los atributos de la clase son privados
    #la clase mascota hereda de la clase medicamentos en una relacion de muchos a muchos 
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
     #definimos los setters y getters de la clase para asignar y ver datos   
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    def medicamentos(self,medicamento):
        nombre_medicamento= [m.verNombre()for m in self.__lista_medicamentos]
        if medicamento.verNombre() in nombre_medicamento:
            print(f"El medicamento {medicamento.verNombre()} ya está en la lista")
            return False 
        else:
            self.__lista_medicamentos(medicamento)
            return True
    def eliminar_medicamento(self, medicamento):
        for medicamento in self.__lista_medicamentos:
            if medicamento.verNombre()== medicamento:
                self.__lista_medicamentos.remove(medicamento)
                return True
            else: 
                print(f"el paciente no tiene medicamento con el nombre {medicamento}")
class sistemaV:
    #Sistema hereda tanto de medicamentos como de mascotas 
    #es la clase en la que finalmete se valida el ingreso de la informacion
    def __init__(self): #polimorfimos, tanto caninos como felinos heredan los metodos de la clase mascota para ser almacenados en a lista
        self.__lista_mascotas = {
            "caninos": [],
            "felinos": []

        }

    #definimos los setters y getters de la clase para asignar y ver datos
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        tipo = mascota.verTipo()
        if tipo == "canino":
            self.__lista_mascotas["caninos"].append(mascota)
        else:
            self.__lista_mascotas["felinos"].append(mascota)
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia,tipo):
        if tipo in self.__lista_mascotas:
            lista_mascota2 = self.__lista_mascotas[tipo]
            for mascota in lista_mascota2:
                if historia == mascota.verHistoria():
                    return mascota.verFecha()
        

    def verMedicamento(self,historia,tipo):
        #busco la mascota y devuelvo el atributo solicitado
        if tipo in self.__lista_mascotas:
            lista_mascota2 = self.__lista_mascotas[tipo]
            for mascota in lista_mascota2:
                if historia == mascota.verHistoria():
                    return mascota.verLista_Medicamentos()
        return None
    
    #cada vez que se realiza un llamado de metodos como vermedicamentos
    #estos estan alamcenados en lista_medicamentos creada en la clase mascota
    #que a su vez obtiene la informacion de la clase medicamento obtenida mediante los metodos que en ella existen

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                for medicamento in lista_med: #validamos que el medicamento no se repita en el mismo paciente 
                    mas.medicamentos(medicamento)
                servicio_hospitalario.ingresarMascota(mas)
                

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            tipo = input("Ingrese el tipo de mascota: ")
            fecha = servicio_hospitalario.verFechaIngreso(q,tipo)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            tipo = input('Ingrese el tipo de mascota: ')
            medicamento = servicio_hospitalario.verMedicamento(q,tipo) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

