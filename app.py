import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

# Configuración de la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pelotas rebotando")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Inicializar Pymunk
space = pymunk.Space()
space.gravity = 0, 900  # Fuerza gravitatoria

# Función para crear una pelota
def create_ball(position):
    body = pymunk.Body(1, 100)  # Masa e inercia
    body.position = (position[0], 12)
    shape = pymunk.Circle(body, 20)  # Radio de la pelota
    shape.elasticity = 0.8  # Elasticidad
    space.add(body, shape)
    return shape

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

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
            ball_shape = create_ball(event.pos)
            balls.append(ball_shape)

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
                contacts = ball.shapes_collide(other_ball)
                if contacts.points:
                    normal = contacts.normal
                    distance = contacts.points[0].distance - 10  # Distancia de separación - 20
                    if distance > 0:
                        impulse = normal * distance * 0.5
                        ball.body.apply_impulse_at_world_point(impulse, contacts.points[0])
                        other_ball.body.apply_impulse_at_world_point(-impulse, contacts.points[0])

    # Dibujar las pelotas
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)  # Invertir la posición Y para Pygame
        pygame.draw.circle(screen, blue, (pos_x, pos_y), 20)

    # Actualizar el espacio de Pymunk
    space.step(1 / 60.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
