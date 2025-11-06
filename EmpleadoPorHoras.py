from Empleados import Empleado

class EmpleadoPorHoras(Empleado):
    # Inicializa al EmpleadoPorHoras
    def __init__(self, nombre, apellido, id, salario_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, apellido, id, salario_base)
        self._horas_trabajadas = horas_trabajadas
        self._pago_por_hora = pago_por_hora

    # Calcula el salario total (Polimorfismo)
    def calcularSalario(self):
        return self._horas_trabajadas * self._pago_por_hora