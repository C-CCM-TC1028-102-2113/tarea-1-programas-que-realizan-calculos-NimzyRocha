def main():
pprint ('Dame el número de mensajes:')
mensajes= int(input())
pprint ('Dame el número de megas:')
megas= float(input())
pprint ('Dame el número de minutos:')
minutos= int(input())
minutos= round (minutos,2)
costo=(mensajes*0.80)+(megas*0.80)+(minutos*0.80)
pprint ('El costo mensual es:', costo)
    pass


if __name__ == '__main__':
    main()
