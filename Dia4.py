from random import randint

nombre_usuario = input('Dime tu nombre: ')
print(f'Bueno {nombre_usuario} he pensado un numero que esta entre el 1 y el 100, y tienes solo 8 intenos'
      f' para adivinarlo, cual crees que es el numero?')
numero_usuario = None
print(type(numero_usuario))
numero = randint(0, 55)
intentos = 8

while numero_usuario != numero and intentos != 0:
    intentos -= 1
    numero_usuario = int(input('Dime tu numero: '))
    if numero_usuario == numero:
        print(f'Excelenete {nombre_usuario} tu numero es el correcto,')
    elif numero_usuario < 0 or numero_usuario > 101:
        print(f"{nombre_usuario} tu numero debe ser mayor a 1 y menor a 100")
        print(f'Te quedan {intentos} intentos ')
    elif numero_usuario < numero:
        print(f'{nombre_usuario} el numero que alejiste es menor al que he pensado')
        print(f'Te quedan {intentos} intentos')
    elif numero_usuario > numero:
        print(f'{nombre_usuario} el numero que alejiste es mayor al que he pensado')
        print(f'Te quedan {intentos} intentos')
else:
    if intentos == 0:
        print(f'Lo siento te haz quedado sin intentos, el numero secreto era {numero}')
    else:
        print(f'Lo lograste en el intento {intentos}')







