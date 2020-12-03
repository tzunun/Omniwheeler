"""
Wheel Movement
    from observation there are only three whell spining states which dictate the direction that
    the robot moves.
        ACW = Anti-clockwise
        CW = Clockwise
        Still = No movement.

Four Wheels
    These are controlled by GPIO indicating motor state (on/off) and rotation
    ACW/CW.

    Wheel 1:
        Motor: ON/OFF 
            GPIO 7
        Rotation: ACW/CW
            GPIO 11

    Wheel 2:
        Motor: ON/OFF 
            GPIO 13
        Rotation: ACW/CW
            GPIO 15

    Wheel 3:
        Motor: ON/OFF 
            GPIO 19
        Rotation: ACW/CW
            GPIO 21
        
    Wheel 4:
        Motor: ON/OFF 
            GPIO 23
        Rotation: ACW/CW
            GPIO 29

Direction of Movement (Robot)
    There are at the moment 11 possible directions of movement for the robot.
    
    North   East    North-East  North-West  Clockwise       Full-Stop
    South   West    South-West  South-East  Anti-Clockwise    N/A
    """

import time
import curses

def set_gpio_mode():
    GPIO.setmode(GPIO.BOARD)
    # Wheel 1
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    # Wheel 2
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    # Wheel 3
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    # Wheel 4
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(29,GPIO.OUT)
    
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.IN)
    # GPIO setup(37, GPIO. ?)
    # GPIO setup(3, GPIO. ?)
    # GPIO setup(5, GPIO. ?)
    # GPIO setup(32, GPIO. ?)


# Dictionary wheels to easily change GPIOs associated withe the wheels
def wheels_GPIOs() -> dict:
    return {
        "wheel_1" : {
            "motor_gpio": 7,
            "rotation_gpio": 11
            },
        "wheel_2" : {
               "motor_gpio": 13,
               "rotation_gpio": 15
               },
        "wheel_3" : {
               "motor_gpio": 19,
               "rotation_gpio": 21
               },
        "wheel_4" : {
               "motor_gpio": 23,
               "rotation_gpio": 29
               }
        }

def rotation_types() -> dict:
    return {
        # rotation(motor_on, rotation_direction)
        "clockwise": (True, True),
        "anticlockwise": (True, False),
        "stop": (False, False)
    }

# Direction of movement

def direction_of_movement(requested_direction: str) -> tuple:
    """
        This function expects a north, south, east, etc parameter and returns
        a tuple with the requested direction of wheel movement.

        calling: 
            direction_of_movement("north")
        will return:
            ("anticlockwise", "clockwise","clockwise", "anticlockwise" ),
        which is described as:
        tuple: (wheel_1_rotation, wheel_2_rotation, wheel_3_rotation, wheel_4_rotation)
    """

    directions = {
    "north": ("anticlockwise", "clockwise","clockwise", "anticlockwise" ),
    "north-east": ("anticlockwise", "still","clockwise", "still" ),
    "east": ("anticlockwise", "anticlockwise","clockwise", "clockwise" ),
    "south-east": ("still", "anticlockwise","still", "clockwise" ),
    "south": ("clockwise", "anticlockwise","anticlockwise", "clockwise" ),
    "south-west": ("clockwise", "still","anticlockwise", "still" ),
    "west": ("clockwise", "clockwise","anticlockwise", "anticlockwise" ),
    "north-west": ("still", "clockwise","still", "anticlockwise" ),
    "clockwise": ("clockwise", "clockwise","clockwise", "clockwise" ),
    "anticlockwise": ("anticlockwise", "anticlockwise","anticlockwise", "anticlockwise" ),
    "full_stop": ("still", "still","still", "still" )
    }

    return directions[requested_direction]

def move_direction(requested_direction_of_movement):

    wheels = wheels_GPIOs()  # Wheels dict
    rotation = rotation_types() # Rotation dict
    direction = direction_of_movement(requested_direction_of_movement)

    for index,wheel in enumerate(wheels):
        motor_gpio = wheels[wheel]["motor_gpio"]
        rotation_gpio = wheels[wheel]["rotation_gpio"]
        rotation_type = rotation[direction[index]]  # clockwise, anticlockwise, still
        print(wheel, ":")
        print("GPIO.output({}, {})".format(motor_gpio,rotation_type[0]))
        print("GPIO.output({}, {})".format(rotation_gpio, rotation_type[1]))

if __name__== "__main__":
    # This will run on a Rasberry Pi.  WIll cause error
    # On Desktop
    import RPI.GPIO as GPIO
    while True:
        direction = input("Please enter the requested direction of movement, north, south, etc,.: \n")
        move_direction(direction)