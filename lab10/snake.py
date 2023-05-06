# импорт библиотек
import pygame
import time
import random

import psycopg2cffi as psycopg2
from config import config

snake_speed = 15

# размер окна
window_x = 720
window_y = 480

# определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# инициализация
pygame.init()

# Инициализирование игрового окно
pygame.display.set_caption("Змейка")
game_window = pygame.display.set_mode((window_x, window_y))

# Контроллер FPS (кадры в секунду)
fps = pygame.time.Clock()

# определение положения змеи по умолчанию
snake_position = [100, 50]

# определение первых 4 блоков тела змеи
snakebody = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
fruit_position = [
    random.randrange(1, (window_x // 10)) * 10,
    random.randrange(1, (window_y // 10)) * 10,
]

fruit_spawn = True

# установка направления змеи по умолчанию к
# право
direction = "RIGHT"
change_to = direction

# начальная оценка
score = 0

level = 1

params = config()
conn = psycopg2.connect(**params)  # подключение
cur = conn.cursor()  # доступ к базе данных

# создать таблицу game с сохранёнными данными для игры Змейки
cur.execute(
    """CREATE TABLE IF NOT EXISTS game (
                name VARCHAR(255) NOT NULL,
                score INTEGER NOT NULL,
                level INTEGER NOT NULL);"""
)

name = input("Введите имя пользователя: ")
# Найти всех пользователей в базе данных с таким именем
cur.execute(
    f"""
            SELECT * FROM game
            WHERE name='{name}';
            """
)
# Получить результат
matching_name = cur.fetchone()

if matching_name is None:
    # Игрока нет в базе данных, регистрируем
    print("Вас нет в базе данных, регистрируем...")
    cur.execute(
        f"""
                INSERT INTO game(name, score, level)
                VALUES ('{name}', {score}, {level});
                """
    )
    print("Вы зарегистрированы!")
else:
    # Игрок есть в базе данных, читаем сохранённые данные
    score = matching_name[1]
    level = matching_name[2]
    print("Вход прошёл успешно!")


def save_game():
    print(f"Сохраняем ваши данные: ваш уровень = {level}, счёт = {score}")
    command = f"""
        UPDATE game
        SET score={score}, level={level}
        WHERE name='{name}';
        """
    cur.execute(command)
    conn.commit()
    print("Данные сохранены!")


# отображение функции Score
def show_score(choice, color, font, size):
    # создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)

    # создать объект поверхности отображения
    # score_surface
    score_surface = score_font.render(f"Score: {score}, level: {level}", True, color)

    # создаем прямоугольный объект для текста
    # поверхностный объект
    score_rect = score_surface.get_rect()

    # отображение текста
    game_window.blit(score_surface, score_rect)


# функция завершения игры
def game_over():
    # создание объекта шрифта my_font
    my_font = pygame.font.SysFont("times new roman", 50)

    # создание текстовой поверхности, на которой текст
    # будет нарисовано
    game_over_surface = my_font.render(f"Ваш счёт: {score}", True, red)

    # создать прямоугольный объект для текста
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # установка положения текста
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit нарисует текст на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # через 2 секунды мы выйдем из программы
    time.sleep(2)

    # деактивация библиотеки pygame
    pygame.quit()

    # Записать сохранение в базу данных
    save_game()

    conn.commit()  # Сохранить записанное в базу данных
    cur.close()  # Закрыть доступ
    # Если conn (подключение) ещё существует
    if conn is not None:
        conn.close()  # Закрыть подключение
        print("Подключение к базе данных закрыто.")

    # quit the program
    quit()


# Main Function
while True:
    level = score // 5

    # обработка ключевых событий
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Если две клавиши нажаты одновременно
    # мы не хотим, чтобы змея разделялась на две
    # направлений одновременно
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Перемещение змеи
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    # Механизм роста тела змеи
    # если фрукты и змеи сталкиваются, то очки
    # будет увеличено на 10
    snakebody.insert(0, list(snake_position))
    if (
        snake_position[0] == fruit_position[0]
        and snake_position[1] == fruit_position[1]
    ):
        score += 10
        fruit_spawn = False
    else:
        snakebody.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10,
        ]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snakebody:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(
        game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)
    )

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Touching the snake body
    for block in snakebody[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score countinuously
    show_score(1, white, "times new roman", 20)

    snake_speed = level + 15

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
