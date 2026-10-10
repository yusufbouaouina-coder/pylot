import sys
import os
import pygame
import pygame._sdl2

path = os.path.dirname(os.path.abspath(__file__))
pygame.init()

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    return rotated_image, new_rect

original_plane = pygame.image.load(os.path.join(path, 'base_assets', 'plane.png'))
planex, planey = original_plane.get_size()
plane_rect = pygame.Rect(50, 50, planex, planey)
angle = 0

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
window = pygame._sdl2.Window.from_display_module()
window.maximize()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        plane_rect.x -= 5
    if key[pygame.K_d]:
        plane_rect.x += 5
    if key[pygame.K_w]:
        plane_rect.y -= 5
    if key[pygame.K_s]:
        plane_rect.y += 5
    if key[pygame.K_q]:
        angle += 1
    if key[pygame.K_e]:
        angle -= 1

    plane_rect.clamp_ip(screen.get_rect())

    rotated_plane, rotated_rect = rot_center(original_plane, angle, plane_rect.centerx, plane_rect.centery)

    width, height = screen.get_size()
    ground_rect = pygame.Rect(0, height - height // 4, width, height // 4)

    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (0, 160, 0), ground_rect)
    screen.blit(rotated_plane, rotated_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()