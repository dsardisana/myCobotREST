import time
from flask import jsonify
from pymycobot.genre import Angle

def hello(mc):
    print("Moving to initial position...")
    mc.send_angles([-90, 0, 0, 0, 0, 0], 50)
    time.sleep(2.5)
    # Make the robotic arm swing  for a specified number of loops
    num = 3  # You can adjust the number of loops as needed
    print("Swinging left and right...")
    while num > 0:
        mc.send_angle(Angle.J4.value, 50, 100)
        time.sleep(1)
        mc.send_angle(Angle.J4.value, -50, 100)
        time.sleep(1)

        num -= 1

    print("Moving to final position...")
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    return jsonify({"status": "Success", "message": "Executed 'Hola' command"}), 200

def reset(mc):
    # Move all joints to the [0, 0, 0, 0, 0, 0] position
    print("Reseting position...")
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    return jsonify({"status": "Success", "message": "Executed 'Reset' command"}), 200


def map_angle(angle, original_min, original_max, new_min=-160, new_max=160):
    mapped = ((angle - original_min) / (original_max - original_min)) * (new_max - new_min) + new_min
    return (round(mapped))

def custom_angles(mc, angles):
    # Define the original ranges for each angle
    original_ranges = [
        (0, 180),  # Angle 1
        (30, 135), # Angle 2
        (45, 135),  # Angle 3
        (30, 150), # Angle 4
        (0, 180),  # Angle 5
        (0, 180)   # Angle 6
    ]
    
    # Map each angle to the new range and round to the nearest integer
    mapped_angles = [map_angle(angle, original_min, original_max) for angle, (original_min, original_max) in zip(angles, original_ranges)]
    
    # Check if any mapped angle is greater than 160 or smaller than -160
    if any(angle > 160 or angle < -160 for angle in mapped_angles):
        print("Invalid angles received. Angles must be between -160 and 160.")
        return jsonify({"status": "Error", "message": "Invalid angle values. Angles must be between -160 and 160."}), 400

    print("Moving to custom angles...")
    print(mapped_angles)
    mc.send_angles(mapped_angles, 50)
    
    return jsonify({"status": "Success", "message": "Moved to custom angles"}), 200


def baile(mc):
    speed=100
    sleep_time=0.8
    mc.set_color(0,0,0)
    mc.send_angles([-90, 0, 0, 0, 0, 0], speed)
    time.sleep(1)
    
    mc.set_color(255,255,255)
    print("Starting the dance...")
    mc.send_angles([-90, 60, -40, 40, 0, 0], speed)
    time.sleep(sleep_time)
    
    mc.set_color(255,0,0)
    mc.send_angles([-90, -60, 40, -40, 0, 0], speed)
    time.sleep(sleep_time)

    mc.set_color(0,255,0)
    mc.send_angles([-90, 60, -40, 40, 0, 0], speed)
    time.sleep(sleep_time)

    mc.set_color(0,0,255)
    mc.send_angles([-90, -60, 40, -40, 0, 0], speed)
    time.sleep(sleep_time)
    
    mc.set_color(192,38,2)
    mc.send_angles([-90, 60, -40, 40, 0, 0], speed)
    time.sleep(sleep_time)
    
    # Move back to initial position
    mc.send_angles([0, 0, 0, 0, 0, 0], speed)
    time.sleep(1)
    
    print("Dance completed.")
    return jsonify({"status": "Success", "message": "Executed 'Baile' command"}), 200
