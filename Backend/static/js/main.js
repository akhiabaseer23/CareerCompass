// static/js/main.js

function submitQuiz() {
  const answers = ["design", "code"]; // replace with actual user inputs

  fetch('http://localhost:5000/submit-quiz', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ answers })
  })
    .then(res => res.json())
    .then(data => {
      alert("Your matched career: " + data.career_match);
    });
}
