from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post_ride():
    if request.method == 'POST':
        name = request.form['name']
        origin = request.form['origin']
        destination = request.form['destination']
        time = request.form['time']
        contact = request.form['contact']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO rides (name, origin, destination, time, contact) VALUES (?, ?, ?, ?, ?)",
                  (name, origin, destination, time, contact))
        conn.commit()
        conn.close()

        print(f"Mock notification sent to {contact} confirming ride post.")
        return redirect('/rides')
    return render_template('post_ride.html')

@app.route('/rides')
def view_rides():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM rides ORDER BY id DESC")
    rides = c.fetchall()
    conn.close()
    return render_template('rides.html', rides=rides)

if __name__ == '__main__':
    app.run(debug=True)
