from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

def initialize_mycobot():
    print("Initializing MyCobot...")
    mc = MyCobot(PI_PORT, PI_BAUD)
    return mc