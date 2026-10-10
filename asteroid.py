import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # Override parent draw method to render a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Move the asteroid along its velocity vector over time
        self.position += self.velocity * dt

    def split(self) -> None:
        # Immediately kill itself
        self.kill()

        # If the radius is less than or equal to ASTEROID_MIN_RADIUS, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the split event
        log_event("asteroid_split")

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new rotated velocity vectors
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)

        # Compute the new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two new smaller asteroids at the current position
        # (Assuming your constructor looks like Asteroid(x, y, radius))
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities and scale them up by 1.2 to make them faster
        asteroid1.velocity = new_velocity_1 * 1.2
        asteroid2.velocity = new_velocity_2 * 1.2
