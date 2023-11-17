# Promedio de salario y clasificación en bajo,normal y mayor a lo normal
#
# Juan percibio  u$ 300  de ene a jun
#                u$ 500  de jul A oct
#                U$ 700  DE NOV A DIC    
#
# Siendo: 
#           Salario bajo menos de u$ 300
#                       normal de u$ 300 a 900
#        más de lo normal: más de u$ 900   


class Persona :
    def __init__(self,nombre="Nombre",
                 apellido="apellido",
                 num_legajo="NNNN",
                 sueldo_anual=0,
                 antiguedad=0,
                 salario_promedio=0
                ):
        self.nombre=nombre
        self.apellido=apellido
        self.num_legajo=num_legajo
        self.sueldo_anual=sueldo_anual
        self.antiguedad=antiguedad
        self.salario_promedio=salario_promedio

    def promed_saldo(self):
        self.salario_promedio = self.sueldo_anual / 12
        print(" \n El salario promedio mensual es de u$ ",self.salario_promedio)
    
    def clasificacion_sueldo(self):

        if self.salario_promedio < 300 :
            print(" \n Sueldo bajo \n")
        elif self.salario_promedio > 300 and self.salario_promedio< 900:
            print(" \n Sueldo normal \n")
        elif self.salario_promedio  > 900:
            print(" \n Sueldo mejor de lo normal \n")

    def calc_saldo_anual (self):
        meses=["Enero","Febrero","Marzo","Abril","mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        suma_sueldo = 0
        for mes in meses:       
           sueldo = int(input("Ingrese el sueldo de mes de "+(mes)+" "))
           self.sueldo_anual = suma_sueldo + sueldo   
           sueldo = suma_sueldo 
           suma_sueldo = self.sueldo_anual    
        print(" \n El Sueldo anual es u$ ",self.sueldo_anual)

# se instancia el objeto Juan pasando los atributos nombre,apelido,num_legajo y antiguedad     

juan = Persona ( 
                nombre="Juan",
                apellido="Gonzalez",
                num_legajo=4548,
                antiguedad=15
               )
#Se llama al metodo calc_saldo_anual y se ingresa 
# los sueldos mensuales para calcular el sueldo anual 

juan.calc_saldo_anual()

#En relación al calc_saldo_anual se calcula 
# el promedio mensual de saldo llamando al metodo promed_saldo

juan.promed_saldo()
juan.clasificacion_sueldo()


# Creando un nuevo objeto se podrá almacenar datos de otras personas
# y usar los metodos ya creados para calcular y clasificar los sueldos mensuales
# ej: Sueldos de Enero a Abril 400,
#                        Mayo a Agosto 600,
#                        Sep a dic 800


Maria = Persona ( 
                nombre="Maria",
                apellido="Bennitez",
                num_legajo=5040,
                antiguedad=10
                )

Maria.calc_saldo_anual()
Maria.promed_saldo()
Maria.clasificacion_sueldo()











