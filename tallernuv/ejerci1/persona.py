
class Persona:
    contador_dni = 1

    class CategoriaIMC:
        BAJO_PESO = -1
        NORMAL = 0
        SOBREPESO = 1
        OBESIDAD = 2
        OBESIDAD_EXTREMA = 3

    def __init__(self, documento='', nombre='', edad=0, sexo='M', peso=0.0, altura=0.0):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__generar_dni()

    def __generar_dni(self):
        dni = Persona.contador_dni
        Persona.contador_dni += 1
        return dni

    def __comprobar_sexo(self, sexo):
        return sexo if sexo in ('M', 'F') else 'M'

    def calcular_imc(self):
        if self.__altura == 0:
            return Persona.CategoriaIMC.BAJO_PESO
        imc = self.__peso / ((self.__altura / 100) ** 2)
        if imc < 18.5:
            return Persona.CategoriaIMC.BAJO_PESO
        elif imc <= 24.9:
            return Persona.CategoriaIMC.NORMAL
        elif imc <= 29.9:
            return Persona.CategoriaIMC.SOBREPESO
        elif imc <= 39.9:
            return Persona.CategoriaIMC.OBESIDAD
        else:
            return Persona.CategoriaIMC.OBESIDAD_EXTREMA

    def es_mayor_de_edad(self):
        return self.__edad >= 18

    def listar_informacion(self):
        genero = 'Masculino' if self.__sexo == 'M' else 'Femenino'
        imc_cat = {
            -1: 'por debajo del peso',
            0: 'normal',
            1: 'con sobrepeso',
            2: 'con obesidad',
            3: 'en obesidad extrema o de alto riesgo'
        }
        imc_resultado = self.calcular_imc()
        return f"Hola {self.__nombre}, tu código dentro del sistema es {self.__dni}. Tu identificación es {self.__documento}. Tu edad es {self.__edad} años. Tu género es {genero}. Tu Peso es {self.__peso} kg y tu Altura es {self.__altura} cm. Al calcular tu IMC concluimos que tu peso está: {imc_cat[imc_resultado]}."

    def set_documento(self, documento):
        self.__documento = documento

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = self.__comprobar_sexo(sexo)

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura
