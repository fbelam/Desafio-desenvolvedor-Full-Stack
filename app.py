from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'pre_venda'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb_resultado_viabilidade")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', students=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Dado inserido com sucesso!")
        id = request.form['id']
        id_viabilidade = request.form['id_par']
        id_parceiro_resposta = request.form['id_via']
        resultado_parceiro=request.form['text']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_resultado_viabilidade (id, id_viabilidade,id_parceiro_resposta, resultado_parceiro) VALUES (%s, %s, %s, %s)", (id, id_viabilidade, id_parceiro_resposta, resultado_parceiro))        
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['GET'])
def delete(id):
    flash("Deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tb_resultado_viabilidade WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        id_viabilidade = request.form['id_par']
        id_parceiro_resposta = request.form['id_via']
        resultado_parceiro=request.form['text']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE tb_resultado_viabilidade SET id_viabilidade=%s, id_parceiro_resposta=%s, resultado_parceiro=%s
        WHERE id=%s
        """, (id, id_viabilidade, id_parceiro_resposta, resultado_parceiro))
        flash("alterado com sucesso")
        mysql.connection.commit()
        return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)
