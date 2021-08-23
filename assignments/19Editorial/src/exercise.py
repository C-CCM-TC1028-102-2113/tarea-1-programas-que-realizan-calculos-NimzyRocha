def main():
    #escribe tu código abajo de esta línea
    pass
import math
print ('Dame el número de palabras:')
palabras=int(input())
if palabras>475:
    pag= math.ceil (palabras/475)
else:
    pag=1
costo= (pag*60)-((pag*60)*.10)
print('El costo de la publicación es:',costo)

if __name__ == '__main__':
    main()
