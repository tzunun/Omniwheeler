import time
import RPi.GPIO as GPIO
# This import will be removed
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
        "still": (False, False)
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
    print("requested_direction_of_movement is: ", requested_direction_of_movement)


    wheels = wheels_GPIOs()  # Wheels dict
    rotation = rotation_types() # Rotation dict
    # direction now becomes ("clockwise", "still", "clockwise", "still")
    direction = direction_of_movement(requested_direction_of_movement)
    print(direction)

    for index,wheel in enumerate(wheels):
        motor_gpio = wheels[wheel]["motor_gpio"]
        rotation_gpio = wheels[wheel]["rotation_gpio"]
        rotation_type = rotation[direction[index]]  # clockwise, anticlockwise, still
        #print(wheel, ":")
        #print("GPIO.output({}, {})".format(motor_gpio,rotation_type[0]))
        #print("GPIO.output({}, {})".format(rotation_gpio, rotation_type[1]))

        # This part of the code turns the motor on, and sets the direction of wheel rotation
        # This receives a tuple (motor state, rotation anticlockwise/clockwise/still)
        GPIO.output(motor_gpio, rotation_type[0])
        GPIO.output(rotation_gpio, rotation_type[1])


if __name__== "__main__":

    set_gpio_mode()

    def match_key_direction(pressed_char: str) -> str:
        print("inside match_key_direction", pressed_char)
        
        key_direction = {
            "108": "clockwise",
            "114": "anticlockwise",
            "115": "full_stop",
            "116": "north-east",
            "101": "north-west",
            "98": "south-east",
            "99": "south-west",
            "259": "north",
            "258": "south",
            "260": "west",
            "261": "east",
        }

        for key in key_direction.keys():
            if key == pressed_char:
                return key_direction[key]
        return "not found"


    while True:
                    # Identify terminal
        screen = curses.initscr()
        # Clear the screen
        # No keystroked echoed to the console
        curses.noecho()
        screen.refresh()
        # Enter/Return not required to register the key pressed
        curses.cbreak()
        screen.keypad(True)

        pressed_key = screen.getch()

        if pressed_key == ord('q'):
            break
        else:
            curses.nocbreak()
            screen.keypad(0)
            curses.echo()           # basically use the keypressed integer to get the direction

            x = match_key_direction(str(pressed_key)) 
            if x != "not found":
                time.sleep(.3)  # Sleeping 300ms, sleep() takes numbers as seconds.
                move_direction(match_key_direction(str(pressed_key)))

    curses.nocbreak()  # Turn off cbreak mode
    curses.echo()  # Turn echo on again
    curses.curs_set(1)  # turn cursor back on 
    screen.keypad(0)  # Turn off keypad keys
    curses.endwin()
    GPIO.cleanup()