from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random
color = "white"
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)
        

    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position, self.radius,LINE_WIDTH)
    
    def update(self, dt):
        to_add = self.velocity * dt
        self.position += to_add

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rdm = random.uniform(20,50)
            ast1 = self.velocity.rotate(rdm)
            rdm *= -1
            ast2 = self.velocity.rotate(rdm)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            aster1 = Asteroid(self.position.x, self.position.y, new_rad)
            aster2 = Asteroid(self.position.x, self.position.y, new_rad)
            aster1.velocity = ast1 * 1.2
            aster2.velocity = ast2 * 1.2
