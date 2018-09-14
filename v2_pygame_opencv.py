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
from tinydb import TinyDB, Query
import cv2
import argparse
import numpy as np
import random
import  time


camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])

db = TinyDB('/home/casa/Documentos/OpenCVandPyGame/assets/db.json')

Data = Query()
#json_object = (db.search(Data.file == 'com_1/aeropuerto.png'))
json_object = (db.search(Data.type == 'img'))

print("#############################################")
print(db.search(Data.type == 'img'))
print("#############################################")
print(json_object[0]['nombre'])
print("#############################################")

def create_json():
    #INSERTAMOS LOS DATOS DE LA COMUNA UNO
    db.insert({'int': 1,'type': 'img','nombre': 'acueducto de popayan','file': 'com_1/acueducto de popayan.png','comuna': 1})
    db.insert({'int': 2,'type': 'img','nombre': 'aeropuerto',          'file': 'com_1/aeropuerto.png'          ,'comuna': 1})
    db.insert({'int': 3,'type': 'img','nombre': 'batallon',            'file': 'com_1/batallon.png'            ,'comuna': 1})
    db.insert({'int': 4,'type': 'img','nombre': 'campanario',          'file': 'com_1/campanario.png'          ,'comuna': 1})
    db.insert({'int': 5,'type': 'img','nombre': 'terminal',            'file': 'com_1/terminal.png'            ,'comuna': 1})

    #INSERTAMOS LOS DATOS DE LA COMUNA DOS
    db.insert({'int': 6, 'type': 'img','nombre': 'puente_viejo_cauca',     'file': 'com_2/puente_viejo_cauca.png'     ,'comuna': 2})
    db.insert({'int': 7, 'type': 'img','nombre': 'recrea_comfacauca',      'file': 'com_2/recrea_comfacauca.png'      ,'comuna': 2})
    db.insert({'int': 8, 'type': 'img','nombre': 'san_nicolas_restaurante','file': 'com_2/san_nicolas_restaurante.png','comuna': 2})
    db.insert({'int': 9, 'type': 'img','nombre': 'sena_norte_cauca',       'file': 'com_2/sena_norte_cauca.png'       ,'comuna': 2})
    db.insert({'int': 10,'type': 'img','nombre': 'terra_plaza',            'file': 'com_2/terra_plaza.png'            ,'comuna': 2})

    #INSERTAMOS LOS DATOS DE LA COMUNA TRES
    db.insert({'int': 11,'type': 'img','nombre': 'club_campestre',        'file': 'com_3/club_campestre.png'        ,'comuna': 3})
    db.insert({'int': 12,'type': 'img','nombre': 'cruz_roja',             'file': 'com_3/cruz_roja.png'             ,'comuna': 3})
    db.insert({'int': 13,'type': 'img','nombre': 'estadio_crio_lopez',    'file': 'com_3/estadio_crio_lopez.png'    ,'comuna': 3})
    db.insert({'int': 14,'type': 'img','nombre': 'galeria_barrio_bolivar','file': 'com_3/galeria_barrio_bolivar.png','comuna': 3})
    db.insert({'int': 15,'type': 'img','nombre': 'loteria_del_cauca',     'file': 'com_3/loteria_del_cauca.png'     ,'comuna': 3})

    #INSERTAMOS LOS DATOS DE LA COMUNA CUATRO
    db.insert({'int': 16,'type': 'img','nombre': 'arcada_herreria'   ,'file': 'com_4/arcada_herreria.png'   ,'comuna': 4})
    db.insert({'int': 17,'type': 'img','nombre': 'casa_negret'       ,'file': 'com_4/casa_negret.png'       ,'comuna': 4})
    db.insert({'int': 18,'type': 'img','nombre': 'casa_poeta'        ,'file': 'com_4/casa_poeta.png'        ,'comuna': 4})
    db.insert({'int': 19,'type': 'img','nombre': 'casa_valencia'     ,'file': 'com_4/casa_valencia.png'     ,'comuna': 4})
    db.insert({'int': 20,'type': 'img','nombre': 'iglesiasanto'      ,'file': 'com_4/iglesiasanto.png'      ,'comuna': 4})
    db.insert({'int': 21,'type': 'img','nombre': 'morro_tulcan'      ,'file': 'com_4/morro_tulcan.png'      ,'comuna': 4})
    db.insert({'int': 22,'type': 'img','nombre': 'museo_religioso'   ,'file': 'com_4/museo_religioso.png'   ,'comuna': 4})
    db.insert({'int': 23,'type': 'img','nombre': 'palacio_nacional'  ,'file': 'com_4/palacio_nacional.png'  ,'comuna': 4})
    db.insert({'int': 24,'type': 'img','nombre': 'panteon'           ,'file': 'com_4/panteon.png'           ,'comuna': 4})
    db.insert({'int': 25,'type': 'img','nombre': 'parque_caldas'     ,'file': 'com_4/parque_caldas.png'     ,'comuna': 4})
    db.insert({'int': 26,'type': 'img','nombre': 'parque_julio'      ,'file': 'com_4/parque_julio.png'      ,'comuna': 4})
    db.insert({'int': 27,'type': 'img','nombre': 'pc1'               ,'file': 'com_4/pc1.png'               ,'comuna': 4})
    db.insert({'int': 28,'type': 'img','nombre': 'pueblito_patojo'   ,'file': 'com_4/pueblito_patojo.png'   ,'comuna': 4})
    db.insert({'int': 29,'type': 'img','nombre': 'puente_humilladero','file': 'com_4/puente_humilladero.png','comuna': 4})
    db.insert({'int': 30,'type': 'img','nombre': 'santuario'         ,'file': 'com_4/santuario.png'         ,'comuna': 4})


#Solo lo inicializamos si la base de datos no esta creada
#create_json()

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

#MEDIO POR EL CUAL SE ESTABLECEN LOS SITIOS EN LA PANTALLA DEL JUEGO
def set_site_screen_1(screen,estado,img_num_1,var_x_1,var_y_1):
    if (estado == True):   
        ruta = "/home/casa/Documentos/OpenCVandPyGame/assets/img/site/"+str(img_num_1)
        btn_play = pygame.image.load(ruta)
        #REDIMENSIONAR TRASFORMAR IMAGEN
        #btn_play = pygame.transform.scale(btn_play, (64, 64))
        screen.blit(btn_play, (var_x_1,var_y_1))
        boton_play = btn_play.get_rect()
        boton_play.left = var_x_1
        boton_play.top  = var_y_1       
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play

def set_site_screen_2(screen,estado,img_num_2,var_x_2,var_y_2):
    if (estado == True):   
        ruta = "/home/casa/Documentos/OpenCVandPyGame/assets/img/site/"+str(img_num_2)
        btn_play = pygame.image.load(ruta)
        #REDIMENSIONAR TRASFORMAR IMAGEN
        #btn_play = pygame.transform.scale(btn_play, (64, 64))
        screen.blit(btn_play, (var_x_2,var_y_2))
        boton_play = btn_play.get_rect()
        boton_play.left = var_x_2
        boton_play.top  = var_y_2       
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play

def set_site_screen_3(screen,estado,img_num_3,var_x_3,var_y_3):
    if (estado == True):   
        ruta = "/home/casa/Documentos/OpenCVandPyGame/assets/img/site/"+str(img_num_3)
        btn_play = pygame.image.load(ruta)
        #REDIMENSIONAR TRASFORMAR IMAGEN
        #btn_play = pygame.transform.scale(btn_play, (64, 64))
        screen.blit(btn_play, (var_x_3,var_y_3))
        boton_play = btn_play.get_rect()
        boton_play.left = var_x_3
        boton_play.top  = var_y_3       
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play

def set_site_screen_4(screen,estado,img_num_4,var_x_4,var_y_4):
    if (estado == True):   
        ruta = "/home/casa/Documentos/OpenCVandPyGame/assets/img/site/"+str(img_num_4)
        btn_play = pygame.image.load(ruta)
        #REDIMENSIONAR TRASFORMAR IMAGEN
        #btn_play = pygame.transform.scale(btn_play, (64, 64))
        screen.blit(btn_play, (var_x_4,var_y_4))
        boton_play = btn_play.get_rect()
        boton_play.left = var_x_4
        boton_play.top  = var_y_4       
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play

def set_site_screen_5(screen,estado,img_num_5,var_x_5,var_y_5):
    if (estado == True):   
        ruta = "/home/casa/Documentos/OpenCVandPyGame/assets/img/site/"+str(img_num_5)
        btn_play = pygame.image.load(ruta)
        #REDIMENSIONAR TRASFORMAR IMAGEN
        #btn_play = pygame.transform.scale(btn_play, (64, 64))
        screen.blit(btn_play, (var_x_5,var_y_5))
        boton_play = btn_play.get_rect()
        boton_play.left = var_x_5
        boton_play.top  = var_y_5       
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play

def circulo(screen,d_x,d_y):
    print(d_x)
    pygame.draw.circle(screen,(255,0,0),(640-d_x,d_y),40) #(random.randint(0, 250)

def mostrar_texto(screen,texto,d_x,d_y):
    fuente = pygame.font.SysFont("arial",70)
    mensaje = fuente.render(texto,1,(random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)))
    text_w = mensaje.get_width()
    text_h = mensaje.get_height()
    screen.blit(mensaje, (((640-d_x)-text_w/2),(d_y-text_h/2)))

def texto_time(screen,texto,d_x,d_y):
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

def ready_0(screen,estado):          #BOTON DE OPCIONES SONIDO E INSTRUCCIONES
    #BOTONES OPCIONALES
    if (estado == True):
        boton_opcionales = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/ready/0.png")
        screen.blit(boton_opcionales, (430,415))

def ready_1(screen,estado):          #BOTON DE OPCIONES SONIDO E INSTRUCCIONES
    #BOTONES OPCIONALES
    if (estado == True):
        boton_opcionales = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/ready/1.png")
        screen.blit(boton_opcionales, (430,415))

def ready_2(screen,estado):          #BOTON DE OPCIONES SONIDO E INSTRUCCIONES
    #BOTONES OPCIONALES
    if (estado == True):
        boton_opcionales = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/ready/2.png")
        screen.blit(boton_opcionales, (430,415))

def ready_3(screen,estado):          #BOTON DE OPCIONES SONIDO E INSTRUCCIONES
    #BOTONES OPCIONALES
    if (estado == True):
        boton_opcionales = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/ready/3.png")
        screen.blit(boton_opcionales, (430,415))

        

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

def check_fin2(screen,estado):                                #PONEMOS EL RESPECTIVO MAPA EN EL SCREEN 1
    if (estado == True):
        map = pygame.image.load("/home/casa/Documentos/OpenCVandPyGame/assets/img/ready/fin.png")
        screen.blit(map, (200,0))

#MEDIO POR EL CUAL SE ESTABLECEN LOS SITIOS EN LA PANTALLA DEL JUEGO
def check_fin(screen,estado):
    if (estado == True):   
        ruta = "/home/casa/Documentos/OpenCVandPyGame/assets/img/ready/fin.png"
        btn_play = pygame.image.load(ruta)
        #REDIMENSIONAR TRASFORMAR IMAGEN
        #btn_play = pygame.transform.scale(btn_play, (64, 64))
        screen.blit(btn_play, (500,280))
        boton_play = btn_play.get_rect()
        boton_play.left = 500
        boton_play.top  = 280       
        pygame.draw.rect(screen,(100,0,0),boton_play,1) 
        return boton_play

#CREACION DE LOS 9 RECTANGULOS QUE REPRESENTARAN LAS 9 COMUNAS CADA UNO
def bar_progress(screen,estado,acumulador_tiempo,minutes,seconds):                         #PONEMOS IMAGEN MENU DE FONDO PARA INCIAR EL JUEGO
    if (estado == True):
        boton_rc_1 = pygame.Rect(300,10,(acumulador_tiempo/5),15)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(120,120,0),boton_rc_1,0) 

        #AQUI DEFINIMOS EL TIEMPO DEL JUEGO 5 MINUTOS
        total_tiempo = 4 # MINUTOS
        texto_time(screen,( (str(total_tiempo-minutes)+(":")+str(60-seconds) ) ),360,20)

        boton_rc_1 = pygame.Rect(300,10,100,15)         #BOTON DE SONIDO TRUE Y FALSE
        pygame.draw.rect(screen,(0,0,0),boton_rc_1,1) 
        return boton_rc_1

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

def get_ramdon():
    total_img = 29
    return int(random.randint(1,int(total_img)))
d_y = 0
d_x = 0


#DEFINIMOS LOS 5 LUGARES QUE APARECERAN EN LA PANTALLA
img_num_1 = json_object[get_ramdon()]['file']
img_num_2 = json_object[get_ramdon()]['file']
img_num_3 = json_object[get_ramdon()]['file']
img_num_4 = json_object[get_ramdon()]['file']
img_num_5 = json_object[get_ramdon()]['file']

def main():
    args = get_arguments()
    range_filter = args['filter'].upper()

    audio_fondo()

    var_screen_menu = True
    var_screen_game = False
    var_btn_opc     = True
    
    var_ready_0     = True
    var_ready_1     = False
    var_ready_2     = False
    var_ready_3     = False

    setup_trackbars(range_filter)

    #DEFINIMOS LA POSICION DEL OBJETO 1 PAR APONERLO FUERA DEL MAPA
    var_x_1   = 20
    var_y_1   = 20

    #DEFINIMOS LA POSICION DEL OBJETO 2 PAR APONERLO FUERA DEL MAPA
    var_x_2   = 147
    var_y_2   = 107

    #DEFINIMOS LA POSICION DEL OBJETO 3 PAR APONERLO FUERA DEL MAPA
    var_x_3   = 15
    var_y_3   = 351

    #DEFINIMOS LA POSICION DEL OBJETO 4 PAR APONERLO FUERA DEL MAPA
    var_x_4   = 471
    var_y_4   = 198

    #DEFINIMOS LA POSICION DEL OBJETO 5 PAR APONERLO FUERA DEL MAPA
    var_x_5   = 396
    var_y_5   = 314

    # obtiene la resolución del temporizador
    clock = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0

    acumulador_tiempo = 0

    global_time = 0
    global_time_temp = 0

    global_check_time_temp  = 0
    global_check            = 0

    global_img_1_time_temp  = 0
    global_img_1            = 0

    global_img_2_time_temp  = 0
    global_img_2            = 0
    
    global_img_3_time_temp  = 0
    global_img_3            = 0

    global_img_4_time_temp  = 0
    global_img_4            = 0

    global_img_5_time_temp  = 0
    global_img_5            = 0

    global_sonido           = 0
    global_sonido_colli     = 0

    inicio_de_tiempo = time.time()
    tiempo_final = time.time() 
    tiempo_transcurrido = tiempo_final - inicio_de_tiempo
    

    while True:

        

        #print("\nTomo %d segundos." % (tiempo_transcurrido))

        if(global_sonido == 1):
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(100)

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
            screen_game(screen,var_screen_game)           #DIBUJAMOS EL FONDO DESPUES DE DARLE PLAY AL JUEGO
            motrar_mapa(screen,var_screen_game)           #DIBUJAMOS EN EL FONDO EL MAPA 
            tl_init(screen,var_screen_menu)               #TITULO
            btn_opc(screen,var_btn_opc)                   #BOTONES DE OPCIONES
            
            ready_0(screen,var_ready_0)                   #BOTONES DE READY 0
            ready_1(screen,var_ready_1)                   #BOTONES DE READY 1
            ready_2(screen,var_ready_2)                   #BOTONES DE READY 2
            ready_3(screen,var_ready_3)                   #BOTONES DE READY 3

            #VERIFICAMOS QUE EL PUNTERO ESTE EN EL CUADRO DE TERMINAR
            check = check_fin(screen,var_screen_game)     #CHECK FIN DEL EVENTO

            
            
            #DEFINIMOS LOS 5 LUGARES
            img_1 = set_site_screen_1(screen,var_screen_game,img_num_1,var_x_1,var_y_1)
            img_2 = set_site_screen_2(screen,var_screen_game,img_num_2,var_x_2,var_y_2)
            img_3 = set_site_screen_3(screen,var_screen_game,img_num_3,var_x_3,var_y_3)
            img_4 = set_site_screen_4(screen,var_screen_game,img_num_4,var_x_4,var_y_4)
            img_5 = set_site_screen_5(screen,var_screen_game,img_num_5,var_x_5,var_y_5)

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

                
        sprite_puntero = puntero(screen,d_x,d_y)

        #CONDICIONALES DE LAS COLISIONES
        if (var_screen_menu):                           #COLISIONES DE MENU * ERROR POR QUE NO RETORNA BOTONPLAY POR ELLO EL IF
            if boton_play.colliderect(sprite_puntero):  #PUNTERO Y EL BOTON PLAY
                print("PLAY")
                var_screen_menu = False
                var_screen_game = True
        else:
            bar_progress(screen,True,acumulador_tiempo,minutes,seconds)
            if((global_img_1_time_temp == 0 or global_img_2_time_temp == 0 or global_img_3_time_temp == 0 or global_img_4_time_temp == 0 or global_img_5_time_temp == 0 )):
                var_ready_0     = True
                var_ready_1     = False
                var_ready_2     = False
                var_ready_3     = False

            #VERIFICAMOS QUE LA PERSONA HALLA ELEGIDO TEMRINAR PONIENDO EL LA ZONA DEL CIRCULO NEGRO EL PUNTERO DEL JEUGO Y ESPERAR 8 SEGUNDOS
            if check.colliderect(sprite_puntero):
                if (global_check_time_temp == 0):
                    global_check_time_temp = global_check
                elif ((global_check-global_check_time_temp) == 1):
                    print("TERMINO 1")
                    mostrar_texto(screen,"8",300,300)
                elif ((global_check-global_check_time_temp) == 2):
                    print("TERMINO 2")
                    mostrar_texto(screen,"7",300,300)
                elif ((global_check-global_check_time_temp) == 3):
                    print("TERMINO 3")
                    mostrar_texto(screen,"6",300,300)
                elif ((global_check-global_check_time_temp) == 4):
                    print("TERMINO 4")
                    mostrar_texto(screen,"5",300,300)
                elif ((global_check-global_check_time_temp) == 5):
                    print("TERMINO 5")
                    mostrar_texto(screen,"4",300,300)
                elif ((global_check-global_check_time_temp) == 6):
                    print("TERMINO 6")
                    mostrar_texto(screen,"3",300,300)
                elif ((global_check-global_check_time_temp) == 7):
                    print("TERMINO 7")
                    mostrar_texto(screen,"2",300,300)
                elif ((global_check-global_check_time_temp) == 8):
                    print("TERMINO 8")
                    mostrar_texto(screen,"1",300,300)
            else:
                print("FIN")
                global_check_time_temp = 0

            #VERIFICAMOS SI EXISTE COLISION POR DETERMINADO TIEMPO PARA AGARRAR EL OBJETO
            if img_1.colliderect(sprite_puntero):
                print("Imagen 1")
                if (global_img_1_time_temp == 0):
                    global_img_1_time_temp = global_img_1
                
                elif ((global_img_1-global_img_1_time_temp) == 1):
                    #print("PREPARADO: "+str(global_img_1-global_img_1_time_temp)+" : "+str(milliseconds))
                    var_ready_0     = False
                    var_ready_1     = True
                    var_ready_2     = False
                    var_ready_3     = False

                elif ((global_img_1-global_img_1_time_temp) == 2):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = True
                    var_ready_3     = False
                
                elif ((global_img_1-global_img_1_time_temp) == 3):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True

                elif ((global_img_1-global_img_1_time_temp) > 3):
                    print((global_img_1-global_img_1_time_temp))
                    var_x_1 = d_x
                    var_y_1 = d_y
                    print("COMUNA 1")
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True
                else:
                    var_ready_0     = True
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = False
            else:
                global_img_1_time_temp = 0

            if img_2.colliderect(sprite_puntero):
                print("Imagen 2")
                if (global_img_2_time_temp == 0):
                    global_img_2_time_temp = global_img_2

                elif ((global_img_2-global_img_2_time_temp) == 1):
                    #print("PREPARADO: "+str(global_img_1-global_img_1_time_temp)+" : "+str(milliseconds))
                    var_ready_0     = False
                    var_ready_1     = True
                    var_ready_2     = False
                    var_ready_3     = False

                elif ((global_img_2-global_img_2_time_temp) == 2):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = True
                    var_ready_3     = False
                
                elif ((global_img_2-global_img_2_time_temp) == 3):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True

                elif ((global_img_2-global_img_2_time_temp) > 3):
                    print((global_img_2-global_img_2_time_temp))
                    var_x_2 = d_x
                    var_y_2 = d_y
                    print("COMUNA 2")
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True
                else:
                    var_ready_0     = True
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = False

                
            else:
                global_img_2_time_temp = 0

            if img_3.colliderect(sprite_puntero):
                print("Imagen 3")
                if (global_img_3_time_temp == 0):
                    global_img_3_time_temp = global_img_3

                elif ((global_img_3-global_img_3_time_temp) == 1):
                    #print("PREPARADO: "+str(global_img_1-global_img_1_time_temp)+" : "+str(milliseconds))
                    var_ready_0     = False
                    var_ready_1     = True
                    var_ready_2     = False
                    var_ready_3     = False

                elif ((global_img_3-global_img_3_time_temp) == 2):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = True
                    var_ready_3     = False
                
                elif ((global_img_3-global_img_3_time_temp) == 3):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True

                elif ((global_img_3-global_img_3_time_temp) > 3):
                    print((global_img_3-global_img_3_time_temp))
                    var_x_3 = d_x
                    var_y_3 = d_y
                    print("COMUNA 3")
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True
                else:
                    var_ready_0     = True
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = False
                
            else:
                global_img_3_time_temp = 0

            if img_4.colliderect(sprite_puntero):
                print("Imagen 4")
                if (global_img_4_time_temp == 0):
                    global_img_4_time_temp = global_img_4
                elif ((global_img_4-global_img_4_time_temp) == 1):
                    #print("PREPARADO: "+str(global_img_1-global_img_1_time_temp)+" : "+str(milliseconds))
                    var_ready_0     = False
                    var_ready_1     = True
                    var_ready_2     = False
                    var_ready_3     = False

                elif ((global_img_4-global_img_4_time_temp) == 2):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = True
                    var_ready_3     = False
                
                elif ((global_img_4-global_img_4_time_temp) == 3):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True

                elif ((global_img_4-global_img_4_time_temp) > 3):
                    print((global_img_4-global_img_4_time_temp))
                    var_x_4 = d_x
                    var_y_4 = d_y
                    print("COMUNA 4")
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True
                else:
                    var_ready_0     = True
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = False
                
            else:
                global_img_4_time_temp = 0

            if img_5.colliderect(sprite_puntero):
                print("Imagen 5")
                if (global_img_5_time_temp == 0):
                    global_img_5_time_temp = global_img_5
                elif ((global_img_5-global_img_5_time_temp) == 1):
                    #print("PREPARADO: "+str(global_img_1-global_img_1_time_temp)+" : "+str(milliseconds))
                    var_ready_0     = False
                    var_ready_1     = True
                    var_ready_2     = False
                    var_ready_3     = False

                elif ((global_img_5-global_img_5_time_temp) == 2):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = True
                    var_ready_3     = False
                
                elif ((global_img_5-global_img_5_time_temp) == 3):
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True

                elif ((global_img_5-global_img_5_time_temp) > 3):
                    print((global_img_5-global_img_5_time_temp))
                    var_x_5 = d_x
                    var_y_5 = d_y
                    print("COMUNA 5")
                    var_ready_0     = False
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = True
                else:
                    var_ready_0     = True
                    var_ready_1     = False
                    var_ready_2     = False
                    var_ready_3     = False

            else:
                global_img_5_time_temp = 0

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
            
            if(global_sonido_colli == 0):

                if(global_sonido == 0):
                    global_sonido = 1
                    print("ON")
                else:
                    global_sonido = 0
                    print("OFF")
            global_sonido_colli = 1
        else:
            global_sonido_colli = 0

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
            if(var_screen_menu == False):
                acumulador_tiempo += 1
            milliseconds -= 1000
        if seconds > 60:
            minutes += 1
            seconds -= 60            

        #print ("{}:{}".format(minutes, seconds))
        global_time  = (minutes+seconds)
        global_check = (minutes+seconds)
        global_img_1 = (minutes+seconds)
        global_img_2 = (minutes+seconds)
        global_img_3 = (minutes+seconds)
        global_img_4 = (minutes+seconds)
        global_img_5 = (minutes+seconds)
        
        #print (minutes+seconds)

        milliseconds += clock.tick_busy_loop(60) #returns the

        pygame.display.update()

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


if __name__ == '__main__':
    main()