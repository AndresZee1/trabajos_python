
from persona import Persona

def ejecutar_personas():
    while True:
        documento = input("Documento: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ").upper()
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (cm): "))

        p1 = Persona(documento, nombre, edad, sexo, peso, altura)
        p2 = Persona(documento, nombre, edad, sexo)
        p3 = Persona()
        p3.set_documento("000000")
        p3.set_nombre("Persona por defecto")
        p3.set_edad(25)
        p3.set_sexo('F')
        p3.set_peso(55)
        p3.set_altura(160)

        personas = [p1, p2, p3]

        for p in personas:
            print(p.listar_informacion())
            print("Mayor de edad:", "Sí" if p.es_mayor_de_edad() else "No")
            print("-" * 30)

        cont = input("¿Desea ingresar otra persona? (s/n): ").lower()
        if cont != 's':
            break

ejecutar_personas()
