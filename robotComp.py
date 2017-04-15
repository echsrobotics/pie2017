# Calling motorID as variables
arm = ""
left_lift = ""
right_lift = ""
left_motor = ""
right_motor = ""

# Motor Speeds
wheel_speed = 1.0
up_speed = 0.55
down_speed = 0.01
arm_speed = 0.5

def autonomous_setup():
    Robot.run()

def autonomous_main():
    pass

async def pick_up():
    # Move forward for 1 second
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(1.0)

    # Stop when all autonomous code is done
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)
def teleop_setup():
    print("Tele-OP has been started")

def teleop_main():
    # Tank Control
    Robot.set_value(left_motor, "duty_cycle", Gamepad.get_value("joystick_left_y"))
    Robot.set_value(right_motor, "duty_cycle", -Gamepad.get_value("joystick_right_y"))

    # Arm Lift
    if Gamepad.get_value("l_bumper"): # Lift up
        Robot.set_value(left_lift, "duty_cycle", up_speed)
        Robot.set_value(right_lift, "duty_cycle", -up_speed)
    elif Gamepad.get_value("r_bumper"): # Lift down
        Robot.set_value(left_lift, "duty_cycle", -down_speed)
        Robot.set_value(right_lift, "duty_cycle", down_speed)
    else:
        Robot.set_value(left_lift, "duty_cycle", 0)
        Robot.set_value(right_lift, "duty_cycle", 0)

    # Arm
    if Gamepad.get_value("button_a"): # Open
        Robot.set_value(arm, "duty_cycle", arm_speed)
    elif Gamepad.get_value("button_b"): # Close
        Robot.set_value(arm, "duty_cycle", -arm_speed)
    else:
        Robot.set_value(arm, "duty_cycle", 0)
