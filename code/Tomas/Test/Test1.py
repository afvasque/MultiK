
import sys

import pygame

pygame.init()

width = 680
height = 480

redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)



myfont = pygame.font.SysFont("monospace", 15)

window = pygame.display.set_mode((width,height))

def empty_screen():
    window.fill(pygame.Color(255,255,255))
    pygame.display.flip()

def start_screen():
    
    empty_screen()

    myfont = pygame.font.SysFont("monospace", 15)

    label = myfont.render("Elija el ejercicio a ver", 1, (0,0,0))
    window.blit(label,(100,40))

    label = myfont.render("a Asociar fonema con grafema correspondiente", 1, (0,0,0))
    window.blit(label,(100,60))

    label = myfont.render("b Reconocer grafema en palabras dadas", 1, (0,0,0))
    window.blit(label,(100,80))

    label = myfont.render("c Separar palabras en silabas", 1, (0,0,0))
    window.blit(label,(100,100))

    label = myfont.render("d Construccion por silabas de palabras", 1, (0,0,0))
    window.blit(label,(100,120))

    label = myfont.render("e Reconocer signos de interrogacion/exclamacion", 1, (0,0,0))
    window.blit(label,(100,140))

    label = myfont.render("f Colocar signos de interrogacion/exclamacion", 1, (0,0,0))
    window.blit(label,(100,160))

    label = myfont.render("g Diferenciar sustantivos propios de comunes", 1, (0,0,0))
    window.blit(label,(100,180))

    label = myfont.render("h Aplicar mayusculas en nombres propios", 1, (0,0,0))
    window.blit(label,(100,200))

    label = myfont.render("i Reconocer v/b", 1, (0,0,0))
    window.blit(label,(100,220))

    label = myfont.render("j Uso de 'b' en 'aba' ", 1, (0,0,0))
    window.blit(label,(100,240))

    label = myfont.render("k Mp, mb, nv", 1, (0,0,0))
    window.blit(label,(100,260))

    pygame.display.flip()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                print event
                if event.key == pygame.K_a:
                    p1_screen()
                elif event.key == pygame.K_b:
                    p2_screen()
                elif event.key == pygame.K_c:
                    p3_screen()
                elif event.key == pygame.K_d:
                    p6_screen()
                elif event.key == pygame.K_e:
                    p4_screen()
                elif event.key == pygame.K_f:
                    p5_screen()
                elif event.key == pygame.K_g:
                    p7_screen()
                elif event.key == pygame.K_h:
                    p8_screen()
                elif event.key == pygame.K_i:
                    p9_screen()

def p1_screen():
    empty_screen()
    
    input_text = ""
    
    pygame.draw.rect(window,blueColor,(width / 5, height / 7, 3 * width / 5,  height / 7))
    
    pygame.draw.rect(window,greenColor,(width / 5, 3 * height / 7, 3 * width / 5,  height / 7))
    
    pygame.draw.rect(window,redColor,(width / 5, 5 * height / 7, 3 * width / 5,  height / 7))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                elif event.key >= 97 and event.key <= 122:
                    myfont = pygame.font.SysFont("monospace", height / 7)
                    input_text = input_text + chr(event.key)
                    label = myfont.render(input_text, 1, (255,255,255))
                    window.blit(label,(width / 5, height / 7))
                    pygame.display.flip()
                elif event.key == 13:
                    input_text = ""
                    pygame.draw.rect(window,blueColor,(width / 5, height / 7, 3 * width / 5,  height / 7))
                    pygame.display.flip()

def p2_screen():
    x = 0
    y = 0
    
    def p2_draw():
        empty_screen()
    
        image_1 = pygame.image.load("Images/pato.png")
        image_1 = pygame.transform.scale(image_1,(width  / 5,height / 5))
        window.blit(image_1,(width/5,height/5))
    
        image_2 = pygame.image.load("Images/pelota.png")
        image_2 = pygame.transform.scale(image_2,(width/5,height/5))
        window.blit(image_2,(3*width/5,height/5))
    
        image_3 = pygame.image.load("Images/perro.png")
        image_3 = pygame.transform.scale(image_3,(width/5,height/5))
        window.blit(image_3,(width/5,3*height/5))
    
        image_4 = pygame.image.load("Images/casa.png")
        image_4 = pygame.transform.scale(image_4,(width/5,height/5))
        window.blit(image_4,(3*width/5,3*height/5))
    
        myfont = pygame.font.SysFont("monospace", height / 10)
    
        label_1 = myfont.render("pato",1,(0,0,0))
        label_2 = myfont.render("pelota",1,(0,0,0))
        label_3 = myfont.render("perro",1,(0,0,0))
        label_4 = myfont.render("casa",1,(0,0,0))
    
        window.blit(label_1,(width/5, 2*height/5))
        window.blit(label_2,(3*width/5,2*height/5))
        window.blit(label_3,(width/5,4*height/5))
        window.blit(label_4,(3*width/5,4*height/5))
    
        pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
        pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
        pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
        pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
    
        pygame.draw.circle(window, greenColor,(7 * width / 10 - 5,height / 5 - 5),10,10)
        pygame.draw.circle(window, greenColor,(7 * width / 10 - 5, 2 * height / 5 - 5),10,10)
        pygame.draw.circle(window, greenColor,(3 * width / 5 - 5, 3 * height / 10 - 5),10,10)
        pygame.draw.circle(window, greenColor,(4 * width / 5 - 5, 3 * height / 10 - 5),10,10)
    
        pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 3 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 3 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 4 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 4 * height / 5 - 5),10,10)
    
        pygame.display.flip()

    p2_draw()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                
                pygame.draw.circle(window, whiteColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)

                
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                    
                elif event.key == pygame.K_DOWN:
                    y+=1
                    y = y%2
                    
                elif event.key == pygame.K_UP:  
                    y+=1
                    y = y%2
                    
                elif event.key == pygame.K_LEFT:
                    x+=1
                    x = x%2
                    
                elif event.key == pygame.K_RIGHT:
                    x+=1
                    x = x%2
                
                pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
                pygame.display.flip()

def p3_screen():
    x = 0
    y = 0
    
    def p3_draw():
        empty_screen()
    
        image_1 = pygame.image.load("Images/pato.png")
        image_1 = pygame.transform.scale(image_1,(width  / 5,height / 5))
        window.blit(image_1,(width/5,height/5))
    
        image_2 = pygame.image.load("Images/pelota.png")
        image_2 = pygame.transform.scale(image_2,(width/5,height/5))
        window.blit(image_2,(3*width/5,height/5))
    
        image_3 = pygame.image.load("Images/perro.png")
        image_3 = pygame.transform.scale(image_3,(width/5,height/5))
        window.blit(image_3,(width/5,3*height/5))
    
        image_4 = pygame.image.load("Images/casa.png")
        image_4 = pygame.transform.scale(image_4,(width/5,height/5))
        window.blit(image_4,(3*width/5,3*height/5))
    
        myfont = pygame.font.SysFont("monospace", height / 20)
    
        label_0 = myfont.render("Busca la palabra de tres silabas",1,(0,0,0))
        
        myfont = pygame.font.SysFont("monospace", height / 10)
        
        label_1 = myfont.render("pato",1,(0,0,0))
        label_2 = myfont.render("pelota",1,(0,0,0))
        label_3 = myfont.render("perro",1,(0,0,0))
        label_4 = myfont.render("casa",1,(0,0,0))
    
        window.blit(label_0,(5, 5))
        window.blit(label_1,(width/5, 2*height/5))
        window.blit(label_2,(3*width/5,2*height/5))
        window.blit(label_3,(width/5,4*height/5))
        window.blit(label_4,(3*width/5,4*height/5))
    
        pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
        pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
        pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
        pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
    
        pygame.draw.circle(window, greenColor,(7 * width / 10 - 5,height / 5 - 5),10,10)
        pygame.draw.circle(window, greenColor,(7 * width / 10 - 5, 2 * height / 5 - 5),10,10)
        pygame.draw.circle(window, greenColor,(3 * width / 5 - 5, 3 * height / 10 - 5),10,10)
        pygame.draw.circle(window, greenColor,(4 * width / 5 - 5, 3 * height / 10 - 5),10,10)
    
        pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 3 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 3 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 4 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 4 * height / 5 - 5),10,10)
    
        pygame.display.flip()

    p3_draw()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                
                pygame.draw.circle(window, whiteColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)

                
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                    
                elif event.key == pygame.K_DOWN:
                    y+=1
                    y = y%2
                    
                elif event.key == pygame.K_UP:  
                    y+=1
                    y = y%2
                    
                elif event.key == pygame.K_LEFT:
                    x+=1
                    x = x%2
                    
                elif event.key == pygame.K_RIGHT:
                    x+=1
                    x = x%2
                
                pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 1) * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, (y * 2 + 2) *height / 5 - 5),10,10)
                pygame.display.flip()
                
def p4_screen():
    x = 0
    
    def p4_draw():
        empty_screen()
        
        myfont = pygame.font.SysFont("monospace", height / 5)
        
        label_1 = myfont.render("?",1,(0,0,0))
        label_2 = myfont.render("!",1,(0,0,0))
        
        window.blit(label_1,(1 * width / 5, 2 * height / 5))
        window.blit(label_2,(3 * width / 5, 2 * height / 5))
        
        pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, 2 * height / 5 - 5),10,0)
        pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, 2 * height / 5 - 5),10,0)
        pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, 3 * height / 5 - 5),10,0)
        pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, 3 * height / 5 - 5),10,0)
    
        pygame.draw.circle(window, greenColor,(7 * width / 10 - 5, 2 * height / 5 - 5),10,10)
        pygame.draw.circle(window, greenColor,(7 * width / 10 - 5, 3 * height / 5 - 5),10,10)
        pygame.draw.circle(window, greenColor,(3 * width / 5 - 5, 5 * height / 10 - 5),10,10)
        pygame.draw.circle(window, greenColor,(4 * width / 5 - 5, 5 * height / 10 - 5),10,10)
    
        pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 2 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 2 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 3 * height / 5 - 5),10,10)
        pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 3 * height / 5 - 5),10,10)
        
        pygame.display.flip()
    
    p4_draw()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                
                pygame.draw.circle(window, whiteColor,((x * 2 + 1) * width / 5 - 5, 2 * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 2) * width / 5 - 5, 2 * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 2) * width / 5 - 5, 3 * height / 5 - 5),10,10)
                pygame.draw.circle(window, whiteColor,((x * 2 + 1) * width / 5 - 5, 3 * height / 5 - 5),10,10)
                
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                elif event.key == pygame.K_LEFT:
                    x+=1
                    x = x%2
                elif event.key == pygame.K_RIGHT:
                    x+=1
                    x = x%2
                
                pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, 2 * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, 2 * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 2) * width / 5 - 5, 3 * height / 5 - 5),10,10)
                pygame.draw.circle(window, redColor,((x * 2 + 1) * width / 5 - 5, 3 * height / 5 - 5),10,10)
    
                pygame.display.flip()

def p5_screen():
    x = 0
    
    empty_screen()
    
    myfont = pygame.font.SysFont("monospace", height / 10)
    label_1 = myfont.render(u'\u00bf',1,(0,0,0))
    label_2 = myfont.render('?',1,(0,0,0))
    label_3 = myfont.render('como estas',1,(0,0,0))
    
    window.blit(label_1,(1 * width / 10, 1 * height / 5))
    window.blit(label_2,(2 * width / 10, 1 * height / 5))
    window.blit(label_3,(3 * width / 10, 1 * height / 5))
    
    pygame.draw.rect(window, redColor, (1 * width / 10, 1 * height / 5, width / 20, height / 7),2)
    pygame.draw.rect(window, greenColor, (2 * width / 10, 1 * height / 5, width / 20, height / 7),2)
    pygame.draw.rect(window, blueColor, (3 * width / 10, 1 * height / 5, width / 2, height / 7),2)
    
    pygame.draw.line(window, blackColor, (1 * width / 10, 4 * height / 5), (3 * width / 20, 4 * height / 5),2)
    pygame.draw.line(window, blackColor, (5 * width / 20, 4 * height / 5), (15 * width / 20, 4 * height / 5),2)
    pygame.draw.line(window, blackColor, (17 * width / 20, 4 * height / 5), (9 * width / 10, 4 * height / 5),2)
    
    pygame.draw.circle(window,redColor, (5 * width / 40 - 5, 3 * height / 5), 10, 0)
    pygame.draw.circle(window,greenColor, (5 * width / 40 - 5, 27 * height / 40), 10, 0)
    pygame.draw.circle(window,blueColor, (5 * width / 40 - 5, 30 * height / 40), 10, 0)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                pygame.draw.circle(window, whiteColor, (5 * width / 40 - 5, 3 * height / 5), 10, 0)
                pygame.draw.circle(window, whiteColor, (20 * width / 40 - 5, 3 * height / 5), 10, 0)
                pygame.draw.circle(window, whiteColor, (35 * width / 40 - 5, 3 * height / 5), 10, 0)
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                elif event.key == pygame.K_RIGHT:
                    x+=1
                    x = x%3
                elif event.key == pygame.K_LEFT:
                    if x == 0:
                        x = 2
                    else:
                        x-=1
                
                if x == 0:
                    pygame.draw.circle(window, redColor, (5 * width / 40 - 5, 3 * height / 5), 10, 0)
                elif x == 1:
                    pygame.draw.circle(window, redColor, (20 * width / 40 - 5, 3 * height / 5), 10, 0)
                elif x == 2:
                    pygame.draw.circle(window, redColor, (35 * width / 40 - 5, 3 * height / 5), 10, 0)
                
                pygame.display.flip()

def p6_screen():
    
    empty_screen()
    
    y = 0
    x = 0
    
    image_1 = pygame.image.load("Images/sombrero.png")
    image_1 = pygame.transform.scale(image_1,(width  / 5 - 10,height / 5 - 10))
    window.blit(image_1,(5,height/5))
    
    image_2 = pygame.image.load("Images/campana.png")
    image_2 = pygame.transform.scale(image_2,(width  / 5 - 10,height / 5 - 10))
    window.blit(image_2,(5, 2 * height/5))
    
    image_3 = pygame.image.load("Images/envase.png")
    image_3 = pygame.transform.scale(image_3,(width  / 5 - 10,height / 5 - 10))
    window.blit(image_3,(5, 3 * height/5))
    
    myfont = pygame.font.SysFont("monospace", height / 10)
    label_1_1 = myfont.render("som",1,(0,0,0))
    label_1_2 = myfont.render("bre",1,(0,0,0))
    label_1_3 = myfont.render("ro",1,(0,0,0))
    
    label_2_1 = myfont.render("cam",1,(0,0,0))
    label_2_2 = myfont.render("pa",1,(0,0,0))
    label_2_3 = myfont.render("na",1,(0,0,0))
    
    label_3_1 = myfont.render("en",1,(0,0,0))
    label_3_2 = myfont.render("va",1,(0,0,0))
    label_3_3 = myfont.render("se",1,(0,0,0))
    
    window.blit(label_1_1,(width/5 + 10, height/5))
    window.blit(label_2_1,(width/5 + 10, 2 * height/5))
    window.blit(label_3_1,(width/5 + 10, 3 * height/5))
    
    window.blit(label_2_2,(2 * width/5 + 10, height/5))
    window.blit(label_3_2,(2 * width/5 + 10, 2 * height/5))
    window.blit(label_1_2,(2 * width/5 + 10, 3 * height/5))
    
    window.blit(label_2_3,(3 * width/5 + 10, height/5))
    window.blit(label_3_3,(3 * width/5 + 10, 2 * height/5))
    window.blit(label_1_3,(3 * width/5 + 10, 3 * height/5))
    
    pygame.draw.circle(window, redColor,(width / 5 + 15, height / 5),10,10)
    pygame.draw.circle(window, redColor,(2 * width / 5 - 20, height / 5),10,10)
    pygame.draw.circle(window, redColor,(2 * width / 5 - 20, 2 * height / 5 - 30),10,10)
    pygame.draw.circle(window, redColor,(width / 5 + 15, 2 * height / 5 - 30),10,10)
    
    pygame.draw.circle(window, greenColor,(3 * width / 10 - 5, 2 * height / 5),10,10)
    pygame.draw.circle(window, greenColor,(3 * width / 10 - 5, 3 * height / 5 - 30),10,10)
    pygame.draw.circle(window, greenColor,(width / 5 + 15, 5 * height / 10 - 20),10,10)
    pygame.draw.circle(window, greenColor,(2 * width / 5 - 20, 5 * height / 10 - 20),10,10)
    
    pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 3 * height / 5),10,10)
    pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 3 * height / 5),10,10)
    pygame.draw.circle(window, blueColor,(7 * width / 20 - 5, 4 * height / 5 - 30),10,10)
    pygame.draw.circle(window, blueColor,(5 * width / 20 - 5, 4 * height / 5 - 30),10,10)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                pygame.draw.circle(window, whiteColor,((1 + x) * width / 5 + 15, (y + 1) * height / 5),10,10)
                pygame.draw.circle(window, whiteColor,((2 + x) * width / 5 - 20, (y + 1) * height / 5),10,10)
                pygame.draw.circle(window, whiteColor,((2 + x) * width / 5 - 20, (y + 2) * height / 5 - 30),10,10)
                pygame.draw.circle(window, whiteColor,((1 + x) * width / 5 + 15, (y + 2) * height / 5 - 30),10,10)
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                elif event.key == pygame.K_DOWN:
                    y+=1
                    y=y%3
                elif event.key == pygame.K_UP:
                    if y == 0:
                        y = 2
                    else:
                        y-=1
                elif event.key == 13:
                    if x <= 2:
                        label_1_1 = myfont.render("som",1,(255,0,0))
                        label_1_2 = myfont.render("bre",1,(255,0,0))
                        label_1_3 = myfont.render("ro",1,(255,0,0))
    
                        label_2_1 = myfont.render("cam",1,(255,0,0))
                        label_2_2 = myfont.render("pa",1,(255,0,0))
                        label_2_3 = myfont.render("na",1,(255,0,0))
    
                        label_3_1 = myfont.render("en",1,(255,0,0))
                        label_3_2 = myfont.render("va",1,(255,0,0))
                        label_3_3 = myfont.render("se",1,(255,0,0))
                        
                        if x == 0:
                            if y == 0:
                                window.blit(label_1_1,(width/5 + 10, height/5))
                            elif y == 1:
                                window.blit(label_2_1,(width/5 + 10, 2 * height/5))
                            elif y == 2:
                                window.blit(label_3_1,(width/5 + 10, 3 * height/5))
                        elif x == 1:
                            if y == 2:
                                window.blit(label_1_2,(2 * width/5 + 10, 3 * height/5))
                            elif y == 0:
                                window.blit(label_2_2,(2 * width/5 + 10, height/5))
                            elif y == 1:
                                window.blit(label_3_2,(2 * width/5 + 10, 2 * height/5))
                        elif x == 2:
                            if y == 2:
                                window.blit(label_1_3,(3 * width/5 + 10, 3 * height/5))
                            elif y == 0:
                                window.blit(label_2_3,(3 * width/5 + 10, height/5))
                            elif y == 1:
                                window.blit(label_3_3,(3 * width/5 + 10, 2 * height/5))
                                  
                        y = 0
                        x+=1
                        if x == 3:
                            x+=20
                        
                    else:
                        x+=20
                    
                pygame.draw.circle(window, redColor,((1 + x) * width / 5 + 15, (y + 1) * height / 5),10,10)
                pygame.draw.circle(window, redColor,((2 + x) * width / 5 - 20, (y + 1) * height / 5),10,10)
                pygame.draw.circle(window, redColor,((2 + x) * width / 5 - 20, (y + 2) * height / 5 - 30),10,10)
                pygame.draw.circle(window, redColor,((1 + x) * width / 5 + 15, (y + 2) * height / 5 - 30),10,10)
                
                pygame.display.flip()

def p7_screen():
    empty_screen()
    
    x = 0
    
    myfont = pygame.font.SysFont("monospace", height / 10)
    
    title_a = myfont.render("Comunes",1,(0,0,0))
    title_b = myfont.render("Propios",1,(0,0,0))
    
    window.blit(title_a,(5,5))
    window.blit(title_b,(2 * width / 3, 5))
    
    label_1 = myfont.render("Daniela",1,(255,0,0))
    label_2 = myfont.render("auto",1,(0,255,0))
    label_3 = myfont.render("Talca",1,(0,0,255))
    
    window.blit(label_1,(width/3, height/5))
    window.blit(label_2,(width/3, 2 * height/5))
    window.blit(label_3,(width/3, 3 * height/5))
    
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                elif event.key == pygame.K_LEFT and x > -1:
                    pygame.draw.rect(window,whiteColor,(0, height / 5, width,  height / 5))
                    x-=1
                    window.blit(label_1,((1 + x) * width/3, height/5))
                elif event.key == pygame.K_RIGHT and x < 1:
                    pygame.draw.rect(window,whiteColor,(0, height / 5, width,  height / 5))
                    x+=1
                    window.blit(label_1,((1 + x) * width/3, height/5))
            pygame.display.flip()

def p8_screen():
    empty_screen()
    y = 0
    
    myfont = pygame.font.SysFont("monospace", height / 10)
    letter_1_1 = myfont.render("C",1,(0,0,0))
    letter_1_2 = myfont.render("c",1,(0,0,0))
    palabra_1 = myfont.render("arlos",1,(0,0,0))
    
    window.blit(letter_1_1,(width / 3,height / 10))
    window.blit(palabra_1,(width / 3 + height / 10 ,2 * height / 10))
    window.blit(letter_1_2,(width / 3, 3 *height / 10))
    
    letter_2_1 = myfont.render("T",1,(0,0,0))
    letter_2_2 = myfont.render("t",1,(0,0,0))
    palabra_2 = myfont.render("oma",1,(0,0,0))
    
    window.blit(letter_2_1,(width / 3,4 * height / 10))
    window.blit(palabra_2,(width / 3 + height / 10 ,5 * height / 10))
    window.blit(letter_2_2,(width / 3, 6 *height / 10))
    
    letter_2_1 = myfont.render("A",1,(0,0,0))
    letter_2_2 = myfont.render("a",1,(0,0,0))
    palabra_2 = myfont.render("gua",1,(0,0,0))
    
    window.blit(letter_2_1,(width / 3,7 * height / 10))
    window.blit(palabra_2,(width / 3 + height / 10 ,8 * height / 10))
    window.blit(letter_2_2,(width / 3, 9 *height / 10))
    
    pygame.draw.rect(window,redColor,(width / 3, 2 * height / 10, height / 15,  height / 10),1)
    pygame.draw.rect(window,greenColor,(width / 3, 5 * height / 10, height / 15,  height / 10),1)
    pygame.draw.rect(window,blueColor,(width / 3, 8 * height / 10, height / 15,  height / 10),1)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                pygame.draw.rect(window,whiteColor,(width / 3, (2 + y) * height / 10, height / 15,  height / 10),3)
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                elif event.key == pygame.K_UP and y > -1:
                    y-=1
                elif event.key == pygame.K_DOWN and y < 1:
                    y+=1
                pygame.draw.rect(window,redColor,(width / 3, (2 + y) * height / 10, height / 15,  height / 10),1)
                pygame.display.flip()

def p9_screen():
    empty_screen()

    image_1 = pygame.image.load("Images/abeja.png")
    image_1 = pygame.transform.scale(image_1,(width  / 5,height / 5))
    window.blit(image_1,(width/5,height/5))
    
    image_2 = pygame.image.load("Images/abuelo.png")
    image_2 = pygame.transform.scale(image_2,(width/5,height/5))
    window.blit(image_2,(3*width/5,height/5))
    
    image_3 = pygame.image.load("Images/abrazo.png")
    image_3 = pygame.transform.scale(image_3,(width/5,height/5))
    window.blit(image_3,(width/5,3*height/5))
    
    image_4 = pygame.image.load("Images/avion.png")
    image_4 = pygame.transform.scale(image_4,(width/5,height/5))
    window.blit(image_4,(3*width/5,3*height/5))
    
    myfont = pygame.font.SysFont("monospace", height / 20)

    pygame.display.flip()

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                
start_screen()


              
              
