# pedidos/menu.py
from .models import Platillo

class Menu:
    def __init__(self):
        self.platillos = Platillo.objects.filter(disponible=True)

    def obtener_platillos(self):
        return self.platillos
