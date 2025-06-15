from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Landing Page
@app.route('/')
def home():
    return render_template('index.html')

# Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
