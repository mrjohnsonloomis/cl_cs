# controller_support.py
import pygame

# Global controller state (updated by events and accessible by OOP)
_controllers = {}
_controller_events = []

def init():
    """Initialize controller support"""
    if not pygame.get_init():
        pygame.init()
    if not pygame.joystick.get_init():
        pygame.joystick.init()
    
    # Initialize any connected controllers
    for i in range(pygame.joystick.get_count()):
        try:
            controller = pygame.joystick.Joystick(i)
            controller.init()
            _controllers[controller.get_instance_id()] = {
                'joystick': controller,
                'name': controller.get_name(),
                'buttons': [False] * controller.get_numbuttons(),
                'axes': [0.0] * controller.get_numaxes(),
                'hats': [(0, 0)] * controller.get_numhats(),
                'connected': True
            }
            print(f"Controller {i} initialized: {controller.get_name()}")
        except pygame.error as e:
            print(f"Error initializing controller {i}: {e}")

def process_events(events):
    """
    Process controller events and update the global state.
    Call this from your main game loop.
    
    Returns: List of processed controller events for event-driven approach
    """
    global _controller_events
    _controller_events = []
    
    for event in events:
        # Handle controller connection
        if event.type == pygame.JOYDEVICEADDED:
            try:
                controller = pygame.joystick.Joystick(event.device_index)
                controller.init()
                _controllers[controller.get_instance_id()] = {
                    'joystick': controller,
                    'name': controller.get_name(),
                    'buttons': [False] * controller.get_numbuttons(),
                    'axes': [0.0] * controller.get_numaxes(),
                    'hats': [(0, 0)] * controller.get_numhats(),
                    'connected': True
                }
                print(f"Controller connected: {controller.get_name()}")
                
                # Add to event list
                _controller_events.append({
                    'type': 'connected',
                    'controller_id': controller.get_instance_id(),
                    'name': controller.get_name()
                })
            except pygame.error as e:
                print(f"Error connecting controller: {e}")
        
        # Handle controller disconnection
        elif event.type == pygame.JOYDEVICEREMOVED:
            if event.instance_id in _controllers:
                controller_name = _controllers[event.instance_id]['name']
                _controllers[event.instance_id]['connected'] = False
                print(f"Controller disconnected: {controller_name}")
                
                # Add to event list
                _controller_events.append({
                    'type': 'disconnected',
                    'controller_id': event.instance_id,
                    'name': controller_name
                })
        
        # Handle button presses
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.instance_id in _controllers:
                _controllers[event.instance_id]['buttons'][event.button] = True
                
                # Add to event list
                _controller_events.append({
                    'type': 'button_down',
                    'controller_id': event.instance_id,
                    'button': event.button
                })
        
        # Handle button releases
        elif event.type == pygame.JOYBUTTONUP:
            if event.instance_id in _controllers:
                _controllers[event.instance_id]['buttons'][event.button] = False
                
                # Add to event list
                _controller_events.append({
                    'type': 'button_up',
                    'controller_id': event.instance_id,
                    'button': event.button
                })
        
        # Handle D-pad movement
        elif event.type == pygame.JOYHATMOTION:
            if event.instance_id in _controllers and event.hat < len(_controllers[event.instance_id]['hats']):
                _controllers[event.instance_id]['hats'][event.hat] = event.value
                
                # Add to event list
                _controller_events.append({
                    'type': 'hat_motion',
                    'controller_id': event.instance_id,
                    'hat': event.hat,
                    'value': event.value
                })
        
        # Handle analog stick movement
        elif event.type == pygame.JOYAXISMOTION:
            if event.instance_id in _controllers and event.axis < len(_controllers[event.instance_id]['axes']):
                _controllers[event.instance_id]['axes'][event.axis] = event.value
                
                # Add to event list if significant movement
                if abs(event.value) > 0.2:  # Only track significant movements
                    _controller_events.append({
                        'type': 'axis_motion',
                        'controller_id': event.instance_id,
                        'axis': event.axis,
                        'value': event.value
                    })
    
    return _controller_events

def get_controller_count():
    """Get the number of active controllers"""
    return sum(1 for c in _controllers.values() if c['connected'])

def get_first_controller():
    """Get the first active controller ID or None"""
    for controller_id, data in _controllers.items():
        if data['connected']:
            return controller_id
    return None

# For event-driven approach
def get_recent_events():
    """Get the most recent controller events (since last process_events call)"""
    return _controller_events

# OOP-based Controller Class
class Controller:
    """
    Controller class for OOP-based usage in sprites
    
    Example:
    controller = Controller()  # Gets first available controller
    if controller.is_connected():
        if controller.is_button_pressed(0):  # A button
            do_something()
    """
    
    # Common button mappings (adjust as needed for your controller)
    A = 0  # Usually the bottom button
    B = 1  # Usually the right button
    X = 2  # Usually the left button
    Y = 3  # Usually the top button
    LB = 4  # Left bumper/shoulder
    RB = 5  # Right bumper/shoulder
    BACK = 6  # Back/Select button
    START = 7  # Start button
    
    def __init__(self, controller_id=None):
        """
        Initialize controller with specified ID or first available
        
        Args:
            controller_id: Specific controller ID or None for first available
        """
        self.controller_id = controller_id or get_first_controller()
    
    def is_connected(self):
        """Check if this controller is connected"""
        return (self.controller_id in _controllers and 
                _controllers[self.controller_id]['connected'])
    
    def is_button_pressed(self, button):
        """Check if a specific button is currently pressed"""
        if not self.is_connected():
            return False
        
        buttons = _controllers[self.controller_id]['buttons']
        return button < len(buttons) and buttons[button]
    
    def get_dpad(self):
        """Get D-pad state as (x, y) tuple: -1/0/1 for each axis"""
        if not self.is_connected():
            return (0, 0)
        
        hats = _controllers[self.controller_id]['hats']
        return hats[0] if hats else (0, 0)
    
    def get_axis(self, axis):
        """Get specific axis value (-1.0 to 1.0)"""
        if not self.is_connected():
            return 0.0
        
        axes = _controllers[self.controller_id]['axes']
        return axes[axis] if axis < len(axes) else 0.0
    
    def get_left_stick(self):
        """Get left analog stick as (x, y) tuple with dead zone applied"""
        if not self.is_connected():
            return (0, 0)
        
        x = self.get_axis(0)
        y = self.get_axis(1)
        
        # Apply dead zone
        if abs(x) < 0.2:
            x = 0
        if abs(y) < 0.2:
            y = 0
        
        return (x, y)
    
    def get_right_stick(self):
        """Get right analog stick as (x, y) tuple with dead zone applied"""
        if not self.is_connected():
            return (0, 0)
        
        x = self.get_axis(2)  # Typically axis 2
        y = self.get_axis(3)  # Typically axis 3
        
        # Apply dead zone
        if abs(x) < 0.2:
            x = 0
        if abs(y) < 0.2:
            y = 0
        
        return (x, y)
    
    # Convenience methods for common actions
    def is_left_pressed(self):
        """Check if left direction is pressed (D-pad or left stick)"""
        if not self.is_connected():
            return False
        
        # Check D-pad
        if self.get_dpad()[0] < 0:
            return True
        
        # Check left stick
        return self.get_left_stick()[0] < 0
    
    def is_right_pressed(self):
        """Check if right direction is pressed (D-pad or left stick)"""
        if not self.is_connected():
            return False
        
        # Check D-pad
        if self.get_dpad()[0] > 0:
            return True
        
        # Check left stick
        return self.get_left_stick()[0] > 0
    
    def is_up_pressed(self):
        """Check if up direction is pressed (D-pad or left stick)"""
        if not self.is_connected():
            return False
        
        # Check D-pad
        if self.get_dpad()[1] > 0:
            return True
        
        # Check left stick
        return self.get_left_stick()[1] < 0  # Inverted Y axis
    
    def is_down_pressed(self):
        """Check if down direction is pressed (D-pad or left stick)"""
        if not self.is_connected():
            return False
        
        # Check D-pad
        if self.get_dpad()[1] < 0:
            return True
        
        # Check left stick
        return self.get_left_stick()[1] > 0  # Inverted Y axis
    
    def is_jump_pressed(self):
        """Check if jump button (A) or D-pad up is pressed"""
        return self.is_button_pressed(self.A) or self.is_up_pressed()