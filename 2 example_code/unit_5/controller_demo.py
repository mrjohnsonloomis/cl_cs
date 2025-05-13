import pygame, sys, random, controller_support

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
        
        # Initialize controller
        self.controller = controller_support.Controller()  # Get first available controller
    
    def update(self):
        """Called once per frame. Handles player movement based on key presses and controller input."""
        # Get a dictionary of all currently pressed keys
        keys = pygame.key.get_pressed()
        
        # Move left/right with keyboard
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        # Handle jumping with keyboard
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.y_velocity = -15  # Negative velocity means upward movement
            self.on_ground = False
        
        # Controller input for movement (only if connected)
        if self.controller.is_connected():
            # Move left/right with controller
            if self.controller.is_left_pressed():
                self.rect.x -= self.speed
            if self.controller.is_right_pressed():
                self.rect.x += self.speed
            
            # Handle jumping with controller
            if (self.controller.is_jump_pressed() or self.controller.is_button_pressed(self.controller.A)) and self.on_ground:
                self.y_velocity = -15
                self.on_ground = False
            
            # Alternative: use analog stick for smoother movement
            left_stick = self.controller.get_left_stick()
            if abs(left_stick[0]) > 0:  # If there's significant horizontal movement
                self.rect.x += int(left_stick[0] * self.speed)
        
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
    
    def shoot(self):
        # Now can be triggered by keyboard or controller button
        # Check for controller button press (if connected)
        # Using B button (index 1) for shooting
        if self.controller.is_connected() and self.controller.is_button_pressed(self.controller.B):
            return Rock(20, 20)
        
        # Original implementation
        return Rock(20, 20)

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
    controller_support.init()

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
        events = pygame.event.get()
        for event in events:
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

        #controller events
        controller_events = controller_support.process_events(events)
        # Handle controller events in an event-driven way
        for controller_event in controller_events:
        # Check for button press events (when button is first pressed down)
            if controller_event['type'] == 'button_down':
                # Check if it's the B button (index 1)
                if controller_event['button'] == 1:  # B button
                    rock_group.add(mink.shoot())
      
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