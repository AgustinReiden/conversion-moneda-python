# Paso 1:Definir el valor actual del euro y dolar con respecto al peso mexicano

tipo_cambio_eur_a_mex = 23.70
tipo_cambio_usd_a_mex = 20.75

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)

tipo_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ").upper()

# Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente
# Paso 5: Mostrar el resultado de la conversión al usuario

if tipo_conversion == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mex
    print("El resultado de la conversión de EUR a MEX es: ", resultado)
elif tipo_conversion == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mex
    print("El resultado de la conversión de USD a MEX es: ", resultado)
else:
    print("No está disponible este tipo de conversión actualmente")
