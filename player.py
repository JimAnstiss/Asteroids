import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):



    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        # Create cooldown and zero
        self.shot_cooldown: float = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        # Override parent draw method to render a polygon/triangle
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # CCW
        if keys[pygame.K_d]:
            self.rotate(dt)  # CW
        if keys[pygame.K_w]:
            self.move(dt)    # forwards
        if keys[pygame.K_s]:
            self.move(-dt)   # backwards
        if keys[pygame.K_SPACE]:    #FIRE!
            self.shoot()

    # Decrease the shot cooldown
        self.shot_cooldown -= dt

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:

    # If the current value of the timer is greater than 0, prevent shooting
        if self.shot_cooldown > 0:
            return
    # Otherwise, set the timer equal to PLAYER_SHOOT_COOLDOWN_SECONDS then use existing firing code.
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        bullet = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        bullet.velocity = direction * PLAYER_SHOOT_SPEED
