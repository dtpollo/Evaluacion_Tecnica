from Empleados import Empleado

class EmpleadoTiempoCompleto(Empleado):
    # Calcula el salario base (Polimorfismo)
    def calcularSalario(self):
        return self._salario_base + self._salario_base * 0.10