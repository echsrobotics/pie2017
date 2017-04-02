# Motor ids passed in strings
left_lift = "47255190923709730375194"
right_lift = "47245556432598227082168"
arm = "INSERT"

def autonomous_setup():
    print("Autonomous mode")
    
def autonomous_main():
    pass

async def autonomous_actions():
    print("Autonomous code")
    await Actions.sleep(1.0)                              #preset function
    print("1 second has passed in autonomous mode")
    
def teleop_setup():
    print("Tele-operated mode")

def teleop_main():
# Arm Lift
    if Gamepad.get_value("dpad_down"):
        Robot.set_value(right_lift, "duty_cycle", -0.3)
        Robot.set_value(left_lift, "duty_cycle", 0.3)
    elif Gamepad.get_value("dpad_up"):
        Robot.set_value(right_lift, "duty_cycle", 0.3)
        Robot.set_value(left_lift, "duty_cycle", -0.3)
    else:
        Robot.set_value(left_lift, "duty_cycle", 0)
        Robot.set_value(right_lift, "duty_cycle", 0)
        
#Arm
    if Gamepad.get_value("l_bumper"):
        Robot.set_value(arm, "duty_cycle", 0.3)
    elif Gamepad.get_value("r_bumper"):
        Robot.set_value(arm, "duty_cycle", -0.3)
    else:
        Robot.set_value(arm, "duty_cycle", 0)