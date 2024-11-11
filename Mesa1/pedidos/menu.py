from .models import Platillo
from .models import Bebida
from django.db import models
class Menu:
    def __init__(self):
        self.platillos = Platillo.objects.filter(disponible=True)
        self.bebidas = Bebida.objects.filter(disponible=True)  # Asegúrate de tener esto

    def obtener_platillos(self):
        # Aquí es donde colocas el código actualizado
        platillos_por_categoria = {}
        
        for platillo in self.platillos:
            categoria = platillo.categoria
            if categoria not in platillos_por_categoria:
                platillos_por_categoria[categoria] = []
            platillos_por_categoria[categoria].append({
                "nombre": platillo.nombre,
                "precio": platillo.precio
            })
        
        return platillos_por_categoria

    def obtener_bebidas(self):
            bebidas_por_categoria = {}
            
            for bebida in self.bebidas:
                categoria = bebida.categoria
                if categoria not in bebidas_por_categoria:
                    bebidas_por_categoria[categoria] = []
                bebidas_por_categoria[categoria].append({
                    "nombre": bebida.nombre,
                    "precio": bebida.precio
                })
            
            return bebidas_por_categoria
    
