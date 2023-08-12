import airsim
import keyboard

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# request control of the APIs
client.enableApiControl(True)

# take off
client.takeoffAsync().join()


def take_off():
    client.takeoffAsync().join()

# move forward


def move_forward():
    client.moveByVelocityAsync(10, 0, 0, 5).join()

# turn right


def turn_right():
    client.rotateByYawRateAsync(30, 5).join()

# move backward


def move_backward():
    client.moveByVelocityAsync(-10, 0, 0, 5).join()

# land


def land():
    client.landAsync().join()


# assign keys to functions
keyboard.add_hotkey('t', take_off)
keyboard.add_hotkey('w', move_forward)
keyboard.add_hotkey('d', turn_right)
keyboard.add_hotkey('s', move_backward)
keyboard.add_hotkey('l', land)

# wait for keys to be pressed
keyboard.wait()
