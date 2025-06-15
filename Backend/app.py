from flask import Flask, render_template

app = Flask(__name__)

@app.route('/resources')
def resources():
    courses = [
        {
            "name": "UI/UX Design",
            "description": "Basics of designing user interfaces",
            "topics": ["Figma Basics", "Design Principles", "Wireframing"],
            "price": "Free"
        },
        {
            "name": "Frontend Development",
            "description": "HTML, CSS, and JS fundamentals",
            "topics": ["HTML Tags", "Flexbox/Grid", "JavaScript Basics"],
            "price": "Free"
        },
        {
            "name": "Testing Basics",
            "description": "QA fundamentals for software testing",
            "topics": ["Manual Testing", "Bug Reporting", "Test Cases"],
            "price": "Free"
        }
    ]
    return render_template("resources.html", courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
