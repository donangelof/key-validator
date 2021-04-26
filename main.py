import io
import os
from time import sleep
import sqlite3
from sqlite3 import Error
import mysql.connector
from mysql.connector.constants import ClientFlag
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import subprocess
import smtplib


logo = 'C:\\ISolution\\Logo.jpg'
icon = 'C:\\ISolution\\icon.ico'
logoCliente = 'C:\\ISolution\\Logo.jpg'
caminhoDB = 'C:\\ISolution\\Database\\storage.db'
nomechave = 'C:\\ISolution\\chave.txt'


def credencial():
    with open(nomechave, 'r', encoding='utf8') as f:
        keyname = f.read()
    

    config = {
    'user': 'user',
    'password': 'password',
    'host': 'host',
    'database': 'database',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

    conn = mysql.connector.connect(**config)
    c = conn.cursor(buffered=True)

    result = c.execute('SELECT MAX(id) from tb_keys')
    if result == None:
        nextID = 1
    else:
        for row in result:
            id = row[0]
        nextID = int(id) + 1
    sql = "SELECT * FROM tb_keys WHERE name = %s"
    c.execute(sql, (keyname, ))
    myresult = c.fetchall()
    try:
        for row in myresult:
            l2 = row[3]
            l3 = row[6]
        conn.commit()
        if l3 == 1:
            Menus()
        else:
            tkinter.messagebox.showerror('', 'Sua licença EXPIROU, renove para voltar a acessar oo sistema.')
    except:
        tkinter.messagebox.showerror('', 'Chave inválida')

credencial()