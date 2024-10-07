from flask import Flask, render_template, jsonify, request
from database import fetch_data_as_dict, fetch_job_from_db, send_data_to_db

app = Flask(__name__)



@app.route("/")
def home_page():
    # Fetch data from the jobs table
    
    data = fetch_data_as_dict()

    return render_template('home.html', title = "Home", jobs = data)

#fetch single job from DB
@app.route("/job/<int:id>")
def list_jobs(id):
    job = fetch_job_from_db(id)
    return render_template('job_detail.html', job = job)

# from post to db

@app.route("/job/<int:id>/apply", methods = ['post'])
def job_apply(id):
    form_data = request.form
    send_data_to_db(id, form_data)
    
    job = fetch_job_from_db(id)
    return render_template('submit.html', application = form_data, job = job)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)