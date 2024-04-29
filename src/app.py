from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/src/templates/componentes.html')
def componentes():
    return render_template('componentes.html')

@app.route('/src/templates/carros.html')
def carros():
    return render_template('carros.html')