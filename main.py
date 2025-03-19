import math
import pygame
import constants
import particles
from particles import Particle 
import time
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGTH))

## Time
clock = pygame.time.Clock()
global prev
prev:float = time.time()
global dt
dt:float = 0
### ----------------------
running = True

def Physics(parts:list[Particle]) -> None:
    k = constants.COULOMBS_CONSTANT
    partsNum:int = len(parts)

    for i in range(0, partsNum):
        particle_i:Particle = parts[i]
        charge_i:float = particle_i.charge
        
        deltaPos:list[float] = [0, 0]
        deltaVel:list[float] = [0, 0]
        
        for j in range(partsNum):
            if i != j:
                particle_j:Particle = parts[j]
                charge_j:float = particle_j.charge

                distance:float = math.sqrt(math.pow(particle_i.position[0] - particle_j.position[0], 2) + math.pow(particle_i.position[1] - particle_j.position[1], 2))
                if distance > 10:
                    deltaVel[0] = (k * charge_i * charge_j * (particle_i.position[0] - particle_j.position[0]) * (dt))/(particle_i.mass*(math.pow(distance,3)))
                    deltaVel[1] = (k * charge_i * charge_j * (particle_i.position[1] - particle_j.position[1]) * (dt))/(particle_i.mass*(math.pow(distance,3)))
        
        particle_i.velocity[0] += deltaVel[0]
        particle_i.velocity[1] += deltaVel[1]
        

        # Bounce off walls
        if particle_i.position[0] <= 0 or particle_i.position[0] >= constants.SCREEN_WIDTH:
            particle_i.velocity[0] *= -1
        if particle_i.position[1] <= 0 or particle_i.position[1] >= constants.SCREEN_HEIGTH:
            particle_i.velocity[1] *= -1
            
        deltaPos[0] += particle_i.velocity[0] * dt 
        deltaPos[1] += particle_i.velocity[1] * dt 

        particle_i.position = (particle_i.position[0] + (deltaPos[0] * constants.SPACE_DRAG), particle_i.position[1] + (deltaPos[1] * constants.SPACE_DRAG))
        pygame.draw.circle(screen, particle_i.color, particle_i.position, particle_i.radius)
             

def updateDeltaTime() -> None:
    global dt, prev
    now = time.time()
    dt = now - prev
    prev = now



## ---------------------------- RUNNING APP ------------------------------------------ ##
while running:
    clock.tick(constants.FRAMERATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.key == pygame.K_1:
                Particle(mouse_x, mouse_y, constants.ELECTRON_CHARGE, 0)
            elif event.key == pygame.K_2:
                Particle(mouse_x, mouse_y, constants.PROTON_CHARGE, 1)
            elif event.key == pygame.K_3:
                Particle(mouse_x, mouse_y, constants.NEUTRON_CHARGE, 2)
            elif event.key == pygame.K_4:
                Particle(mouse_x, mouse_y, constants.EXTRA_CHARGE, 3)


    screen.fill(constants.BACKGROUND_COLOR)
    
    updateDeltaTime()    
    Physics(particles.getAlive())
    pygame.display.flip()

    