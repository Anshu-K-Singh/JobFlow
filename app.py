from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
    {
        "id": 1,
        "job_name": "Data Analyst",
        "location": "Bengaluru (India)",
        "Salary": "10 LPA"
    },
    {
        "id": 2,
        "job_name": "Software Engineer",
        "location": "Hyderabad (India)",
        "Salary": "15 LPA"
    },
    {
        "id": 3,
        "job_name": "Product Manager",
        "location": "Gurgaon (India)",
        "Salary": "25 LPA"
    },
    {
        "id": 4,
        "job_name": "UI/UX Designer",
        "location": "Pune (India)",
        "Salary": "12 LPA"
    },
    {
        "id": 5,
        "job_name": "DevOps Engineer",
        "location": "Chennai (India)",
        "Salary": "18 LPA"
    },
    {
        "id": 6,
        "job_name": "Marketing Specialist",
        "location": "Mumbai (India)",
        "Salary": "14 LPA"
    },
    {
        "id": 7,
        "job_name": "Quality Assurance Engineer",
        "location": "Noida (India)",
        "Salary": "11 LPA"
    },
    {
        "id": 8,
        "job_name": "Technical Writer",
        "location": "Ahmedabad (India)",
        "Salary": "9 LPA"
    },
    {
        "id": 9,
        "job_name": "Cloud Architect",
        "location": "Toronto, Canada",
        "Salary": "110,000 CAD"
    },
    {
        "id": 10,
        "job_name": "Cybersecurity Analyst",
        "location": "Sydney, Australia",
        "Salary": "95,000 AUD"
    }
]



@app.route("/")
def home_page():
    return render_template('home.html', title = "Home", jobs = JOBS)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)