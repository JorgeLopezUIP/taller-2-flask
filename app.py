from flask import Flask, jsonify
from conexion import obtener_conexion
import pymysql.cursors

app = Flask(__name__)

@app.route("/", methods=["GET"])
def mostar_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()

    return jsonify(tablas)

if __name__ == "__main__":
    app.run(debug=True)

