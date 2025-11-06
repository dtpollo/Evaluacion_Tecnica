from Empleados import Empleado
from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto
from EmpleadoPorHoras import EmpleadoPorHoras

# Instancio un empleado a tiempo completo
Emp_completo = EmpleadoTiempoCompleto(
    nombre="Rafaela",
    apellido="Peralta",
    id="1",
    salario_base=1000.00
)

# Instancio un empleado por horas
Emp_por_horas = EmpleadoPorHoras(
    nombre="Daniel",
    apellido="Troya",
    id="2",
    salario_base=700.00,
    horas_trabajadas=45,
    pago_por_hora=12.50
)

print("INFORMACION\n")
Emp_completo.mostrarInformacion()
print("-" * 20)
Emp_por_horas.mostrarInformacion()
print("-" * 20)

# Polimorfismo
lista_de_empleados = [Emp_completo, Emp_por_horas]

print("\nPOLIMORFISMO\n")
for empleado in lista_de_empleados:
    empleado.mostrarInformacion() 
    print("-" * 20)