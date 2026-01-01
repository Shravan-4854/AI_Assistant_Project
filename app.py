from flask import Flask, render_template# Import Flask and render_template
import assistant# Import the assistant module

app = Flask(__name__)# Initialize the Flask app

@app.route("/")# use to define the home route
def home():# user visits home page
    return render_template("index.html")# Render the home page

@app.route("/listen")# Route to listen for commands
def listen():# Listen for a command
    command = assistant.sptext()# Get the spoken command
    response = assistant.process_command(command)# Process the command and get the response
    return render_template("index.html", command=command, response=response)# Render the template with command and response

if __name__ == "__main__":# used to run the app
    app.run(debug=True)#use debug mode for development
