import pygame
from threading import Thread
import sys
import math 

width = 1280
height = 800
whiteColor = pygame.Color(255,255,255)

window = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)

#Contiene id del jugador y los datos de su pantalla
individual_screen = {}


def start(num_screens):

	line_number_x= int(math.sqrt(num_screens))
	line_number_y= int(math.sqrt(num_screens))

	if line_number_x * line_number_y < num_screens:
		line_number_x+=1

	if line_number_x * line_number_y < num_screens:
	    line_number_y+=1

	for i in range(0, num_screens):
		screen_data = {}
		screen_data['pos_x'] = i%line_number_x
		screen_data['pos_y'] = i/line_number_x
		screen_data['width'] = width/line_number_x
		screen_data['height'] = height/line_number_y
		screen_data['canvas'] = pygame.Surface((screen_data['width'],screen_data['height']))

		screen_data['canvas'].fill(whiteColor)
		screen_data['Objects'] = []

		individual_screen[i] = screen_data

		window.blit(individual_screen[i]['canvas'],(individual_screen[i]['width'] *individual_screen[i]['pos_x'],individual_screen[i]['height']*individual_screen[i]['pos_y']))
	
	pygame.font.init()
	pygame.display.flip()

def screen(screen_id):
	return individual_screen[int(screen_id)]['canvas'] 

def react(screen_id, input):
	individual_screen[int(screen_id)]['Objects'][0].react(input)

def refresh_window(screen_id):
	window.blit(screen(screen_id),(individual_screen[int(screen_id)]['width'] *individual_screen[int(screen_id)]['pos_x'],individual_screen[int(screen_id)]['height']*individual_screen[int(screen_id)]['pos_y']))

def reset_layout(screen_id):
	screen(screen_id).fill(whiteColor)
	individual_screen[int(screen_id)]['Objects'] = []

def write(screen_id, text, xtext, ytext):
	size= int(1.5 * individual_screen[int(screen_id)]['width']/len(text))	
	myfont = pygame.font.SysFont("monospace", size)
	
	label = myfont.render(text, 1, (0,0,0))

	screen(screen_id).blit(label,(xtext, ytext))
	refresh_window(screen_id)
	pygame.display.flip()
	

def draw_textbox(screen_id, textbox_size):
	textbox_x= int(individual_screen[int(screen_id)]['width']*0.05)
	textbox_y= textbox_size+individual_screen[int(screen_id)]['height']*0.2

	height_textbox= int(self.height-textbox_y)

	if height_textbox > int(individual_screen[int(screen_id)]['height']*0.3):
		height_textbox= int(individual_screen[int(screen_id)]['height']*0.3)

	individual_screen[int(screen_id)]['Objects'].append(Textbox(textbox_x,textbox_y,int(individual_screen[int(screen_id)]['width']*0.8),height_textbox))
	individual_screen[int(screen_id)]['canvas'].blit(individual_screen[int(screen_id)]['Objects'][0].screen(),(individual_screen[int(screen_id)]['Objects'][0].pos_x, individual_screen[int(screen_id)]['Objects'][0].pos_y))

class PygameThread(Thread):    
    def run(self):
        clock = pygame.time.Clock()
        print("RUNNING")
        running = True
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONUP:
                    print("SALIR")
                    running = False
            clock.tick(20)            
        pygame.quit()
        sys.exit()

try:
    pygame_thread = PygameThread()
    pygame_thread.start()
except:
    print("-----===== EXCEPTION threading exception =====-----")
