"""
Enunciado:
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir una función principal para lanzar el programa, control de ejecución del script principal con la variable __name__ y al menos una función simple con parámetros y retorno de resultado. El programa debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo, con un único ciclo para todo el proceso), y debe hacer lo siguiente sin usar un menú de opciones:
1. Determinar la cantidad de palabras que tienen cuatro o más caracteres e incluyen tres o más vocales (en mayúscula o minúscula). Por ejemplo, en el texto: “Hay muchas vocales en este escrito.” Respuesta: hay 2 palabras que cumplen: “vocales” y “escrito”.
2. Determinar el promedio entero de caracteres por palabra, de las palabras que tienen una o más veces una ‘s’ o una o más veces una ‘n’ o una o más veces una ‘p’ (minúsculas o mayúsculas). Por ejemplo, en el texto: “La pelota sirve apenas.” hay cuatro palabras que cumplen el criterio (“pelota”, “sirve”, “apenas”). Entre las tres suman 17 caracteres, por lo que el promedio entero pedido es 5 caracteres por palabra.
3. Determinar cuántas palabras empiezan y terminan con el mismo caracter (si es letra, en minúscula o en mayúscula en forma indistinta). Por ejemplo, en el texto “Sabes que ese oso es pardo y malo.” Hay 4 palabras que cumplen: “Sabes”, “ese”, “oso”, “y”. Notar que la palabra “y” solo contiene un carácter, pero cumple en forma trivial con la condición.
4. Determinar cuántas palabras incluyen la expresión “pa” (con cualquiera de sus letras en minúscula o en maúscula) pero no contienen al mismo tiempo una “t”. Por ejemplo, en el texto: “La patada hizo que el tiro raspara el palo.” Hay dos palabras que cumplen: “raspara” y “palo”. La palabra “patada” no cuenta porque si bien tiene “pa”, incluye también una “t”.
"""
def es_vocal(car):
    return car in "aeiouAEIOUáéíóúÁÉÍÓÚ"

def calc_promedio(n1, n2):
    if n2 == 0:
        return None
    promedio = n1 // n2
    return promedio

def principal():
    # INICIALIZACIÓN
    cl = hay_vocal = 0
    cpal = cpal_vocales = cpal_nsp = acu = cpal_coincidentes = cpal_pa = 0
    hay_s = hay_p = hay_n = hay_p2 = hay_pa = hay_t = False
    primera_letra = ult_letra = " "

    # CUERPO
    cadena = input("Ingrese un texto: ")
    for car in cadena:
        if car != " " and car != ".":
            cl += 1
            # 1
            if es_vocal(car):
                hay_vocal += 1

            # 2
            if car == "s" or car == "S":
                hay_s = True

            if car == "p" or car == "P":
                hay_p = True

            if car == "n" or car == "N":
                hay_n = True

            # 3
            if cl == 1:
                primera_letra = car

            ult_letra = car

            # 4
            if car == "t" or car == "T":
                hay_t = True

            if car == "p" or car == "P":
                hay_p2 = True
            else:
                if hay_p2 and (car == "a" or car == "A"):
                    hay_pa = True
                hay_p2 = False

        else:
            cpal += 1
            # 1
            if cl >= 4 and hay_vocal >= 3:
                cpal_vocales += 1
            # 2
            if hay_n or hay_s or hay_p:
                cpal_nsp += 1
                acu += cl

            # 3
            if primera_letra == ult_letra:
                cpal_coincidentes += 1

            # 4
            if hay_pa and not hay_t:
                cpal_pa += 1


            cl = hay_vocal = 0
            hay_s = hay_p = hay_n = hay_p2 = hay_pa = hay_t = False
            ult_letra = primera_letra = " "

    print("Cantidad de palabras con 4 o más caractéres y 3 o más vocales: ", cpal_vocales)
    promedio = calc_promedio(acu, cpal_nsp)
    print("Palabras con ´n´, ´s´ o ´p´: ", cpal_nsp)
    print("Promedio de palabras con al menos una o más ´n´, ´s´ o ´p´: ", promedio)
    print("Palabras que empiezan y terminan con la misma letra: ", cpal_coincidentes)
    print("Palabras con la expresión ´pa´ y sin ´t´: ", cpal_pa)

if __name__ == '__main__':
    principal()
