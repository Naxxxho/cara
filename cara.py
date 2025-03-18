import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gato con Botas en la Lluvia")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
blue = (30, 144, 255)  # Color de la lluvia
brown = (139, 69, 19)  # Color del gato
yellow = (255, 255, 0)  # Color de los ojos
gray = (192, 192, 192)  # Color de la espada
red = (255, 0, 0)  # Color del sombrero (ajustado para mayor visibilidad)

# Configuración de la lluvia
num_drops = 200  # Número de gotas de lluvia
rain_drops = []  # Lista para almacenar las posiciones de las gotas

# Inicializar las gotas de lluvia
for _ in range(num_drops):
    x = random.randint(0, width)
    y = random.randint(-height, 0)
    speed = random.randint(5, 15)
    rain_drops.append([x, y, speed])

# Variables para el pestañeo del gato
blink = False  # Estado de los ojos (abiertos o cerrados)
last_blink_time = time.time()  # Tiempo del último pestañeo


# Función para dibujar la lluvia
def draw_rain(surface, drops):
    for drop in drops:
        pygame.draw.line(surface, blue, (drop[0], drop[1]), (drop[0], drop[1] + 10), 2)


# Función para dibujar al gato con botas
def draw_puss_in_boots(surface, eyes_open):
    # Cuerpo
    pygame.draw.ellipse(surface, brown, (350, 300, 100, 200))

    # Cabeza
    pygame.draw.circle(surface, brown, (400, 250), 50)

    # Ojos
    if eyes_open:
        pygame.draw.circle(surface, yellow, (380, 240), 10)
        pygame.draw.circle(surface, yellow, (420, 240), 10)
        pygame.draw.circle(surface, black, (380, 240), 5)
        pygame.draw.circle(surface, black, (420, 240), 5)
    else:
        pygame.draw.line(surface, black, (370, 240), (390, 240), 3)  # Ojo izquierdo cerrado
        pygame.draw.line(surface, black, (410, 240), (430, 240), 3)  # Ojo derecho cerrado

    # Nariz
    pygame.draw.polygon(surface, black, [(395, 260), (405, 260), (400, 270)])

    # Bigotes
    pygame.draw.line(surface, black, (390, 265), (340, 260), 2)
    pygame.draw.line(surface, black, (390, 275), (340, 275), 2)
    pygame.draw.line(surface, black, (410, 265), (460, 260), 2)
    pygame.draw.line(surface, black, (410, 275), (460, 275), 2)

    # Orejas
    pygame.draw.polygon(surface, brown, [(360, 210), (380, 170), (400, 210)])
    pygame.draw.polygon(surface, brown, [(440, 210), (420, 170), (400, 210)])

    # Sombrero (ajustado para mayor visibilidad)
    pygame.draw.rect(surface, red, (370, 150, 60, 40))  # Parte superior del sombrero
    pygame.draw.polygon(surface, red, [(350, 190), (450, 190), (400, 230)])  # Ala del sombrero

    # Botas
    pygame.draw.ellipse(surface, black, (330, 450, 60, 40))  # Bota izquierda
    pygame.draw.ellipse(surface, black, (410, 450, 60, 40))  # Bota derecha

    # Cola
    pygame.draw.polygon(surface, brown, [(450, 400), (500, 350), (520, 400), (500, 450)])

    # Espada (ajustada para mayor visibilidad)
    pygame.draw.rect(surface, gray, (320, 280, 10, 100))  # Hoja de la espada
    pygame.draw.polygon(surface, gray, [(320, 280), (330, 280), (325, 260)])  # Punta de la espada
    pygame.draw.rect(surface, black, (315, 370, 20, 20))  # Empuñadura de la espada


# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control del pestañeo
    current_time = time.time()
    if current_time - last_blink_time > 5:  # Pestañea cada 5 segundos
        blink = not blink  # Alternar entre abrir y cerrar los ojos
        last_blink_time = current_time

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar la lluvia
    for drop in rain_drops:
        drop[1] += drop[2]  # Mover la gota hacia abajo
        if drop[1] > height:  # Si la gota sale de la pantalla, reiniciar su posición
            drop[1] = random.randint(-50, 0)
            drop[0] = random.randint(0, width)
    draw_rain(screen, rain_drops)

    # Dibujar al gato con botas
    draw_puss_in_boots(screen, not blink)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    clock.tick(30)

# Salir de Pygame
pygame.quit()
