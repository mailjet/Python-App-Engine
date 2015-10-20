from flask import Flask
from mailjet_rest import Client
app = Flask(__name__)
app.config['DEBUG'] = True

client = Client(auth=('api key', 'api secret'))

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/send')
def send():
    """Send an email"""
    result = client.send.create({
        'FromEmail': 'your sender email',
        'Subject': 'Hello Mailjet!',
        'Text-Part': 'Welcome Onboard',
        'Recipients': [{'Email': 'recipient email'}]
    })
	# print the result on the client's screen
    return result.text


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
