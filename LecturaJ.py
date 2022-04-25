import json

f = open('clientes.json',) 
   
data = json.load(f)

#for i in data: 
#    print(f"{i['nombre']}")
print(len(data))

Datos = len(data)
for i in range(1):
   Nit1 = data[i]['nit']
   print(Nit1)
   
var1 = "Dato"
var21 = "'"+var1+"'"
var1 = 'C3'
var1 = 'C4'
var1 = 'C5'

   
cadena1 = {}
cadena1 = []
for i in range(3):
   cadena1.append({
      'C1': var1,
      'C2': 'Mannock',
      'C3': 27,
      'C4': 7.17})


print(cadena1)
   

cadena = """
[ 
  {
      "codigo":"1",
      "descripcion":"papas",
      "precio":"13.45"
  },
  {
      "codigo":"2",
      "descripcion":"manzanas",
      "precio":"45"
  }  
]  
"""
print(cadena)

diccionario = json.loads(cadena)
print(diccionario)
lista=json.loads(cadena)
print(lista) # imprimimos una lista
for elemento in lista:
    print(f"{elemento['codigo']}")

