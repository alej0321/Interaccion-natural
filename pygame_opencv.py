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
face_cascade = cv2.CascadeClassifier('/home/casa/Documentos/OpenCVandPyGame/assets/dataset/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/casa/Documentos/OpenCVandPyGame/assets/dataset/haarcascade_eye.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

def audio_fondo():
    file="/home/casa/Documentos/OpenCVandPyGame/assets/audio/fondo.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(0)

def screen_menu(screen,estado):
    #PONEMOS IMAGEN MENU DE FONDO
    if (estado == True):
        print("FONDO MENU")
        fondo = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/bg.png").convert()
        screen.blit(fondo, (0,0))

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
    #frame = np.invert(frame)    # MODO NEGATIVO
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))

#PONEMOS TODOS LOS GRAFICOS EN SU LUGAR
def btn_play(screen,estado):         #FONDO
    if (estado == True):   
        btn_play = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/btn_play.png")
        screen.blit(btn_play, (20,180))
        boton_play = btn_play.get_rect()
        boton_play.left = 20
        boton_play.top  = 180            
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play


def tl_init(screen,estado):          #MOSTRAMOS LA IMAGEN DEL TITULO
    if (estado == True):
        titulo = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/tl_init.png")
        screen.blit(titulo, (20,10))

def btn_opc(screen,estado):          #BOTON DE OPCIONES SONIDO E INSTRUCCIONES
    #BOTONES OPCIONALES
    if (estado == True):
        boton_opcionales = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/btn_opc.png")
        screen.blit(boton_opcionales, (500,420))

def puntero(screen,d_x,d_y):  #PUNTERO
    #CONVERTIMOS EL PUNTERO EN SCPRITE PARA PODER USAR BIEN LAS COLISIONES       
    puntero = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/puntero50.png")
    sprite_puntero = pygame.sprite.Sprite()            
    sprite_puntero.image = puntero
    sprite_puntero.rect  = puntero.get_rect()
    sprite_puntero.rect.top  = (d_y)+(d_h/2)        #OBTENEMOS LA MITA ORIZONTAL DEL OBJETO RECONOCIDO EN EJE Y
    sprite_puntero.rect.left = 640-((d_x)+(d_w/2))    #OBTENEMOS LA MITA ORIZONTAL DEL OBJETO RECONOCIDO EN EJE X
    screen.blit(sprite_puntero.image, sprite_puntero.rect)
    return sprite_puntero

def rec_sonido(screen,estado):
    if (estado == True):
        boton_sonido = pygame.Rect(510,420,50,50)       #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(255,0,0),boton_sonido,1) 
        return boton_sonido

def rec_ayuda(screen,estado):
    if (estado == True):
        boton_ayuda = pygame.Rect(570,420,50,50)
        pygame.draw.rect(screen,(200,0,0),boton_ayuda,1)  #BOTON DE PANTALLA DE AYUDA
        return boton_ayuda

#METODOS DEL JUEGO SCREEN 1
def screen_game(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        fondo = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/bg_game.png").convert()
        screen.blit(fondo, (0,0))

def motrar_mapa(screen,estado):                                #PONEMOS EL RESPECTIVO MAPA EN EL SCREEN 1
    if (estado == True):
        map = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/map.png")
        screen.blit(map, (60,0))

#CREACION DE LOS 9 RECTANGULOS QUE REPRESENTARAN LAS 9 COMUNAS CADA UNO
def rec_comuna_1(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_1 = pygame.Rect(300,200,25,50)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_1,1) 
        return boton_rc_1

def rec_comuna_2(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_2 = pygame.Rect(455,40,25,50)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_2,1) 
        return boton_rc_2

def rec_comuna_3(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_3 = pygame.Rect(377,195,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_3,1) 
        return boton_rc_3

def rec_comuna_4(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_4 = pygame.Rect(270,290,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_4,1) 
        return boton_rc_4

def rec_comuna_5(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_5 = pygame.Rect(300,350,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_5,1) 
        return boton_rc_5

def rec_comuna_6(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_6 = pygame.Rect(238,337,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_6,1) 
        return boton_rc_6

def rec_comuna_7(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_7 = pygame.Rect(165,280,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_7,1) 
        return boton_rc_7

def rec_comuna_8(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_8 = pygame.Rect(200,255,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_8,1) 
        return boton_rc_8

def rec_comuna_9(screen,estado):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_9 = pygame.Rect(120,195,25,40)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_9,1) 
        return boton_rc_9

audio_fondo()  #PONEMOS MUSICA DE FONDO

d_x = 0
d_y = 0
d_w = 0
d_h = 0

var_screen_menu = True
var_screen_game = False
var_btn_opc     = True

try:
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            d_x = x
            d_y = y
            d_w = w
            d_h = h

            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        star_opencv(frame,screen)                     #INIT OPENCV        
        screen_menu(screen,var_screen_menu)           #DIBUJAMOS EL FONDO DESPUES DE ESTABLECER LA CAMARA
        screen_game(screen,var_screen_game)          #DIBUJAMOS EL FONDO DESPUES DE DARLE PLAY AL JUEGO
        motrar_mapa(screen,var_screen_game)           #DIBUJAMOS EN EL FONDO EL MAPA 
        tl_init(screen,var_screen_menu)               #TITULO
        btn_opc(screen,var_btn_opc)                   #BOTONES DE OPCIONES

        #ESTABLECEMOS LAS VARIABLES DE LOS BOTONES
        boton_sonido   = rec_sonido(screen,var_btn_opc)   #DIBUJAMOS SUS RESPECTIVOS RECTANGULO DE MANERA INDIVIDUAL SONIDO
        boton_ayuda    = rec_ayuda(screen,var_btn_opc)    #DIBUJAMOS SUS RESPECTIVOS RECTANGULO DE MANERA INDIVIDUAL AYUDA
        boton_play     = btn_play(screen,var_screen_menu) #BOTON PLAY
        sprite_puntero = puntero(screen,d_x,d_y)          #ES PERMANENTE RETORNADO EN SCRIPT PATA LAS COLISIONES

        #RECTANGULOS DE CADA COMUNA
        btn_comuna_1   = rec_comuna_1(screen,var_screen_game)
        btn_comuna_2   = rec_comuna_2(screen,var_screen_game)
        btn_comuna_3   = rec_comuna_3(screen,var_screen_game)
        btn_comuna_4   = rec_comuna_4(screen,var_screen_game)
        btn_comuna_5   = rec_comuna_5(screen,var_screen_game)
        btn_comuna_6   = rec_comuna_6(screen,var_screen_game)
        btn_comuna_7   = rec_comuna_7(screen,var_screen_game)
        btn_comuna_8   = rec_comuna_8(screen,var_screen_game)
        btn_comuna_9   = rec_comuna_9(screen,var_screen_game)
        #CREACION DE UN POLYGONO
        """
        color_p = (100,255,100)                         #COLORES DEL POLYGONO
        points  = [(40,400),(200,280),(40,150)]         #COORDENADAS DEL POLYGONO
        pygame.draw.polygon(screen,color_p,points,4)    #DIBUJAMOS EL POLYGONO
        """
        #CREACION DEL RECTANGULO EJEMPLO 
        """
        rectangulo = pygame.Rect(250,100,150,150)
        pygame.draw.rect(screen,(255,0,0),rectangulo)  
        """

        

        #CONDICIONALES DE LAS COLISIONES
        if (var_screen_menu):                           #COLISIONES DE MENU * ERROR POR QUE NO RETORNA BOTONPLAY POR ELLO EL IF
            if boton_play.colliderect(sprite_puntero):  #PUNTERO Y EL BOTON PLAY
                print("PLAY")
                var_screen_menu = False
                var_screen_game = True

        if boton_sonido.colliderect(sprite_puntero):  #PUNTERO Y EL BOTON SONIDO TRUE O FALSE
            print("SONIDO")
        if boton_ayuda.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE AYUDA
            print("AYUDA")


        pygame.display.update()

        #PREPARAMOS LOS EVENTOS POR TECLAS
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print ("pos x es: ",pos[0]," pos y es: ",pos[1])

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
