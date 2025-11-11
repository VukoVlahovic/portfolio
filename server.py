import os
from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("./index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/notebooks/<string:notebook_name>')
def show_notebook(notebook_name):
    """Serve converted Jupyter notebooks as HTML"""
    return render_template(f'notebooks/{notebook_name}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        email = data.get('email', '')
        subject = data.get('subject', '')
        message = data.get('message', '')

        csv_path = 'database.csv'
        # Write header if file doesn't exist or is empty
        need_header = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0

        with open(csv_path, mode='a', newline='', encoding='utf-8') as database:
            csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if need_header:
                csv_writer.writerow(['email', 'subject', 'message'])
            csv_writer.writerow([email, subject, message])

        return redirect(url_for('html_page', page_name='thankyou.html'))
    # optional: redirect on GET
    return redirect(url_for('home_page'))

# How it was done before the route rework:

# @app.route("/index.html")
# def home_page():
#     return render_template("./index.html")

# @app.route("/works.html")
# def works():
#     return render_template("./works.html")
