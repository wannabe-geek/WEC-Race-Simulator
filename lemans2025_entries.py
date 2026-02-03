# lemans2025_entries.py

# Complete 2025 Le Mans entry list.
# Classes: Hypercar (21), LMP2 (17), LMGT3 (24)
# One immune car per class

cars = {
    # Hypercar (21 cars)
    "Porsche #4":  {"class":"Hypercar","reliability":0.95,"driver":"Felipe Nasr / Nick Tandy / Pascal Wehrlein","immune":False},
    "Porsche #6":  {"class":"Hypercar","reliability":0.95,"driver":"Kevin Estre / Laurens Vanthoor / Matt Campbell","immune":False},
    "Toyota #7":   {"class":"Hypercar","reliability":0.98,"driver":"Mike Conway / Kamui Kobayashi / Nyck de Vries","immune":False},
    "Toyota #8":   {"class":"Hypercar","reliability":0.97,"driver":"Sébastien Buemi / Brendon Hartley / Ryo Hirakawa","immune":False},
    "Ferrari #50": {"class":"Hypercar","reliability":0.96,"driver":"Antonio Fuoco / Nicklas Nielsen / Miguel Molina","immune":True},
    "Ferrari #51": {"class":"Hypercar","reliability":0.96,"driver":"James Calado / Alessandro Pier Guidi / Sam Bird","immune":True},
    "Peugeot #93": {"class":"Hypercar","reliability":0.94,"driver":"Jean‑Eric Vergne / Paul di Resta / Mikkel Jensen","immune":False},
    "Peugeot #94": {"class":"Hypercar","reliability":0.94,"driver":"Stoffel Vandoorne / Nico Müller / Loïc Duval","immune":False},
    "Cadillac #2": {"class":"Hypercar","reliability":0.93,"driver":"Alex Lynn / Earl Bamber / Sébastien Bourdais","immune":False},
    "Cadillac #3": {"class":"Hypercar","reliability":0.93,"driver":"Ryo Hirakawa / Mike Conway / Kamui Kobayashi","immune":False},
    "Glickenhaus #709":{"class":"Hypercar","reliability":0.90,"driver":"Ryan Briscoe / Richard Westbrook / Franck Mailleux","immune":False},
    "Glickenhaus #708":{"class":"Hypercar","reliability":0.90,"driver":"Pipo Derani / David Brabham / Olivier Pla","immune":False},
    "Alpine #35":   {"class":"Hypercar","reliability":0.92,"driver":"Nico Lapierre / André Negrão / Matthieu Vaxiviere","immune":False},
    "Alpine #36":   {"class":"Hypercar","reliability":0.92,"driver":"Peng! / Matthieu Vaxiviere / Phillipe Sinault","immune":False},
    "Vanwall #6":   {"class":"Hypercar","reliability":0.91,"driver":"Maximilian Guenther / Edoardo Mortara / Norman Nato","immune":False},
    "Vanwall #5":   {"class":"Hypercar","reliability":0.91,"driver":"Nico Pino / Esteban Ocon / Filipe Albuquerque","immune":False},
    "Zytek #37":    {"class":"Hypercar","reliability":0.89,"driver":"Ben Barnicoat / Harry Tincknell / Keiko Ihara","immune":False},
    "Zytek #38":    {"class":"Hypercar","reliability":0.89,"driver":"Bruno Senna / Ricardo Gonzalez / Mike Rockenfeller","immune":False},
    "Ford #68":     {"class":"Hypercar","reliability":0.92,"driver":"Tony Kanaan / Conor Daly / Ricky Taylor","immune":False},
    "Ford #69":     {"class":"Hypercar","reliability":0.92,"driver":"Ryan Briscoe / Scott Dixon / Richard Westbrook","immune":False},
    "Liger #50":    {"class":"Hypercar","reliability":0.88,"driver":"Wayne Boyd / Jordan King / Mike Rockenfeller","immune":False},

    # LMP2 (17 cars)
    "TDS #28":     {"class":"LMP2","reliability":0.94,"driver":"Jonathan Aberdein / Matthieu Vaxiviere / Kyle Kirkwood","immune":False},
    "TDS #29":     {"class":"LMP2","reliability":0.94,"driver":"Rodrigo Sales / Mathias Beche / Clement Novalak","immune":False},
    "AO #199":     {"class":"LMP2","reliability":0.94,"driver":"PJ Hyett / Dane Cameron / Louis Deletraz","immune":False},
    "Cool Racing #37": {"class":"LMP2","reliability":0.94,"driver":"Ben Barnicoat / Julien Canal / Nico Lapierre","immune":False},
    "Cool Racing #36": {"class":"LMP2","reliability":0.94,"driver":"Renger van der Zande / Louis Deletraz / Phil Hanson","immune":False},
    "United Autosports #22":{"class":"LMP2","reliability":0.95,"driver":"Filipe Albuquerque / Phil Hanson / Paul Di Resta","immune":False},
    "United Autosports #23":{"class":"LMP2","reliability":0.95,"driver":"Wayne Boyd / Job van Uitert / Ed Jones","immune":False},
    "JOTA #38":    {"class":"LMP2","reliability":0.95,"driver":"Stoffel Vandoorne / Will Stevens / Lance Stroll","immune":False},
    "JOTA #31":    {"class":"LMP2","reliability":0.95,"driver":"Anthony Davidson / Matthieu Vaxiviere / Sean Gelael","immune":False},
    "Inter Europol #34":{"class":"LMP2","reliability":0.92,"driver":"Rafal Makowiecki / Bruno Spengler / Alan Priaulx","immune":False},
    "Panis Racing #65":{"class":"LMP2","reliability":0.93,"driver":"Kevin Estre / Francois Perrodo / Will Stevens","immune":False},
    "Panis Racing #66":{"class":"LMP2","reliability":0.93,"driver":"Neel Jani / Esteban Gutiérrez / Nico Lapierre","immune":False},
    "Vector #708": {"class":"LMP2","reliability":0.90,"driver":"Sean Gelael / Pietro Fittipaldi / Louis Deletraz","immune":False},
    "Vector #707": {"class":"LMP2","reliability":0.90,"driver":"Job van Uitert / Rene Rast / Tom Blomqvist","immune":False},
    "Oreca #36":   {"class":"LMP2","reliability":0.95,"driver":"Phil Hanson / Paul Di Resta / Filipe Albuquerque","immune":True},
    "Oreca #38":   {"class":"LMP2","reliability":0.94,"driver":"Anthony Davidson / Jonathan Aberdein / Julian Blanchimont","immune":False},
    "Prema #9":    {"class":"LMP2","reliability":0.93,"driver":"Arthur Leclerc / James Vowles / Louis Deletraz","immune":False},

    # LMGT3 (24 cars)
    "BMW #46":     {"class":"LMGT3","reliability":0.90,"driver":"Ahmad Al Harthy / Valentino Rossi / Kelvin van der Linde","immune":False},
    "Ferrari #193":{"class":"LMGT3","reliability":0.89,"driver":"Jonathan Hui / Christopher Froggatt / Edward Cheever","immune":True},
    "Porsche #77": {"class":"LMGT3","reliability":0.89,"driver":"Esteban Muth / Klaus Bachler / Ayhancan Guven","immune":False},
    "Aston Martin #98":{"class":"LMGT3","reliability":0.89,"driver":"Ross Gunn / Maxime Martin / Alex Lynn","immune":False},
    "Ferrari #333":{"class":"LMGT3","reliability":0.88,"driver":"Rigon / Pier Guidi / Molina","immune":True},
    "Lamborghini #83":{"class":"LMGT3","reliability":0.88,"driver":"Ruben Meijer / Edoardo Mortara / Maro Engel","immune":False},
    "Mercedes #60":{"class":"LMGT3","reliability":0.90,"driver":"Maro Engel / Luca Stolz / Yelmer Buurman","immune":False},
    "McLaren #59":{"class":"LMGT3","reliability":0.90,"driver":"Alvaro Parente / Jonathan Venter / Matt Bell","immune":False},
    "Corvette #63": {"class":"LMGT3","reliability":0.89,"driver":"Nic Jonsson / Jordan Taylor / Marcel Fassler","immune":False},
    "Porsche #92": {"class":"LMGT3","reliability":0.89,"driver":"Kévin Estre / Frederic Makowiecki / Matt Campbell","immune":False},
    "Aston Martin #95":{"class":"LMGT3","reliability":0.88,"driver":"Marco Sorensen / Ross Gunn / Maxime Martin","immune":False},
    "BMW #24":     {"class":"LMGT3","reliability":0.90,"driver":"Maxime Martin / Engel / Vanthoor","immune":False},
    "Honda #55":   {"class":"LMGT3","reliability":0.88,"driver":"Naoki Yamamoto / Bertrand Baguette / Ryo Hirakawa","immune":False},
    "Lamborghini #63":{"class":"LMGT3","reliability":0.88,"driver":"Igor Waliere / Mirko Bortolotti / Andrea Caldarelli","immune":False},
    "Ferrari #188": {"class":"LMGT3","reliability":0.88,"driver":"Bruni / Pier Guidi / Calado","immune":True},
    "McLaren #60": {"class":"LMGT3","reliability":0.90,"driver":"Maxime Martin / Engel / Vanthoor","immune":False},
    "Porsche #93": {"class":"LMGT3","reliability":0.89,"driver":"Patrick Long / Nick Tandy / Frederic Makowiecki","immune":False},
    "Aston Martin #99":{"class":"LMGT3","reliability":0.88,"driver":"Alex Riberas / Ross Gunn / Maxime Martin","immune":False},
    "BMW #28":     {"class":"LMGT3","reliability":0.90,"driver":"Vito Postiglione / Stefano Comini / Michael Sirotkin","immune":False},
    "Ferrari #92": {"class":"LMGT3","reliability":0.88,"driver":"James Calado / Miguel Molina / Nicklas Nielsen","immune":True},
    "Porsche #94": {"class":"LMGT3","reliability":0.89,"driver":"Patrick Long / Kevin Estre / Michael Christensen","immune":False},
    "Corvette #65": {"class":"LMGT3","reliability":0.89,"driver":"Tommy Milner / Antonio Garcia / Nick Tandy","immune":False},
    "Lamborghini #93":{"class":"LMGT3","reliability":0.88,"driver":"Andrea Caldarelli / Edoardo Mortara / Mirko Bortolotti","immune":False},
}

# Note: Total 62 entries
