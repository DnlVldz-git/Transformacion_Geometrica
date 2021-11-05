import cv2
import numpy as np
import math

img = cv2.imread('imagen.png')

filas, columnas = img.shape[:2]

resp = 1
while(resp!=0):
    print("---------------------------------")    
    print("---------------------------------")
    print("Introduzca la operación que desea realizar")
    print("Traslación = 1")
    print("Rotación = 2")
    print("Escala = 3")
    print("Deformación = 4")
    print("---------------------------------")
    print("Salir = 0")
    resp = int(input())
    if(resp == 1):
        print("Introduzca la cantidad de traslación en el eje de las X")
        tX = float(input())
        print("Introduzca la cantidad de traslación en el eje de las Y")
        tY = float(input())
        
        matrix = [[1, 0, tX], #x 
                 [0, 1, tY]] #y
        t = np.float32(matrix)

        img3 = cv2.warpAffine(img, t, (filas, columnas))

        cv2.imshow('original', img)
        cv2.imshow('trasladada', img3)
        cv2.waitKey()

    elif(resp == 2):
        print("Introduzca la cantidad de grados de rotación")

        alfa = int(input())        

        x = filas/2
        y = columnas/2

        matrix = [[(math.cos(math.radians(alfa))), (math.sin(math.radians(alfa))), x - x*math.cos(math.radians(alfa)) - y*math.sin(math.radians(alfa))], #x 
                 [(-math.sin(math.radians(alfa))), (math.cos(math.radians(alfa))), y + x*math.sin(math.radians(alfa)) - y*math.cos(math.radians(alfa))]] #y
        t = np.float32(matrix)

        img3 = cv2.warpAffine(img, t, (filas, columnas))

        cv2.imshow('original', img)
        cv2.imshow('rotada', img3)
        cv2.waitKey()
    elif(resp == 3):
        print("Introduzca la cantidad de escala en el eje de las X")
        eX = float(input())
        print("Introduzca la cantidad de escala en el eje de las Y")
        eY = float(input())
        
        matrix = [[eX, 0, 0], #x 
                 [0, eY, 0]] #y
        t = np.float32(matrix)

        img3 = cv2.warpAffine(img, t, (filas, columnas))

        cv2.imshow('original', img)
        cv2.imshow('escalada', img3)
        cv2.waitKey()
    elif(resp == 4):
        print("Introduzca la cantidad de inclinación en el eje de las X")
        iX = float(input())
        print("Introduzca la cantidad de inclinación en el eje de las Y")
        iY = float(input())
        
        matrix = [[1, iX, 0], #x 
                 [iY, 1, 0]] #y
        t = np.float32(matrix)

        img3 = cv2.warpAffine(img, t, (filas, columnas))

        cv2.imshow('original', img)
        cv2.imshow('inclinada', img3)
        cv2.waitKey()