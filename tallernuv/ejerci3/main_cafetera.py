
from cafetera import Cafetera

def ejecutar_cafetera():
    cafetera = Cafetera()
    cafetera.llenar_cafetera()
    print(f"Café disponible: {cafetera.cantidad_actual} cc")
    servido = cafetera.servir_taza(250)
    print(f"Se sirvieron {servido} cc")
    cafetera.agregar_cafe(300)
    print(f"Café disponible después de agregar: {cafetera.cantidad_actual} cc")
    cafetera.vaciar_cafetera()
    print(f"Café disponible después de vaciar: {cafetera.cantidad_actual} cc")

ejecutar_cafetera()
