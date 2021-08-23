def main():
    #escribe tu código abajo de esta línea
    pass
pprint ("Dame el saldo del mes anterior:")
saldoanterior = float (input())
pprint ("Dame los ingresos:")
ingresos = float (input())
pprint ("Dame los egresos:")
egresos = float(input())
pprint ("Dame el numero de cheques expedidos:")
cheques = int(input())
saldoanterior= (saldoanterior-(saldoanterior*0.075))
saldomes=ingresos-egresos
cheques=cheques*13
saldo=(saldomes-(saldomes*0.075)) - cheques + saldoanterior
saldo= round (saldo,2)
print ("El saldo final es:", saldo)
if __name__ == '__main__':
    main()
