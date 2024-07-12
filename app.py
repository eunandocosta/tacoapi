from flask import Flask
from flask_cors import CORS
from database import init_db
from routes.route import app as app_routes

app = Flask(__name__)
CORS(app) 

app.register_blueprint(app_routes)

init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
