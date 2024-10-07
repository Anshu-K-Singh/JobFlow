from sqlalchemy import create_engine, text

# Database credentials
MYSQL_USER = "root"
MYSQL_PASSWORD = "gsaJRRDwCveDQdaoEaXUrhjzfSlXHlxq"
MYSQL_HOST = "junction.proxy.rlwy.net"
MYSQL_PORT = 42886
MYSQL_DATABASE = "railway"

# Create the engine
engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
)

def fetch_data_as_dict():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from jobs"))
        # Fetch all rows
        rows = result.fetchall()

        # Get column names
        column_names = result.keys()

        # Create a list of dictionaries
        data = []
        for row in rows:
            row_dict = {column: row[i] for i, column in enumerate(column_names)}
            data.append(row_dict)

    return data

def fetch_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        job = result.fetchone()  # Fetch a single row

        if job:  # Check if a job was found
            # Get column names
            column_names = result.keys()
            # Create a dictionary for the job
            job_dict = {column: job[i] for i, column in enumerate(column_names)}
            return job_dict
    return None
# # Print the list of dictionaries
# print(data)

def send_data_to_db(job_id, form_data):
    with engine.connect() as conn:
       query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)")

       params = {'job_id': job_id, 'full_name': form_data['full_name'], 'email': form_data['email'], 'linkedin_url': form_data['linkedin_url'],'education': form_data['education'],'experience': form_data['experience'],'resume_url': form_data['resume_url']}

# Execute the query with the parameters

       
       try:
        with engine.begin() as conn:  # Automatically handles commit and rollback
            conn.execute(query, params)
        print("Application data inserted successfully.")
       except Exception as e:
        print(f"Error inserting data: {e}")
