from lifestore_file import lifestore_products as products, lifestore_sales as sales, lifestore_searches as searches
from operator import itemgetter
from collections import Counter
import os
import numpy as np 

usuarios = [['Hugo', '123', 'Admin'], ['Paco', '456', 'No Admin'], ['Luis','789', 'Admin'], ['Cesar', '321', 'No Admin']]

usuario = 'Hugo'
password = '123'
#usuario = input('Ingresa nombre de usuario: ')
#password = input('Ingresa contraseña de usuario: ')

os.system('cls' if os.name == 'nt' else 'clear')

admins = list(filter(lambda x: str(x[2]) == 'Admin', usuarios))
#no_admins = list(filter(lambda x: str(x[2]) == 'No Admin', usuarios))

nombres_todos = list(map(itemgetter(0), usuarios)) 
nombres_admins = list(map(itemgetter(0), admins))

inicio_sesion = 'No'
if usuario in nombres_todos:
  if usuario in nombres_admins:
    usuario_encontrado = [usuario, password, 'Admin']
    if usuario_encontrado in usuarios:
      print('Inicio de sesión exitoso, BIENVENIDO.')
      inicio_sesion = 'Si'
    else:
      print('Contraseña incorrecta.')
  else:
    print('Usuario encontrado, pero no es administrador.')
else:
  print('No Existe Usuario')

"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""

# Listado de los 100 Productos con más búsquedas

busquedas_producto = list(map(itemgetter(1), searches)) 

nombres_productos = list(map(itemgetter(1), products))
#id_productos = list(map(itemgetter(0), products))

categorias_productos = list(map(itemgetter(3), products))

categorias_unicas = np.unique(categorias_productos)

print(categorias_unicas)

#categoriayproducto = list(zip(nombres_productos, categorias_productos))

busquedas = dict(Counter(busquedas_producto))

busquedas_copia = busquedas.copy()

busquedas_categoria = []

for busqueda in busquedas:
  busqueda_nombre = nombres_productos[int(busqueda)]
  llave_nueva = busqueda_nombre
  llave_vieja = busqueda
  busquedas_copia[llave_nueva] = busquedas_copia.pop(llave_vieja)
  
  #[categorias_productos[int(busqueda)]] * int(busquedas_copia[llave_nueva]) # es la cantidad del nuevo producto

busquedas = busquedas_copia.copy()
busquedas_copia.clear()

busquedas_ordenadas = sorted(busquedas.items(), key=lambda x: x[1], reverse=True)

input('\nHit Key para ver Listado de 100 productos más buscados.\n')

os.system('cls' if os.name == 'nt' else 'clear')
print('100 PRODUCTOS MÁS BUSCADOS:\n')

for busqueda in busquedas_ordenadas:
  print('Búsqueda de producto:', busqueda[0]+'. Realizada:',busqueda[1],'veces.\n')
  #print(products.index(busqueda[0]))

#print('\nListado de productos más buscados\n', *busquedas_ordenadas[:101], sep='\n')
#print('\n'.join(map(str, busquedas_ordenadas)))

#input('\nHit Key para ver Listado de 100 productos menos buscados.')
#os.system('cls' if os.name == 'nt' else 'clear')

#print('\nListado de productos menos buscados\n', *busquedas_ordenadas[100::-1], sep='\n')


productos_audifonos = []
prodcutos_bocinas = []
productos_dicos_duros = []
busquedas_memorias_usb = []
busquedas_pantallas = []
busquedas_procesadores = []
busquedas_tarjetas_video = []
busquedas_tarjetas_madre = []

for product in products:
  any(e[1] == search for e in data)
  



# Listado de los Productos con más Ventas

compras_producto = list(map(itemgetter(1), sales))
compras = dict(Counter(compras_producto))

compras_copia = compras.copy()
for compra in compras:
  compra_nombre = nombres_productos[int(compra)]
  llave_nueva = compra_nombre
  llave_vieja = compra
  compras_copia[llave_nueva] = compras_copia.pop(llave_vieja)

compras = compras_copia.copy()
compras_copia.clear()
compras_ordenadas = sorted(compras.items(), key=lambda x: x[1], reverse=True)

input('\nHit Key para ver Listado de 50 productos más vendidos.')
os.system('cls' if os.name == 'nt' else 'clear')

print('50 PRODUCTOS MÁS VENDIDOS:\n')
for venta in compras_ordenadas:
  print('Venta de producto:', venta[0]+'. Realizada:',venta[1],'veces.\n')

#print('\nListado de 50 productos más vendidos\n', *compras_ordenadas[:51], sep='\n')

#print('\nListado de 50 productos menos vendidos\n', *compras_ordenadas[50::-1], sep='\n')

input('\nHit Key para ver Listado de 50 productos menos vendidos por categoría.')
os.system('cls' if os.name == 'nt' else 'clear')
print('50 PRODUCTOS MENOS VENDIDOS - categoría:\n')

