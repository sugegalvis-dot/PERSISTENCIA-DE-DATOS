ruta = r"C:\Users\juand\Downloads\mbox.txt"

salida = r"C:\Users\juand\Downloads\mensajes.txt"

correos = []

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        if linea.startswith("From:"):
            correo = linea.split()[1]
            correos.append(correo)

with open(salida, "w", encoding="utf-8") as nuevo:
    for correo in correos[::-1]:
        mensaje = correo + " enviado [ok]"
        print(mensaje)
        nuevo.write(mensaje + "\n")

print("Archivo guardado correctamente en:", salida)