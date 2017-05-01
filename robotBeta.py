# Calling motorID as string variables
arm = "47260304209747780370249"
left_lift = "47244777713041566566067"
right_lift = "47245556432598227082168"
left_motor = "47249793534930396697565"
right_motor = "47248320646768022011260"

# Motor Speeds
wheel_speed = 1.0
up_speed = 0.9
down_speed = 0.5
arm_speed = 0.3

def autonomous_setup():
    Robot.run(pick_up)

def autonomous_main():
    pass

async def pick_up():
    #Move forward for 1.1 second out of box
    Robot.run(moveForward, 1.1)
    #Turn right for 90 degree
    Robot.run(turnRight, 2.15)
    #Move forward for 1.8 second to the coins
    Robot.run(moveForward, 1.8)
    #Turn left for 180 degree after getting coins
    Robot.run(turnLeft, 4.15)
    #Move forward for 3.15 second towards the slot
    Robot.run(moveForward, 3.15)
    #Turn left for 90 degree towards the slot
    Robot.run(turnLeft, 1.9)
    #Move forward for 1.8 second towards the slot
    Robot.run(moveForward, 1.8)
    #Move back for 1.95 second to release the coins
    Robot.run(moveBackward, 1.95)
    #Arm close to shift down
    Robot.set_value(arm, "duty_cycle", -arm_speed)
    await Actions.sleep(0.5)
    #Arm open to push coins
    Robot.set_value(arm, "duty_cycle", arm_speed)
    await Actions.sleep(0.2)
    #Arm stop after action
    Robot.set_value(arm, "duty_cycle", 0)
    #Move forward for 2.7 second to push the coins in
    Robot.run(moveForward, 2.7)
    #Move back for 1 second away from slot
    Robot.run(moveBackward, 1.0)
    #Move forward for 1 second to push remaining coins in
    Robot.run(moveForward, 1.0)
    #Arm close to get a better angle
    Robot.set_value(arm, "duty_cycle", -0.1)
    await Actions.sleep(1.4)
    #Arm stop after closing
    Robot.set_value(arm, "duty_cycle", 0)
    #Move back for 2 second away from the slot
    Robot.run(moveBackward, 2.0)
    #Move forward for 2.1 second
    Robot.run(moveForward, 2.1)
    #Arm close to get a better angle
    Robot.set_value(arm, "duty_cycle", -0.1)
    await Actions.sleep(0.5)
    #Arm stop after action
    Robot.set_value(arm, "duty_cycle", 0)
    #Move back for 2.0 second to get out of starting box
    Robot.run(moveBackward, 2.0)
    #Stop when all autonomous code is done
    Robot.run(stop)


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

# Basic movement code for autonomous
async def turnLeft(t):
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(t)

async def turnRight(t):
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(t)

async def moveForward(t):
    Robot.set_value(left_motor, "duty_cycle", wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", -wheel_speed)
    await Actions.sleep(t)

async def moveBackward(t):
    Robot.set_value(left_motor, "duty_cycle", -wheel_speed)
    Robot.set_value(right_motor, "duty_cycle", wheel_speed)
    await Actions.sleep(t)

async def stop():
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)
