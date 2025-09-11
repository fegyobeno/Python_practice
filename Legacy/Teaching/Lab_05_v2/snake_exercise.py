# Importok
import pygame
import time
import random

# Előre definiált színek
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#----------Feladat-----------------------
# Hozd létre a kígyó sebességét kontroláló változót, ez lesz az FPS

# Hozd létre az ablak méretét tároló változókat

#Inicializáld a pygame-t

# Inicializád az ablakot (Caption -> opcionális, size -> kötelező)

# Hozd létre a játékórát, ez lesz a játék sebességét szabályzó változó

# Hozz létre egy két elemű listát, amely a kígyó pozícióját tárolja

# Hozz létre egy listák listáját, ami a kígyó testét tárolja

# Hozd létre a gyümölcs pozícióját tároló listát

# Hozz létre egy változót, ami azt tárolja, hogy a gyümölcs megjelent-e

# Hozz létre egy véltozót, ami tárolja a kígyó irányát

# implementáld a függvényt ami azért felel, hogy leellenőrizze, a játék véget ért-e.
# Amennyiben igen, akkor áljon le a játék
def game_over():
    return NotImplementedError


# Fő ciklus
while True:

    # Fejezd be a for-ciklust, ami kezeli a leütött billentyűket
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
    
    # Kezeld le azokat az eseteket, amikor a kígyónak magába kéne harapnia
    # pl: ha jobbra megy és megnyomod a ball gombot vagy az "a"-t

    # Hozd létre a kígyó mozgásáért felelős mechanizmust. 
    # Frissítsd a kígyó pozícióját a megfelelő irányba

    # Kezeld le, hogy amennyiben a kígyó feje és a gyümölcs átfedik egymást 
    # akkor a kígyó testéhez adj hozzá egy újabb elemet

    # Amikor a kígyó megette a gyümölcsöt, akkor generálj egy új gyümölcsöt
    
    # Rajzold ki az összes elemet: kígyó feje kígyó teste és a gyümölcs

    # A játék végét itt kezeld le
    
    # Frissítsd a képernyőt
    pygame.display.update()

    # Hívd meg a játékórát a játék sebességének szabályozására létrehozott változóval
