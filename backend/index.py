from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client

client = Client('AC1519f6c35abae292854d60746394de52', '48e3893e7ad7e865b6893ba175160fe4')
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/sms', methods=['POST','GET'])
def textfrom():

    body = request.values.get('Body', None)

    print(body)

    echo = MessagingResponse()

    echo.message("hello")

    return(str(echo))

