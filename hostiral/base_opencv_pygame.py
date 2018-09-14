import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import random

#INICIALIZAMOS OPENCV Y PYGAME SCREEN
camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])

#ESTABLECEMOS LOS DATA SET .XML PARA RECONOCER EL ROSTRO
face_cascade = cv2.CascadeClassifier('/home/casa/Documentos/Pygame/Game_letras/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/casa/Documentos/Pygame/Game_letras/haarcascade_eye.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml


def img_fondo(screen):
    fondo = pygame.image.load("/home/casa/Documentos/Pygame/Game_letras/img/fondo.png").convert()
    screen.blit(fondo, (-50,0))

def circulo(screen,d_x,d_y):
    print(d_x)
    pygame.draw.circle(screen,(255,0,0),(640-d_x,d_y),40) #(random.randint(0, 250)

def mostrar_texto(screen,texto,d_x,d_y):
    fuente = pygame.font.SysFont("arial",20)
    mensaje = fuente.render(texto,1,(random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)))
    text_w = mensaje.get_width()
    text_h = mensaje.get_height()
    screen.blit(mensaje, (((640-d_x)-text_w/2),(d_y-text_h/2)))

def star_opencv(frame,screen):
    screen.fill([0,0,0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)     # LE DAMOS ROTACION A LA VISUALIZACION
    frame = np.invert(frame)    # MODO NEGATIVO
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))

def start_screen():
    d_x = 0
    d_y = 0
    try:
        while True:
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x,y,w,h) in faces:
                d_x = x
                d_y = y

                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            
            star_opencv(frame,screen)       #INIT OPENCV        
            #img_fondo(screen)               #DIBUJAMOS EL FONDO DESPUES DE ESTABLECER LA CAMARA
            circulo(screen,d_x,d_y)                 #DIBUJAMOS EL CIRCULO
            mostrar_texto(screen,"Tesis",d_x,d_y)   #DIBUJAMOS EL TEXTO
                
            pygame.display.update()

            #PREPARAMOS LOS EVENTOS POR TECLAS
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:     #CON ESTO VERIFICAMOS QUE SE PRESIONO UNA TECLA
                    print("Tecla presionada")
                    if event.key == pygame.K_ESCAPE: #CON ESTO VERIFICAMOS QUE SE PRESIONO LA TECLA ESCAPE TODAS LAS KEYS ESTAN EN https://www.pygame.org/docs/ref/key.html
                        print("ESCAPE")
                        pygame.quit()
                        break        
                    elif event.key == pygame.K_RIGHT: # MOVEMOS HACIA LA DERECHA EL CIRCULO
                        d_x = d_x + 20
                    elif event.key == pygame.K_LEFT:  # MOVEMOS HACIA LA IZQUIERDA EL CIRCULO
                        d_x = d_x -20
            
    except (KeyboardInterrupt, SystemExit):
        pygame.quit()
    cv2.destroyAllWindows()

start_screen()