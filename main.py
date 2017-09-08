import pygame as pg 
import random as rm 
from os import path

#game constants
FPS = 30
WIDTH = 300
HEIGHT = 300

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
CYAN = (0,255,255)

#initilise pygame
pg.init()
pg.mixer.init()
pg.display.set_caption('Tic Tac Toe')

screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill(BLACK)
clock = pg.time.Clock()

#init music dir
musicdir = path.join(path.dirname(__file__),'assets')

#load music
textSnd = pg.mixer.Sound(path.join(musicdir,'clickSound.ogg'))
pg.mixer.music.load(path.join(musicdir,'Sparkling_mist.ogg'))


#set up font and text func
myfont = pg.font.match_font('ariel')


def text(surface,text,text_size,x_coordinate,y_coordinate,text_color):
    font = pg.font.Font(myfont,text_size)
    text_surf = font.render(text,True,text_color)  #true for anti_alignising
    text_rect = text_surf.get_rect()
    text_rect.center = (x_coordinate,y_coordinate) 
    surface.blit(text_surf,text_rect)

#for dividing the screen into 9 boxes() 
class Divider(pg.sprite.Sprite):
    def __init__(self,center,size):
        pg.sprite.Sprite.__init__(self)
        self.image = size
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = center

#class objects
div0 = Divider((100,0),pg.Surface((2,HEIGHT*2)))
div1 = Divider((200,0),pg.Surface((2,HEIGHT*2)))
div2 = Divider((0,100),pg.Surface((WIDTH*2,2)))
div3 = Divider((0,200),pg.Surface((WIDTH*2,2)))

#sprite groups
divGroups = pg.sprite.Group()

#add sprite to group
divGroups.add(div0)
divGroups.add(div1)
divGroups.add(div2)
divGroups.add(div3)

b1 = False
b2 = False
b3 = False
b4 = False
b5 = False
b6 = False
b7 = False
b8 = False
b9 = False

firstClick = False

xchoic = rm.choice([50,150,250])
ychoic = rm.choice([50,250])

b1symbol = ''                   
b2symbol = ''
b3symbol = ''
b4symbol = ''
b5symbol = ''
b6symbol = ''
b7symbol = ''
b8symbol = ''
b9symbol = ''

pg.mixer.music.play(loops=-1)    
#game loop
running = True
while running:
    clock.tick(FPS)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
       
        m_pos = list(pg.mouse.get_pos())

        #THIS IS THE AI BELOW

        # B1 
        if m_pos[0] >= 0 and m_pos[1] >= 0:
            if m_pos[0] <= 100 and m_pos[1] <= 100:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b1 == False:
                        text(screen,'X',100,50,50,RED)   
                        b1 = True
                        b1symbol = 'X' 
                                                 
                        if firstClick == False:                           
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True                 
                            b5 = True
                            b5symbol = 'O'
                                                                              
                        elif b1symbol == 'X' and b2symbol == 'X':
                            if b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True 

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                               
                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True
                               
                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True
                               
                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
           
                        elif b1symbol == 'X' and b3symbol == 'X':
                            if b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True

                            elif b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True


                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
           
                        elif b1symbol == 'X' and b4symbol == 'X':
                            if b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
      
                        elif b1symbol == 'X' and b5symbol == 'X':
                            if b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                            elif b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                                
                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True                          
                        
                        elif b1symbol == 'X' and b7symbol == 'X':
                            if b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                                
                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b1symbol == 'X' and b9symbol == 'X':
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                                
                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                                #else:
                            
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b1symbol == 'X' and b6symbol == 'X':
                            if b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True
                                        
                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True
    
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b1symbol == 'X' and b8symbol == 'X':
                            if b1symbol == 'X' and b2symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1symbol == 'X' and b3symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b1symbol == 'X' and b4symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b1symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True
                                        
                            elif b1symbol == 'X' and b7symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b1symbol == 'X' and b9symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True
    
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                     
        # B2
        if m_pos[0] > 100 and m_pos[1] >= 0:
            if m_pos[0] <= 200 and m_pos[1] <= 100:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b2 == False:
                        text(screen,'X',100,150,50,RED)
                        b2 = True
                        b2symbol = 'X'
                        
                        if firstClick == False:                         
                            text(screen,'O',107,150,150,CYAN)
                            b5 = True
                            firstClick = True                                                                        
                            b5symbol = 'O'
    

                        elif b2symbol == 'X' and b1symbol == 'X':
                            if b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True    
                                  
                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
                     
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True                     

                        elif b2symbol == 'X' and b3symbol == 'X':
                            if b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b2symbol == 'X' and b5symbol == 'X':
                            if b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True 
                                                       
                            elif b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b2symbol == 'X' and b8symbol == 'X':
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b2symbol == 'X' and b4symbol == 'X':
                            if b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True                       

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b2symbol == 'X' and b6symbol == 'X':
                            if b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True                       

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b2symbol == 'X' and b7symbol == 'X':
                            if b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b2symbol == 'X' and b9symbol == 'X':
                            if b2symbol == 'X' and b1symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b2symbol == 'X' and b3symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b2symbol == 'X' and b5symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b2symbol == 'X' and b8symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                    else:
                        pass

        # B3
        if m_pos[0] > 200 and m_pos[1] >= 0:
            if m_pos[0] <= 300 and m_pos[1] <= 100:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b3 == False:
                        text(screen,'X',100,250,50,RED)                 
                        b3 = True
                        b3symbol = 'X'

                        if firstClick == False:                        
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True                                                                        
                            b5 = True
                            b5symbol = 'O'
                  

                        elif b3symbol == 'X' and b1symbol == 'X':
                            if b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True    
                                                       
                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b3symbol == 'X' and b2symbol == 'X': 
                            if b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                                #else:
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                                 
                        elif b3symbol == 'X' and b5symbol == 'X':
                            if b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True
                                                      
                            elif b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                    
                        elif b3symbol == 'X' and b6symbol == 'X': 
                            if b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                            elif b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                                #else:
             
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                           
                        elif b3symbol == 'X' and b7symbol == 'X': 
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b3symbol == 'X' and b9symbol == 'X':
                            if b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:
  
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b3symbol == 'X' and b4symbol == 'X': 

                            if b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b3symbol == 'X' and b8symbol == 'X': 
                            if b3symbol == 'X' and b1symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b3symbol == 'X' and b2symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b3symbol == 'X' and b5symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b3symbol == 'X' and b6symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b3symbol == 'X' and b7symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b3symbol == 'X' and b9symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                    else:
                        pass

        # B4
        if m_pos[0] >= 0 and m_pos[1] >= 100:
            if m_pos[0] <= 100 and m_pos[1] <= 200:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b4 == False:
                        text(screen,'X',100,50,150,RED)                    
                        b4 = True
                        b4symbol = 'X'

                        if firstClick == False:
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True                                                                        
                            b5 = True
                            b5symbol = 'O'

                        elif b4symbol == 'X' and b1symbol == 'X':
                            if b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                                #else:
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b4symbol == 'X' and b5symbol == 'X':
                            if b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                                #else:
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b4symbol == 'X' and b6symbol == 'X': 
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b4symbol == 'X' and b7symbol == 'X': 
                            if b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b4symbol == 'X' and b2symbol == 'X': 
                            if b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                            
                        elif b4symbol == 'X' and b3symbol == 'X': 
                            if b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b4symbol == 'X' and b8symbol == 'X': 
                            if b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b4symbol == 'X' and b9symbol == 'X':
                            if b4symbol == 'X' and b1symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b4symbol == 'X' and b5symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b4symbol == 'X' and b6symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b4symbol == 'X' and b7symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                    else:
                        pass

        # B5 
        if m_pos[0] >= 100 and m_pos[1] >= 100:
            if m_pos[0] <= 200 and m_pos[1] <= 200:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b5 == False:
                        text(screen,'X',100,150,150,RED)
                        b5 = True
                        b5symbol = 'X'

                        if firstClick == False:
                            text(screen,'O',107,xchoic,ychoic,CYAN)
                            firstClick = True                 
                            b5 = True 
                                                                                  
                            if xchoic == 50 and ychoic == 50:
                                b1symbol = 'O'
                                b1 = True

                            elif xchoic == 150 and ychoic == 50:
                                b2symbol = 'O'
                                b2 = True
                                        
                            elif xchoic == 250 and ychoic == 50:
                                b3symbol = 'O'
                                b3 = True

                            elif xchoic == 50 and ychoic == 150:
                                b4symbol = 'O'
                                b4 = True

                            elif xchoic == 250 and ychoic == 150:
                                b6symbol = 'O'
                                b6 = True

                            elif xchoic == 50 and ychoic == 250:
                                b7symbol = 'O'
                                b7 = True

                            elif xchoic == 150 and ychoic == 250:
                                b8symbol = 'O'
                                b8 = True

                            elif xchoic == 250 and ychoic == 250:
                                b9symbol = 'O'
                                b9 = True

                        elif b5symbol == 'X' and b1symbol == 'X':
                            if b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True                           


                        elif b5symbol == 'X' and b2symbol == 'X': 
                            if b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                        elif b5symbol == 'X' and b3symbol == 'X': 
                            if b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                        elif b5symbol == 'X' and b4symbol == 'X':
                            if b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                        elif b5symbol == 'X' and b6symbol == 'X': 
                            if b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                        elif b5symbol == 'X' and b7symbol == 'X': 
                            if b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                        elif b5symbol == 'X' and b8symbol == 'X': 
                            if b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True

                        elif b5symbol == 'X' and b9symbol == 'X':
                            if b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True
                    else:
                        pass

        # B6
        if m_pos[0] > 200 and m_pos[1] > 100:
            if m_pos[0] <= 300 and m_pos[1] <= 200:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b6 == False:
                        text(screen,'X',100,250,150,RED)
                        b6 = True
                        b6symbol = 'X'

                        if firstClick == False:
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True
                            b5 = True                                                                        
                            b5symbol = 'O'

                        elif b6symbol == 'X' and b3symbol == 'X': 
                            if b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True     

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b6symbol == 'X' and b3symbol == 'X': 
                                    if b9 == False:
                                        pass

                                #elif b4 == False:
                                #    text(screen,'O',107,50,150,CYAN)
                                #    b4 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                                #else:
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b6symbol == 'X' and b4symbol == 'X':
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b6symbol == 'X' and b5symbol == 'X': 
                            if b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b6symbol == 'X' and b9symbol == 'X':
                            if b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True
                                
                            elif b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b6symbol == 'X' and b1symbol == 'X':
                            if b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True                                                 

                        elif b6symbol == 'X' and b2symbol == 'X': 
                            if b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b6symbol == 'X' and b7symbol == 'X': 
                            if b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True
                            
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b6symbol == 'X' and b8symbol == 'X': 
                            if b6symbol == 'X' and b3symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b6symbol == 'X' and b4symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b6symbol == 'X' and b5symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b6symbol == 'X' and b9symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True


                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                    else:
                        pass

        # B7
        if m_pos[0] >= 0 and m_pos[1] >= 200:
            if m_pos[0] <= 100 and m_pos[1] <= 300:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b7 == False:
                        text(screen,'X',100,50,250,RED)
                        b7 = True
                        b7symbol = 'X'

                        if firstClick == False:
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True
                            b5 = True                                                                        
                            b5symbol = 'O'

                        elif b7symbol == 'X' and b1symbol == 'X':
                            if b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:
                          
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                         
                        elif b7symbol == 'X' and b3symbol == 'X':
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:
                       
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                                                 
                        elif b7symbol == 'X' and b4symbol == 'X':
                            if b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True
                            elif b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                                               
                        elif b7symbol == 'X' and b5symbol == 'X':
                            if b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True
                            elif b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                            
                        elif b7symbol == 'X' and b8symbol == 'X':
                            if b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                            elif b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b7symbol == 'X' and b9symbol == 'X':
                            if b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                                #else:
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b7symbol == 'X' and b2symbol == 'X':
                            if b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True
                                       
                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True
                        
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                  
                        elif b7symbol == 'X' and b6symbol == 'X':
                            if b7symbol == 'X' and b1symbol == 'X':
                                if b4 == False:
                                    text(screen,'O',107,50,150,CYAN)
                                    b4 = True

                            elif b7symbol == 'X' and b3symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True
                                
                            elif b7symbol == 'X' and b4symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b7symbol == 'X' and b5symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b7symbol == 'X' and b8symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b7symbol == 'X' and b9symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                    else:
                        pass

        # B8
        if m_pos[0] > 100 and m_pos[1] > 200:
            if m_pos[0] <= 200 and m_pos[1] <= 300:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b8 == False:    
                        text(screen,'X',100,150,250,RED)
                        b8 = True
                        b8symbol = 'X'

                        if firstClick == False:
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True
                            b5 = True                                                                        
                            b5symbol = 'O'

                        elif b8symbol == 'X' and b2symbol == 'X':
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True
                                                
                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b8symbol == 'X' and b5symbol == 'X': 
                            if b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
                            elif b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                               # else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b8symbol == 'X' and b7symbol == 'X': 
                            if b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                            elif b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True        
                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                          
                        elif b8symbol == 'X' and b9symbol == 'X':
                            if b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True
                                
                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b8symbol == 'X' and b1symbol == 'X':
                            if b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                        
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
   
                        elif b8symbol == 'X' and b3symbol == 'X': 
                            if b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True
                            
                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                                                        
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b8symbol == 'X' and b4symbol == 'X':
                            if b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                            
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                            
                        elif b8symbol == 'X' and b6symbol == 'X': 
                            if b8symbol == 'X' and b2symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True
                            
                            elif b8symbol == 'X' and b5symbol == 'X':
                                if b2 == False:
                                    text(screen,'O',107,150,50,CYAN)
                                    b2 = True

                            elif b8symbol == 'X' and b7symbol == 'X':
                                if b9 == False:
                                    text(screen,'O',107,250,250,CYAN)
                                    b9 = True

                            elif b8symbol == 'X' and b9symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True                                
               
                    else:
                        pass

        # B9
        if m_pos[0] > 200 and m_pos[1] > 200:
            if m_pos[0] <= 300 and m_pos[1] <= 300:
                if event.type == pg.MOUSEBUTTONUP:
                    textSnd.play()
                    if b9 == False:
                        text(screen,'X',100,250,250,RED)
                        b9 = True
                        b9symbol = 'X'

                        if firstClick == False:
                            text(screen,'O',107,150,150,CYAN)
                            firstClick = True
                            b5 = True                                                                        
                            b5symbol = 'O'

                        elif b9symbol == 'X' and b1symbol == 'X':
                            if b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True  
                                              
                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                                elif b9symbol == 'X' and b8symbol == 'X':
                                    if b7 == False:
                                        text(screen,'O',107,50,250,CYAN)
                                        b7 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                                #else:
                            
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b9symbol == 'X' and b3symbol == 'X': 
                            if b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b9symbol == 'X' and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                                #else:
                     
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b9symbol == 'X' and b5symbol == 'X': 
                            if b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b9symbol == 'X' and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                                #else:
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b9symbol == 'X' and b6symbol == 'X': 
                            if b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b9symbol == 'X' and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                       
                        elif b9symbol == 'X' and b7symbol == 'X': 
                            if b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9symbol == 'X' and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                                
                        elif b9symbol == 'X' and b8symbol == 'X':
                            if b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b9symbol == 'X' and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                                #else:

                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b9symbol == 'X' and b2symbol == 'X': 
                            if b9symbol == 'X'and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                           
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True

                        elif b9symbol == 'X' and b4symbol == 'X':
                            if b9symbol == 'X'and b1symbol == 'X':
                                if b5 == False:
                                    text(screen,'O',107,150,150,CYAN)
                                    b5 = True

                            elif b9symbol == 'X' and b3symbol == 'X':
                                if b6 == False:
                                    text(screen,'O',107,250,150,CYAN)
                                    b6 = True

                            elif b9symbol == 'X' and b5symbol == 'X':
                                if b1 == False:
                                    text(screen,'O',107,50,50,CYAN)
                                    b1 = True

                            elif b9symbol == 'X' and b6symbol == 'X':
                                if b3 == False:
                                    text(screen,'O',107,250,50,CYAN)
                                    b3 = True

                            elif b9symbol == 'X' and b7symbol == 'X':
                                if b8 == False:
                                    text(screen,'O',107,150,250,CYAN)
                                    b8 = True

                            elif b9symbol == 'X' and b8symbol == 'X':
                                if b7 == False:
                                    text(screen,'O',107,50,250,CYAN)
                                    b7 = True
                        
                            elif b1 == False:
                                text(screen,'O',107,50,50,CYAN)
                                b1 = True

                            elif b2 == False:
                                text(screen,'O',107,150,50,CYAN)
                                b2 = True
        
                            elif b3 == False:
                                text(screen,'O',107,250,50,CYAN)
                                b3 = True

                            elif b4 == False:
                                text(screen,'O',107,50,150,CYAN)
                                b4 = True

                            elif b5 == False:
                                text(screen,'O',107,150,150,CYAN)
                                b5 = True

                            elif b6 == False:
                                text(screen,'O',107,250,150,CYAN)
                                b6 = True

                            elif b7 == False:
                                text(screen,'O',107,50,250,CYAN)
                                b7 = True

                            elif b8 == False:
                                text(screen,'O',107,150,250,CYAN)
                                b8 = True

                            elif b9 == False:
                                text(screen,'O',107,250,250,CYAN)
                                b9 = True
                                 
                    else:
                        pass
    #update section
    
    #draw section
    divGroups.draw(screen)
    pg.display.flip()

pg.quit()

#Over 4000 lines
