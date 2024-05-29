import pygame
import ramdom
import math
import sys
import os


#inicializar pygame
pygame.init()

#establecer el tamaño de pantalla 
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width,screen_height))


#Funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MESPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path,relative_path)

#importar imagen de fondo 
asset_background = resource_path('asset/images/background.png')
background= pygame.image.load(assets_background.png)

#Cargar icono de ventana 
asset_icon = resourse_path('asset/images/ufo.png')
icon = pygame.image.load(asset_icon)

#Cargar sonido de fondo 
asset_sound= audio_path('asset/audios/background_misic.mp3')
backgound_sound = pygame.mixer.music.load(asset_sound)

#Cargar imagen del jugador
asset_playerimg = resourse_path('asset/images/espace-invaders.png')
playermig= pygame.image.load(asset_playerimg)

#Cargar imagen de balas
asset_bulleting = resourse_path('asset/images/bullet.png')
bulleting= pygame.image.load(asset_bulleting)

#Cargar texto de game over
asset_over_font = resourse_path('asset/fonts/RAVIE.TTF')
over_font= pygame.font.Font(asset_over_font, 60)

#Cargar fuente para texto de puntaje
asset_ = resourse_path('asset/fonts/comicbd.ttf')
font= pygame.font.Font(asset_font, 32)

#Establecer titulo de ventana 
pygame.display.set_caption("Space Invader")

#Establecer icono de ventana
pygame.display.set_icon(icon)

#Reproducir sonido  de fondo
pygame.mixer.music.play(-1)

#Creaer un reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

#Posicion inicial del jugador
playerX = 370
playerY = 470
playerx_change = 0
playery_change = 0

#Lista para almacenar posiciones de los enemigos
enemying = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

#Se inicializan las variables para guardar las posiciones de los enemigos
for i in range(no_of_enemies):
    # Se carga la imagen del enemigo 1

    enemy1 = resource_path('assets/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))
     #Se carga la imagen del enemigo 2

    enemy2 = resource_path('assets/images/enemy2.png')
    enemyimg.append(pygame.image.load(enemy2))

    #se asigna una posicion aleatorea en X y Y para el enemigo
    enemyX.append(ramdom.randint(0,736))
    enemyY.append(ramdom.randint(0,150))
    
    #se esstablece la velocidad de movimiento del enemigo en X y en Y
    enemyX_change.append(5)
    enemyY_change.append(20)

    #se inicializan las variables para guardar la posicion de la bala 
    bulletX = 0
    bulletY = 480
    bulletX_change = 0 
    bulletY_change = 10
    bullet_state = "ready"

    #se iicializa puntuacion en 0
    score = 0

    #funcion para mostrar la puntuacion en la  pantalla 
    def show_score():
        score_value = font.render("SCORE" + str(score), True,(255, 255, 255))
        screen.blit(score_value, (10,10))

    #funcion para dibujar al jugador en la pantalla 
    def player(x, y):
        screen.blit(playermig,(x, y))

    #funcion para dibujar al enemigo en la pantalla 
    def enemy(x, y, i):
        screen.blit(enemyimg, {i}, (x, y))
    
    #funcion para disparar la bala 
    def fire_bullet(x, y):
        global bullet_state

        bullet_state = "fire"
        screen.blit(bulletimg, (x +16, y + 10))

    # funcion para comprobar si ha habido una colision entre la bala y el enemigo
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                              (math.pow(enemyY-bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False
    
    #funcion par mostrar texto de game over en pantalla 
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        text_rect = over_text.get_rect(
            center=(int(screen_with/2), int (screen_heigth/2)))
        screen.blit(over_text, text_rect)

    #funcion principal del juego 
    def gameloop():

        #declarar variables globales 
        global score
        global playerX
        global playerx_change
        global bulletX
        global bulletY
        global Collision
        global bullet_state

        in_game = True
        while in_game:
            #Maneja eventos, actualiza y renderiza el juego 
            #limpia la pnatalla 
            screen.fill((0, 0 ,0))
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game == False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #maneja los movimientos del jugador y el disparo 
                    if event.key == pyagme.K_LEFT:
                        playerx_change = -5
                    
                    if event.key == pygame.K_RIGHT:
                        playerx_change = 5

                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)
                    
                if event.type == pygame.KEYUP:
                    playerx_change = 0 

            #se actualiza la posicion del jugador 
            playerX += playerx_change

            if playerX <= 0:
             playerX = 0 
            elif playerX >= 736:
                playerX = 736

            #bucle que se ejecuta para cada enemigo 
            for i in range(no_of_enemies):
                if enemyY[i] > 440:
                    for j in range(no_of_enemies):
                        enemyY[j] = 2000
                    game_over_text()

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]
                
                #aqui se comprueba si ha habido colision entre un enemigo y una bala 

                collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collison: 
                    bulleY = 454
                    bullet_state = "ready"
                    score += 1
                    enemyX[i] = ramdom.randint(0, 736)
                    enemyY[i] = ramdom.randint(0, 150)
                    enemy(enemyX[i], enemyY[i], i)
            
            if bulletY < 0:
                bulletY = 454
                bullet = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            player(playerX, playerY)
            show_score()

            pygame.display.update()

            clock.tick(120)

gameloop()                
