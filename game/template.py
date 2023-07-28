import pygame, sys, random
from pygame import math



cell_size = 20
cell_number = 20
FPS = 30
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('SNAKE')

class Main:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()


    def update(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.check_collisions()
        self.check_fail()
        self.draw_score()
        self.check_edges()


    def check_collisions(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.grow()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.reset()

    def reset(self):
        self.snake.__init__()
        self.snake.direction = math.Vector2(0, 0)

    def check_edges(self):
            for i in range(len(self.snake.body)):
                body_copy = self.snake.body
                current_pos = math.Vector2(0, self.snake.body[0].y)
                if body_copy[i].x >= cell_number and self.snake.direction.x == 1:
                    current_pos = math.Vector2(0, self.snake.body[0].y)
                    self.snake.body[i] = current_pos
                    current_pos -= math.Vector2(1, 0)
                elif body_copy[i].x < 0 and self.snake.direction.x == -1:
                    current_pos = math.Vector2(cell_number, self.snake.body[0].y)
                    self.snake.body[i] = current_pos
                    current_pos += math.Vector2(1, 0)
                elif body_copy[i].y >= cell_number and self.snake.direction.y == 1:
                    current_pos = math.Vector2(self.snake.body[0].x, 0)
                    self.snake.body[i] = current_pos
                    current_pos -= math.Vector2(0, 1)
                elif body_copy[i].y < 0 and self.snake.direction.y == -1:
                    current_pos = math.Vector2(self.snake.body[0].x, cell_number)
                    self.snake.body[i] = current_pos
                    current_pos -= math.Vector2(0, 1)



    def draw_score(self):
        game_font = pygame.font.Font('MinecraftRegular-Bmg3.ttf', 18)
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (54, 76, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)





class Fruit:
    def __init__(self):
        self.randomize()
        apple = pygame.image.load('assets/Apple.png')
        self.apple = pygame.transform.scale(apple,(cell_size, cell_size))
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * cell_number, self.y * cell_number, cell_size, cell_size)
        screen.blit(self.apple, fruit_rect)
        # pygame.draw.rect(screen, (255, 0, 0), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number -1)
        self.y = random.randint(0, cell_number -1)
        self.pos = math.Vector2(self.x, self.y)
        return self.pos




class Snake:
    def __init__(self):
        #стартовая позиция
        self.body = [math.Vector2(5, 10), math.Vector2(4, 10), math.Vector2(3, 10)]
        self.direction = math.Vector2(1, 0)
        self.new_block = False


        head_right = pygame.image.load('assets/head_right.png')
        self.head_right = pygame.transform.scale(head_right, (cell_size, cell_size))
        self.head_down = pygame.transform.rotate(self.head_right, 90)
        self.head_left = pygame.transform.rotate(self.head_down, 90)
        self.head_up = pygame.transform.rotate(self.head_left, 90)

        body = pygame.image.load('assets/body.png')
        self.body_horizontal = pygame.transform.scale(body, (cell_size, cell_size))
        self.body_vertical = pygame.transform.rotate(self.body_horizontal, 90)

        tail = pygame.image.load('assets/tail.png')
        self.tail_r = pygame.transform.scale(tail, (cell_size, cell_size))
        self.tail_d = pygame.transform.rotate(self.tail_r, 90)
        self.tail_l = pygame.transform.rotate(self.tail_d, 90)
        self.tail_up = pygame.transform.rotate(self.tail_l, 90)

        turn = pygame.image.load('assets/turn_rb.png')
        self.turn_br = pygame.transform.scale(turn, (cell_size, cell_size))
        self.turn_bl = pygame.transform.rotate(self.turn_br, 90)
        self.turn_tl = pygame.transform.rotate(self.turn_bl, 90)
        self.turn_tr = pygame.transform.rotate(self.turn_tl, 90)




    def draw_snake(self):
        self.update_head()
        self.update_tail()
        for index, block in enumerate (self.body):
            rect = pygame.Rect(block.x * cell_number, block.y * cell_number, cell_size, cell_size)
            if index == 0 :
                screen.blit(self.head, rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail, rect)
            else:
                prev_block = self.body[index + 1]-block
                next_block = self.body[index - 1]-block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical, rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal, rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.turn_br, rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.turn_bl, rect)
                    elif prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.turn_tr, rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.turn_tl, rect)

            # pygame.draw.rect(screen, (0, 255, 0), rect)


    def movie(self):
        if self.new_block == True:
            copy_body = self.body[:]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body
            self.new_block = False
        else:
            copy_body = self.body[:-1]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body

    def update_head(self):
        head_dir = self.body[1] - self.body[0]
        if head_dir.x == 1:
            self.head = self.head_left
        elif head_dir.x == -1:
            self.head = self.head_right
        elif head_dir.y == 1:
            self.head = self.head_down
        elif head_dir.y == -1:
            self.head = self.head_up


    def update_tail(self):
        tail_dir = self.body[-2] - self.body[-1]
        if tail_dir == math.Vector2(1, 0):
            self.tail = self.tail_r
        elif tail_dir ==math.Vector2(-1, 0):
            self.tail = self.tail_l
        elif tail_dir == math.Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_dir == math.Vector2(0, -1):
            self.tail = self.tail_d



    def grow(self):
        self.new_block = True









SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
main = Main()
running = True

while running:

    for event in pygame.event.get():
        clock.tick(FPS)
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == SCREEN_UPDATE:
           main.snake.movie()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                  main.snake.direction = math.Vector2(0, -1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                 main.snake.direction = math.Vector2(0, 1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = math.Vector2(1, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = math.Vector2(-1, 0)




#Обновлениe
    screen.fill((100, 200, 122))
    main.update()
    # screen.update()


#Рендеринг




#Переворачиваем экран
    pygame.display.flip()

