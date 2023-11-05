
numero_magico = 12345679 
numero_usuario = int(input('Numero entre 1 y 9: '))
if numero_usuario >= 1 and numero_usuario <= 9 :
    # numero_usuario = numero_usuario * 9
    numero_usuario *= 9
    # numero_magico = numero_magico * numero_usuario
    numero_magico *= numero_usuario
    print(f'Numero magico: {numero_magico}')
else: 
    print('el numero no esta entre 1 y 9')

