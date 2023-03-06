import pygame
import random
import mysql.connector
dbconfig={
    "host":"127.0.0.1",
    "user":"root",
    "password":"Aa10219791.",
    "database":"race"
}
conection=mysql.connector.connect(**dbconfig)
cursor=conection.cursor()
sqlrecvest="select * from users"
cursor.execute(sqlrecvest)
#conection.commit()
res=cursor.fetchall()
print(res)
Name = input("введіть ваше імя")
while Name == "":
    Name = input("введіть ваше імя")
for user in res:
    if(user)[1] == Name:
       print("такий користувач вже існує")
    else:
        sqlrecvest1=f"insert into users(name)values(\"{Name}\")"
        cursor.execute(sqlrecvest1)
        conection.commit()
cursor.close()
conection.close()
pygame.init()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BROWN = (100, 40, 0)
WHITEBlUE = (0, 255, 255)
RANDOM_COLIR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)
first_apple_y = 250
second_apple_y = 200
third_aplle_y = 180
fourth_aplle_y = 270
fifth_aplle_y = 300
first_aplle_dir = True
second_apple_dir = True
third_aplle_dir = True
first_car_dir = True
second_car_dir = True
third_car_dir = True
first_car_x = 10
second_car_x = 10
third_car_x = 10
FPS = 60
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
x, y = 0, 0
x1, y1 = 0, 70
y2,y3 = 100,300
direction = 0
ROAD = []
offset = 15
random.choice((70,330))
rect = pygame.Rect(10,10,10,10)
frame_count = 0
distance = 0
is_collide = False
game_mode ="меню"
car_btm = pygame.Rect(290,290,100,30)
car1_btm = pygame.Rect(410,290,100,30)
setting = pygame.Rect(355,335,120,30)
car =  pygame.transform.scale(pygame.image.load("1669943398_20-pibig-info-p-mashina-sprait-instagram-29.png"),(200, 200))
car_1 =  pygame.transform.scale(pygame.image.load("untitled.png"),(200, 200))
mushroom = pygame.transform.scale(pygame.image.load("images-removebg-preview.png"),(150, 150))
wall = pygame.transform.scale(pygame.image.load("brick-wall-seamless-texture-vector-pattern-background-game-design-brick-wall-vector-seamless-patterns-107356273 (1).jpg"),(100, 100))
hole = pygame.transform.scale(pygame.image.load("pngtree-yellow-black-hole-image_1199230-removebg-preview.png"),(150, 150))
heart = pygame.transform.scale(pygame.image.load("heart_pixel_art_254x254-removebg-preview.png"),(100, 100))
car_rect = pygame.Rect(0,0,car.get_rect()[2],car.get_rect()[3]-100)
chosed_button = 0
fond_stile = pygame.font.SysFont("arial",55)
fond_stile_1 = pygame.font.SysFont("arial",15)
fond_stile_2 = pygame.font.SysFont("arial",30)
lable = fond_stile.render("МЕНЮ", True , BLACK)
lable_green_buton = fond_stile_1.render("Машина №1",True,BLUE)
lable_blue_buton = fond_stile_1.render("Машина №2",True,GREEN)
lable_black_buton = fond_stile_1.render("Налаштування",True,BLACK)
lable_setting_W = fond_stile.render("W - UP",True, WHITE)
lable_setting_S = fond_stile.render("S - DOWN",True, WHITE)
lable_setting_A = fond_stile.render("A - LEFT",True, WHITE)
lable_setting_D = fond_stile.render("D - RIGHT",True, WHITE)
back_from_settings = pygame.Rect(WIDTH-30,0,30,30)
lable_setting_exit = fond_stile_2.render("<-",True,WHITE)
lable_distance = fond_stile_2.render(f"проїхано {str(distance)} км",True,WHITE)
barier_rect = pygame.Rect(WIDTH,random.choice([40,230]),mushroom.get_rect()[2],mushroom.get_rect()[3])
back_sound = pygame.mixer.Sound("back_sound.mp3")
back_sound.set_volume(0.05)
game_sound = pygame.mixer.Sound("game_sound.mp3")
game_sound.set_volume(0.05)
game_over_sound = pygame.mixer.Sound("game_over_sound.wav")
game_over_sound.set_volume(0.05)
# Names = ["Ivan","Maxsim","Volodumyr","Andriy","Victor","Ostap","Denis","Ariel","Eva"]
# Name_3 = []
# for I in range(3):
#     Name_3.append(random.choice(Names))
# file = open("Rezalt","a")
# for I in Name_3:
#     file.write(I+"\n")
# file.close()
counter = 0
speed = 5
lifes = 100
lifes_rect = pygame.Rect(WIDTH-100,0,lifes,20)
disel = 100
disel_rect = pygame.Rect(WIDTH-100,30,disel,20,)
array_off_sprites = [mushroom,wall,hole]
sprite = random.choice(array_off_sprites)
bonus = pygame.Rect(WIDTH,random.choice([40,230]),heart.get_rect()[2],heart.get_rect()[3])
is_move = False
for number in range(1, WIDTH, 50):
    ROAD.append([number, 200, 50 - offset, 20])
while True:
    window.fill(RANDOM_COLIR)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.rect(window,RANDOM_COLIR,(event.pos[0],event.pos[1],5,5))
                if back_from_settings.collidepoint(event.pos):
                    game_mode = "меню"
                if car_btm.collidepoint(event.pos):
                    chosed_button = 1
                    game_mode = "гра"
                if car1_btm.collidepoint(event.pos):
                    chosed_button = 2
                    game_mode = "гра"
                if setting.collidepoint(event.pos):
                    chosed_button = 3
                    game_mode = "гра"

           # window.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = 1
            elif event.key == pygame.K_s:
                direction = 2
            if event.key == pygame.K_a:
                direction = 3
            elif event.key == pygame.K_d:
                direction = 4
        elif event.type == pygame.KEYUP:
            direction = 0
        if event.type == pygame.QUIT:
            pygame.quit()
    if game_mode == "меню":
        back_sound.play()
        window.fill(WHITE)
        window.blit(lable,(320,100))
        pygame.draw.rect(window, GREEN, (car_btm))
        pygame.draw.rect(window, BLUE, (car1_btm))
        pygame.draw.rect(window, RED,(setting))
        window.blit(lable_green_buton , (300, 295))
        window.blit(lable_blue_buton , (420, 295))
        window.blit(lable_black_buton, (360, 340))
    elif game_mode =="гра":
        back_sound.stop()
        game_sound.play()
        if car_rect.colliderect(bonus) and lifes < 100 and is_move:
            lifes += 20
            lifes_rect = pygame.Rect(WIDTH - 100, 0, lifes, 20)
            bonus = pygame.Rect(WIDTH,random.choice([40,230]),heart.get_rect()[2],heart.get_rect()[3])
            is_move = False
        if car_rect.colliderect(barier_rect):
            lifes -= 20
            lifes_rect = pygame.Rect(WIDTH - 100, 0, lifes, 20)
            if lifes <= 0:
                is_collide = True

                if chosed_button == 1:
                    file = open("Rezalt", "a", encoding="utf-8")
                    file.write(f"Зелена машина проїхала: {str(distance)}\n")
                    file.close()
                else:
                    file = open("Rezalt", "a", encoding="utf-8")
                    file.write(f"Синя машина проїхала: {str(distance)}\n")
                    file.close()
            counter += 1
            barier_rect = pygame.Rect(WIDTH,random.choice([40,230]),mushroom.get_rect()[2],mushroom.get_rect()[3])
            sprite = random.choice(array_off_sprites)
        if car_rect.x <= 0 and car_rect.x >= 800:
            direction = 0
        if car_rect.y <= 0 and car_rect.y >= 400:
            direction = 0
        if direction == 1 and car_rect.y > 0:
            car_rect = pygame.Rect.move(car_rect,0,-5)
        if direction == 2 and car_rect.y < 550:
            car_rect = pygame.Rect.move(car_rect,0,+5)
        if direction == 3 and car_rect.x > 0:
            car_rect = pygame.Rect.move(car_rect,-5,0)
        if direction == 4 and car_rect.x < 750:
            car_rect = pygame.Rect.move(car_rect,+5,0)
        if direction == 0:
            pass
        if x1 <= 0 and x1 >= 800:
            direction = 0
        if y1 <= 0 and y1 >= 235:
            direction = 0
        if direction == 1 and y1 > 0:
            y1 -= 5
        if direction == 2 and y1 < 550:
            y1 += 5
        if direction == 3 and x1 > 0:
            x1 -= 5
        if direction == 4 and x1 < 750:
            x1 += 5
        if direction == 0:
            pass
        pygame.draw.rect(window, BLACK, (0, 0, WIDTH, 400))
        for number in ROAD:
            number[0] -= speed
            if number[0] <= 0:
                number[0] = WIDTH
                disel -= 0.18
                disel_rect = pygame.Rect(WIDTH - 100, 30, disel, 20, )
            pygame.draw.rect(window, WHITE, number)
        if chosed_button == 1:
            window.blit(car, (car_rect.x, car_rect.y-50))
        else:
            window.blit(car_1,(car_rect.x,car_rect.y-50))
        barier_rect = pygame.Rect.move(barier_rect,-speed,0)
        if distance % 10 == 0 or is_move:
            is_move = True
            window.blit(heart,(bonus.x,bonus.y))
            bonus = pygame.Rect.move(bonus,-speed,0)
        if bonus.x <= 0:
            bonus = pygame.Rect(WIDTH,random.choice([40,230]),heart.get_rect()[2],heart.get_rect()[3])
            is_move = False
        if barier_rect.x <= 0:
            barier_rect = pygame.Rect(WIDTH,random.choice([40,230]),mushroom.get_rect()[2],mushroom.get_rect()[3])
            sprite = random.choice(array_off_sprites)
        window.blit(sprite,(barier_rect.x,barier_rect.y))
        pygame.draw.rect(window,RED,rect)
        pygame.draw.rect(window, RED, (lifes_rect))
        pygame.draw.rect(window, BROWN,(disel_rect))
        rect.left += 5
        if chosed_button == 3:
            window.fill(RANDOM_COLIR)
            pygame.draw.rect(window, BLACK, (10,10,300,100))
            window.blit(lable_setting_W, (25,30))
            pygame.draw.rect(window, BLACK, (10,120, 300, 100))
            window.blit(lable_setting_S, (25, 140))
            pygame.draw.rect(window, BLACK, (10, 230, 300, 100))
            window.blit(lable_setting_A, (25, 245))
            pygame.draw.rect(window, BLACK, (10, 340, 300, 100))
            window.blit(lable_setting_D, (25, 355))
            pygame.draw.rect(window,BLACK,(back_from_settings))
            window.blit(lable_setting_exit,(WIDTH-30,-3))
        window.blit(lable_distance, (0, 0))
    else:
        window.fill(RED)
        game_sound.stop()
        game_over_sound.play()
    lable_distance = fond_stile_2.render(f"проїхано {str(distance)}км", True, WHITE)
    if is_collide == True:
        game_mode ="гра закінчена"
        background = pygame.transform.scale(pygame.image.load(("png-clipart-es-game-over-text-thumbnail.png")),(800,600))
        window.blit(background,(0,0))
        file = open("Rezalt", "r",encoding="utf-8")
        Score = file.readlines()
        file.close()
        y = 10
        x = 600
        for I in Score[-5:]:
            Score_lable = fond_stile_1.render(I, True, BROWN)
            window.blit(Score_lable, (x,y))
            y+=30
    frame_count += 1
    distance = frame_count//FPS
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
