# -*- coding: utf-8 -*-
# Auteur : Lucas Stil
# Long vît à Lateb

from __future__ import print_function
import barcode
import os
import configparser
import sqlalchemy
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

def create_empty_config():
    config = open('./config.cfg', "w")
    config.write("[Server]\nhost = localhost\nport = 3306\ndatabase = membres\n\n[Login]\nuser = AzureDiamond \npassword = hunter2\n")

def picture_gen(row):
    photo_name = "./photos/" + row['EMAIL'] + '.jpg'
    if not (os.path.isfile(photo_name)):
        return
    code = barcode.codex.Code39(row['CARD'],
                                add_checksum=False,
                                writer=ImageWriter())
    barcode_pic = Image.open(code.save('barcode_temp'))
    photo = Image.open(photo_name)
    photo = photo.resize([210, 270])
    logo = Image.open('logo.jpg')
    barcode_pic = barcode_pic.resize([960, 150])
    final_pic = Image.new("RGB", [975, 624], "white")
    final_pic.paste(logo, (366, 63))
    final_pic.paste(photo, (66, 60))
    final_pic.paste(barcode_pic, (0, 450))
    draw = ImageDraw.Draw(final_pic)
    font_obj = ImageFont.truetype("typo.ttf", 42)
    draw.text((366, 303), row['FIRSTNAME'],
              font=font_obj,
              fill="black")
    draw.text((366, 357), row['LASTNAME'],
              font=font_obj, fill="black")
    font_obj = ImageFont.truetype("typo.ttf", 8*3)
    draw.rectangle([(0, 570), (975, 630)], fill="white")
    draw.text((750, 414), u"2013/2014", font=font_obj,
              fill="black")
    file_name = "./result/" + row['SEARCHKEY'] + '.jpg'
    final_pic.save(file_name)

# Initialisation du fichier de config
CONFIG = configparser.RawConfigParser()
CONFIG.read('./config.cfg')

# Récupération des variables depuis la configuration
try:
    HOST = CONFIG.get('Server', 'host')
    PORT = CONFIG.get('Server', 'port')
    DATABASE = CONFIG.get('Server', 'database')
    LOGIN = CONFIG.get('Login', 'user')
    PASS = CONFIG.get('Login', 'password')
except:
    print("Il n'y a pas de fichier de configuration !")
    create_empty_config()
    print("Fichier de configuration créé ! Merci d'aller l'éditer.")
    exit(0)

mysql_addr = "mysql+oursql://" + LOGIN + ":" + PASS + "@" + HOST + ":" + PORT + "/" + DATABASE
engine = sqlalchemy.create_engine(mysql_addr,
                                  convert_unicode=True)
try:
    connection = engine.connect()
except:
    print("Problème de connexion à la base de données.")
    exit(1)
result = connection.execute("select NAME, FIRSTNAME, LASTNAME, SEARCHKEY, CARD, EMAIL from CUSTOMERS WHERE EMAIL IS NOT NULL")
for row in result:
    picture_gen(row)
connection.close()
