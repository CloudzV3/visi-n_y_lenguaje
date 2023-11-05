import math
from PIL import Image
import io
import matplotlib.pyplot as plt

def abrir_BMP(file_path):
    with open(file_path, "rb") as bmp_file:
        bmp_enc = bmp_file.read(14)
        pixel_begin = int.from_bytes(bmp_enc[10:14], byteorder='little')

        bmp_info = bmp_file.read(40)
        columnas = int.from_bytes(bmp_info[4:8], byteorder='little')
        filas = int.from_bytes(bmp_info[8:12], byteorder='little')
        bits_per_pixel = int.from_bytes(bmp_info[14:16], byteorder='little')
        # Calcular la cantidad de bytes por fila (debe ser un múltiplo de 4)
        bytes_por_fila = ((columnas * 24 + 31) // 32) * 4
        bmp_file.seek(pixel_begin)
        pixeles = bmp_file.read()

    return {
        'columnas': columnas,
        'filas': filas,
        'pixeles': pixeles,
        'bytes_por_fila': bytes_por_fila,
        'bits': bits_per_pixel
    }
def compensar(bits):
    if bits != 24:
        flag=True
    else: 
        flag= False
    return flag

def borrar_alpha(pixeles, filas, columnas, bytes_por_fila):
    alpha_channel = 0
    new_pixeles = []
    for y in range(filas):
        for x in range(columnas):
            index = (y * bytes_por_fila)+ (x * 3)
            index=index+alpha_channel
            alpha_channel = alpha_channel + 1
            new_pixeles.append(pixeles[index])
            new_pixeles.append(pixeles[index+1])
            new_pixeles.append(pixeles[index+2])
    return new_pixeles

def mostrar_imagen_bmp(filas, columnas, bytes_por_fila, pixeles, ):
    # Crear una imagen en blanco
    alpha_channel = 0
    imagen = Image.new("RGB", (columnas, filas))
    for y in range(filas):
        for x in range(columnas):
            index = (y * bytes_por_fila)+ (x * 3)
            b = pixeles[index]
            g = pixeles[index + 1]
            r = pixeles[index + 2]
            a = filas - y - 1
            imagen.putpixel((x,a), (r, g, b))
    imagen.show()



def histograma (filas, columnas, bytes_por_fila, pixeles):
    pix_data_r = []
    pix_data_g = []
    pix_data_b = []
    for y in range(filas):
        for x in range(columnas):
            index = (y * bytes_por_fila)+ (x * 3)
            b = pixeles[index]
            g = pixeles[index + 1]
            r = pixeles[index + 2]
            pix_data_r.append(r)
            pix_data_g.append(g)
            pix_data_b.append(b)
    hist=[]  
    for i in range(256):
        r = pix_data_r.count(i)
        g = pix_data_g.count(i)
        b = pix_data_b.count(i)
        hist.append((i,r,g,b))

    num_pix = [dato[0] for dato in hist]
    rep_r = [dato[1] for dato in hist]
    rep_g = [dato[2] for dato in hist]
    rep_b = [dato[3] for dato in hist]
    show_hist(num_pix, rep_r, 'rojo')
    show_hist(num_pix, rep_g, 'verde')
    show_hist(num_pix, rep_b, 'azul')

def show_hist(num_pix, rep, canal):
    plt.bar(num_pix, rep, width=1)
    plt.xlabel('Número de píxeles')
    plt.ylabel('Repeticiones') 
    plt.title('Histograma canal '+ canal)
    plt.show()

def sumar(filas, filas2, columnas, columnas2, pixeles, pixeles2):
    if filas != filas2 or columnas != columnas2:
        raise ValueError("Las imágenes deben tener las mismas dimensiones")
    new_pixel_data = []
    for i in range(len(pixeles)):
        pixel_sum = pixeles[i] + pixeles2[i]
        new_pixel_data.append(min(pixel_sum, 255)) 
    return new_pixel_data

def restar(filas, filas2, columnas, columnas2, pixeles, pixeles2):
    if filas != filas2 or columnas != columnas2:
        raise ValueError("Las imágenes deben tener las mismas dimensiones")
    new_pixel_data = []
    for i in range(len(pixeles)):
        pixel_res = pixeles[i] - pixeles2[i]
        new_pixel_data.append(max(pixel_res, 0))

    return new_pixel_data

#Imagen 1
ruta = "Image.bmp"

bmp_data = abrir_BMP(ruta)

columnas = bmp_data['columnas']
filas = bmp_data['filas']
bits = bmp_data['bits']
pixeles = bmp_data['pixeles']
bytes_por_fila = bmp_data['bytes_por_fila']
alpha_exist= compensar(bits)
if alpha_exist is True:
    pixeles = borrar_alpha(pixeles, filas, columnas, bytes_por_fila)
mostrar_imagen_bmp(filas, columnas, bytes_por_fila, pixeles)
hist = int(input("Desea conocer el histograma de la imagen?"))
if hist == 1:
    histograma(filas, columnas, bytes_por_fila, pixeles)

#Imagen 2
ruta2 = "c.bmp"

bmp_data2 = abrir_BMP(ruta2)

columnas2 = bmp_data2['columnas']
filas2 = bmp_data2['filas']
bits2 = bmp_data2['bits']
pixeles2 = bmp_data2['pixeles']
bytes_por_fila2 = bmp_data2['bytes_por_fila']
alpha_exist2= compensar(bits2)
if alpha_exist2 is True:
    pixeles2 = borrar_alpha(pixeles2, filas2, columnas2, bytes_por_fila2)
mostrar_imagen_bmp(filas2, columnas2, bytes_por_fila2, pixeles2)

hist = int(input("Desea conocer el histograma de la imagen?"))
if hist == 1:
    histograma(filas2, columnas2, bytes_por_fila2, pixeles2)

suma = int(input("Desea sumar las images?"))
if suma == 1:
    result = sumar(filas, filas2, columnas, columnas2, pixeles, pixeles2)
    mostrar_imagen_bmp(filas, columnas, bytes_por_fila, result)

resta = int(input("Desea restar las images?"))
if resta == 1:
    result = restar(filas, filas2, columnas, columnas2, pixeles, pixeles2)
    mostrar_imagen_bmp(filas, columnas, bytes_por_fila, result)
