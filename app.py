from flask import Flask, send_file, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def upload_form():
    print("Hello")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, template_folder='templates')