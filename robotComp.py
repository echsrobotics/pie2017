# Calling motorID as string variables
arm = "47260304209747780370249"
left_lift = "47244777713041566566067"
right_lift = "47245556432598227082168"
left_motor = "47249793534930396697565"
right_motor = "47245443110826771407393"

# Motor Speeds
wheel_speed = 1.0
up_speed = 0.9
down_speed = 0.1
arm_speed = 0.3

def autonomous_setup():
    Robot.run(pick_up)

def autonomous_main():
    pass

async def pick_up():
    #Move forward for 1.15 second
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(1.15)

    #Turn right for 1.05 second
    Robot.set_value(left_motor, "duty_cycle", 0.6)
    Robot.set_value(right_motor, "duty_cycle", 0.6)
    await Actions.sleep(1.05)
    
    #Move Forward for 0.45 second
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(0.45)
    
    #Turn right for 0.15 second
    Robot.set_value(left_motor, "duty_cycle", 0.6)
    Robot.set_value(right_motor, "duty_cycle", 0.6)
    await Actions.sleep(0.15)
    
    #Move Forward for 0.155
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(0.155)
    
    #Turn right for 1.65 second
    Robot.set_value(left_motor, "duty_cycle", 0.6)
    Robot.set_value(right_motor, "duty_cycle", 0.6)
    await Actions.sleep(1.65)
    
    #Move forward for 1.5 second
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(1.5)
    
    #Turn right for 0.3 second
    Robot.set_value(left_motor, "duty_cycle", 0.6)
    Robot.set_value(right_motor, "duty_cycle", 0.6)
    await Actions.sleep(0.3)
    
    #Move forward for 1.15 second to put coins in goal
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(1.15)
    
    #Close arm all the way for 2.0 second
    Robot.set_value(arm, "duty_cycle", 0.4)
    await Actions.sleep(2.0)

    #Turn right to get second set of coins for 1.5 second
    Robot.set_value(left_motor, "duty_cycle", 0.6)
    Robot.set_value(right_motor, "duty_cycle", 0.6)
    await Actions.sleep(1.5)
    
    #Move Backward for 1.4 second
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(1.4)
    
    #Turn left for 1.05 second
    Robot.set_value(left_motor, "duty_cycle", -0.6)
    Robot.set_value(right_motor, "duty_cycle", -0.6)
    await Actions.sleep(1.05)
    
    #Move Backward for 0.45 second
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(0.45)
    
    #Turn left for 0.15 second
    Robot.set_value(left_motor, "duty_cycle", -0.6)
    Robot.set_value(right_motor, "duty_cycle", -0.6)
    await Actions.sleep(0.15)
    
    # Move Backward for .155 second
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(0.155)
    
    #Turn right for 0.5 second
    Robot.set_value(left_motor, "duty_cycle", 0.6)
    Robot.set_value(right_motor, "duty_cycle", 0.6)
    await Actions.sleep(0.5)
    
    #Move forward for 1.5 second
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(1.5)
    
    #Turn left for 1.6 second
    Robot.set_value(left_motor, "duty_cycle", -0.6)
    Robot.set_value(right_motor, "duty_cycle", -0.6)
    await Actions.sleep(1.6)
    
    #Move backward to get out of the starting box of 2 second
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(2.0)

    #Stop when all autonomous code is done
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)


async def pick_up1():
    # Move backward for 1 second
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(1.4)
    print("Move done")

    # Turn left for
    Robot.set_value(left_motor, "duty_cycle", -0.3)
    Robot.set_value(right_motor, "duty_cycle", -0.6)
    await Actions.sleep(1.3)
    print("Turn done")

    # Stop when all autonomous code is done
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)

def teleop_setup():
    print("Tele-OP has been started")

def teleop_main():
    # Tank Control
    Robot.set_value(left_motor, "duty_cycle", -Gamepad.get_value("joystick_left_y"))
    Robot.set_value(right_motor, "duty_cycle", Gamepad.get_value("joystick_right_y"))

    # Arm Lift
    if Gamepad.get_value("l_bumper"): # Lift up
        Robot.set_value(left_lift, "duty_cycle", -up_speed)
        Robot.set_value(right_lift, "duty_cycle", up_speed)
    elif Gamepad.get_value("r_bumper"): # Lift down
        Robot.set_value(left_lift, "duty_cycle", down_speed)
        Robot.set_value(right_lift, "duty_cycle", -down_speed)
    else:
        Robot.set_value(left_lift, "duty_cycle", 0)
        Robot.set_value(right_lift, "duty_cycle", 0)

    # Arm
    if Gamepad.get_value("l_trigger"): # Open
        Robot.set_value(arm, "duty_cycle", arm_speed)
    elif Gamepad.get_value("r_trigger"): # Close
        Robot.set_value(arm, "duty_cycle", -arm_speed)
    else:
        Robot.set_value(arm, "duty_cycle", 0)
