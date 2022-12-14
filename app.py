from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

from datetime import date
from config import config

# Models:
from Models.ModelRoll import ModelRoll
from Models.ModelsTable import ModelTable
from Models.ModelPuc import ModelPuc
from Models.ModelProducts import ModelProducts
from Models.ModelTxt import ModelTxt


# Entities:
from Entities.Products import Products


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


@app.route('/interface_consignment')
def interfaceConsignment():
    return render_template('interface_consignment.html')


@app.route('/insert_consignment', methods=['POST'])
def insertConsignment():
    if request.method == 'POST':
        detalle = request.form['detalle']
        valor = request.form['valor']
        fecha = date.today()
        nombre = f'{detalle}.txt'
        ModelTxt.createConsignment(fecha, detalle, valor)
        ModelPuc.consignmentTable(db, nombre)
        ModelPuc.consignment(db, detalle, valor)
        flash('Consignment was saved successfully')
        return redirect(url_for('index'))
    else:
        flash('there was an error, please check')
        return redirect(url_for('index'))


@app.route('/show_consignment')
def ShowConsignment():
    datos = ModelTxt.showConsignment(db)
    return render_template('show_consignment.html', datos=datos)

# ******************** productos *************************


@app.route('/interface_create_products')
def interfaceCreateProducts():
    return render_template('interface_create_products.html')


@app.route('/create_product', methods=['POST'])
def createProduct():
    if request.method == 'POST':
        nombre = request.form['nombre']
        valor = request.form['valor']
        cantidad = request.form['cantidad']
        file = request.files['file']
        basepath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        nuevo_nombre_file = nombre + extension
        upload_path = os.path.join(basepath, 'static/img_products', nuevo_nombre_file)
        file.save(upload_path)
        producto = Products(nombre, valor, cantidad, imagen=nuevo_nombre_file)
        ModelProducts.insertProduct(db, producto)
        flash('Product was saved successfully')
        return redirect(url_for('index'))
    else:
        flash('there was an error, please check')
        return redirect(url_for('index'))


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>P??gina no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
