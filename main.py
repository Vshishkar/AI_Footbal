import sys, pygame
from pygame.color import Color
pygame.init()
import colors

SIZE = WIDTH, HEIGHT = 1280, 720
W_MIDDLE = WIDTH / 2
H_MIDDLE = HEIGHT / 2

class Game:
    def __init__(self):
        self.FPS = pygame.time.Clock()
        self.FPS.tick(60)
        self.screen = pygame.display.set_mode(SIZE)
        self.background = colors.Colors.GREEN
        self.score = [0, 0]

    def on_render(self):
        self.screen.fill(self.background.value)
        pygame.draw.circle(self.screen, colors.Colors.WHITE.value, (W_MIDDLE, H_MIDDLE), HEIGHT * 0.2, 10)
        pygame.draw.line(self.screen, colors.Colors.WHITE.value, (W_MIDDLE, 0), (W_MIDDLE , HEIGHT), 10)
        pygame.draw.polygon(
            self.screen,
            colors.Colors.WHITE.value,
            [
                (0, HEIGHT * 0.2),
                (WIDTH * 0.15, HEIGHT * 0.2),
                (WIDTH * 0.15, HEIGHT * 0.8),
                (0, HEIGHT * 0.8)], 
                10)
        
        pygame.draw.polygon(
            self.screen,
            colors.Colors.WHITE.value,
            [
                (WIDTH, HEIGHT * 0.2),
                (WIDTH * 0.85, HEIGHT * 0.2),
                (WIDTH * 0.85, HEIGHT * 0.8),
                (WIDTH, HEIGHT * 0.8)], 
                10)

    def start(self):
        font = GameFont()
        b = Ball()
        lg = Goal(True)
        rg = Goal(False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            b.move()

            text = font.render_score(self.score)

            self.on_render()
            b.draw(self.screen)
            lg.draw(self.screen)
            rg.draw(self.screen)
            self.screen.blit(text, (20, 0))
            pygame.display.flip()


    def draw_score(self):
        print

class Goal(pygame.sprite.Sprite):
    def __init__(self, isLeft):
        super().__init__()
        if isLeft:
            self.reg_line = [(1, HEIGHT * 0.4), (1, HEIGHT * 0.6)]
        else:
            self.reg_line = [(WIDTH - 1, HEIGHT * 0.4), (WIDTH - 1, HEIGHT * 0.6)]

    def draw(self, screen):
        pygame.draw.line(screen, colors.Colors.WHITE.value, self.reg_line[0], self.reg_line[1], 20)

    def isScored(self, ball: Ball):
        return self.rect.contains

        

class GameFont:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render_score(self, score):
        return self.font.render("{0}-{1}".format(score[0], score[1]), False, colors.Colors.BLACK.value)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 16
        self.x, self.y = self.radius, self.radius
        self.speed = [0.5, 0.5]
        self.image = pygame.image.load("assets/ball.png")
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect()
        
    
    @property
    def pos(self):
        return self.x, self.y

    @property
    def int_pos(self):
        return map(int, self.pos)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.centerx, self.rect.centery = self.int_pos
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    # execute only if run as a script
    main()