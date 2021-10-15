
def entrada():
    vueltas=0
    ingresando=True
    lista_numeros=[]
    while ingresando==True:
        if vueltas==0:
            print('por favor ingrese un numero')
            numero=float(input())
        else:
            print('por favor ingrese otro numero')
            numero=float(input())
        lista_numeros.append(numero)
        if vueltas>0:
            decidir=True
            while decidir==True:
                print('quiere ingresar otro numero?.... escriba (si) para ingresar otro numero, escriba (no) para terminar')
                decision=input()
                if decision=='si' or decision=='SI':
                    ingresando=True
                    break
                elif decision=='no' or decision=='NO':
                    ingresando=False
                    break
                else:
                    print('la opcion no es valida')
        vueltas=vueltas+1
    return lista_numeros

def media(lista_numeros):
    cantidad=len(lista_numeros)
    movimiento=cantidad-1
    suma=0
    while movimiento>=0:
        suma=suma+lista_numeros[movimiento]
        movimiento=movimiento-1

    media=suma/cantidad
    media=round(media,2)
    return media

def desviacion(lista_numeros,media):
    cantidad=len(lista_numeros)
    movimiento=cantidad-1
    suma=0
    while movimiento>=0:
        operacion=media-lista_numeros[movimiento]
        operacion=operacion**2
        suma=suma+operacion
        movimiento=movimiento-1
    cantidad=cantidad-1
    division=suma/cantidad
    resultado=division**0.5
    resultado=round(resultado,2)
    return resultado

def main():
    lista_numeros=entrada()
    media1=media(lista_numeros)
    resultado=desviacion(lista_numeros,media1)
    print('la media es: ', media1)
    print('la desviacion estandar es: ', resultado)

main()