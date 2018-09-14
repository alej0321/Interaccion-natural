# python dynamic_color_tracking.py --filter HSV --webcam
"""
https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv
https://stackoverflow.com/questions/43086584/typeerror-float-object-cannot-be-interpreted-as-an-index
https://github.com/TutorProgramacion/opencv-traincascade
http://acodigo.blogspot.com/2015/12/entrenar-opencv-en-deteccion-de-objetos.html
https://programarfacil.com/blog/vision-artificial/deteccion-de-movimiento-con-opencv-python/
https://www.youtube.com/watch?v=aHTVDoOWYB8
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html

"""
import pygame
from pygame.locals import *
import cv2
import argparse
import numpy as np


camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")

screen = pygame.display.set_mode([640,480])

def callback(value):
    pass


def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)

    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255

        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


def get_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--filter', required=True,
                    help='Range filter. RGB or HSV')
    ap.add_argument('-w', '--webcam', required=False,
                    help='Use webcam', action='store_true')
    args = vars(ap.parse_args())

    if not args['filter'].upper() in ['RGB', 'HSV']:
        ap.error("Please speciy a correct filter.")

    return args


def get_trackbar_values(range_filter):
    values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)
    return values

def screen_menu(screen,estado):
    #PONEMOS IMAGEN MENU DE FONDO
    if (estado == True):
        fondo = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/bg.png").convert()
        screen.blit(fondo, (0,0))


def audio_fondo():
    file="/home/casa/Documentos/OpenCVandPyGame/assets/audio/fondo.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(0)

def screen_menu(screen,estado):
    #PONEMOS IMAGEN MENU DE FONDO
    if (estado == True):
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

def puntero(screen,d_x,d_y):  #PUNTERO
    #CONVERTIMOS EL PUNTERO EN SCPRITE PARA PODER USAR BIEN LAS COLISIONES       
    puntero = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/puntero50.png")
    sprite_puntero = pygame.sprite.Sprite()            
    sprite_puntero.image = puntero
    sprite_puntero.rect  = puntero.get_rect()
    sprite_puntero.rect.top  = (d_y)        #OBTENEMOS LA MITA ORIZONTAL DEL OBJETO RECONOCIDO EN EJE Y
    sprite_puntero.rect.left = ((d_x))    #OBTENEMOS LA MITA ORIZONTAL DEL OBJETO RECONOCIDO EN EJE X
    screen.blit(sprite_puntero.image, sprite_puntero.rect)
    return sprite_puntero

d_y = 0
d_x = 0


def main():
    args = get_arguments()
    range_filter = args['filter'].upper()

    var_screen_menu = True
    var_screen_game = False
    var_btn_opc     = True
    setup_trackbars(range_filter)

    # obtiene la resolución del temporizador
    clock = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0
    global_time = 0
    global_time_temp = 0


    while True:

        

        if args['webcam']:
            ret, image = camera.read()
            
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            screen.fill([0,0,0])
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)     # LE DAMOS ROTACION A LA VISUALIZACION
            #frame = np.invert(frame)    # MODO NEGATIVO
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0,0))
            
            screen_menu(screen,var_screen_menu)           #DIBUJAMOS EL FONDO DESPUES DE ESTABLECER LA CAMARA
            screen_game(screen,var_screen_game)          #DIBUJAMOS EL FONDO DESPUES DE DARLE PLAY AL JUEGO
            motrar_mapa(screen,var_screen_game)           #DIBUJAMOS EN EL FONDO EL MAPA 
            tl_init(screen,var_screen_menu)               #TITULO
            btn_opc(screen,var_btn_opc)                   #BOTONES DE OPCIONES

            #ESTABLECEMOS LAS VARIABLES DE LOS BOTONES
            boton_sonido   = rec_sonido(screen,var_btn_opc)   #DIBUJAMOS SUS RESPECTIVOS RECTANGULO DE MANERA INDIVIDUAL SONIDO
            boton_ayuda    = rec_ayuda(screen,var_btn_opc)    #DIBUJAMOS SUS RESPECTIVOS RECTANGULO DE MANERA INDIVIDUAL AYUDA
            boton_play     = btn_play(screen,var_screen_menu) #BOTON PLAY

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

            
            
            if not ret:
                break

            if range_filter == 'RGB':
                frame_to_thresh = image.copy()
            else:
                frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)

        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        kernel = np.ones((5,5),np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
 
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(image, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(image, center, 3, (0, 0, 255), -1)
                cv2.putText(image,"centroid", (center[0]+10,center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
                cv2.putText(image,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
                
                d_y = y
                d_x = x

                
        sprite_puntero = puntero(screen,640-d_x,d_y)

        #CONDICIONALES DE LAS COLISIONES
        if (var_screen_menu):                           #COLISIONES DE MENU * ERROR POR QUE NO RETORNA BOTONPLAY POR ELLO EL IF
            if boton_play.colliderect(sprite_puntero):  #PUNTERO Y EL BOTON PLAY
                print("PLAY")
                var_screen_menu = False
                var_screen_game = True
        else:

            if btn_comuna_1.colliderect(sprite_puntero):     #PUNTERO Y EL BOTON DE AYUDA
                if (global_time_temp == 0):
                    global_time_temp = global_time
                if ((global_time-global_time_temp) > 3):
                    print((global_time-global_time_temp))
                    print("COMUNA 1")
            else:
                global_time_temp = 0
                
            if btn_comuna_2.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 2")
            elif btn_comuna_3.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 3")
            elif btn_comuna_4.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 4")
            elif btn_comuna_5.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 5")
            elif btn_comuna_6.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 6")
            elif btn_comuna_7.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 7")
            elif btn_comuna_8.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 8")
            elif btn_comuna_9.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE UNA COMUNA
                print("COMUNA 9")
        
        if boton_sonido.colliderect(sprite_puntero):  #PUNTERO Y EL BOTON SONIDO TRUE O FALSE
            print("SONIDO")
        if boton_ayuda.colliderect(sprite_puntero):   #PUNTERO Y EL BOTON DE AYUDA
            print("AYUDA")



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
        # show the frame to our screen
        cv2.imshow("Original", image)
        cv2.imshow("Thresh", thresh)
        cv2.imshow("Mask", mask)

        

        #do stuff here
        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
        if seconds > 60:
            minutes += 1
            seconds -= 60

        #print ("{}:{}".format(minutes, seconds))
        global_time = (minutes+seconds)
        #print (minutes+seconds)

        milliseconds += clock.tick_busy_loop(60) #returns the

        pygame.display.update()

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


if __name__ == '__main__':
    main()