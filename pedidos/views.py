from django.shortcuts import render
from .menu import Menu

def home(request):
    return render(request, 'pedidos/home.html')

def cliente(request):
    return render(request, 'pedidos/cliente.html')

def mesero(request):
    return render(request, 'pedidos/mesero.html')

def comida(request):
    menu = Menu()
    # Obtenemos los platillos de comida
    comida = menu.obtener_platillos().filter(categoria='comida')
    
    # Definimos las categorías de comida
    categorias_comida = [
        {"nombre": "Para Botanear", "url": "para_botanear"},
        {"nombre": "Hamburguesas", "url": "hamburguesas"},
        {"nombre": "Tacos Ahogados", "url": "tacos_ahogados"},
        {"nombre": "Tacos y Quesadillas", "url": "tacos_y_quesadillas"},
        {"nombre": "Especialidades", "url": "especialidades"},
        {"nombre": "Platillos", "url": "platillos"},
        {"nombre": "Para Tostadear", "url": "para_tostadear"},
        {"nombre": "Brochetas", "url": "brochetas"}
    ]
    
    return render(request, 'pedidos/comida.html', {'platillos': comida, 'categorias': categorias_comida})

def bebidas(request):
    menu = Menu()
    # Obtenemos los platillos de bebidas
    bebidas = menu.obtener_platillos().filter(categoria='bebida')
    
    # Definimos las categorías de bebidas
    categorias_bebidas = [
        {"nombre": "Cerveza", "url": "cerveza"},
        {"nombre": "Peceras", "url": "peceras"},
        {"nombre": "Cocteles", "url": "cocteles"},
        {"nombre": "Especial", "url": "especial"},
        {"nombre": "Tequila", "url": "tequila"},
        {"nombre": "Vodka", "url": "vodka"},
        {"nombre": "Brandy", "url": "brandy"},
        {"nombre": "Refresco", "url": "refresco"}
    ]
    
    return render(request, 'pedidos/bebidas.html', {'platillos': bebidas, 'categorias': categorias_bebidas})



def detalle_bebida(request, categoria):
    # Diccionario de bebidas por categoría
    bebidas_por_categoria = {
        "cerveza": ["Cerveza Modelo", "Corona", "Heineken"],
        "peceras": ["Pecera Roja", "Pecera Azul"],
        "cocteles": ["Margarita", "Mojito"],
        "especial": ["Especial de la Casa"],
        "tequila": ["Tequila Blanco", "Tequila Reposado"],
        "vodka": ["Vodka Absolut", "Vodka Smirnoff"],
        "brandy": ["Brandy Torres", "Brandy Fundador"],
        "refresco": ["Coca-Cola", "Sprite", "Fanta"]
    }
    # Obtener la lista de bebidas para la categoría seleccionada
    bebidas = bebidas_por_categoria.get(categoria, [])
    return render(request, 'pedidos/detalle_bebida.html', {'bebidas': bebidas, 'categoria': categoria})


def detalle_comida(request, categoria):
    # Diccionario de platillos por categoría
    comida_por_categoria = {
        "para_botanear": ["Dedos de Queso", "Papas Gajo"],
        "hamburguesas": ["Hamburguesa Arrachera", "Hamburguesa Pollo"],
        "tacos_ahogados": ["Tacos Camarón", "Tacos Pastor"],
        "tacos_y_quesadillas": ["Quesadilla de Carne", "Taco de Carnitas"],
        "especialidades": ["Cecina con Camarones", "NIDADA Combo"],
        "platillos": ["Costillas (12 Pzas)", "Boneless"],
        "para_tostadear": ["Tostada de Mariscos", "Tostada de Ceviche"],
        "brochetas": ["Brochetas de Pollo", "Brochetas de Camarón"]
    }
    # Obtener la lista de platillos para la categoría seleccionada
    platillos = comida_por_categoria.get(categoria, [])
    return render(request, 'pedidos/detalle_comida.html', {'platillos': platillos, 'categoria': categoria})

def editar_orden(request):
    # Lógica para editar la orden
    return render(request, 'pedidos/editar_orden.html')
