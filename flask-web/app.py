from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database Connection Setup
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # or your MySQL server
        user='your_username',       # MySQL username
        password='your_password', # MySQL password
        database='your_DB'  # your database name
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('success'))
        except Error as e:
            print(f"Error: {e}")
            return "There was an error while saving data."

@app.route('/success')
def success():
    return """
    <div class="alert alert-success" role="alert">
        <h2>Data Saved Successfully!</h2>
        <p>Your information has been saved to the database.</p>
        <a href="/" class="btn btn-primary">Go Back to Home <i class="fas fa-home"></i></a>
    </div>
    """


if __name__ == "__main__":
    app.run(debug=True)
