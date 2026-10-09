import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
# Initialize bullet using the shared global bullet radius
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen: pygame.Surface) -> None:
        # Render the bullet onto the screen surface - This looks same as Asteroid
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Advance the bullet position along its assigned velocity heading - Again same as Asteroid?
        self.position += self.velocity * dt
