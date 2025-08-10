'''
Program written by Meyan Adhikari

A program to visualize the 'colliding boxes computing pi' problem by 3Blue1Brown.
'''

import pygame
import math
import numpy as np

# initializing pygame
pygame.init()
pygame.font.init()
pygame.display.init()
pygame.mixer.init()

# setting up the screen
font = pygame.font.SysFont('Arial', 24)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colliding Boxes Computing Pi")

def display_text(screen, collision_count, font, is_paused=False):
    """
    Displays collision count and instructions on the screen.
    
    Args:
        screen: Pygame display surface
        collision_count: Current number of collisions
        font: Pygame font object for rendering text
        is_paused: Boolean indicating if simulation is paused
    """
    # Display collision count
    collision_text = font.render(f"COLLISIONS: {collision_count}", True, (255, 255, 255))
    screen.blit(collision_text, (20, 20))
    
    # Display pause status and instructions
    status = "PAUSED" if is_paused else "RUNNING"
    instruction_text = font.render(f"Status: {status} | Press SPACE to Play/Pause", True, (255, 255, 255))
    screen.blit(instruction_text, (20, 60))

def setup_collision_sound():
    """Sets up a 100Hz collision sound and returns a function to play it"""
    import numpy as np
    
    # Generate a 100Hz sine wave sound
    sample_rate = 44100  # standard audio sample rate
    duration = 0.05  # 50ms - very short "tick" sound
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Create a more percussive tick with exponential decay
    envelope = np.exp(-t * 50)  # Exponential decay
    tone = np.sin(2 * np.pi * 150 * t) * envelope
    
    # Convert to 16-bit PCM and make stereo (2D array)
    tone = np.int16(tone * 32767)
    stereo_tone = np.column_stack((tone, tone))  # Create stereo by duplicating mono channel
    
    # Create the sound object
    tick_sound = pygame.sndarray.make_sound(stereo_tone)
    tick_sound.set_volume(0.3)  # Lower volume to prevent it from being too loud
    
    def play_collision_sound():
        """Play the collision sound"""
        tick_sound.play()
    
    return play_collision_sound

play_collision_sound = setup_collision_sound()


# Big box class
class BigBox():
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.width = min(mass * 0.1 + 50,200)
        self.height = min(mass * 0.1 + 50,200)
        self.mass = mass
        self.speed = -0.1 # pixels per second
        self.color = (255, 0, 0)  # red
    
    def update(self):
        self.x += self.speed
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Small box class
class SmallBox():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.mass = 1  # added mass here
        self.speed = 0
        self.color = (0, 255, 0)  # green
    
    def update(self):
        self.x += self.speed 
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

running = True

# creating objects
big_box = BigBox(800, 300,10000)  # use higher mass for more digits of pi
small_box = SmallBox(300, 300 + (big_box.height - 50))
boxes = [big_box, small_box]

paused = False

collisionCounter = 0

# main loop
while running:
    screen.fill((0, 0, 0))  # clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                


    # draw ground and wall
    pygame.draw.line(screen, (255, 255, 255), (0, 300 + big_box.height), (800, 300 + big_box.height), 1)
    pygame.draw.line(screen, (255, 255, 255), (10, 0), (10, 600), 1)

    # wall collision
    if small_box.x <= 10:
        print("HI")
        small_box.x = 10
        small_box.speed *=  -1
        collisionCounter += 1
        print("Collision Count:", collisionCounter)
        play_collision_sound()
    
        

    # box collision
    if big_box.x <= small_box.x + small_box.width :
        # check if they are moving toward each other
        if big_box.speed < small_box.speed:
            m1 = big_box.mass
            m2 = small_box.mass
            u1 = big_box.speed
            u2 = small_box.speed

            # elastic collision formula
            v1 = (u1 * (m1 - m2) + 2 * m2 * u2) / (m1 + m2)
            v2 = (u2 * (m2 - m1) + 2 * m1 * u1) / (m1 + m2)

            big_box.speed = v1
            small_box.speed = v2

            collisionCounter += 1
            print("Collision Count:", collisionCounter)
            play_collision_sound()

    # update and draw boxes
    if not paused:
        big_box.update()
        small_box.update()
    
        display_text(screen,collisionCounter,font,paused)

        pygame.display.update()
