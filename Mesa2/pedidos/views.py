from django.shortcuts import render
from .menu import Menu
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import ClienteSession  # Importa ClienteSession
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'pedidos/home.html')

def cliente(request):
    return render(request, 'pedidos/cliente.html')

def mesero(request):
    return render(request, 'pedidos/mesero.html')


def bebidas(request):
    categorias_bebidas = [
        {"nombre": "Cerveza", "url": "cerveza"},
        {"nombre": "Peceras", "url": "peceras"},
        {"nombre": "Cocteles", "url": "cocteles"},
        {"nombre": "Especial", "url": "especial"},
        {"nombre": "Tequila", "url": "tequila"},
        {"nombre": "Whisky", "url": "whisky"},
        {"nombre": "Vodka", "url": "vodka"},
        {"nombre": "Brandy", "url": "brandy"},
        {"nombre": "Refresco", "url": "refresco"},
        {"nombre": "Bebidas", "url": "bebidas"},
    ]
    return render(request, 'pedidos/bebidas.html', {'categorias': categorias_bebidas})

# Diccionario de menú de bebidas en la vista detalle_bebida
bebidas_menu = {
    "cerveza": [
        {"nombre": "Corona Clara", "precio": 35},
        {"nombre": "Corona Clara - Cubeta", "precio": 185},
        {"nombre": "Corona Ámbar", "precio": 35},
        {"nombre": "Corona Ámbar - Cubeta", "precio": 185},
        {"nombre": "Victoria", "precio": 35},
        {"nombre": "Victoria - Cubeta", "precio": 185},
        {"nombre": "XX Lager", "precio": 35},
        {"nombre": "XX Lager - Cubeta", "precio": 185},
        {"nombre": "Miller Caguama", "precio": 85},
        {"nombre": "Corona Familiar", "precio": 80},
        {"nombre": "Modelo Especial", "precio": 90},
        {"nombre": "Michelada Chica", "precio": 40},
        {"nombre": "Michelada Litro", "precio": 75},
        {"nombre": "Michelada Piña Chica", "precio": 40},
        {"nombre": "Michelada Piña Litro", "precio": 80},
        {"nombre": "Michelada Mango Chica", "precio": 40},
        {"nombre": "Michelada Mango Litro", "precio": 80},
        {"nombre": "Michelada con Camarones", "precio": 145},
        {"nombre": "Chelada Chica", "precio": 45},
        {"nombre": "Chelada Litro", "precio": 75},
        {"nombre": "Preparado Chica", "precio": 25},
        {"nombre": "Preparado Litro", "precio": 35}
    ],
    "peceras": [
        {"nombre": "Pecera Ahogada", "precio": 700},
        {"nombre": "Pecera Sangrada", "precio": 700},
        {"nombre": "Pecera Mentirosa", "precio": 700}
    ],
    "cocteles": [
        {"nombre": "Bacahorchata", "precio": 100},
        {"nombre": "Sangrona", "precio": 100},
        {"nombre": "Mentirosa", "precio": 100},
        {"nombre": "Paloma", "precio": 100},
        {"nombre": "Vampiro", "precio": 100},
        {"nombre": "Sex on the Beach", "precio": 100},
        {"nombre": "Ahogada", "precio": 100},
        {"nombre": "Pitufo", "precio": 100}
    ],
    "especial": [
        {"nombre": "Mojito Clásico Chico", "precio": 70},
        {"nombre": "Mojito Clásico Grande", "precio": 120},
        {"nombre": "Mojito Frutos Rojos Chico", "precio": 75},
        {"nombre": "Mojito Frutos Rojos Grande", "precio": 130},
        {"nombre": "Piña Colada Chico", "precio": 65},
        {"nombre": "Piña Colada Grande", "precio": 115},
        {"nombre": "Carajillo Chico", "precio": 85},
        {"nombre": "Perla Negra Chico", "precio": 90},
        {"nombre": "Gin Tonic Chico", "precio": 80},
        {"nombre": "Margarita Chico", "precio": 75},
        {"nombre": "Mezcal Chico (3x4 Promo)", "precio": 50},
        {"nombre": "Cornada Chico", "precio": 30},
        {"nombre": "Shot Baby Mango Chico (3x4 Promo)", "precio": 50},
        {"nombre": "Cartucho Chico (3x4 Promo)", "precio": 50}
    ],
    "tequila": [
        {"nombre": "Centenario Plata - Pomo", "precio": 800},
        {"nombre": "Centenario Plata - Cuba", "precio": 65},
        {"nombre": "Centenario Plata - Litro", "precio": 125},
        {"nombre": "Centenario Reposado - Pomo", "precio": 800},
        {"nombre": "Centenario Reposado - Cuba", "precio": 65},
        {"nombre": "Centenario Reposado - Litro", "precio": 125},
        {"nombre": "Maestro Dobel Diamante - Pomo", "precio": 1600},
        {"nombre": "Maestro Dobel Diamante - Cuba", "precio": 115},
        {"nombre": "Maestro Dobel Diamante - Litro", "precio": 200},
        {"nombre": "1800 Cristalino - Pomo", "precio": 1700},
        {"nombre": "1800 Cristalino - Cuba", "precio": 130},
        {"nombre": "1800 Cristalino - Litro", "precio": 240},
        {"nombre": "Hacienda de Tepa - Pomo", "precio": 660},
        {"nombre": "Hacienda de Tepa - Cuba", "precio": 60},
        {"nombre": "Hacienda de Tepa - Litro", "precio": 110}
    ],
    "whisky": [
        {"nombre": "Black & White - Pomo", "precio": 650},
        {"nombre": "Black & White - Cuba", "precio": 60},
        {"nombre": "Black & White - Litro", "precio": 110},
        {"nombre": "Red Label - Pomo", "precio": 760},
        {"nombre": "Red Label - Cuba", "precio": 70},
        {"nombre": "Red Label - Litro", "precio": 130},
        {"nombre": "Buchanan's - Pomo", "precio": 1600},
        {"nombre": "Buchanan's - Cuba", "precio": 120},
        {"nombre": "Buchanan's - Litro", "precio": 220},
        {"nombre": "Centenario Plata - Pomo", "precio": 1100},
        {"nombre": "Centenario Plata - Cuba", "precio": 100}
    ],
    "vodka": [
        {"nombre": "Smirnoff Tamarindo - Pomo", "precio": 650},
        {"nombre": "Smirnoff Tamarindo - Cuba", "precio": 60},
        {"nombre": "Smirnoff Tamarindo - Litro", "precio": 100},
        {"nombre": "Absolut - Pomo", "precio": 700},
        {"nombre": "Absolut - Cuba", "precio": 70},
        {"nombre": "Absolut - Litro", "precio": 125}
    ],
    "brandy": [
        {"nombre": "Torres 5 - Pomo", "precio": 600},
        {"nombre": "Torres 5 - Cuba", "precio": 55},
        {"nombre": "Torres 5 - Litro", "precio": 100},
        {"nombre": "Torres 10 - Pomo", "precio": 750},
        {"nombre": "Torres 10 - Cuba", "precio": 70},
        {"nombre": "Torres 10 - Litro", "precio": 125}
    ],
    "refresco": [
        {"nombre": "Coca-Cola", "precio": 30},
        {"nombre": "Squirt", "precio": 25},
        {"nombre": "Sidral Aga", "precio": 25},
        {"nombre": "Agua Mineral", "precio": 25},
        {"nombre": "Sprite", "precio": 25}
    ],
    "bebidas": [
        {"nombre": "Horchata Chica", "precio": 45},
        {"nombre": "Horchata Litro", "precio": 75},
        {"nombre": "Horchata Jarra", "precio": 130},
        {"nombre": "Limonada Chica", "precio": 40},
        {"nombre": "Limonada Litro", "precio": 70},
        {"nombre": "Limonada Jarra", "precio": 140},
        {"nombre": "Naranjada Chica", "precio": 45},
        {"nombre": "Naranjada Litro", "precio": 80},
        {"nombre": "Naranjada Jarra", "precio": 130},
        {"nombre": "Piñada Chica", "precio": 45},
        {"nombre": "Piñada Litro", "precio": 80}
    ]
}


def detalle_bebida(request, categoria):
    # Obtener los productos de la categoría seleccionada
    bebidas = bebidas_menu.get(categoria, [])

    # Manejo de la sesión para cantidades seleccionadas
    if "selected_bebidas" not in request.session:
        request.session["selected_bebidas"] = {}

    selected_items = request.session["selected_bebidas"].get(categoria, {})

    for bebida in bebidas:
        bebida["cantidad"] = selected_items.get(bebida["nombre"], 0)

    request.session.modified = True

    return render(request, 'pedidos/detalle_bebida.html', {
        "categoria": categoria,
        "bebidas": bebidas,
    })

def editar_orden(request):
    # Lógica para editar la orden
    return render(request, 'pedidos/editar_orden.html')

def para_botanear(request):
    return render(request, 'pedidos/comida/botanear.html')


# Vista para el menú de categorías de comida
def comida(request):
    # Definimos las categorías de comida con nombre y URL
    categorias_comida = [
        {"nombre": "Para Botanear", "url": "para_botanear"},
        {"nombre": "Hamburguesas", "url": "hamburguesas"},
        {"nombre": "Tacos Ahogados", "url": "tacos_ahogados"},
        {"nombre": "Tacos y Quesadillas", "url": "tacos_y_quesadillas"},
        {"nombre": "Especialidades", "url": "especialidades"},
        {"nombre": "Platillos", "url": "platillos"},
        {"nombre": "Para Tostadear", "url": "para_tostadear"},
        {"nombre": "Brochetas", "url": "brochetas"},
    ]
    
    return render(request, 'pedidos/comida.html', {'categorias': categorias_comida})

# Vista para los detalles de cada categoría de comida
def detalle_comida(request, categoria):
    # Diccionario que contiene platillos por categoría
    menu = {
        "para_botanear": [
            {"nombre": "Alitas 6 Piezas", "precio": 85},
            {"nombre": "Alitas 12 Piezas", "precio": 170},
            {"nombre": "Costillas 6 Piezas", "precio": 100},
            {"nombre": "Costillas 12 Piezas", "precio": 185},
            {"nombre": "Costillas Kilo", "precio": 330},
            {"nombre": "Boneless", "precio": 110},
            {"nombre": "Papas a la Francesa", "precio": 75},
            {"nombre": "Cecina", "precio": 150},
            {"nombre": "Cecina con Camarones", "precio": 220},
            {"nombre": "Dedos de Queso (5 Piezas)", "precio": 95},
            {"nombre": "Nidada Combo", "precio": 200},
        ],
        "hamburguesas": [
            {"nombre": "Hamburguesa de Arrachera", "precio": 110},
            {"nombre": "Hamburguesa de Pollo", "precio": 100},
            {"nombre": "Hamburguesa Mar y Tierra", "precio": 135},
            {"nombre": "Hamburguesa Especial", "precio": 120},
        ],
        "tacos_ahogados": [
            {"nombre": "Taco de Pastor", "precio": 85},
            {"nombre": "Taco de Carnitas", "precio": 90},
            {"nombre": "Taco de Camarón", "precio": 110},
        ],
        "tacos_y_quesadillas": [
            {"nombre": "Taco de Pastor", "precio": 20},
            {"nombre": "Quesadilla de Pastor", "precio": 30},
            {"nombre": "Taco de Chorizo", "precio": 20},
            {"nombre": "Quesadilla de Chorizo", "precio": 30},
            {"nombre": "Taco de Bistec", "precio": 20},
            {"nombre": "Quesadilla de Bistec", "precio": 30},
            {"nombre": "Taco de Arrachera", "precio": 25},
            {"nombre": "Quesadilla de Arrachera", "precio": 35},
        ],
        "especialidades": [
            {"nombre": "Papas San Isidro", "precio": 85},
            {"nombre": "Taco Abrevadero", "precio": 60},
            {"nombre": "Taco Gobernador", "precio": 65},
            {"nombre": "Volcán Mar y Tierra", "precio": 200},
            {"nombre": "Pulpo Luminaria", "precio": 320},
            {"nombre": "Coctel Abrevadero", "precio": 150},
        ],
        "platillos": [
            {"nombre": "Camarones a la Diabla", "precio": 200},
            {"nombre": "Camarones al Mojo de Ajo", "precio": 190},
            {"nombre": "Camarones Encintado", "precio": 220},
            {"nombre": "Filete Empanizado", "precio": 120},
            {"nombre": "Filete al Ajillo", "precio": 140},
            {"nombre": "Pulpo a la Plancha", "precio": 290},
            {"nombre": "Mariscada del Tío", "precio": 250},
        ],
        "para_tostadear": [
            {"nombre": "Aguachile Pradera (pieza)", "precio": 70},
            {"nombre": "Aguachile Pradera (orden)", "precio": 230},
            {"nombre": "Aguachile Fuego Noche (pieza)", "precio": 70},
            {"nombre": "Aguachile Fuego Noche (orden)", "precio": 230},
            {"nombre": "Ceviche (pieza)", "precio": 50},
            {"nombre": "Ceviche (orden)", "precio": 175},
            {"nombre": "Ceviche de Camarón (pieza)", "precio": 65},
            {"nombre": "Ceviche de Camarón (orden)", "precio": 260},
        ],
        "brochetas": [
            {"nombre": "Brocheta de Arrachera", "precio": 50},
            {"nombre": "Brocheta de Camarón", "precio": 60},
            {"nombre": "Brocheta Combinada", "precio": 70},
        ],
    }

    # Si existe la clave 'categoria_actual' en la sesión y es diferente a la categoría actual,
    # limpia los platillos de la sesión
    if request.session.get('categoria_actual') != categoria:
        request.session['platillos_comida'] = []
        request.session['categoria_actual'] = categoria  # Actualiza la categoría actual en la sesión

       # Obtén los platillos de la categoría seleccionada
    platillos = menu.get(categoria, [])

    # Inicializa el diccionario en la sesión si no existe
    if "selected_items" not in request.session:
        request.session["selected_items"] = {}

    # Carga las cantidades guardadas en la sesión para la categoría actual
    selected_items = request.session["selected_items"].get(categoria, {})

    # Incluye las cantidades guardadas en cada platillo
    for platillo in platillos:
        platillo["cantidad"] = selected_items.get(platillo["nombre"], 0)

    # Actualiza la sesión para reflejar los cambios
    request.session.modified = True

    return render(request, 'pedidos/comida/detalle_comida.html', {
        "categoria": categoria,
        "platillos": platillos,
    })
# En views.py
def resumen_pedido(request):
    selected_items = request.session.get("selected_items", {})
    selected_bebidas = request.session.get("selected_bebidas", {})

    # Instancia de Menu y asignación de los platillos
    menu = Menu().obtener_platillos()
    print("Platillos obtenidos:", menu)  # Depuración
    if not isinstance(menu, dict):
        menu = {}  # Manejo de caso si menu no tiene el formato esperado

    todos_items = []
    total = 0

    # Procesar los platillos de comida
    for categoria, items in selected_items.items():
        for nombre, cantidad in items.items():
            if cantidad > 0:
                platillos = menu.get(categoria, [])
                precio = next((p["precio"] for p in platillos if p["nombre"] == nombre), 0)
                print(f"Nombre: {nombre}, Precio encontrado: {precio}")  # Depuración
                subtotal = precio * cantidad
                todos_items.append({"nombre": nombre, "cantidad": cantidad, "precio": precio, "subtotal": subtotal})
                total += subtotal

    # Procesar las bebidas
    bebidas_menu = Menu().obtener_bebidas()  # Suponiendo un método similar para bebidas
    print("Bebidas obtenidas:", bebidas_menu)  # Depuración
    if not isinstance(bebidas_menu, dict):
        bebidas_menu = {}

    for categoria, items in selected_bebidas.items():
        for nombre, cantidad in items.items():
            if cantidad > 0:
                bebidas = bebidas_menu.get(categoria, [])
                precio = next((b["precio"] for b in bebidas if b["nombre"] == nombre), 0)
                print(f"Bebida: {nombre}, Precio encontrado: {precio}")  # Depuración
                subtotal = precio * cantidad
                todos_items.append({"nombre": nombre, "cantidad": cantidad, "precio": precio, "subtotal": subtotal})
                total += subtotal

    return render(request, 'pedidos/resumen_pedido.html', {
        "todos_items": todos_items,
        "total": total,
    })



def iniciar_sesion_invitado(request, mesa_id):
    """
    Vista para iniciar sesión como cliente (invitado) al escanear un código QR.
    Crea o recupera la sesión de cliente para la mesa especificada.
    """
    # Crear o recuperar la sesión de cliente para esta mesa
    cliente_session, created = ClienteSession.objects.get_or_create(mesa_id=mesa_id)
    if not cliente_session.estado:
        cliente_session.estado = True
        cliente_session.save()
    return redirect('pedidos:home')  # Redirige a la vista principal de cliente (home)

@login_required
def cerrar_sesion_invitado(request, mesa_id):
    """
    Vista para que el mesero cierre la sesión del cliente.
    Solo accesible para usuarios autenticados con permisos.
    """
    # Verificar si el usuario es staff (mesero)
    if request.user.is_staff:
        cliente_session = get_object_or_404(ClienteSession, mesa_id=mesa_id)
        cliente_session.estado = False  # Cerrar la sesión de cliente
        cliente_session.save()
        return redirect('pedidos:editar_orden')  # Redirige a la vista de edición de orden
    else:
        return redirect('pedidos:home')  # Redirige a la página principal si no tiene permisos
    
    # pedidos/views.py

@login_required
def editar_orden(request):
    """
    Vista para que el mesero administre y cierre sesiones de clientes.
    Solo accesible para usuarios autenticados y con permisos de staff.
    """
    if request.user.is_staff:
        sesiones = ClienteSession.objects.filter(estado=True)  # Sesiones activas
        return render(request, 'pedidos/editar_orden.html', {'sesiones': sesiones})
    else:
        return redirect('pedidos:home')


def iniciar_sesion_invitado(request, mesa_id):
    from .models import ClienteSession  # Coloca la importación aquí
    cliente_session, created = ClienteSession.objects.get_or_create(mesa_id=mesa_id)
    if not cliente_session.estado:
        cliente_session.estado = True
        cliente_session.save()
    return redirect('pedidos:home')

class CustomLoginView(LoginView):
    template_name = 'pedidos/login.html'  # Asegúrate de tener una plantilla de inicio de sesión

def reiniciar_pedido(request):
    # Elimina la clave 'selected_items' de la sesión, que es donde se almacenan los pedidos
    if 'selected_items' in request.session:
        del request.session['selected_items']
    if 'selected_bebidas' in request.session:
        del request.session['selected_bebidas']
    
    # Establece `modified` para que Django guarde los cambios en la sesión
    request.session.modified = True
    
    # Redirige al resumen del pedido (o a otra página si prefieres)
    return redirect('pedidos:resumen_pedido')

def seleccionar_mesa(request, mesa_id):
    # Establece la mesa seleccionada en la sesión
    request.session['mesa_id'] = mesa_id
    return redirect('pedidos:resumen_pedido')  # Redirige al resumen del pedido o cualquier otra página adecuada

def actualizar_cantidad(request):
    if request.method == "POST":
        categoria = request.POST.get("categoria")
        nombre_platillo = request.POST.get("nombre")
        cantidad = int(request.POST.get("cantidad", 0))

        # Asegura que la sesión tenga la estructura correcta
        if "selected_items" not in request.session:
            request.session["selected_items"] = {}

        if categoria not in request.session["selected_items"]:
            request.session["selected_items"][categoria] = {}

        # Actualiza la cantidad en la sesión
        request.session["selected_items"][categoria][nombre_platillo] = cantidad
        request.session.modified = True

        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def actualizar_cantidad_bebida(request):
    
    if request.method == "POST":
        categoria = request.POST.get("categoria")
        nombre_bebida = request.POST.get("nombre")
        cantidad = int(request.POST.get("cantidad", 0))

        # Inicializa 'selected_bebidas' en la sesión si no existe
        if "selected_bebidas" not in request.session:
            request.session["selected_bebidas"] = {}

        # Inicializa la categoría en la sesión si no existe
        if categoria not in request.session["selected_bebidas"]:
            request.session["selected_bebidas"][categoria] = {}

        # Actualiza la cantidad de la bebida seleccionada
        request.session["selected_bebidas"][categoria][nombre_bebida] = cantidad
        request.session.modified = True

        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

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