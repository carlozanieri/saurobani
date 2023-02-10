#!/usr/bin/env python
#import os
#import time
#import logging
import os
import time
import logging
import MySQLdb
#from tomlkit import datetime
from datetime import datetime
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
import tornado.escape
import smtplib
import codecs
from smtplib import SMTP, SMTPException

# *******
import bcrypt
import concurrent.futures
#import MySQLdb
import markdown
import pymysql
import os.path
import re
import subprocess

import tornado.escape
from datetime import datetime
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import os.path, random, string
from tornado.options import define, options
# *******
from tornado import gen
import pymysql.cursors
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
class Connect:

    define("mysql_host", default="carlozanieri.eu", help="carlozanieri database host")
    define("mysql_database", default="saurobani", help="carlozanieri database name")
    define("mysql_user", default="root", help="carlozanieri database user")
    define("mysql_password", default="@trex39@", help="carlozanieri database password")

    def get(sbarcode):
        barcodes = str(sbarcode)
        print(b"abcde".decode("utf-8"))
        print(bytes(barcodes, "utf-8").decode("utf-8"))

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        #b = bytes(barcodes, "utf-8").decode("utf-8")
        b = "pppp"
        print(b"ppp".decode("utf-8"))
        cursor = db.cursor()
        cursor.execute("SELECT *  from barcode where barcode = %s", b)

        barcode = cursor.fetchone()
       # if not barcode: raise tornado.web.HTTPError()
        #print( str(barcode['barcode']))
        #for centralinos in barcode:
        #print(barcode['nome'])
        return barcode
    def feed(sbarcode):
        import feedparser
        rss = Connect.rss("")
        for rssm in rss:
            d = [feedparser.parse(rssm['link'])]
            for post in d.entries:
                print(post.title + ": " + post.link + "       ")
            return d
    def rss(self):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from feed  order by id asc")

        rss = cursor.fetchall()

        return rss

    def pdf(self):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where id >= 13 and id <= 17 order by id asc")

        pdf = cursor.fetchall()

        return pdf

    def primanota(self, id):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where data='" + id + "'" )

        primanota = cursor.fetchall()
        #primanota = primanota[1]["descrizione"]
        return primanota

    def tab_primanota(self,datada, dataa):
        print(datada)
        print(dataa)
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
       ##### db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
       ##### db = pymysql.connect("carlozanieri.net", "root", "trex39", "prolocogest", cursorclass=pymysql.cursors.DictCursor)
        print(dataa)
        print(datada)
        cursor = db.cursor()

        cursor.execute("SELECT *  from primanota where data >='" + datada + "' and data <='" + dataa + "'" + " order by data")
        ## cursor.execute("SELECT *  from primanota")
        #print(datada, dataa)
        primanota = cursor.fetchall()
        #print(primanota)
        return primanota

    def conta(self, datada,dataa):
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        #db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where data >='" + datada + "' and data <='" + dataa + "'" + " order by data")
        ## cursor.execute("SELECT *  from primanota")
        conta= cursor.rowcount
        #primanota = cursor.fetchall()
        #primanota = primanota[1]["descrizione"]
        print(conta)
        return conta

    def menu(self):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)

        cursor = db.cursor()
        cursor.execute("SELECT *  from menuweb where livello=2")

        rows = cursor.fetchall()
        menu = [dict(id=row[0], codice=row[1],radice=row[2], titolo=row[4], link=row[6]) for row in rows]
        #menu = primanota[1]["descrizione"]
        return menu

    def submenu(self, menu):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from menuweb where livello=3 and radice = '" + menu + "'")

        submenu = cursor.fetchall()
        #menu = primanota[1]["descrizione"]
        return submenu
    def submnu(self):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from menuweb where livello=3 ")

        rows = cursor.fetchall()
        submenu = [dict(id=row[0], codice=row[1],radice=row[2], titolo=row[4], link=row[6]) for row in rows]
        return submenu
    def submnu2(self):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from menuweb where livello=4 ")

        rows = cursor.fetchall()
        submenu2 = [dict(id=row[0], radice=row[2], titolo=row[4], link=row[6]) for row in rows]
        return submenu2
    def body(self, pagina):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from entries where slug = '" + pagina + "'")

        body = cursor.fetchone()
        #menu = primanota[1]["descrizione"]
        return body
    def slider(self, luogo):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from slider where codice = '" + luogo + "'")
        ##cursor.execute("SELECT *  from slider")
        slider = cursor.fetchall()
        #menu = primanota[1]["descrizione"]
        return slider

    def news(self):
        data =datetime.now()
        #data = "2021-06-08 00:00:00"
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        ##cursor.execute("SELECT *  from news where published <= '" + str(data) + "'")
        cursor.execute("SELECT *  from news")
        ##cursor.execute("SELECT *  from slider")
        rows = cursor.fetchall()
        news = [dict(id=row[0], title=row[2], dir=row[8], img=row[7], html=row[4], html2=row[9], date=row[6]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return news

    def blog(self):
        data =datetime.now()
        #data = "2021-06-08 00:00:00"
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        ##cursor.execute("SELECT *  from blog where published <= '" + str(data) + "'")
        cursor.execute("SELECT *  from blog")
        ##cursor.execute("SELECT *  from slider")
        rows = cursor.fetchall()
        blogs = [dict(id=row[0], title=row[2], dir=row[8], img=row[7], html=row[4], html2=row[9],date=row[6]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return blogs
    
    def blogs_one(self, titolo, id):
        #data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data = "2021-06-08 00:00:00"
        ##titolo=titolo
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(titolo)
        cursor = db.cursor()
        ####cursor.execute("SELECT *  from blog where id = 3")
        cursor.execute("SELECT *  from blog where id = '" + id + "'")
        ##cursor.execute("SELECT *  from slider")
        ##news = cursor.fetchall()
        rows = cursor.fetchall()
        blogs = [dict(id=row[0], title=row[3], dir=row[9], img=row[7], html=row[4], date=row[6]) for row in rows]
        return blogs
    
    def news_one(self, titolo, id):
        #data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data = "2021-06-08 00:00:00"
        ##titolo=titolo
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(titolo)
        cursor = db.cursor()
        ####cursor.execute("SELECT *  from news where id = 3")
        cursor.execute("SELECT *  from news where id = '" + id + "'")
        ##cursor.execute("SELECT *  from slider")
        ##news = cursor.fetchall()
        rows = cursor.fetchall()
        news = [dict(id=row[0], title=row[3], dir=row[9], img=row[7], html=row[5], date=row[6]) for row in rows]
        return news

    def manifesta(self):
        data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data="2021-06-08 00:00:00"
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from manifestazioni where published >= '" + data + "'")
        ##cursor.execute("SELECT *  from slider")
        rows = cursor.fetchall()
        manifesta = [dict(id=row[0], title=row[3], html=row[5], date=row[6], dir=row[9], img=row[8]) for row in rows]
        return manifesta

    def manifesta_one(self, titolo, id):
        data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data = "2021-06-08 00:00:00"
        ##titolo=titolo
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(titolo)
        cursor = db.cursor()
        ####cursor.execute("SELECT *  from news where id = 3")
        cursor.execute("SELECT *  from manifestazioni where id = '" + id + "'")
        ##cursor.execute("SELECT *  from slider")
        rows = cursor.fetchall()
        manifesta = [dict(id=row[0], title=row[3], dir=row[9], img=row[8], html=row[5], date=row[6]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return manifesta

    def ins_manifesta(self, dir, file, titolo, descrizione):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        mycursor = db.cursor()
        data=str(datetime.now())
        riga="INSERT INTO manifestazioni (id,author_id,title, markdown, html, img, dir, html2, html3, img2,img3) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
        valori = (0,2,titolo,descrizione,descrizione,file,dir,'html2','html3','img2','img3')
        mycursor.execute(riga, valori)
        args = (data, data)
        #mycursor.execute(insertQuery)
  
        print("No of Record Inserted :", mycursor.rowcount)
  
        # we can use the id to refer to that row later.
        print("Inserted Id :", mycursor.lastrowid)
  
        # To ensure the Data Insertion, commit database.
        db.commit() 
  
        # close the Connection
        db.close()
    
    def ins_news(self, dir, file, titolo, descrizione, tipo):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        mycursor = db.cursor()
        data=str(datetime.now())
        riga="INSERT INTO news (id,author_id,title, markdown, html, img, dir, html2, html3, img2,img3) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
        valori = (0,2,titolo,descrizione,descrizione,file,dir,'html2','html3','img2','img3')
        mycursor.execute(riga, valori)
        args = (data, data)
        #mycursor.execute(insertQuery)
  
        print("No of Record Inserted :", mycursor.rowcount)
  
        # we can use the id to refer to that row later.
        print("Inserted Id :", mycursor.lastrowid)
  
        # To ensure the Data Insertion, commit database.
        db.commit() 
  
        # close the Connection
        db.close()
    
    def get_class(kls):
        parts = kls.split('.')
        function = ".".join(parts[:-1])
        m = __import__(function)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m
    
    def get_class(kls):
        parts = kls.split('.')
        function = ".".join(parts[:-1])
        m = __import__(function)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m



        # read image as grey scale
        img = cv2.imread('D:/image-1.png')

        # do some transformations on img

        # save matrix/array as image file
        isWritten = cv2.imwrite('D:/image-2.png', img)

        if isWritten:
            print('Image is successfully saved as file.')