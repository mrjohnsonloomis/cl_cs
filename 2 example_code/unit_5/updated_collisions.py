import pygame, sys, random

#global variables
screen_width = 1000
screen_height = 800

'''---------------------------------SPRITES/CLASSES---------------------'''
class Minkie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/minkie.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (20, screen_height - 20)
        self.speed = 5
        self.y_velocity = 0  
        self.on_ground = True

    # Added this so that our guy can move
    def update(self):
        """Called once per frame. Handles player movement based on key presses."""
        # Get a dictionary of all currently pressed keys
        keys = pygame.key.get_pressed()
        
        # Move left/right
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        # Handle jumping
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.y_velocity = -15  # Negative velocity means upward movement
            self.on_ground = False
        
        # Apply gravity
        self.y_velocity += 0.8  # Gravity constant
        
        # Cap falling speed
        if self.y_velocity > 15:
            self.y_velocity = 15
        
        # Update vertical position based on velocity
        self.rect.y += self.y_velocity
        
        # Check for ground collision (simplified - you'll need actual collision detection)
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.y_velocity = 0
            self.on_ground = True
    
    #create and return a rock
    def shoot(self):
        #print('pew')
        #return Rock(self.rect.centerx, self.rect.centery)
        return Rock(20,20)

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/lava_rock.png') 

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.xvel = random.randint(-3,3)
        self.yvel = random.random()*6 - 3


    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if self.rect.right > screen_width:
            #self.rect.right = screen_width
            self.xvel *= -1
        elif self.rect.left < 0:
            #self.rect.left = 0
            self.xvel *= -1

        if self.rect.bottom > screen_height:
            #self.rect.bottom = screen_height
            self.yvel *= -1
        elif self.rect.top < 0:
            #self.rect.top = 0
            self.yvel *= -1

def main():
    '''---------------------------------SETUP-------------------------------'''
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Game Title')

    # Instantiate objects and groups
    rock_group = pygame.sprite.Group()
    #rock_group.add(Rock())

    sprite_group = pygame.sprite.Group()
    mink = Minkie()
    sprite_group.add(mink)
    
    # For Option 3: Create a group specifically for Minkie
    minkie_group = pygame.sprite.Group()
    minkie_group.add(mink)
    
    # Track which collision method to use (1, 2, or 3)
    collision_method = 2  # Default to Option 2

    '''----------------------------------LOOP-------------------------------'''
    while True:
        #Handling input (EVENTS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rock_group.add(mink.shoot())
                # Add keys to switch between collision methods
                elif event.key == pygame.K_1:
                    collision_method = 1
                    print("Switched to collision method 1: individual sprite collision")
                elif event.key == pygame.K_2:
                    collision_method = 2
                    print("Switched to collision method 2: sprite vs group collision")
                elif event.key == pygame.K_3:
                    collision_method = 3
                    print("Switched to collision method 3: group vs group collision")

        # Updating Sprites
        rock_group.update()
        minkie_group.update()

        #Collisions
        if collision_method == 1:
            #Option 1: Individual sprite collision with collide_rect
            for rock in rock_group:
                if pygame.sprite.collide_rect(mink, rock):
                    print('ouch - method 1')
                    rock.kill()
        elif collision_method == 2:
            #Option 2: Sprite vs Group with spritecollide
            collided_rocks = pygame.sprite.spritecollide(mink, rock_group, True)
            if collided_rocks:
                print(f'ouch - method 2 (hit {len(collided_rocks)} rocks)')
        else:
            #Option 3: Group vs Group with groupcollide
            collisions = pygame.sprite.groupcollide(minkie_group, rock_group, False, True)
            if collisions:
                rocks_hit = collisions.get(mink, [])
                if rocks_hit:
                    print(f'ouch - method 3 (hit {len(rocks_hit)} rocks)')

        # Drawing
        screen.fill('black') #replace with image or whatever you use up top
        sprite_group.draw(screen)
        rock_group.draw(screen)
        minkie_group.draw(screen)
        
        # Display current collision method
        font = pygame.font.Font(None, 36)
        method_text = font.render(f"Collision Method: {collision_method} (Press 1, 2, or 3 to change)", True, (255, 255, 255))
        screen.blit(method_text, (10, 10))
        
        rock_count = font.render(f"Rocks: {len(rock_group)} (Press SPACE to add)", True, (255, 255, 255))
        screen.blit(rock_count, (10, 50))

        # Updating the window
        pygame.display.flip()
        clock.tick(60)

main()
