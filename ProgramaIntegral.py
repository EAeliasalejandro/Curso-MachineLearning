#Codigo par ejemplificar una tienda de abarrotes
#//////CLASE CLIENTE//////
class Cliente:
#Constructor y parametros
 def __init__(self,nombre,telefono,producto):
  self.nombre = nombre
  self.telefono = telefono
  self.producto = producto

print('\n' + '*Persona 1 llega a la tienda*')
nombre=input('Cliente 1 puede teclear su nombre: ')
telefono=input('Cliente 1 puede teclear su telefono: ')
producto=input('Cliente 1 puede teclear su producto a comprar: ')
#instanciar objeto
Cliente1 = Cliente(nombre,telefono,producto)

print('\n' + '*Persona 2 llega a la tienda*')
nombre=input('Cliente 2 puede teclear su nombre: ')
telefono=input('Cliente 2 puede teclear su telefono: ')
producto=input('Cliente 2 puede teclear su producto a comprar: ')
#instanciar objeto
Cliente2 = Cliente(nombre,telefono,producto)

print('\n' + '*Persona 3 llega a la tienda*')
nombre=input('Cliente 3 puede teclear su nombre: ')
telefono=input('Cliente 3 puede teclear su telefono: ')
producto=input('Cliente 3 puede teclear su producto a comprar: ')
#instanciar objeto
Cliente3 = Cliente(nombre,telefono,producto)

#Arreglo de objetos
ListaClientes = [Cliente1,Cliente2,Cliente3]

#Imprimir en un txt el nombre de los clientes
miArchivo= open ('nombreClientes.txt','w')
miArchivo.write(ListaClientes[0].nombre + '\n')
miArchivo.write(ListaClientes[1].nombre + '\n')
miArchivo.write(ListaClientes[2].nombre)
miArchivo.close()
