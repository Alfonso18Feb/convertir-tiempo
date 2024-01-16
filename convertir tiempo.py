import math

#def tiempo(s,m,h,d,a):
numero=float(input('escribe un numero:'))
print('1.segundos')
print('2.minutos')
print('3.horas')
print('4.dia')
sal=int(input('elige en que esta es numero:'))
print('1.segundos')
print('2.minutos')
print('3.horas')
print('4.dia')
agua=int(input('elige numero para convertir:'))
print('el numero es:')
if sal==agua:
    print(numero)
elif sal==2 and agua==1 or sal==3 and agua==2:
    print(numero*60)
elif sal==3 and agua==1:
    print(numero*360)
elif sal==4 and agua==3:
    print(numero*24)
elif sal==1 and agua==2 or sal==2 and agua==3:
    print(numero/60)
elif sal==1 and agua==3:
    print(numero/360)
elif sal==3 and agua==4:
    print(numero/24)
elif sal==4 and agua==2 or agua==1:
    if agua==2:
        print(numero*24*60)
    else:
        print(numero*24*360)
elif sal==1 or sal==2 and agua==4:
    if sal==1:
        print(numero/(24*360))
    else:
        print(numero/(60*24))