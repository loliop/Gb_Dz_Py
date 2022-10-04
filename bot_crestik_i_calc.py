# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# Прикрутить бота к задачам с предыдущего семинар

from ast import Break
from gettext import find
from cgitb import text
import random
from time import sleep
from tkinter import font
from turtle import color
import pygame
import sys


def checkwin(mas):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
    for sign in ['o', 'x']:
        for row in mas:
            if row.count(sign) == 3:
                return sign
        for col in range(3):
            if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
                return sign
            if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
                return sign
            if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
                return sign
    if zeroes == 0:
        return 'piece'
    return False


pygame.init()
size_block = 100
margin = 15
width = height = size_block*3 + margin*4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False


while True:

    if query % 2 == 0:  # bot

        while not game_over:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            print(row, col)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                break

        query += 1

    else:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse // (size_block + margin)
                row = y_mouse // (size_block + margin)

                if row < 0 and row > 2:
                    continue
                if col < 0 and col > 2:
                    continue

                if mas[row][col] == 0:
                    if query % 2 == 0:
                        mas[row][col] = 'x'
                    else:
                        mas[row][col] = 'o'
                    query += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False
                mas = [[0] * 3 for i in range(3)]
                query = 0
                screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col*size_block + (col+1)*margin
                y = row*size_block + (row+1)*margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5),
                                     (x + size_block-5, y + size_block-5), 3)
                    pygame.draw.line(screen, white, (x + size_block-5, y + 5),
                                     (x + 5, y + size_block-5), 3)
                elif color == green:
                    pygame.draw.circle(
                        screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2-3, 3)

    game_over = checkwin(mas)

    if game_over:
        pygame.display.update()
        sleep(1)
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()


# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования


print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = complex(input("x="))
        y = complex(input("y="))
        match s:
            case '+':
                print(f"{x} + {y} =  {x+y}")
            case '-':
                print(f"{x} - {y} =  {x-y}")
            case '*':
                print(f"{x} * {y} =  {x*y}")
            case '/':
                if y != 0:
                    print(f"{x} / {y} =  {x/y}")
                else:
                    print("Деление на ноль!")
            case _:
                print("Неверный знак операции!")

express = input("vvedite formulu :")
print(f"{express} = { eval(express)}")
