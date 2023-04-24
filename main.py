import pygame, sys, asyncio
from settings import *
from level import Level

class Game: ## formerly called Game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Stardew Valley created by FRANKENMILLER © 2023")
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

async def main():
    if __name__ == '__main__':
        game = Game() ## Game() class formerly instantiated here
        game.run()
        await asyncio.sleep(0)

asyncio.run(main())