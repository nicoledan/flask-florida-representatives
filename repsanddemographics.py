from flask import Flask, render_template, redirect, url_for
from datasets import DISTRICTS
from repdata import REPS
app = Flask(__name__)

# web host requires application in passenger_wsgi
application = app

#from repdata.py
def get_districts_reps_and_parties (source):
    districts_reps_and_parties=[]
    for row in source:
            district = row["district"]
            rep = row["name"]
            party = row["party"]
            districts_reps_and_parties.append([district, rep, party])
    return districts_reps_and_parties

#from datasets.py

#def get_ids_and_districts (source):
    #ids_and_districts = []
    #for row in source:
        #id = row["id"]
        #district = row["district"]
        #ids_and_districts.append([id, district])
    #return ids_and_districts


@app.route('/')
@app.route('/index/')
def index():
    districts_reps_and_parties = get_districts_reps_and_parties(REPS)
    return render_template('index.html', pairs=districts_reps_and_parties)


@app.route('/detail/<district>')

def detail(district):
    DISTRICTS[district]
    district = district
    total_citizens = DISTRICTS[district][1]
    eighteen_twentynine = DISTRICTS[district][2]
    thirty_fortyfour = DISTRICTS[district][3]
    fortyfive_sixtyfour = DISTRICTS[district][4]
    sixtyfive_over = DISTRICTS[district][5]
    districts_reps_and_parties = get_districts_reps_and_parties(REPS)
    return render_template ('detail.html', district = district, eighteen_twentynine = eighteen_twentynine, thirty_fortyfour = thirty_fortyfour, fortyfive_sixtyfour = fortyfive_sixtyfour, sixtyfive_over = sixtyfive_over)
    #id, district, total_citizens, eighteen_twentynine, thirty_fortyfour, fortyfive_sixtyfour, sixtyfive_over = get_demographicdata(DEMOGRAPHICS,id)
    #return render_template('detail.html', district = district, total_citizens = total_citizens, eighteen_twentynine = eighteen_twentynine, thirty_fortyfour = thirty_fortyfour, fortyfive_sixtyfour = fortyfive_sixtyfour, sixtyfive_over = sixtyfive_over )

if __name__ == '__main__':
    app.run(debug=True)
