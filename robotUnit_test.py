# Sun / March / 12 / 2017
# George Ceja


# Motor ids passed in strings
left_motor = "47245882351169526624416"
right_motor = "47246204322983744914166"

def autonomous_setup():
	print("Autonomous mode")
	Robot.set(####)

def autonomous_main():
	pass

async def autonomous_actions():
	print("Autonomous code")
 	await Actions.sleep(1.0)                              #preset function
	print("1 second has passed in autonomous mode")

def teleop_setup():
	print("Tele-operated mode")

def teleop_main():
	if Gamepad.get_value("joystick_right_y") < -.2:
		Robot.set_value(right_motor, "duty_cycle", -1)
	if Gamepad.get_value("joystick_right_y") > .2:
		Robot.set_value(right_motor, "duty_cycle", 1)
	if Gamepad.get_value("joystick_left_y") < -.2:
		Robot.set_value(left_motor, "duty_cycle", 1)
	if Gamepad.get_value("joystick_left_y") > .2:
		Robot.set_value(left_motor, "duty_cycle", -1)
	if Gamepad.get_value("joystick_left_y") == 0 and Gamepad.get_value("joystick_right_y") == 0:
		Robot.set_value(left_motor, "duty_cycle", 0)
		Robot.set_value(right_motor, "duty_cycle", 0)
