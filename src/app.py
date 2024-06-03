from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'carros_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/src/templates/componentes.html')
def componentes():
    return render_template('componentes.html')

@app.route('/src/templates/carros.html')
def carros():
    return render_template('carros.html')

@app.route('/opinioes', methods=['GET', 'POST'])
def opinioes():
    if request.method == 'POST':
        nome = request.form['nome']
        opiniao = request.form['opiniao']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO opinioes (nome, opiniao) VALUES (%s, %s)', (nome, opiniao))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('opinioes'))
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM opinioes ORDER BY data DESC')
    opinioes = cursor.fetchall()
    cursor.close()
    return render_template('opinioes.html', opinioes=opinioes)

@app.route('/test_db')
def test_db():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT 1 ''')
    result = cursor.fetchone()
    return f"Conexão bem-sucedida! {result}"

if __name__ == '__main__':
    app.run(debug=True)