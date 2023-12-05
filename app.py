import pygame
import pymunk
import pymunk.pygame_util
from Data.BallData import * 
import random

pygame.init()

# Configuración de la pantalla
screenWidth, screenHeight = 1000, 800
width, height = 400, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pelotas rebotando")


# Inicializar Pymunk
space = pymunk.Space()
space.gravity = 0, 900  # Fuerza gravitatoria


# Función para crear los límites de la ventana
def create_static_lines():
    static_lines = [
        pymunk.Segment(space.static_body, (((screenWidth / 2) - (width / 2)), 0), (((screenWidth / 2) - (width / 2)) + width, 0), 5),
        pymunk.Segment(space.static_body, (((screenWidth / 2) - (width / 2)), height), (((screenWidth / 2) - (width / 2)) + width, height), 5),
        pymunk.Segment(space.static_body, (((screenWidth / 2) - (width / 2)), 0), (((screenWidth / 2) - (width / 2)), height), 5),
        pymunk.Segment(space.static_body, (((screenWidth / 2) - (width / 2)) + width, 0), (((screenWidth / 2) - (width / 2)) + width, height), 5)
    ]
    for line in static_lines:
        line.elasticity = 1.0
        line.friction = 1.0
        space.add(line)  # Agregar cada segmento individualmente al espacio
    return static_lines

balls = []  # Lista para almacenar las pelotas
static_lines = create_static_lines()  # Crear los límites estáticos
last_mouse_pos = None
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
            if event.pos[0] > ((screenWidth / 2) - (width / 2)) and event.pos[0] < ((screenWidth / 2) - (width / 2)) + width:   
                numero_aleatorio = random.randint(0, 4)
                ball_shape = BallData(event.pos, space, ((numero_aleatorio + 1) * 10))
                balls.append(ball_shape)
                pygame.draw.line(screen, grey, (event.pos[0], 0), (event.pos[0], height), 2)
        elif event.type == pygame.MOUSEMOTION :
            last_mouse_pos = event.pos
            



    # Dibujar los límites de la ventana
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = pv1.x, height - pv1.y
        p2 = pv2.x, height - pv2.y
        pygame.draw.line(screen, black, (pv1.x, pv1.y), (pv2.x, pv2.y), 5)

    # Colisiones entre las pelotas
    for ball in balls:
        for other_ball in balls:
            if ball != other_ball:
                contacts = ball.shape.shapes_collide(other_ball.shape)
                if contacts.points:
                    normal = contacts.normal
                    distance = contacts.points[0].distance - 5  # Distancia de separación - 20
                    
                    if ball.ballType == other_ball.ballType:
                        
                        balls.remove(other_ball)
                        shapes = space.shapes
                        space.remove(other_ball.shape)
                        space.remove(ball.shape)
                        ball.upLevel(space)
                        shapes1 = space.shapes
                        storageBalls = balls
                    else :
                        if distance > 0:
                            impulse = normal * distance * 0.5
                            ball.shape.body.apply_impulse_at_world_point(impulse, contacts.points[0])
                            other_ball.shape.body.apply_impulse_at_world_point(-impulse, contacts.points[0])

    if last_mouse_pos is not None:
        if last_mouse_pos[0] > ((screenWidth / 2) - (width / 2)) and last_mouse_pos[0] < ((screenWidth / 2) - (width / 2)) + width:
            pygame.draw.line(screen, grey, (last_mouse_pos[0], 0), (last_mouse_pos[0], height), 2)
        
    # Dibujar las pelotas
    for ball in balls:
        pos_x = int(ball.shape.body.position.x)
        pos_y = int(ball.shape.body.position.y)  # Invertir la posición Y para Pygame
        pygame.draw.circle(screen, ball.color, (pos_x, pos_y), ball.ballType)

    # Actualizar el espacio de Pymunk
    space.step(1 / 60.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
