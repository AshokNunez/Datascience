# SQL Server Data Insert & Print Example

This project demonstrates how to **insert data into** and **print data from** a SQL Server table using Python and `pyodbc`.

---

## Prerequisites

- Python 3.x
- [pyodbc](https://pypi.org/project/pyodbc/)
- SQL Server (local or remote)
- [ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) (e.g., ODBC Driver 17 for SQL Server)

---

## Setup

1. **Install Python dependencies:**
    ```
    pip install pyodbc
    ```

2. **Install the ODBC Driver for SQL Server**  
   Download and install from [Microsoft's official page](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

3. **Create your SQL Server table**  
   Example:
   ```sql
   CREATE TABLE testTable (
       id INT PRIMARY KEY,
       email NVARCHAR(255),
       name NVARCHAR(255)
   );
   ```

---

## Usage

### 1. Insert Data

Edit `INSERT_ROWS.py` and update the connection details:

```python
import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=YourDatabaseName;'
        'UID=YourUsername;'
        'PWD=YourPassword;'
    )
    cursor = conn.cursor()
    data_to_insert = [
        (1, 'your_name', 'your_email_ID')
    ]
    cursor.executemany(
        "INSERT INTO testTable (id, email, name) VALUES (?, ?, ?)",
        data_to_insert
    )
    conn.commit()
    print("Data inserted successfully.")
except pyodbc.Error as e:
    print("Error while connecting to SQL Server:", e)
```

**Run the script:**
```
python INSERT_ROWS.py
```

---

### 2. Print Data

To print all rows from the table, add this code to your script:

```python
import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=YourDatabaseName;'
        'UID=YourUsername;'
        'PWD=YourPassword;'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM testTable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except pyodbc.Error as e:
    print("Error while connecting to SQL Server:", e)
```

---

## Notes

- Replace `YourDatabaseName`, `YourUsername`, and `YourPassword` with your actual SQL Server credentials.
- Make sure the ODBC driver name matches what is installed on your system (check with `pyodbc.drivers()`).
- You can modify the data and table structure as needed.

---

## Troubleshooting

- **Driver not found:**  
  Make sure you have the correct ODBC driver installed and use the exact name in the connection string.
- **Authentication errors:**  
  Double-check your username and password.
- **Table not found:**  
  Ensure the table exists in your database.

---
