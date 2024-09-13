from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import os

app = Flask(__name__)

# Set the path for the images folder
IMAGES_FOLDER = 'images'

@app.route('/')
def index():
    return render_template('password.html')

@app.route('/check-pin', methods=['POST'])
def check_pin():
    pin = request.form.get('pin1') + request.form.get('pin2') + request.form.get('pin3') + request.form.get('pin4') + request.form.get('pin5') + request.form.get('pin6')
    if pin == '150923': 
        return redirect(url_for('anniversary_message'))
    return render_template('password.html', error='Incorrect PIN. Please try again.')

@app.route('/anniversary')
def anniversary_message():
    return render_template('anniversary_message.html')

@app.route('/game1')
def game():
    return render_template('game_1.html')

@app.route('/images/list')
def list_images():
    images = [f for f in os.listdir(IMAGES_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return jsonify(images)

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/hangman')
def hangman():
    return render_template('game_2.html')

@app.route('/message')
def message():
    return render_template('message.html')

if __name__ == '__main__':
    app.run(debug=True)
