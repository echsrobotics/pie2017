# Calling motorID as string variables
arm = "47250366310977878277732"
left_lift = "47244777713041566566067"
right_lift = "47245556432598227082168"
left_motor = "47259833172070488766065"
right_motor = "47254869497321097390333"

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
