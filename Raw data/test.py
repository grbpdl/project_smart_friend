import sys
import pygame
from pygame.locals import *
import time
from csv import writer
import smtplib
import os
from pygame import mixer

mixer.init()
clock = pygame.time.Clock()
mixer.music.load("E:\learn\Project (Smart Friend)\step.mp3")
mixer.music.set_volume(0.5)
WIDTH ,HEIGHT=720,463
BG_COLOR=(255, 53, 184)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
white=(255,255,255)
j=[]
i=[]
username=os.environ.get('mygmail')
password=os.environ.get('mypassword')
# crush_name=''



img = pygame.image.load('E:\learn\Project (Smart Friend)\Intro.jpg')
img=pygame.transform.scale(img,(WIDTH,HEIGHT))
rect = img.get_rect()
img2 = pygame.image.load('E:\learn\Project (Smart Friend)\Result.jpg')
img2=pygame.transform.scale(img2,(WIDTH,HEIGHT))
rect2 = img2.get_rect()
img3 = pygame.image.load('E:\learn\Project (Smart Friend)\mat11.png')
img3=pygame.transform.scale(img3,(WIDTH,HEIGHT))
rect3 = img3.get_rect()
img4 = pygame.image.load('E:\learn\Project (Smart Friend)\mat2.png')
img4=pygame.transform.scale(img4,(WIDTH,HEIGHT))
rect4 = img4.get_rect()
ready = pygame.image.load('E:\learn\Project (Smart Friend)\mat3.png')
ready=pygame.transform.scale(ready,(WIDTH,HEIGHT))
rect4 = ready.get_rect()


class Text:
        def __init__(self, text,pos,font,size,color):
                self.text = text
                self.pos = pos
                self.fontname = font
                self.fontsize = size
                self.fontcolor = color
                self.set_font()
                self.render()
        
        def set_font(self):#Set the font from its name and size.
            self.font = pygame.font.Font(self.fontname, self.fontsize)


        def render(self):#Render the text into an image.
            self.img = self.font.render(self.text, True, self.fontcolor)
            self.rect = self.img.get_rect()
            self.rect.topleft = self.pos

        def draw(self):#Draw the text image to the screen.
            App.screen.blit(self.img, self.rect)
class gamestate:
    def __init__(self):
        self.screenid= 0
        self.input_rect = pygame.Rect(470, 170, 85, 85)
        self.username=''
        self.useremail=''
        self.select_sound=mixer.Sound('E:\learn\Project (Smart Friend)\clickselect.mp3')
        self.process_sound=mixer.Sound('E:\learn\Project (Smart Friend)\process.mp3')
        self.reveal_sound=mixer.Sound('E:\learn\Project (Smart Friend)\spb.mp3')
        
    
        
    
    def intro(self):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        mixer.music.play()
                        self.screenid= 1
            App.screen.blit(img,rect)
            App.t = Text('Press the heart to continue',(50,420),None,30,(32,32,132))   
            if time.time() % 1 > 0.5:
                App.t.draw()
            pygame.display.update()
    def game1(self):
            def input_text():
                self.text = pygame.font.Font('freesansbold.ttf', 25).render('Next', True, (0,0,255),(255,165,0))
                self.textRect = self.text.get_rect()
                self.textRect.center = (680,430)
                App.screen.fill((29,41,81))
                App.screen.blit(self.text, self.textRect)
                font = pygame.font.Font(None, 32)
                input_box = pygame.Rect(170, 100, 140, 40)
                input_box2 = pygame.Rect(170, 200, 140, 40)
                color_inactive = pygame.Color('lightskyblue3')
                color_active = pygame.Color('dodgerblue2')
                name_active=(255,0,0)
                color = color_inactive
                color1=color_inactive
                active = False
                active1 = False
                Name=""
                Email=""
                
                
                done = False
                while not done:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.textRect.collidepoint(event.pos):
                                mixer.music.play()
                                if Name!="" and Email!="":
                                    done=True
                                    self.screenid= 2
                            # If the user clicked on the input_box rect.
                            elif input_box.collidepoint(event.pos):
                                # Toggle the active variable.
                                active = not active
                            else:
                                active = False
                            # Change the current color of the input box.
                            color1 = name_active if active else color_inactive
                        if event.type == pygame.KEYDOWN:
                            if active:
                                if event.key == pygame.K_RETURN:
                                    Name = ''
                                elif event.key == pygame.K_BACKSPACE:
                                    Name = Name[:-1]
                                else:
                                    Name += event.unicode
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # If the user clicked on the input_box rect.
                            if input_box2.collidepoint(event.pos):
                                # Toggle the active variable.
                                active1 = not active1
                            else:
                                active1 = False
                            # Change the current color of the input box.
                            color = color_active if active1 else color_inactive
                        if event.type == pygame.KEYDOWN:
                            if active1:
                                if event.key == pygame.K_RETURN:
                                    Email = ''
                                elif event.key == pygame.K_BACKSPACE:
                                    Email = Email[:-1]
                                else:
                                    Email += event.unicode
                    App.screen.fill((30, 30, 30))
                    App.t = Text('Enter Your Information',(90,0),'freesansbold.ttf',50,(0,204,204))
                    App.t.draw()
                    App.t = Text('Name:',(10,100),'freesansbold.ttf',50,(0,204,204))
                    App.t.draw()
                    App.t = Text('Email:',(10,200),'freesansbold.ttf',50,(0,204,204))
                    App.t.draw()
                    App.screen.blit(self.text, self.textRect) 
                    # Render the current text
                    txt_surface = font.render(Name, True, color1)
                    txt_surface1 = font.render(Email, True, color)
                    # Resize the box if the Name is too long.
                    width = max(200, txt_surface.get_width()+10)
                    input_box.w = width
                    width1 = max(200, txt_surface1.get_width()+10)
                    input_box2.w = width1
                    # Blit the Name.
                    App.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                    App.screen.blit(txt_surface1, (input_box2.x+5, input_box2.y+5))
                    # Blit the input_box rect.
                    pygame.draw.rect(App.screen, color1, input_box, 2)
                    pygame.draw.rect(App.screen, color, input_box2, 2)
                    pygame.display.update()
                    pygame.display.flip()
                    
                return Name, Email

            n,e=input_text()
            self.username,self.useremail=n,e
            list_data=['S.N',n,e]
            with open('namemail.csv', 'a', newline='') as f_object:  
                writer(f_object).writerow(list_data)  
                f_object.close()
    def game2(self):
            self.text = pygame.font.Font('freesansbold.ttf', 25).render('Lets Go', True, (0,0,255),(255,165,0))
            self.textRect = self.text.get_rect()
            self.textRect.center = (650,430)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.textRect.collidepoint(event.pos):
                        mixer.music.play()
                        self.textRect.inflate_ip(-10,-10)
                        self.screenid= 3        
            App.screen.blit(ready,rect4)
            App.screen.blit(self.text, self.textRect)
            pygame.display.update()
    def game3(self):
            self.text = pygame.font.Font('freesansbold.ttf', 25).render('Next', True, (0,0,255),(255,165,0))
            self.textRect = self.text.get_rect()
            self.textRect.center = (680,430)
            self.textone = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textoneRect = self.textone.get_rect()
            self.textoneRect.center = (155,435)
            self.texttwo = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.texttwoRect = self.texttwo.get_rect()
            self.texttwoRect.center = (255,435)
            self.textthree = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textthreeRect = self.textthree.get_rect()
            self.textthreeRect.center = (355,435)
            self.textfour = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textfourRect = self.textfour.get_rect()
            self.textfourRect.center = (455,435)
            self.textfive = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textfiveRect = self.textfive.get_rect()
            self.textfiveRect.center = (555,435)
            self.textsix = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textsixRect = self.textsix.get_rect()
            self.textsixRect.center = (655,435)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.textRect.collidepoint(event.pos):
                        mixer.music.play()
                        self.textRect.inflate_ip(-10,-10)
                        self.screenid= 4       
                    if self.textoneRect.collidepoint(event.pos):
                        self.select_sound.play()
                        j.append(0)
                        self.textoneRect.inflate_ip(-10,-10)       
                    if self.texttwoRect.collidepoint(event.pos):
                        self.select_sound.play()
                        j.append(1)
                        self.texttwoRect.inflate_ip(-10,-10)
                    if self.textthreeRect.collidepoint(event.pos):
                        self.select_sound.play()
                        j.append(2)
                        self.textthreeRect.inflate_ip(-10,-10)
                    if self.textfourRect.collidepoint(event.pos):
                        self.select_sound.play()
                        j.append(3)
                        self.textfourRect.inflate_ip(-10,-10)
                    if self.textfiveRect.collidepoint(event.pos):
                        self.select_sound.play()
                        j.append(4)
                        self.textfiveRect.inflate_ip(-10,-10)
                        
            App.screen.blit(img3,rect3)
            App.screen.blit(self.text, self.textRect)
            App.screen.blit(self.textone, self.textoneRect)
            App.screen.blit(self.texttwo, self.texttwoRect)
            App.screen.blit(self.textthree, self.textthreeRect)
            App.screen.blit(self.textfour, self.textfourRect)
            App.screen.blit(self.textfive, self.textfiveRect)
            pygame.display.update()
    def game4(self):
            self.text = pygame.font.Font('freesansbold.ttf', 25).render('Next', True, (0,0,255),(255,165,0))
            self.textRect = self.text.get_rect()
            self.textRect.center = (680,430)
            self.textone = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textoneRect = self.textone.get_rect()
            self.textoneRect.center = (145,435)
            self.texttwo = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.texttwoRect = self.texttwo.get_rect()
            self.texttwoRect.center = (255,435)
            self.textthree = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textthreeRect = self.textthree.get_rect()
            self.textthreeRect.center = (355,435)
            self.textfour = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textfourRect = self.textfour.get_rect()
            self.textfourRect.center = (455,435)
            self.textfive = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textfiveRect = self.textfive.get_rect()
            self.textfiveRect.center = (555,435)
            self.textsix = pygame.font.Font('freesansbold.ttf', 20).render('Select', True, white,BLACK)
            self.textsixRect = self.textsix.get_rect()
            self.textsixRect.center = (630,335)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.textRect.collidepoint(event.pos):
                        self.reveal_sound.play()
                        self.screenid= 5       
                    if self.textoneRect.collidepoint(event.pos):
                        self.select_sound.play()
                        i.append(0)
                        self.textoneRect.inflate_ip(-10,-10)       
                    if self.texttwoRect.collidepoint(event.pos):
                        self.select_sound.play()
                        i.append(1)
                        self.texttwoRect.inflate_ip(-10,-10)
                    if self.textthreeRect.collidepoint(event.pos):
                        self.select_sound.play()
                        i.append(2)
                        self.textthreeRect.inflate_ip(-10,-10)
                    if self.textfourRect.collidepoint(event.pos):
                        self.select_sound.play()
                        i.append(3)
                        self.textfourRect.inflate_ip(-10,-10)
                    if self.textfiveRect.collidepoint(event.pos):
                        self.select_sound.play()
                        i.append(4)
                        self.textfiveRect.inflate_ip(-10,-10)
                    if self.textsixRect.collidepoint(event.pos):
                        self.select_sound.play()
                        i.append(5)
                        self.textsixRect.inflate_ip(-10,-10)
                        
            App.screen.blit(img4,rect4)
            App.screen.blit(self.text, self.textRect)
            App.screen.blit(self.textone, self.textoneRect)
            App.screen.blit(self.texttwo, self.texttwoRect)
            App.screen.blit(self.textthree, self.textthreeRect)
            App.screen.blit(self.textfour, self.textfourRect)
            App.screen.blit(self.textfive, self.textfiveRect)
            App.screen.blit(self.textsix, self.textsixRect)
            pygame.display.update()
    def result(self):
            self.text = pygame.font.Font('freesansbold.ttf', 25).render('Finish', True, (0,0,255),(255,180,0))
            self.textRect = self.text.get_rect()
            self.textRect.center = (650,440)
            crush_name=''
            mat=[['b','g','k','f','c'],['s','m','a','r','t'],['j','q','z','i','p'],['w','x','u','e','v'],['l','y','o','n','h'],['$','$','$','d','$']]
            
            if len(i)!=len(j):
                crush_name="wrong ip"
            else:
                for x in range(len(j)):
                    crush_name=crush_name+mat[i[x]][j[x]]               
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.textRect.collidepoint(event.pos):
                        self.process_sound.play()
                        i.clear()
                        j.clear()
                        s = smtplib.SMTP('smtp.gmail.com', 587)
                        s.ehlo()
                        s.starttls()
                        s.ehlo()
                        s.login(username, password)
                        SUBJECT='Help from Smart Friend'
                        receiver=self.useremail
                        letter='''My dear {} ,I am not very good at expressing my feelings in words, even though I assure you, I am quite a sensitive person. Somehow, often I get shy and run out of words even before I start talking.
However, I now want to tell you about my feelings.

We have been seeing each other for a while and I realize that the more I see you, the more I want to be with you. You are like a beacon of light in a starless night and I am drawn to you with a powerful pull that I can’t resist.
When I am not with you, I keep thinking about you and my day is rather empty. I find myself looking forward to our next meeting.
Yes, I realize now that I care for you very much and my feelings for you have awakened and are getting stronger and stronger each day.
I am starting to fall in love with you and my heart is fluttering every time I am near you … I just hope you have the same sensations and feelings as I do.

I just wanted to write my thoughts down and secretly send this love letter to you.

        I am yours {} , forever …

PS:Have the guts and be positive,fordward this love mail to your crush!Wishing you best of luck!
    -yours Smart Friend'''
                        TEXT=letter.format(crush_name,self.username)
                        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                        message=message.encode('ascii', 'ignore').decode('ascii')
                        if crush_name!="wrong ip":           
                            try:
                                s.sendmail(username,receiver,message)
                            except:
                                pass
                        
                        s.quit()
                        self.screenid= 0
                # name_finder()
            App.screen.blit(img2,rect2)
            App.t = Text(crush_name.upper(),(290,200),None,50,(255,255,0))
            App.t.draw()
            App.t = Text('Project Members',(20,300),None,40,(255,255,255))
            App.t.draw()
            App.t = Text('Yubraj Adhikari',(20,330),None,30,(255,255,0))
            App.t.draw()
            App.t = Text('Binay Rijal',(20,360),None,30,(255,255,0))
            App.t.draw()
            App.t = Text('Suman Sharma',(20,390),None,30,(255,255,0))
            App.t.draw()
            App.t = Text('Gaurab Paudyal',(20,420),None,30,(255,255,0))
            App.t.draw()
            
            App.screen.blit(self.text, self.textRect)
            
            pygame.display.update()
    def scene_manager(self):
        self.result()
        
        # if self.screenid == 0:
        #     self.intro()
        # if self.screenid == 1:
        #     self.game1()
        # if self.screenid == 2:
        #     self.game2()
        # if self.screenid == 3:
        #     self.game3()
        # if self.screenid == 4:
        #     self.game4()
        # if self.screenid == 5:
        #     self.result()
    
            
class App:
    def __init__(self):
            
            pygame.init()
            flags = RESIZABLE
            App.screen = pygame.display.set_mode((WIDTH,HEIGHT), flags)
            App.running = True
            self.bg_sound=mixer.Sound('E:\learn\Project (Smart Friend)\smoothbg.mp3')
            self.bg_sound.set_volume(0.14)
            
    def run(self):
        gs=gamestate()
        self.bg_sound.play()
        while App.running:
            gs.scene_manager()
            clock.tick(60)
            
        pygame.quit()
    
if __name__ == '__main__':
        App().run()
    