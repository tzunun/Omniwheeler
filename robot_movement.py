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
    these can be achieved with 6 functions
    
    Original:   North   East    North-East  North-West  Clockwise       Full-Stop
    Inverted:   South   West    South-West  South-East  Anti-Clockwise    N/A
    """

import time
import curses
import GPIO

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
j

# Direction of movement

def north():
    print("Moving North")
    direction = ["anticlockwise", "clockwise","clockwise", "anticlockwise" ]
    move_direction(direction)

def north_east():
    print("Moving North-East")
    direction = ["anticlockwise", "still","clockwise", "still" ]
    move_direction(direction)

def east():
    print("Moving East")
    direction = ["anticlockwise", "anticlockwise","clockwise", "clockwise" ]
    move_direction(direction)

def south_east():
    print("Moving South-East")
    direction = ["still", "anticlockwise","still", "clockwise" ]
    move_direction(direction)

def south():
    print("Moving South")
    direction = ["clockwise", "anticlockwise","anticlockwise", "clockwise" ]
    move_direction(direction)

def south_west():
    print("Moving South-West")
    direction = ["clockwise", "still","anticlockwise", "still" ]
    move_direction(direction)

def west():
    print("Moving West")
    direction = ["clockwise", "clockwise","anticlockwise", "anticlockwise" ]
    move_direction(direction)

def north_west():
    print("Moving North-West")
    direction = ["still", "clockwise","still", "anticlockwise" ]
    move_direction(direction)

def spin_clockwise():
    print("Moving Clockwise")
    direction = ["clockwise", "clockwise","clockwise", "clockwise" ]
    move_direction(direction)

def spin_anticlockwise():
    print("Moving Antilockwise")
    direction = ["anticlockwise", "anticlockwise","anticlockwise", "anticlockwise" ]
    move_direction(direction)

def full_stop():
    print("Full Stopp")
    direction = ["still", "still","still", "still" ]
    move_direction(direction)


def move_direction(direction):
    wheels = wheels_GPIOs()  # Wheels dict
    rotation = rotation_types() # Rotation dict

    for index,wheel in enumerate(wheels):
        motor_gpio = wheels[wheel]["motor_gpio"]
        rotation_gpio = wheels[wheel]["rotation_gpio"]
        rotation_type = rotation[direction[index]]  # clockwise, anticlockwise, still
          ...:
        #print(wheel, wheels[wheel], direction[index], rotation[direction[index]])
        print(wheel, ":")
        print("GPIO.output({}, {})".format(motor_gpio,rotation_type[0]))
        print("GPIO.output({}, {})".format(rotation_gpio, rotation_type[1]))