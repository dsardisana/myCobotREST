import time
from flask import jsonify
from pymycobot.genre import Angle

def hello(mc):
    # Move all joints to the [0, 0, 0, 0, 0, 0] position
    print("Moving to initial position...")
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)

    # Wait for the robotic arm to reach the specified position
    time.sleep(2.5)

    # Move joint 1 to the 90-degree position
    print("Moving Joint 1 to 90 degrees...")
    mc.send_angle(Angle.J1.value, 90, 50)

    # Wait for the robotic arm to reach the specified position
    time.sleep(2)

    # Make the robotic arm swing left and right for a specified number of loops
    num = 2  # You can adjust the number of loops as needed
    print("Swinging left and right...")
    while num > 0:
        print("Swinging left...")
        mc.send_angle(Angle.J2.value, 50, 100)
        time.sleep(1.5)

        print("Swinging right...")
        mc.send_angle(Angle.J2.value, -50, 100)
        time.sleep(1.5)

        num -= 1

    # Move the robotic arm to a specific position
    print("Moving to a specific position...")
    mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)
    print("Moving to final position...")
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    return jsonify({"status": "Success", "message": "Executed 'Hola' command"}), 200

def reset(mc):
    # Move all joints to the [0, 0, 0, 0, 0, 0] position
    print("Reseting position...")
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    return jsonify({"status": "Success", "message": "Executed 'Reset' command"}), 200

def custom_angles(mc, angles):
    print("Moving to custom angles...")
    print(angles)
    mc.send_angles(angles, 50)
    time.sleep(2.5)
    return jsonify({"status": "Success", "message": "Moved to custom angles"}), 200
