def main():
print ('Dame el número de mensajes:')
mensajes= int(input())
print ('Dame el número de megas:')
megas= float(input())
print ('Dame el número de minutos:')
minutos= int(input())
minutos= round (minutos,2)
costo=(mensajes*0.80)+(megas*0.80)+(minutos*0.80)
print ('El costo mensual es:', costo)
    pass


if __name__ == '__main__':
    main()
