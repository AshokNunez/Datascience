import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=YourDatabaseName;'
        'UID=YourUsername;'
        'PWD=YourPassword;'
    )
    cursor = conn.cursor()
    # Example data to insert
    data_to_insert = [
        (1,'your_name', 'your_email_ID')
    ]
    # Insert data into the table
    cursor.executemany(
        "INSERT INTO testTable (id,email,name ) VALUES (?,?, ?)",
        data_to_insert
    )
    conn.commit()
    conn.close()
    print("Data inserted successfully.")
except pyodbc.Error as e:
    print("Error while connecting to SQL Server:", e)   
