from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

def initialize_mycobot():
    try:
        print("Initializing MyCobot...")
        mc = MyCobot(PI_PORT, PI_BAUD)
        print("myCobot initialized. ")
        return mc
        
    except Exception as e:
        print(f"An error occurred while initializing MyCobot: {str(e)}")
        return None