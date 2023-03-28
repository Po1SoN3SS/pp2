import pygame
import random

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption("GFG Paint")

is_drawing = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

selected_shape = "circle"
color = (0, 0, 0)


def rounded_line(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)


def shape(pos):
    if selected_shape == "rectangle":
        pygame.draw.rect(screen, color, pygame.Rect(pos[0] - 30, pos[1] - 30, 60, 60))
    elif selected_shape == "circle":
        pygame.draw.circle(screen, color, pos, radius)


try:
    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:  # Left mouse button
                shape(e.pos)
                is_drawing = True

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                selected_shape = "rectangle"
            elif e.key == pygame.K_c:
                selected_shape = "circle"
            elif (
                e.key == pygame.K_0
                or e.key == pygame.K_1
                or e.key == pygame.K_2
                or e.key == pygame.K_3
                or e.key == pygame.K_4
                or e.key == pygame.K_5
                or e.key == pygame.K_6
                or e.key == pygame.K_g
            ):
                number = e.key - pygame.K_0
                color = (number * 25, number * 25, number * 25)

        if e.type == pygame.MOUSEBUTTONUP:
            is_drawing = False

        if e.type == pygame.MOUSEMOTION:
            if is_drawing:
                shape(e.pos)
                rounded_line(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        pygame.display.flip()

except StopIteration:
    pass

# Quit
pygame.quit()
