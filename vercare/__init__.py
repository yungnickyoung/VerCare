from __future__ import print_function
import os
import sys
from flask import Flask, render_template, request, redirect
from . import db
import sqlite3


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'vercare.sqlite'),
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def baseSite():
        return redirect('/home')

    @app.route('/home')
    def home():
        return render_template('home.html', title='Home')

    @app.route('/search')
    def search():
        drgCode = request.args.get('drgCode')
        searchLoc = request.args.get('searchLoc')

        database = db.get_db()
        c = database.cursor()

        c.execute('SELECT * FROM drg_list WHERE DRG=?', (drgCode,))

        list_of_rows = c.fetchall()

        table_info = []
        min_price_appd = 9999999999999
        min_price_care = 9999999999999
        min_price_appd_name = ''
        min_price_care_name = ''
        max_price_appd = -5
        max_price_care = -5
        max_price_appd_name = ''
        max_price_care_name = ''

        for row in list_of_rows:
            hospital_name = row[1]
            avg_total_case = row[2]
            avg_care_case = row[3]
            hospital_id = row[4]

            c.execute('SELECT * FROM hospital_list WHERE hospital_id=?', (hospital_id,))
            hospital_info = c.fetchone()

            hospital_phone_number = hospital_info[2]
            hospital_city = hospital_info[3]
            hospital_state = hospital_info[4]

            avg_total_case_f = float(avg_total_case)
            avg_care_case_f = float(avg_care_case)

            # Fix Shands
            if (hospital_name == 'ShandsGaines'):
                hospital_name = "Shands Hospital"

            # Make the phone number pretty
            phone_number = '(' + str(hospital_phone_number)[0:3] + ') ' + str(hospital_phone_number)[3:6] + '-' + str(hospital_phone_number)[6:10]
            if len(str(hospital_phone_number)) > 10:
                phone_number += " ext. " + str(hospital_phone_number)[10:]

            # Update min appd
            if avg_total_case_f < min_price_appd:
                min_price_appd = avg_total_case_f
                min_price_appd_name = hospital_name

            # Update min medicare
            if avg_care_case_f < min_price_care:
                min_price_care = avg_care_case_f
                min_price_care_name = hospital_name

            # Update max appd
            if avg_total_case_f > max_price_appd:
                max_price_appd = avg_total_case_f
                max_price_appd_name = hospital_name

            # Update max medicare
            if avg_care_case_f > max_price_care:
                max_price_care = avg_care_case_f
                max_price_care_name = hospital_name
            
            print(row)
            print("print(min_price_appd)")
            print(min_price_appd)
            print("min_price_appd_name")
            print(min_price_appd_name)
            print("max_price_appd")
            print(max_price_appd)
            print("max_price_care")
            print(max_price_care)
            print("max_price_care_name")
            print(max_price_care_name)

            #TODO: CHECK IF VALUE IS ERROR CODE LIKE -2

            avg_total_case = '$' + avg_total_case
            avg_care_case = '$' + avg_care_case



            table_row = { 'hospital':hospital_name, 'appd':avg_total_case, 'appdcare':avg_care_case, 'city':hospital_city, 'state':hospital_state, 'phone':phone_number }
            table_info.append(table_row)


        database.commit()
        database.close()

        return render_template('search.html', title='Search', drgCode=drgCode, searchLoc=searchLoc, table_info=table_info, min_appd=min_price_appd_name,
                                max_appd=max_price_appd_name, min_care=min_price_care_name, max_care=max_price_care_name)

    @app.route('/drg-list')
    def drgList():
        results_list = []
        with open('static/drg_desc_final.txt') as f:
            f.readline()
            for line in f:
                line = line.split(';')

                drg = str(line[0]).zfill(3)
                desc = line[1].capitalize()

                result = {'drg':drg, 'desc':desc }
                results_list.append(result)

        return render_template('drg-list.html', title='DRG List', table_info=results_list)
        

    @app.route('/keywords')
    def keywords():
        keywords = request.args.get('keywords').split()
        results_list = []

        if keywords:
            # Search table of DRG/Descriptions for descriptions containing keywords
            with open('static/drg_desc_final.txt') as f:
                f.readline()
                for line in f:
                    contains_keywords = True

                    line = line.split(';')
                    drg = str(line[0]).zfill(3)
                    desc = line[1].capitalize()

                    for word in keywords:
                        if word not in line[1]:
                            contains_keywords = False

                    if contains_keywords:
                        result = {'drg':drg, 'desc':desc }
                        results_list.append(result)
        return render_template('keywords.html', table_info=results_list)

    database = db.get_db()
    c = database.cursor()
    # with open('static/verCareDB.db.sql') as f:
    #     c.executescript(f.read().decode('utf8'))

    database.commit()
    
    database.close()

    return app