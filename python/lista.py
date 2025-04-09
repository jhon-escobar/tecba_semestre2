
# lista_notas =[]
# print ("insgrese las  notas de lsoestudiante ")

# nombre = input('ingrese el nombre del estudiante ')
# lista_notas.append(nombre)
# notas = int(input('ingrese su nota '))
# lista_notas.append(notas)
                  
# print(lista_notas)


# lista = ['maracuya','coco', 'pitajay']
# print(lista)
# lista.append( 'frutaepan')
# print(lista)
# lista.remove('coco')
# print(lista)

# def maximo_numero(lista):
#     if not lista:
#          return None
#     return max(lista)

# numeros = [3, 9, 10, 45,888]
# resultado = maximo_numero(numeros)
# print(f"el valor maximo de la lista es ;{resultado}")

def minimo_numero(lista):
    if not lista:
         return None
    return min(lista)

numeros = [3, 9, 10, 45,888]
resultado = minimo_numero(numeros)
print(f"el valor maximo de la lista es ;{resultado}")
