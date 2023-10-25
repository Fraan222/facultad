
### COLLATZ CONJETURE ###


n = -1
while n <= 0:
    n = int(input("Input: "))
    if n <= 0:
        print("wrong, it must be > 0:")

longitud = 0
acu = 0
primer = n
mayor = None
orbita = [n]
while n != 1:
    if n % 2 == 1:
        n = 3 * n + 1

    else:
        n = n // 2

    orbita.append(n)
    acu += n
    longitud += 1
    if mayor == None or n > mayor:
        mayor = n

acumulador = acu + primer
longitud_real = longitud + 1
print("Length: ", longitud_real)
promedio = acumulador / longitud_real
print("the highest number: ", mayor)
print("average: ", round(promedio, 1))
print("orbit: ", orbita)
