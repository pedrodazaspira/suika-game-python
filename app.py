import pygame
import pymunk
import pymunk.pygame_util
from Data.BallData import * 
pygame.init()

# Configuración de la pantalla
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pelotas rebotando")

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
redGreen = (0, 255, 255)
black = (0, 0, 0)
violent = (255, 255, 0)
grey = (200, 200, 200)

# Inicializar Pymunk
space = pymunk.Space()
space.gravity = 0, 900  # Fuerza gravitatoria


# Función para crear los límites de la ventana
def create_static_lines():
    static_lines = [
        pymunk.Segment(space.static_body, (0, 0), (width, 0), 5),
        pymunk.Segment(space.static_body, (0, height), (width, height), 5),
        pymunk.Segment(space.static_body, (0, 0), (0, height), 5),
        pymunk.Segment(space.static_body, (width, 0), (width, height), 5)
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
            ball_shape = BallData(event.pos, space, BalType.tipo1)
            balls.append(ball_shape)
            pygame.draw.line(screen, grey, (event.pos[0], 0), (event.pos[0], 800), 5)
        elif event.type == pygame.MOUSEMOTION :
            last_mouse_pos = event.pos
            



    # Dibujar los límites de la ventana
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = pv1.x, height - pv1.y
        p2 = pv2.x, height - pv2.y
        pygame.draw.lines(screen, (0, 0, 0), False, [p1, p2])

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
        pygame.draw.line(screen, grey, (last_mouse_pos[0], 0), (last_mouse_pos[0], 400), 5)
        
    # Dibujar las pelotas
    for ball in balls:
        pos_x = int(ball.shape.body.position.x)
        pos_y = int(ball.shape.body.position.y)  # Invertir la posición Y para Pygame
        if ball.ballType == BalType.tipo1:
            pygame.draw.circle(screen, blue, (pos_x, pos_y), 10)
        elif ball.ballType == BalType.tipo2:
            pygame.draw.circle(screen, red, (pos_x, pos_y), 20)
        elif ball.ballType == BalType.tipo3:
            pygame.draw.circle(screen, green, (pos_x, pos_y), 30)
        elif ball.ballType == BalType.tipo4:
            pygame.draw.circle(screen, redGreen, (pos_x, pos_y), 40)
        elif ball.ballType == BalType.tipo5:
            pygame.draw.circle(screen, black, (pos_x, pos_y), 50)
        elif ball.ballType == BalType.tipo6:
            pygame.draw.circle(screen, violent, (pos_x, pos_y), 60)
        elif ball.ballType == BalType.tipo7:
            pygame.draw.circle(screen, blue, (pos_x, pos_y), 60)

    # Actualizar el espacio de Pymunk
    space.step(1 / 60.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
