import pygame
import sys
import math 

pygame.init()



ekran_genislik = 600
ekran_yukseklik = 800
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption("Keep The Car In The ROAD")

begginning_screen = pygame.image.load("beginning_screen.jpg")
begginning_screen = pygame.transform.scale(begginning_screen, (ekran_genislik, ekran_yukseklik))


# Arka plan resmini yükle ve ölçekle
arkaplan = pygame.image.load("main_screen.jpg")
arkaplan = pygame.transform.scale(arkaplan, (ekran_genislik, ekran_yukseklik))

main_screen_left0 = pygame.image.load("main_screen_left0.jpg")
main_screen_left0 = pygame.transform.scale(main_screen_left0, (ekran_genislik, ekran_yukseklik))

main_screen_left1 = pygame.image.load("main_screen_left1.jpg")
main_screen_left1 = pygame.transform.scale(main_screen_left1, (ekran_genislik, ekran_yukseklik))

main_screen_left2 = pygame.image.load("main_screen_left2.jpg")
main_screen_left2 = pygame.transform.scale(main_screen_left2, (ekran_genislik, ekran_yukseklik))

main_screen_left3 = pygame.image.load("main_screen_left3.jpg")
main_screen_left3 = pygame.transform.scale(main_screen_left3, (ekran_genislik, ekran_yukseklik))

main_screen_left4 = pygame.image.load("main_screen_left4.jpg")
main_screen_left4 = pygame.transform.scale(main_screen_left4, (ekran_genislik, ekran_yukseklik))

main_screen_right0 = pygame.image.load("main_screen_right0.jpg")
main_screen_right0 = pygame.transform.scale(main_screen_right0, (ekran_genislik, ekran_yukseklik))

main_screen_right1 = pygame.image.load("main_screen_right1.jpg")
main_screen_right1 = pygame.transform.scale(main_screen_right1, (ekran_genislik, ekran_yukseklik))

main_screen_right2 = pygame.image.load("main_screen_right2.jpg")
main_screen_right2 = pygame.transform.scale(main_screen_right2, (ekran_genislik, ekran_yukseklik))

main_screen_right3 = pygame.image.load("main_screen_right3.jpg")
main_screen_right3 = pygame.transform.scale(main_screen_right3, (ekran_genislik, ekran_yukseklik))

main_screen_right4 = pygame.image.load("main_screen_right4.jpg")
main_screen_right4 = pygame.transform.scale(main_screen_right4, (ekran_genislik, ekran_yukseklik))

ending_lose = pygame.image.load("ending_lose.jpg")
ending_lose = pygame.transform.scale(ending_lose, (ekran_genislik, ekran_yukseklik))

ending_win = pygame.image.load("ending_win.jpg")
ending_win = pygame.transform.scale(ending_win, (ekran_genislik, ekran_yukseklik))

car = pygame.image.load("car.png")
car = pygame.transform.scale(car,(170,170))

wheel = pygame.image.load("steering_wheel_real.png")
wheel = pygame.transform.scale(wheel, (175,175))

healt_coin_1 = pygame.image.load("healt2.png")
healt_coin_1 = pygame.transform.scale(healt_coin_1,(75,75))

healt_coin_2 = pygame.image.load("healt2.png")
healt_coin_2 = pygame.transform.scale(healt_coin_2,(75,75))

healt_coin_3 = pygame.image.load("healt2.png")
healt_coin_3 = pygame.transform.scale(healt_coin_3,(75,75))

state = "beginnig"



clock = pygame.time.Clock()

font = pygame.font.Font(None, 100)
font_warnings = pygame.font.Font(None,30)


first_location_x = 200
first_location_y = 500

t = 0
degree = 0 
q = 0
x,y = 0,0

wheel_orijinal_x = 250
wheel_orijinal_y = 690

original_healt_coins = 3

warning_counter = 0
last_warning_time = 0 
losing_coin_time = 0

def CalculatingDegree(a,b,orijinal_a,orijinal_b):
    thing = math.sqrt((((orijinal_a-a)**2)+((orijinal_b-b)**2)))
    degree = math.acos((orijinal_a-a)/thing)
    return degree*40 

def ShowingAllHealtCoins(original_healt_coins):
    if original_healt_coins == 3:
        ekran.blit(healt_coin_1,(400,80))
        ekran.blit(healt_coin_2,(450,80))
        ekran.blit(healt_coin_3,(500,80))
    elif original_healt_coins == 2:
        ekran.blit(healt_coin_2,(450,80))
        ekran.blit(healt_coin_3,(500,80))
    elif original_healt_coins == 1:
        ekran.blit(healt_coin_3,(500,80))

def Warnings(warning_counter,last_warning_time):
    now = pygame.time.get_ticks()
    if now - last_warning_time >= 3000:
        warning_counter += 1
        last_warning_time = now

    warning_sign = font_warnings.render("CAREFULL! YOU ARE NOT IN THE ROAD!",True,(255,255,0))
    ekran.blit(warning_sign,(100,100))
    warning_counter = warning_counter+1
    return warning_counter,last_warning_time

def LosingAHealtCoin(original_healt_coins,losing_coin_time):
    now = pygame.time.get_ticks()
    losing_announcement = font_warnings.render("You Lost One Of Your Healt Coins!",True,(255,255,90))
    ekran.blit(losing_announcement,(100,120))
    print(f"original healt coins are = {original_healt_coins}")
    if now - losing_coin_time >= 1000:
        losing_coin_time = now
        original_healt_coins = original_healt_coins-1
    ShowingAllHealtCoins(original_healt_coins)
    return original_healt_coins,losing_coin_time

def CheckingWinning(t):
    if t>= 500:
        if state != "begginning":
            if state != "countdown":
                if state != "game_screen":
                    if state != "ending_screen_lose":
                        state = "ending_screen_win"
                        return state


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    tuslar = pygame.key.get_pressed()
    
    if state == "beginnig":
        ekran.blit(begginning_screen, (0, 0))
        if tuslar[pygame.K_SPACE]:
            state = "countdown"
            print("Space'e basıldı oyun başlatılıyor!")
            starting_time = pygame.time.get_ticks()
            ekran.blit(arkaplan, (0, 0))
    
    if state == "countdown":
        now = pygame.time.get_ticks()
        count = now - starting_time
        ShowingAllHealtCoins(original_healt_coins)
        if count < 2000:
            text = font.render("3!", True, (0, 255, 0))
            ekran.blit(text, (270, 250))
        elif count < 3000:
            text = font.render("2!", True, (0, 255, 0))
            ekran.blit(arkaplan, (0, 0))
            ShowingAllHealtCoins(original_healt_coins)
            ekran.blit(text, (270, 250))
        elif count < 4000:
            text = font.render("1!", True, (0, 255, 0))
            ekran.blit(arkaplan, (0, 0))
            ShowingAllHealtCoins(original_healt_coins)
            ekran.blit(text, (270, 250))
        elif count < 5000:
            text = font.render("START!", True, (0, 255, 0))
            ekran.blit(arkaplan, (0, 0))
            ShowingAllHealtCoins(original_healt_coins)
            ekran.blit(text, (180, 250))
        else:
            state = "game_screen"

    if state == "game_screen":
        ekran.blit(car,(200,550))
        ekran.blit(arkaplan, (0, 0))
        ShowingAllHealtCoins(original_healt_coins)
    
        if t < 500:
            new_location = (first_location_x,first_location_y-5)
            first_location_y=first_location_y-5
            ekran.blit(car,new_location)
        
            t = t+5
    
        if q < 500:
            degree = CalculatingDegree(x,y,wheel_orijinal_x,wheel_orijinal_y)
            if 0 < degree <= 60:
                turning_wheel = pygame.transform.rotate(wheel,degree)
                rect = turning_wheel.get_rect(center=(wheel_orijinal_x,wheel_orijinal_y))
                ekran.blit(turning_wheel, rect.topleft)
            if 60 < degree <= 140:
                degree = degree * (-1)
                turning_wheel = pygame.transform.rotate(wheel,degree)
                rect = turning_wheel.get_rect(center=(wheel_orijinal_x,wheel_orijinal_y))
                ekran.blit(turning_wheel, rect.topleft)
            q = q+5
            print(f"The Degree is now : {degree}")
    
        if 0 < degree <= 60:
            if 0 < degree <= 10 :
                ekran.blit(car,new_location)
                ekran.blit(main_screen_left0, (0, 0))
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,(first_location_x-15,first_location_y-5))
            elif 10 < degree < 20 :
                ekran.blit(car,new_location)
                ekran.blit(main_screen_left1, (0, 0))
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,(first_location_x-15,first_location_y-5))
            elif 20 <= degree <40:
                ekran.blit(car,new_location)
                ekran.blit(main_screen_left2, (0, 0))
                warning_counter,last_warning_time = Warnings(warning_counter,last_warning_time)
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,(first_location_x-15,first_location_y-5))
                print(f"the warning count is {warning_counter}")
                if warning_counter >= 3:
                    print("You take 3 and more warnings. ")
                    original_healt_coins,losing_coin_time= LosingAHealtCoin(original_healt_coins,losing_coin_time)
                    print(f"Rest of your healt coins are {original_healt_coins}")
                    if original_healt_coins == 0:
                        state = "ending_screen_lose"
            elif 40<= degree <= 50:
                ekran.blit(car,new_location)
                ekran.blit(main_screen_left3, (0, 0))
                warning_counter,last_warning_time = Warnings(warning_counter,last_warning_time)
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,(first_location_x-15,first_location_y-5))
                print(f"the warning count is {warning_counter}")
                if warning_counter >= 3:
                    print("You take 3 and more warnings. ")
                    original_healt_coins,losing_coin_time= LosingAHealtCoin(original_healt_coins,losing_coin_time)
                    print(f"Rest of your healt coins are {original_healt_coins}")
                    if original_healt_coins == 0:
                        state = "ending_screen_lose"
            elif 50< degree <= 60:
                ekran.blit(car,new_location)
                ekran.blit(main_screen_left4, (0, 0))
                warning_counter,last_warning_time=Warnings(warning_counter,last_warning_time)
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,(first_location_x-15,first_location_y-5))
                print(f"the warning count is {warning_counter}")
                if warning_counter >= 3:
                    print("You take 3 and more warnings. ")
                    original_healt_coins,losing_coin_time= LosingAHealtCoin(original_healt_coins,losing_coin_time)
                    print(f"Rest of your healt coins are {original_healt_coins}")
                    if original_healt_coins == 0:
                        state = "ending_screen_lose"

        elif -60 > degree >= -140:
            if -60 > degree > -70 :
                ekran.blit(main_screen_right0, (0, 0))
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,new_location)
            elif -70 > degree > -80 :
                ekran.blit(main_screen_right1, (0, 0))
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,new_location)
            elif -80 >= degree >-90:
                ekran.blit(main_screen_right2, (0, 0))
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,new_location)
            elif -90>= degree >= -100:
                ekran.blit(main_screen_right3, (0, 0))
                warning_counter,last_warning_time = Warnings(warning_counter,last_warning_time)
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,new_location)
                if warning_counter >= 3:
                    print("You take 3 and more warnings. ")
                    original_healt_coins,losing_coin_time= LosingAHealtCoin(original_healt_coins,losing_coin_time)
                    print(f"Rest of your healt coins are {original_healt_coins}")
                    if original_healt_coins == 0:
                        state = "ending_screen_lose"
            elif -100> degree >= -140:
                ekran.blit(main_screen_right4, (0, 0))
                warning_counter,last_warning_time = Warnings(warning_counter,last_warning_time)
                ShowingAllHealtCoins(original_healt_coins)
                ekran.blit(turning_wheel, rect.topleft)
                ekran.blit(car,new_location)
                if warning_counter >= 3:
                    print("You take 3 and more warnings. ")
                    original_healt_coins,losing_coin_time= LosingAHealtCoin(original_healt_coins,losing_coin_time)
                    print(f"Rest of your healt coins are {original_healt_coins}")
                    if original_healt_coins == 0:
                        state = "ending_screen_lose"
    if t>= 500:
        if state != "begginning":
            if state != "countdown":
                if state != "ending_screen_lose":
                    state = "ending_screen_win"

    if state == "ending_screen_lose":
        ekran.blit(ending_lose,(0,0))

    if state == "ending_screen_win":
        ekran.blit(ending_win,(0,0))
    
    pygame.display.update()
    clock.tick(10)

