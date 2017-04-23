from flask import Flask, render_template, redirect, url_for
from datasets import DISTRICTS
from repdata import REPS
app = Flask(__name__)

# web host requires application in passenger_wsgi
application = app

#from repdata.py
def get_districts_reps_and_parties (source):
    districts_reps_and_parties =[]
    for row in source:
            district = row["district"]
            rep = row["name"]
            party = row["party"]
            return districts_reps_and_parties

#from datasets.py

def get_ids_and_districts (source):
    ids_and_districts = []
    for row in source:
        id = row["id"]
        district = row["district"]
        ids_and_districts.append([id, district])
    return ids_and_districts


@app.route('/')
@app.route('/index/')
def index():
    ids_and_districts = get_ids_and_districts (DEMOGRAPHICS)
    return render_template('index.html', pairs=ids_and_districts)


@app.route('/detail/<district>)

def detail(district):
    DISTRICTS[district]
    eighteen_twentynine = DISTRICTS[district][1]
    thirty_fortyfour = DISTRICTS[district][2]
    fortyfive_sixtyfour = DISTRICTS[district][3]
    sixtyfive_over = DISTRICTS[district][4]
    return render_template ('detail.html', eighteen_twentynine = eighteen_twentynine, thirty_fortyfour = thirty_fortyfour, fortyfive_sixtyfour = fortyfive_sixtyfour, sixtyfive_over = sixtyfive_over)
    #id, district, total_citizens, eighteen_twentynine, thirty_fortyfour, fortyfive_sixtyfour, sixtyfive_over = get_demographicdata(DEMOGRAPHICS,id)
    #return render_template('detail.html', district = district, total_citizens = total_citizens, eighteen_twentynine = eighteen_twentynine, thirty_fortyfour = thirty_fortyfour, fortyfive_sixtyfour = fortyfive_sixtyfour, sixtyfive_over = sixtyfive_over )

if __name__ == '__main__':
    app.run(debug=True)
