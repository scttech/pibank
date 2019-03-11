from flask import Flask
from flask_graphql import GraphQLView
import RPi.GPIO as GPIO
from flask_cors import CORS
from models import db_session
from schema import schema, Customer

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

app.add_url_rule(
        '/api/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True 
            )
        )

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/api/gpio/on', methods=['POST'])
def gpioOn():
    GPIO.output(18, True)
    return "/api/gpio/on accessed"

@app.route('/api/gpio/off', methods=['POST'])
def gpioOff():
    GPIO.output(18, False)
    return "/api/gpio/off accessed"
                     
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
