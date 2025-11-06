class Empleado:
    # Inicializo los atributos que tengra la clase Principal, con el constructor
    def __init__(self, nombre, apellido, id, salario_base):
        self._nombre = nombre
        self._apellido = apellido
        self._ID = id
        self._salario_base = salario_base

    # Metodo 1 (Se puede sobreescribir en clases hijas)
    # Calcula el salario de los empleados
    def calcular_salario(self):
        return self._salario_base

    # Metodo 2
    # Imprime los datos del empleado
    def mostrar_informacion(self):
        print(f"Empleado: {self._nombre} {self._apellido}")
        print(f"ID: {self._ID}")
        print(f"Salario: $ {round(self.calcular_salario(), 2)}")