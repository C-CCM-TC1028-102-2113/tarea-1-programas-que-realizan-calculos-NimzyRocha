def main():
    #escribe tu código abajo de esta línea
    pass
print("Dame un número:")
numero=int(input())
pares=0
numero1= numero/1000
numero1= int(numero1)
numero2= (numero/100)
numero2= (numero/100)-(numero1*10)
numero2= int(numero2)
numero3= (numero/10)
numero3= (numero/10)-(numero1*100)-(numero2*10)
numero3= int(numero3)
numero4= numero-(numero1*1000)-(numero2*100)-(numero3*10)
numero4= int(numero4)
if (numero1%2)== 0:
    pares=pares+1
else:
    pares=pares

if (numero2%2)== 0:
    pares=pares+1
else:
    pares=pares

if (numero3%2)== 0:
    pares=pares+1
else:
    pares=pares

if (numero4%2)== 0:
    pares=pares+1
else:
    pares=pares

print("El número de dígitos pares es:", pares)

if __name__ == '__main__':
    main()
