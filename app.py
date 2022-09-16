from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from config import config

# Models:
from Models.ModelRoll import ModelRoll
from Models.ModelsTable import ModelTable
from Models.ModelPuc import ModelPuc

# Entities:


app = Flask(__name__)
db = MySQL(app)


@app.route('/')
def index():
    return render_template('main_administrator.html')


@app.route('/interface_rolls')
def interfaceRolls():
    return render_template('interface_rolls.html')


@app.route('/create_rolls', methods=['POST'])
def createRolls():
    if request.method == 'POST':
        roll = request.form['roll']
        password = request.form['password']
        ModelRoll.insertRoll(db, roll, password)
        flash('The roll was saved successfully')
        return redirect(url_for('index'))
    else:
        flash('there was an error, please check')
        return redirect(url_for('index'))


@app.route('/interface_show_rolls')
def interfaceShowRolls():
    datos = ModelRoll.showRolls(db)
    return render_template('interface_show_rolls.html', datos=datos)


@app.route('/interface_create_puc')
def interfaceCreatePuc():
    return render_template('interface_create_puc.html')


@app.route('/create_puc', methods=['POST'])
def createPuc():
    if request.method == 'POST':
        cuenta = request.form['cuenta']
        codigo = request.form['codigo']
        ModelTable.tablePuc(db, table_name=cuenta)
        ModelPuc.insertPuc(db, cuenta, codigo)
        flash('Created table and the PUC value was saved successfully')
        return redirect(url_for('index'))
    else:
        flash('there was an error, please check')
        return redirect(url_for('index'))


@app.route('/interface_show_puc')
def interfaceShowPuc():
    datos = ModelPuc.showPuc(db)
    return render_template('interface_show_puc.html', datos=datos)


@app.route('/show_table_puc/<cuenta>')
def ShowTablePuc(cuenta):
    datos = ModelPuc.showTablePuc(db, nameTable=cuenta)
    return render_template('show_table_puc.html', datos=datos, cuenta=cuenta)


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
