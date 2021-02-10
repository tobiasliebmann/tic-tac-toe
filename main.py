import sys
import pygame


def position_test(input_pos, test_dimension):
    """

    :param input_pos:
    :param test_dimension:
    :return:
    """
    if 0 <= input_pos <= test_dimension/3:
        return 0
    elif test_dimension/3 < input_pos <= 2*test_dimension/3:
        return test_dimension/3
    else:
        return 2*test_dimension/3


pygame.init()

im_width = 300
im_height = 300

size = width, height = 900, 900
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

nic_cage = pygame.image.load('head.png')
nic_cage_rect = pygame.Rect(100, 100, im_width, im_height)
cheems = pygame.image.load('cheems.png')
cheems_rect = pygame.Rect(100, 100, im_width, im_height)

mouse_flag = False

while 1:
    pos = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_flag = True
            pos = pygame.mouse.get_pos()
            nic_cage_rect = pygame.Rect(position_test(pos[0], width), position_test(pos[1], height), 256, 256)
    screen.fill(black)
    pygame.draw.line(screen, (255, 0, 0), (0, height/3), (width, height/3))
    pygame.draw.line(screen, (255, 0, 0), (0, 2*height/3), (width, 2*height/3))
    pygame.draw.line(screen, (255, 0, 0), (width/3, 0), (width/3, height))
    pygame.draw.line(screen, (255, 0, 0), (2*width/3, 0), (2*width/3, height))
#    font = pygame.font.SysFont(None, 24)
#    img = font.render('Click somewhere on the screen. DO IT!!11!', True, (100, 100, 100))
#    screen.blit(img, (20, 20))
    if mouse_flag:
        screen.blit(nic_cage, nic_cage_rect)
    pygame.display.flip()
