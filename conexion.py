import pymysql 
import os
from dotenv import load_dotenv

load_dotenv()

conexion = pymysql.connect(
    host=os.getenv("DB_HOST"), 
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="taller-2",
    cursorclass=pymysql.cursors.DictCursor
)


def obtener_conexion(): 
    return conexion