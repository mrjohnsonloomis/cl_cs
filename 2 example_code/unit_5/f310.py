import pygame

class GameController:
    """A robust controller class that handles errors and disconnects
    Button constants for F310
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 7
    """
    def __init__(self, controller_id=0):
        """Initialize controller with error handling"""
        self.controller = None
        self.connected = False
        self.controller_id = controller_id
        
        # Make sure Pygame is initialized
        if not pygame.get_init():
            pygame.init()
        
        # Make sure joystick module is initialized
        if not pygame.joystick.get_init():
            pygame.joystick.init()
        
        # Try to connect to controller
        self._connect_controller()
    
    def _connect_controller(self):
        """Try to connect to the controller"""
        try:
            # Check if any controllers are available
            if pygame.joystick.get_count() > self.controller_id:
                self.controller = pygame.joystick.Joystick(self.controller_id)
                self.controller.init()
                self.connected = True
                print(f"Connected to controller: {self.controller.get_name()}")
            else:
                self.connected = False
                print("No controller available")
        except pygame.error as e:
            self.connected = False
            print(f"Error connecting to controller: {e}")
    
    def check_connection(self):
        """Check if controller is still connected"""
        if not self.connected:
            # Try to reconnect
            self._connect_controller()
        return self.connected
    
    def get_dpad(self):
        """Get D-pad values with error handling"""
        if not self.check_connection():
            return (0, 0)
        
        try:
            if self.controller.get_numhats() > 0:
                return self.controller.get_hat(0)
            return (0, 0)
        except pygame.error:
            self.connected = False  # Mark as disconnected
            return (0, 0)
    
    def get_left_stick(self):
        """Get left stick values with error handling"""
        if not self.check_connection():
            return (0, 0)
        
        try:
            if self.controller.get_numaxes() >= 2:
                x = self.controller.get_axis(0)
                y = self.controller.get_axis(1)
                
                # Apply dead zone
                if abs(x) < 0.2:
                    x = 0
                if abs(y) < 0.2:
                    y = 0
                
                return (x, y)
            return (0, 0)
        except pygame.error:
            self.connected = False
            return (0, 0)
    
    def get_button(self, button_id):
        """Get button state with error handling"""
        if not self.check_connection():
            return False
        
        try:
            if self.controller.get_numbuttons() > button_id:
                return self.controller.get_button(button_id)
            return False
        except pygame.error:
            self.connected = False
            return False