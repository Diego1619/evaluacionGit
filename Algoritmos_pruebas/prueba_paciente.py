# Algoritmo de prueba para el microservicio de pacientes

def validar_paciente(nombre, documento):
    if nombre and documento:
        return "Paciente válido"
    return "Datos incompletos"


# Pruebas
print(validar_paciente("Diego Cuero", "1080832041"))
print(validar_paciente("", ""))