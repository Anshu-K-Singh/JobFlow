from flask import Flask, render_template, jsonify
from database import fetch_data_as_dict
app = Flask(__name__)



@app.route("/")
def home_page():
    # Fetch data from the jobs table
    query = "SELECT * FROM jobs"
    data = fetch_data_as_dict(query)

    return render_template('home.html', title = "Home", jobs = data)



@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)