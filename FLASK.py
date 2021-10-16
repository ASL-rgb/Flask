import random

from flask import Flask, url_for, redirect, request, render_template, make_response
import pandas as pd
import os, requests
#Man muss noch eine Implementierung vornehmen für die Iritation durch die optionalen multiblen Datenunterordner wie bei z.B Frankreich
app = Flask(__name__)
@app.route("/admin")
def admin():
    return redirect(url_for("gobuster", name=", Admin Missing"))

@app.route("/WhatDoYouLookingFor")
def WhatDoYouLookingFor():
    return render_template("mainpage.html")

@app.route("/<name>")
def gobuster(name):
    return f"Hello {name}"

@app.route("/country")
def country():
    resp = make_response(render_template("firstPage.html"))
    resp.set_cookie("auth_cookie", random.randbytes(32))
    return resp

@app.route("/")
def index():
    return redirect(url_for("country"))

@app.route("/home")
def indexo():
    return redirect(url_for("country"))

@app.route("/person")
def person():
    return render_template("mainpage.html")

@app.route("/select_country", methods=['POST'])
def select_country():
    global Countrysearch
    if request.method == "POST":
        Countrysearch = request.form["Country"]
        Countrysearch = Countrysearch.upper()
        resp = make_response(render_template("mainpage.html", Countrysearch=Countrysearch))
        resp.set_cookie("Country", Countrysearch)
        return resp
@app.route("/search/<string:Countrysearch>", methods=['POST', 'GET'])
def search(Countrysearch):
    print(Countrysearch)
    if request.method == 'POST':
        Vorname = request.form["Vorname"]
        Nachname = request.form["Nachname"]
        Country_Cookie = request.cookies.get("Country")
        Countrylist = os.listdir(fr"C:\Users\Blick\PycharmProjects\pythonProject1\Database\{Country_Cookie}")
        try:
            Telefonnummer = request.form["Telefonnummer"]


        except FileNotFoundError:
            Telefonnummer = ""
            return panda(Vorname, Nachname, Telefonnummer=Telefonnummer, *Countrylist)
        return panda(Vorname, Nachname, Telefonnummer=Telefonnummer, *Countrylist)

    elif request.method == "GET":
        Vorname = request.args.get("Vorname")
        Nachname = request.args.get("Nachname")
        Countrylist = os.listdir(fr"C:\Users\Blick\PycharmProjects\pythonProject1\Database\{Countrysearch}")
        try:
            Telefonnummer = request.args.get("Telefonnummer")


        except FileNotFoundError:
            Telefonnummer = ""
            return panda(Vorname, Nachname, *Countrylist, Telefonnummer=Telefonnummer)
        return panda(Vorname, Nachname, *Countrylist, Telefonnummer=Telefonnummer)
    else:
        render_template("firstpage.html")

def rubber(Data):
    string = ""
    Stringsheet = []
    Numbersheet = []
    for i in Data:
        if i == float or int:
            Numbersheet.append(i)
        elif string == " ":
            Stringsheet += string
            string = ""
        else:
            string += i
    if Numbersheet:
        print(Numbersheet)
        return Numbersheet
    elif Stringsheet:
        print(Stringsheet)
        if Stringsheet == "NaN":
            Stringsheet = "Empty"
            return Stringsheet
        return Stringsheet

    else:
        return ""
def panda(Vorname, Nachname, *Countrylist, Telefonnummer):
    count = len(Countrylist)
    pd.set_option('display.max_columns', None)
    if count == 1:
        Country_Cookie = request.cookies.get("Country")
        df = pd.read_table(fr"C:\Users\Blick\PycharmProjects\pythonProject1\Database\{Country_Cookie}\{Countrylist[0]}", error_bad_lines=False)
        if Vorname and Nachname != "":
            Prename = df["Vorname"] == Vorname
            Surname = df["Nachname"] == Nachname
            Credsearch =df[Prename & Surname]

            if Credsearch.empty:
                NotEmty = True
            else:
                NotEmty = False
            if NotEmty:
                Datenliste = df.loc[Prename & Surname]
                print(Datenliste)
                Index = Datenliste.index
                if len(Index) > 1:
                    i = 0
                    while i != len(Index):

                        DataPre = Index[i],["Vorname"]
                        String_Pre = str(DataPre)
                        Select_Pre = String_Pre.split("\n")
                        Edited_Pre = rubber(Select_Pre[i])

                        DataLast = Index[i],["Nachname"]
                        String_Sur = str(DataLast)
                        Select_Sur = String_Sur.split("\n")
                        Edited_Sur = rubber(Select_Sur[i])

                        DataTel = Index[i],["Telefonnummer"]
                        String_Tel = str(DataTel)
                        Select_Tel = String_Tel.strip("\n")
                        Edited_Tel = rubber(Select_Tel[i])

                        DataFBID = Index[i],["FacebookID"]
                        String_FBID = str(DataFBID)
                        Select_FBID = String_FBID.strip("\n")
                        Edited_FBI = rubber(Select_FBID[i])

                        DataSex = Index[i],["Geschlecht"]
                        String_Sex = str(DataSex)
                        Select_Sex = String_Sex.strip("\n")
                        Edited_Sex = rubber(Select_Sex[i])

                        DataLive = Index[i],["Wohnort"]
                        String_Live = str(DataLive)
                        Select_Live = String_Live.strip("\n")
                        Edited_Live = rubber(Select_Live[i])

                        DataCountry = Index[i],["Land"]
                        String_Country = str(DataCountry)
                        Select_Country = String_Country.strip("\n")
                        Edited_Country = rubber(Select_Country[i])

                        DataLove = Index[i],["Beziehungsstatus"]
                        String_Love = str(DataLove)
                        Select_Love = String_Love.strip("\n")
                        Edited_Love = rubber(Select_Love[i])

                        DataWork = Index[i],["Beruf"]
                        String_Work = str(DataWork)
                        Select_Work = String_Work.strip("\n")
                        Edited_Work = rubber(Select_Work[i])

                        DataInfo = Index[i],["Info"]
                        String_Info = str(DataInfo)
                        Select_Info = String_Info.strip("\n")
                        Edited_Info = rubber(Select_Info[i])

                        DataBirth = Index[i],["Geburtstag"]
                        String_Birth = str(DataBirth)
                        Select_Birth = String_Birth.strip("\n")
                        Edited_Birth = rubber(Select_Birth[i])

                        DataMail = Index[i],["E-Mail"]
                        String_Mail = str(DataMail)
                        Select_Mail = String_Mail.strip("\n")
                        Edited_Mail = rubber(Select_Mail[i])

                        return render_template("results.html", Data="Data Found!", DataPre=Edited_Pre,
                                               DataLast=Edited_Sur,
                                               DataTel=Edited_Tel,
                                               DataFBID=Edited_FBI, DataSex=Edited_Sex, DataLive=Edited_Live,
                                               DataCountry=Edited_Country, DataLove=Edited_Love,
                                               DataWork=Edited_Work, DataInfo=Edited_Info, DataBirth=Edited_Birth,
                                               DataMail=Edited_Mail)
                elif len(Datenliste.index) == 1:

                    DataPre = rubber(Datenliste["Vorname"])
                    DataLast = rubber(Datenliste["Nachname"])
                    DataTel = rubber(Datenliste["Telefonnummer"])
                    DataFBID = rubber(Datenliste["FacebookID"])
                    DataSex = rubber(Datenliste["Geschlecht"])
                    DataLive = rubber(Datenliste["Wohnort"])
                    DataCountry = rubber(Datenliste["Land"])
                    DataLove = rubber(Datenliste["Beziehungsstatus"])
                    DataWork = rubber(Datenliste["Beruf"])
                    DataInfo = rubber(Datenliste["Info"])
                    DataBirth = rubber(Datenliste["Geburtstag"])
                    DataMail = rubber(Datenliste["E-Mail"])
                    print(DataTel + "works as it should")

                    return render_template("results.html", Data="Data Found!", DataPre=DataPre,
                                           DataLast=DataLast,
                                           DataTel=DataTel,
                                           DataFBID=DataFBID, DataSex=DataSex, DataLive=DataLive,
                                           DataCountry=DataCountry, DataLove=DataLove,
                                           DataWork=DataWork, DataInfo=DataInfo, DataBirth=DataBirth,
                                           DataMail=DataMail)


            else:
                return render_template("results.html", Data="No Valid Data found!")


        elif Telefonnummer != "":
            Credsearch = df["Telefonnummer"] == Telefonnummer
            if Credsearch.empty:
                NotEmty = True
            else:
                NotEmty = False
            if NotEmty:
                Datenliste = df.loc[Credsearch]
                Index = Datenliste.index
                if len(Index) > 1:
                    i = 0
                    while i != len(Index):
                        DataPre = Index[i], ["Vorname"]
                        String_Pre = str(DataPre)
                        Select_Pre = String_Pre.split("\n")
                        Edited_Pre = rubber(Select_Pre[i])

                        DataLast = Index[i], ["Nachname"]
                        String_Sur = str(DataLast)
                        Select_Sur = String_Sur.split("\n")
                        Edited_Sur = rubber(Select_Sur[i])

                        DataTel = Index[i], ["Telefonnummer"]
                        String_Tel = str(DataTel)
                        Select_Tel = String_Tel.strip("\n")
                        Edited_Tel = rubber(Select_Tel[i])

                        DataFBID = Index[i], ["FacebookID"]
                        String_FBID = str(DataFBID)
                        Select_FBID = String_FBID.strip("\n")
                        Edited_FBI = rubber(Select_FBID[i])

                        DataSex = Index[i], ["Geschlecht"]
                        String_Sex = str(DataSex)
                        Select_Sex = String_Sex.strip("\n")
                        Edited_Sex = rubber(Select_Sex[i])

                        DataLive = Index[i], ["Wohnort"]
                        String_Live = str(DataLive)
                        Select_Live = String_Live.strip("\n")
                        Edited_Live = rubber(Select_Live[i])

                        DataCountry = Index[i], ["Land"]
                        String_Country = str(DataCountry)
                        Select_Country = String_Country.strip("\n")
                        Edited_Country = rubber(Select_Country[i])

                        DataLove = Index[i], ["Beziehungsstatus"]
                        String_Love = str(DataLove)
                        Select_Love = String_Love.strip("\n")
                        Edited_Love = rubber(Select_Love[i])

                        DataWork = Index[i], ["Beruf"]
                        String_Work = str(DataWork)
                        Select_Work = String_Work.strip("\n")
                        Edited_Work = rubber(Select_Work[i])

                        DataInfo = Index[i], ["Info"]
                        String_Info = str(DataInfo)
                        Select_Info = String_Info.strip("\n")
                        Edited_Info = rubber(Select_Info[i])

                        DataBirth = Index[i], ["Geburtstag"]
                        String_Birth = str(DataBirth)
                        Select_Birth = String_Birth.strip("\n")
                        Edited_Birth = rubber(Select_Birth[i])

                        DataMail = Index[i], ["E-Mail"]
                        String_Mail = str(DataMail)
                        Select_Mail = String_Mail.strip("\n")
                        Edited_Mail = rubber(Select_Mail[i])

                        return render_template("results.html", Data="Data Found!", DataPre=Edited_Pre,
                                               DataLast=Edited_Sur,
                                               DataTel=Edited_Tel,
                                               DataFBID=Edited_FBI, DataSex=Edited_Sex, DataLive=Edited_Live,
                                               DataCountry=Edited_Country, DataLove=Edited_Love,
                                               DataWork=Edited_Work, DataInfo=Edited_Info, DataBirth=Edited_Birth,
                                               DataMail=Edited_Mail)



            else:
                return render_template("results.html", Data="No Valid Data found!")



        else:
            return render_template("results.html", Data="Please provide Credentials")

    elif count != 1:
        for file in Countrylist:
            counter = 0
            Country_Cookie = request.cookies.get("Country")
            df = pd.read_table(fr"C:\Users\Blick\PycharmProjects\pythonProject1\Database\{Country_Cookie}\{file}")
            try:
                if Vorname and Nachname != "":
                    Prename = df["Vorname"] == Vorname
                    Surname = df["Nachname"] == Nachname
                    Credsearch = df[Prename & Surname]
                    if Credsearch.empty:
                        NotEmty = True
                    else:
                        NotEmty = False
                    if NotEmty:
                        Datenliste = df.loc[Prename & Surname]

                        Index = Datenliste.index
                        if len(Index) > 1:
                            i = 0
                            while i != len(Index):
                                DataPre = Index[i], ["Vorname"]
                                String_Pre = str(DataPre)
                                Select_Pre = String_Pre.split("\n")
                                Edited_Pre = rubber(Select_Pre[i])

                                DataLast = Index[i], ["Nachname"]
                                String_Sur = str(DataLast)
                                Select_Sur = String_Sur.split("\n")
                                Edited_Sur = rubber(Select_Sur[i])

                                DataTel = Index[i], ["Telefonnummer"]
                                String_Tel = str(DataTel)
                                Select_Tel = String_Tel.strip("\n")
                                Edited_Tel = rubber(Select_Tel[i])

                                DataFBID = Index[i], ["FacebookID"]
                                String_FBID = str(DataFBID)
                                Select_FBID = String_FBID.strip("\n")
                                Edited_FBI = rubber(Select_FBID[i])

                                DataSex = Index[i], ["Geschlecht"]
                                String_Sex = str(DataSex)
                                Select_Sex = String_Sex.strip("\n")
                                Edited_Sex = rubber(Select_Sex[i])

                                DataLive = Index[i], ["Wohnort"]
                                String_Live = str(DataLive)
                                Select_Live = String_Live.strip("\n")
                                Edited_Live = rubber(Select_Live[i])

                                DataCountry = Index[i], ["Land"]
                                String_Country = str(DataCountry)
                                Select_Country = String_Country.strip("\n")
                                Edited_Country = rubber(Select_Country[i])

                                DataLove = Index[i], ["Beziehungsstatus"]
                                String_Love = str(DataLove)
                                Select_Love = String_Love.strip("\n")
                                Edited_Love = rubber(Select_Love[i])

                                DataWork = Index[i], ["Beruf"]
                                String_Work = str(DataWork)
                                Select_Work = String_Work.strip("\n")
                                Edited_Work = rubber(Select_Work[i])

                                DataInfo = Index[i], ["Info"]
                                String_Info = str(DataInfo)
                                Select_Info = String_Info.strip("\n")
                                Edited_Info = rubber(Select_Info[i])

                                DataBirth = Index[i], ["Geburtstag"]
                                String_Birth = str(DataBirth)
                                Select_Birth = String_Birth.strip("\n")
                                Edited_Birth = rubber(Select_Birth[i])

                                DataMail = Index[i], ["E-Mail"]
                                String_Mail = str(DataMail)
                                Select_Mail = String_Mail.strip("\n")
                                Edited_Mail = rubber(Select_Mail[i])

                                return render_template("results.html", Data="Data Found!", DataPre=Edited_Pre,
                                                       DataLast=Edited_Sur,
                                                       DataTel=Edited_Tel,
                                                       DataFBID=Edited_FBI, DataSex=Edited_Sex,
                                                       DataLive=Edited_Live,
                                                       DataCountry=Edited_Country, DataLove=Edited_Love,
                                                       DataWork=Edited_Work, DataInfo=Edited_Info,
                                                       DataBirth=Edited_Birth,
                                                       DataMail=Edited_Mail)
                        else:

                            DataPre = rubber(Datenliste["Vorname"])
                            DataLast = rubber(Datenliste["Nachname"])
                            DataTel = rubber(Datenliste["Telefonnummer"])
                            DataFBID = rubber(Datenliste["FacebookID"])
                            DataSex = rubber(Datenliste["Geschlecht"])
                            DataLive = rubber(Datenliste["Wohnort"])
                            DataCountry = rubber(Datenliste["Land"])
                            DataLove = rubber(Datenliste["Beziehungsstatus"])
                            DataWork = rubber(Datenliste["Beruf"])
                            DataInfo = rubber(Datenliste["Info"])
                            DataBirth = rubber(Datenliste["Geburtstag"])
                            DataMail = rubber(Datenliste["E-Mail"])

                            return render_template("results.html", Data="Data Found!", DataPre=DataPre,
                                                   DataLast=DataLast,
                                                   DataTel=DataTel,
                                                   DataFBID=DataFBID, DataSex=DataSex, DataLive=DataLive,
                                                   DataCountry=DataCountry, DataLove=DataLove,
                                                   DataWork=DataWork, DataInfo=DataInfo, DataBirth=DataBirth,
                                                   DataMail=DataMail)



                    else:
                        return render_template("results.html", Data="No Valid Data found!")


                elif Telefonnummer != "":
                    Credsearch = df["Telefonnummer"] == Telefonnummer
                    if df.Credsearch.empty:
                        NotEmty = False
                    else:
                        NotEmty = True
                    if NotEmty:
                        Datenliste = df.loc[Credsearch]

                        Index = Datenliste.index
                        if len(Index) > 1:
                            i = 0
                            while i != len(Index):
                                DataPre = Index[i], ["Vorname"]
                                String_Pre = str(DataPre)
                                Select_Pre = String_Pre.split("\n")
                                Edited_Pre = rubber(Select_Pre[i])

                                DataLast = Index[i], ["Nachname"]
                                String_Sur = str(DataLast)
                                Select_Sur = String_Sur.split("\n")
                                Edited_Sur = rubber(Select_Sur[i])

                                DataTel = Index[i], ["Telefonnummer"]
                                String_Tel = str(DataTel)
                                Select_Tel = String_Tel.strip("\n")
                                Edited_Tel = rubber(Select_Tel[i])

                                DataFBID = Index[i], ["FacebookID"]
                                String_FBID = str(DataFBID)
                                Select_FBID = String_FBID.strip("\n")
                                Edited_FBI = rubber(Select_FBID[i])

                                DataSex = Index[i], ["Geschlecht"]
                                String_Sex = str(DataSex)
                                Select_Sex = String_Sex.strip("\n")
                                Edited_Sex = rubber(Select_Sex[i])

                                DataLive = Index[i], ["Wohnort"]
                                String_Live = str(DataLive)
                                Select_Live = String_Live.strip("\n")
                                Edited_Live = rubber(Select_Live[i])

                                DataCountry = Index[i], ["Land"]
                                String_Country = str(DataCountry)
                                Select_Country = String_Country.strip("\n")
                                Edited_Country = rubber(Select_Country[i])

                                DataLove = Index[i], ["Beziehungsstatus"]
                                String_Love = str(DataLove)
                                Select_Love = String_Love.strip("\n")
                                Edited_Love = rubber(Select_Love[i])

                                DataWork = Index[i], ["Beruf"]
                                String_Work = str(DataWork)
                                Select_Work = String_Work.strip("\n")
                                Edited_Work = rubber(Select_Work[i])

                                DataInfo = Index[i], ["Info"]
                                String_Info = str(DataInfo)
                                Select_Info = String_Info.strip("\n")
                                Edited_Info = rubber(Select_Info[i])

                                DataBirth = Index[i], ["Geburtstag"]
                                String_Birth = str(DataBirth)
                                Select_Birth = String_Birth.strip("\n")
                                Edited_Birth = rubber(Select_Birth[i])

                                DataMail = Index[i], ["E-Mail"]
                                String_Mail = str(DataMail)
                                Select_Mail = String_Mail.strip("\n")
                                Edited_Mail = rubber(Select_Mail[i])


                                return render_template("results.html", Data="Data Found!", DataPre=Edited_Pre,
                                                       DataLast=Edited_Sur,
                                                       DataTel=Edited_Tel,
                                                       DataFBID=Edited_FBI, DataSex=Edited_Sex,
                                                       DataLive=Edited_Live,
                                                       DataCountry=Edited_Country, DataLove=Edited_Love,
                                                       DataWork=Edited_Work, DataInfo=Edited_Info,
                                                       DataBirth=Edited_Birth,
                                                       DataMail=Edited_Mail)
                            else:

                                DataPre = rubber(Datenliste["Vorname"])
                                DataLast = rubber(Datenliste["Nachname"])
                                DataTel = rubber(Datenliste["Telefonnummer"])
                                DataFBID = rubber(Datenliste["FacebookID"])
                                DataSex = rubber(Datenliste["Geschlecht"])
                                DataLive = rubber(Datenliste["Wohnort"])
                                DataCountry = rubber(Datenliste["Land"])
                                DataLove = rubber(Datenliste["Beziehungsstatus"])
                                DataWork = rubber(Datenliste["Beruf"])
                                DataInfo = rubber(Datenliste["Info"])
                                DataBirth = rubber(Datenliste["Geburtstag"])
                                DataMail = rubber(Datenliste["E-Mail"])

                                return render_template("results.html", Data="Data Found!", DataPre=DataPre,
                                                       DataLast=DataLast,
                                                       DataTel=DataTel,
                                                       DataFBID=DataFBID, DataSex=DataSex, DataLive=DataLive,
                                                       DataCountry=DataCountry, DataLove=DataLove,
                                                       DataWork=DataWork, DataInfo=DataInfo, DataBirth=DataBirth,
                                                       DataMail=DataMail)
                    elif counter != len(Countrylist):
                        counter += 1
                        continue
                    else:
                        return render_template("results.html", Data="No valid Data found")
                else:
                    return render_template("results.html", Data="Please Provide Credentials")
            except TypeError:
                continue

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1337, debug=True)
