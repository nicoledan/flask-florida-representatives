from flask import Flask, render_template, redirect, url_for
from datasets import DISTRICTS
from repdata import REPS
from pfdata import POLITIFACT
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

def get_rep_name (source, district):
    for row in source:
        if district == str( row["district"] ):
            name = row["name"]
            district = str(district)
    return name, district

def get_rep_party (source, district):
    for row in source:
        if district == str( row["district"] ):
            party = row["party"]
            district = str(district)
    return party, district

def get_pfdata (source, district):
    for row in source:
        if district == str( row["district"] ):
            true_statement = row["TRUE"]
            mostly_true = row["mostly true"]
            half_true = row["half true"]
            mostly_false = row["mostly false"]
            false_statement = row["FALSE"]
            pants_on_fire = row["pants on fire"]
            district = str(district)
    return true_statement, mostly_true, half_true, mostly_false, false_statement, pants_on_fire, district

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


@app.route('/detail/<district>.html')

def detail(district):
    DISTRICTS[district]
    district = district
    total_citizens = DISTRICTS[district][1]
    eighteen_twentynine = DISTRICTS[district][2]
    thirty_fortyfour = DISTRICTS[district][3]
    fortyfive_sixtyfour = DISTRICTS[district][4]
    sixtyfive_over = DISTRICTS[district][5]
    male = DISTRICTS[district][6]
    female = DISTRICTS[district][7]
    white = DISTRICTS[district][8]
    black = DISTRICTS[district][9]
    american_indian = DISTRICTS[district][10]
    asian = DISTRICTS[district][11]
    native_hawaiian = DISTRICTS[district][12]
    some_other_race= DISTRICTS[district][13]
    two_or_more = DISTRICTS[district][14]
    hispanic_or_latino = DISTRICTS[district][15]
    not_hispanic_or_latino = DISTRICTS[district][16]
    white_not_hispanic_or_latino = DISTRICTS[district][17]
    bachelors_degree = DISTRICTS[district][19]
    poverty_level = DISTRICTS[district][21]
    over_100k = DISTRICTS[district][23]
    name, district = get_rep_name(REPS, district)
    party, district = get_rep_party(REPS, district)
    true_statement, mostly_true, half_true, mostly_false, false_statement, pants_on_fire, district = get_pfdata(POLITIFACT, district)
    return render_template ('detail.html', name=name, party=party, district = district, total_citizens=total_citizens, eighteen_twentynine = eighteen_twentynine,
    thirty_fortyfour = thirty_fortyfour, fortyfive_sixtyfour = fortyfive_sixtyfour, sixtyfive_over = sixtyfive_over,
    male=male, female=female, white=white, black=black, american_indian=american_indian, asian=asian, native_hawaiian=native_hawaiian, some_other_race=some_other_race,
    two_or_more=two_or_more, hispanic_or_latino=hispanic_or_latino, not_hispanic_or_latino=not_hispanic_or_latino, white_not_hispanic_or_latino=white_not_hispanic_or_latino,
    bachelors_degree=bachelors_degree, poverty_level=poverty_level, over_100k=over_100k,
    true_statement=true_statement, mostly_true=mostly_true, half_true=half_true, mostly_false=mostly_false, false_statement=false_statement, pants_on_fire=pants_on_fire)
    #id, district, total_citizens, eighteen_twentynine, thirty_fortyfour, fortyfive_sixtyfour, sixtyfive_over = get_demographicdata(DEMOGRAPHICS,id)
    #return render_template('detail.html', district = district, total_citizens = total_citizens, eighteen_twentynine = eighteen_twentynine, thirty_fortyfour = thirty_fortyfour, fortyfive_sixtyfour = fortyfive_sixtyfour, sixtyfive_over = sixtyfive_over )

if __name__ == '__main__':
    app.run(debug=True)
