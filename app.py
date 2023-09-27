from flask import Flask, request, jsonify
from mycobot_actions import hello, custom_angles, reset
from mycobot_init import initialize_mycobot

app = Flask(__name__)

mc = initialize_mycobot()

@app.route('/')
def hello_world():
    return "Hello, World!"
    
@app.route('/command', methods=['GET'])
def send_coordinates():
    data = request.args  # Get URL parameters
    command = list(data.keys())[0]  # Assuming the first key is the command

    if command == "srs":
        angles = list(map(int, data[command].split()))
        return custom_angles(mc, angles)

    elif command == "hol":
        return hello(mc)

    #elif command == "bai":
        #return baile(mc)
    #Hay que implementarlo
    #elif command == "vas":
      #  return vaso(mc)
    #Hay que implementarlo
    elif command == "res":
        return reset(mc)
    #Hay que implementarlo
    else:
        print("Invalid command received")
        return jsonify({"status":"Failure", "message":"Invalid command"}),400
    # More elif conditions for other commands go here...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
