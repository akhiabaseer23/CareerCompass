from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)  # Allow requests from frontend

@app.route('/')
def home():
    return render_template('index.html')  # Load your frontend page

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    # Example: get quiz answers
    answers = data.get("answers", [])
    
    # Simple example logic (replace with real ML logic later)
    if "design" in answers:
        result = "UI/UX Designer"
    elif "code" in answers:
        result = "Software Engineer"
    else:
        result = "Tech Generalist"

    return jsonify({"career_match": result})

if __name__ == '__main__':
    app.run(debug=True)
