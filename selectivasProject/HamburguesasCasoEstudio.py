#Definir constantes
PRECIO_SENCILLA =20000
PRECIO_DOBLE =25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

#Funcion para calcular el precio
def calcular_precio(tipo_hamburguesa, medio_pago, cantidad):
    #Definir los precios segun el tipo de hamburguesa
    if tipo_hamburguesa == 1:
        precio = PRECIO_SENCILLA
        descripcion = "Sencilla"
    elif tipo_hamburguesa == 2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"
    elif tipo_hamburguesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"
    else:
        return None # Tipo  de hamburguesa no valido!

    #Calcular el total sin cargos
    total_sin_cargo = precio * cantidad
    #Aplicar impuesto si el medio de pago es targeta
    if medio_pago == 1:
        impuesto = round(total_sin_cargo * IMPUESTO_TARJETA)
    else:
        impuesto = 0
    total = round(total_sin_cargo + impuesto)

    #retonar datos relevantes
    return descripcion, precio, cantidad, impuesto, total

#funcion para generar mensaje
def generar_mensaje(descripcion, precio, cantidad, impuesto, total):
    return (f"tipo de hamburguesa: {descripcion}\n"
            f"precio: {precio}\n"
            f"cantidad: {cantidad}\n"
            f"impuesto: {impuesto}\n"
            f"total: {total}\n")

#funcion pata validar los datos
def validar_datos(tipo_hamburguesa, medio_pago, cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and 0 <= cantidad > 0:
        resultado = calcular_precio(tipo_hamburguesa, medio_pago, cantidad)
        #print(resultado: ", resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad, impuesto, total)
        print("---------------------\n" + mensaje)
    else:
        print("verifique las opciones ingresadas.")

#entradas2
tipo_hamburguesa = int(input("ingrese tipo de hamburguesa \n1. Sencilla \n2. Doble \n3. Triple \n"))
medio_pago = int(input("ingrese un medio de pago \n1. Tarjeta \n2. otro \n"))
cantidad = int(input("ingrese la cantidad: "))

#salidas
validar_datos(tipo_hamburguesa, medio_pago, cantidad)
