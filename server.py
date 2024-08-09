from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import csv

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_file(data):
    try:
        with open('data.txt', mode='a') as database:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            print(f"Writing to file: {email}, {subject}, {message}")
            database.write(f'\n{email},{subject},{message}')
    except Exception as e:
        print(f"Failed to write to the file: {e}")

def write_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'