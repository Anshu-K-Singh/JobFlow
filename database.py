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

def fetch_data_as_dict(query):
    with engine.connect() as conn:
        result = conn.execute(text(query))
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


# # Print the list of dictionaries
# print(data)
