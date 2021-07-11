from django.shortcuts import render,redirect
from .forms import PlayerForm,IPL_STATSForm,T20I_STATSForm,TEST_STATSForm,ODI_STATSForm

from firebase_admin import db

def dataentry(request):
    player = PlayerForm()

    form_dict = {'player':player, 'message':"Fill the form"}
    if request.method == 'POST':
        player = PlayerForm(request.POST)
        if player.is_valid():

            url = request.POST['url']
            player={
                "ID" : player.cleaned_data["Player_id"],
                "Name":player.cleaned_data["Name"],
                "Type":player.cleaned_data["Type"],
                "Country":player.cleaned_data["Country"],
                "Debut_year":str(player.cleaned_data["Debut_year"]),
                "ODI_rankings":str(player.cleaned_data["ODI_rankings"]),
                "T20_rankings":str(player.cleaned_data["T20_rankings"]),
                "Test_rankings":str(player.cleaned_data["Test_rankings"]),
                "Profile":player.cleaned_data["Profile"],
                "Batting_style":player.cleaned_data["Batting_style"],
                "BasePrice":player.cleaned_data["BasePrice"],
                "CurrentPrice":player.cleaned_data["CurrentPrice"],
                "Player_img":url,
                "active":player.cleaned_data["active"],
            }


            db.reference("Player").push(player)
        else:
            print("Invalid")
        return redirect('/product/DataEntryIPL')
    else:
        return render(request,'form.html',context=form_dict)


def iplentry(request):
    IPL = IPL_STATSForm()
    form_dict = {'player':IPL, 'message':"Fill the IPLSTATS"}
    if request.method == 'POST':
        IPL = IPL_STATSForm(request.POST)
        if IPL.is_valid():
            ipl = {
                "ipl_matches": 0,
                "ipl_runs": 0,
                "ipl_fours": 0,
                "ipl_sixes": 0,
                "ipl_ducks": 0,
                "ID": '0',
                "ipl_balls": 0,
                "ipl_wicket": 0,
                "ipl_economy": 0,
                "ipl_3w": 0,

            }
            ipl = {
                "ipl_matches":IPL.cleaned_data["ipl_matches"],
                "ipl_runs":IPL.cleaned_data["ipl_runs"],
                "ipl_fours":IPL.cleaned_data["ipl_fours"],
                "ipl_sixes":(IPL.cleaned_data["ipl_sixes"]),
                "ipl_ducks":(IPL.cleaned_data["ipl_ducks"]),
                "ID" : ((IPL.cleaned_data["Player_id"])),
                "ipl_balls": IPL.cleaned_data["ipl_balls"],
                "ipl_wicket": IPL.cleaned_data["ipl_wicket"],
                "ipl_economy": IPL.cleaned_data["ipl_economy"],
                "ipl_3w": IPL.cleaned_data["ipl_3w"],

            }

            db.reference("Player_STATS").child("IPL_STATS").push(ipl)
        else:
            print("Invalid")
        return redirect('/product/DataEntryTEST')
    else:
        return render(request,'form.html',context=form_dict)

def testentry(request):
    test = TEST_STATSForm()

    form_dict = {'player':test, 'message':"Fill the testSTATS"}
    if request.method == 'POST':
        test = TEST_STATSForm(request.POST)
        if test.is_valid():
            test1 = {
                "test_matches": 0,
                "test_runs": 0,
                "test_fours": 0,
                "test_sixes": 0,
                "test_ducks": 0,
                "ID": 0,
                "test_balls": 0,
                "test_wicket": 0,
                "test_economy": 0,
                "test_5w": 0,
            }

            test1 = {
                "test_matches":test.cleaned_data["test_matches"],
                "test_runs":test.cleaned_data["test_runs"],
                "test_fours":test.cleaned_data["test_fours"],
                "test_sixes":test.cleaned_data["test_sixes"],
                "test_ducks":test.cleaned_data["test_ducks"],
                "ID": test.cleaned_data["Player_id"],
                "test_balls": test.cleaned_data["test_balls"],
                "test_wicket": test.cleaned_data["test_wicket"],
                "test_economy": test.cleaned_data["test_economy"],
                "test_5w": test.cleaned_data["test_5w"],
            }

            db.reference("Player_STATS").child("TEST_STATS").push(test1)
        else:
            print("Invalid")
        return redirect('/product/DataEntryODI')
    else:
        return render(request,'form.html',context=form_dict)
def odientry(request):
    odi = ODI_STATSForm()
    form_dict = {'player':odi, 'message':"Fill the odiSTATS"}
    if request.method == 'POST':
        odi = ODI_STATSForm(request.POST)

        if odi.is_valid():
            odi1 = {
                "odi_matches": 0,
                "odi_runs": 0,
                "odi_fours": 0,
                "odi_sixes": 0,
                "odi_ducks": 0,
                "ID": 0,
                "odi_balls": 0,
                "odi_wicket": 0,
                "odi_economy": 0,
                "odi_5w": 0,
            }

            odi1 = {
                "odi_matches":odi.cleaned_data["odi_matches"],
                "odi_runs":odi.cleaned_data["odi_runs"],
                "odi_fours":odi.cleaned_data["odi_fours"],
                "odi_sixes":odi.cleaned_data["odi_sixes"],
                "odi_ducks":odi.cleaned_data["odi_ducks"],
                "ID" : odi.cleaned_data["Player_id"],
                "odi_balls": odi.cleaned_data["odi_balls"],
                "odi_wicket": odi.cleaned_data["odi_wicket"],
                "odi_economy": odi.cleaned_data["odi_economy"],
                "odi_5w": odi.cleaned_data["odi_5w"],
            }

            db.reference("Player_STATS").child("ODI_STATS").push(odi1)
        else:
            print("Invalid")
        return redirect('/product/DataEntryT20I')
    else:
        return render(request,'form.html',context=form_dict)

def t20ientry(request):
    t20i = T20I_STATSForm()
    form_dict = {'player':t20i, 'message':"Fill the t20iSTATS"}
    if request.method == 'POST':
        t20i = T20I_STATSForm(request.POST)
        if t20i.is_valid():

            t20i1 = {
                "test_matches": 0,
                "test_runs": 0,
                "test_fours": 0,
                "test_sixes": 0,
                "test_ducks": 0,
                "ID": 0,
                "test_balls": 0,
                "test_wicket": 0,
                "test_economy": 0,
                "test_5w": 0,
            }
            t20i1 = {
                "t20i_matches":t20i.cleaned_data["t20i_matches"],
                "t20i_runs":t20i.cleaned_data["t20i_runs"],
                "t20i_fours":t20i.cleaned_data["t20i_fours"],
                "t20i_sixes":t20i.cleaned_data["t20i_sixes"],
                "t20i_ducks":t20i.cleaned_data["t20i_ducks"],
                "ID" : t20i.cleaned_data["Player_id"],
                "t20i_balls": t20i.cleaned_data["t20i_balls"],
                "t20i_wicket": t20i.cleaned_data["t20i_wicket"],
                "t20i_economy": t20i.cleaned_data["t20i_economy"],
                "t20i_3w": t20i.cleaned_data["t20i_3w"],
            }

            db.reference("Player_STATS").child("T20I_STATS").push(t20i1)
        else:
            print("Invalid")
        return redirect('/product/DataEntry')
    else:
        return render(request,'form.html',context=form_dict)

