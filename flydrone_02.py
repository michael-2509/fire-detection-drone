# import required module
import airsim
import keyboard

# create a drone client
client = airsim.MultirotorClient()

# confirm connection
client.confirmConnection()

# enable API control
client.enableApiControl(True)

# arm the drone
client.armDisarm(True)

# set the velocity vector to zero initially
velocity = airsim.Vector3r(0, 0, 0)

# set the duration to 0.1 seconds
duration = 0.1

# set the yaw mode to face front initially
yaw_mode = airsim.YawMode(is_rate=False, yaw_or_rate=0)

# set the drivetrain mode to forward only
drivetrain = airsim.DrivetrainType.ForwardOnly

# loop until the user presses ESC key
while not keyboard.is_pressed("X"):
    # check if the user presses T key
    if keyboard.is_pressed("t"):
        # take off the drone
        client.takeoffAsync().join()
    # check if the user presses L key
    elif keyboard.is_pressed("l"):
        # land the drone
        client.landAsync().join()

    # check if the user presses W key
    if keyboard.is_pressed("w"):
        # set the velocity vector to move forward
        velocity.x_val = 3  # positive x is forward
    # check if the user presses S key
    elif keyboard.is_pressed("s"):
        # set the velocity vector to move backward
        velocity.x_val = -3  # negative x is backward
    # otherwise, stop moving forward or backward
    else:
        velocity.x_val = 0

    # check if the user presses A key
    if keyboard.is_pressed("a"):
        # set the velocity vector to move left
        velocity.y_val = -3  # negative y is left
    # check if the user presses D key
    elif keyboard.is_pressed("d"):
        # set the velocity vector to move right
        velocity.y_val = 3  # positive y is right
    # otherwise, stop moving left or right
    else:
        velocity.y_val = 0

    # check if the user presses Q key
    if keyboard.is_pressed("q"):
        # set the yaw mode to turn left at 30 degrees per second
        yaw_mode.is_rate = True  # use rate mode for yaw control
        yaw_mode.yaw_or_rate = -30  # negative rate is left turn
    # check if the user presses E key
    elif keyboard.is_pressed("e"):
        # set the yaw mode to turn right at 30 degrees per second
        yaw_mode.is_rate = True  # use rate mode for yaw control
        yaw_mode.yaw_or_rate = 30  # positive rate is right turn
    # otherwise, stop turning left or right and face front
    else:
        yaw_mode.is_rate = False  # use angle mode for yaw control
        yaw_mode.yaw_or_rate = 0  # zero angle is front

    # move the drone by the velocity vector for the duration with the yaw mode and drivetrain mode
    client.moveByVelocityAsync(velocity.x_val, velocity.y_val, velocity.z_val,
                               duration, drivetrain=drivetrain, yaw_mode=yaw_mode).join()

# disarm the drone
client.armDisarm(False)

# disable API control
client.enableApiControl(False)
