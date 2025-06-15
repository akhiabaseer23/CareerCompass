from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Landing Page
@app.route('/')
def home():
    return render_template('index.html')

# Quiz Page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Result Page
@app.route('/result')
def result():
    return render_template('result.html')

# Handle Quiz Submission
@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()

    if not data or "answers" not in data:
        return jsonify({"error": "Invalid data"}), 400

    answers = data["answers"]

    # Rule-based logic (can be replaced by ML later)
    if "design" in answers:
        result = "UI/UX Designer"
    elif "code" in answers:
        result = "Software Engineer"
    else:
        result = "Tech Generalist"

    return jsonify({"career_match": result})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
