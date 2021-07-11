from collections import namedtuple

from django.shortcuts import render, HttpResponse , redirect

from productdetail.forms import ActiveForm

from firebase_admin import db,auth
def pay(request, player_id):
    keys = {}
    player = dict(db.reference('Player').order_by_child("ID").equal_to(player_id).get())
    if bool(player.keys()):
        pass
    else :
        player = dict(db.reference('Player').order_by_child("ID").equal_to(str(player_id)).get())
    for i in player.keys():
        keys["Profile"] = i
    
    user_list = dict(db.reference("Users").order_by_child("LID").equal_to(player[keys["Profile"]]["User"]).get())
    for i in user_list.keys():
        keys["User"] = i
    cp = int(player[keys["Profile"]]["CurrentPrice"])
    w = int(user_list[keys["User"]]["Money"])
    rm = w - cp
    db.reference("Users").child(keys["User"]).update({"Money": rm})
    user_list = dict(db.reference("Users").order_by_child("LID").equal_to(player[keys["Profile"]]["User"]).get())
    w_new = int(user_list[keys["User"]]["Money"])
    if w_new < w:
        pr_status = "Deducted"
        return redirect("/firebase/playersdetail")
    else :
        pr_status = "failed"
        return redirect("/firebase/profile/"+str(player_id) )  
    return render(reuqest,"")




def index(request):
    player = db.reference('Player').get()
    player = dict(player)
    key = []
    field_list = ["ID", "Name"]
    player_detail = []
    player_store = {}
    K = 1
    for i in player.keys():
        key.append(i)
    for i in key:
        for j in field_list:
            player_detail.append(player[i][j])
        print(player_detail)
        player_1 = dict(zip(field_list, player_detail))
        player_store["A" + str(K)] = namedtuple("Player", player_1.keys())(*player_1.values())
        K = K + 1
        player_detail.clear()

    player_output = {"Player": namedtuple("Player", player_store.keys())(*player_store.values())}

    print(player_output)
    return render(request, 'firebase/index.html', context=player_output)





def profile(request, player_id):
    player = dict(db.reference('Player').order_by_child("ID").equal_to(player_id).get())
    if bool(player.keys()):
        pass
    else :
        player = dict(db.reference('Player').order_by_child("ID").equal_to(str(player_id)).get())
    
    key = {}
    
    
    field_list = []
    player_detail = []
    profile = {}
    for i in player.keys():
        key["Profile"] = i
    
    for j in player[key["Profile"]].keys():
        field_list.append(j)
    
    for j in field_list:
        player_detail.append(player[key["Profile"]][j])
    profile = dict(zip(field_list, player_detail))
    print(profile)
    if "User" in field_list:
        user_list = dict(db.reference("Users").order_by_child("LID").equal_to(profile["User"]).get())
        if user_list.keys() :
            for i in user_list.keys():
                key["user"] = i
            profile["User"] = user_list[key["user"]]["Name"]
        else :
            pass
    else:
        pass
    profile["ActiveF"]=ActiveForm()
    if request.method == "POST":
        active = ActiveForm(request.POST)
        if active.is_valid():
            player = {
                "ID": request.POST["Player_id"],
                "Name": request.POST["Name"],
                "Type": request.POST["Type"],
                "Country": request.POST["Country"],
                "Debut_year": request.POST["Debut_year"],
                "ODI_rankings": request.POST["ODI_rankings"],
                "T20_rankings": request.POST["T20_rankings"],
                "Test_rankings": request.POST["Test_rankings"],
                "Profile": request.POST["Profile"],
                "Batting_style": request.POST["Batting_style"],
                "BasePrice": request.POST["BasePrice"],
                "CurrentPrice": request.POST["CurrentPrice"],
                "Player_img": request.POST["url"],
                "active": active.cleaned_data["active"]
            }
        # print(request.POST.get("active",''))
        print(player)

        db.reference("Player").child(key["Profile"]).update(player)
        return redirect("/firebase/playersdetail")
    else:
        return render(request, 'firebase/profileform.html', context=profile)
#
# #updating ipl stats
#
#
#
#
#
def ipl(request, player_id):
    player = dict(db.reference('Player_STATS').child("IPL_STATS").order_by_child("ID").equal_to((player_id)).get())
    if bool(player.keys()):
        pass
    else:
        player = dict(db.reference('Player_STATS').child("IPL_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    key = []
    field_list = []
    player_detail = []
    stats = {}
    for i in player.keys():
        key.append(i)
    for i in key:
        for j in player[i].keys():
            field_list.append(j)
    for i in key:
        for j in field_list:
            player_detail.append(player[i][j])
        stats = dict(zip(field_list, player_detail))
    if request.method == "POST":

        ipl = {
            "ipl_matches": request.POST["ipl_matches"],
            "ipl_runs": request.POST["ipl_runs"],
            "ipl_fours": request.POST["ipl_fours"],
            "ipl_sixes": (request.POST["ipl_sixes"]),
            "ipl_ducks": (request.POST["ipl_ducks"]),
            "ID": ((request.POST["Player_id"])),
            "ipl_balls": request.POST["ipl_balls"],
            "ipl_wicket": request.POST["ipl_wicket"],
            "ipl_economy": request.POST["ipl_economy"],
            "ipl_3w": request.POST["ipl_3w"],

        }
        db.reference("Player_STATS").child("IPL_STATS").child(key[0]).update(ipl)
        return redirect("/firebase/playersdetail")
    else:
        return render(request, 'firebase/iplstats.html', context=stats)

#
#
#
#
#
def t20i(request, player_id):
    player = dict(db.reference('Player_STATS').child("T20I_STATS").order_by_child("ID").equal_to(player_id).get())
    if bool(player.keys()):
        pass
    else:
        player = dict(db.reference('Player_STATS').child("T20I_STATS").order_by_child("ID").equal_to(str(player_id)).get())
    key = []
    field_list = []
    player_detail = []




    stats = {}
    K = 1

    for i in player.keys():
        key.append(i)
    for i in key:
        for j in player[i].keys():
            field_list.append(j)
    for i in key:
        for j in field_list:
            player_detail.append(player[i][j])
        stats = dict(zip(field_list, player_detail))

    if request.method == "POST":

        t20i = {
            "t20i_matches": request.POST["t20i_matches"],
            "t20i_runs": request.POST["t20i_runs"],
            "t20i_fours": request.POST["t20i_fours"],
            "t20i_sixes": (request.POST["t20i_sixes"]),
            "t20i_ducks": (request.POST["t20i_ducks"]),
            "ID": ((request.POST["Player_id"])),
            "t20i_balls": request.POST["t20i_balls"],
            "t20i_wicket": request.POST["t20i_wicket"],
            "t20i_economy": request.POST["t20i_economy"],
            "t20i_3w": request.POST["t20i_3w"],

        }
        db.reference("Player_STATS").child("T20I_STATS").child(key[0]).update(t20i)
        return redirect("/firebase/playersdetail")
    else:
        return render(request, 'firebase/t20istats.html', context=stats)

#
#
#
#
#
#
#
#
#
#
# #updating odi stats in firebase
#
#
#
#
#
#
#
def odi(request, player_id):
    player = dict(db.reference('Player_STATS').child("ODI_STATS").order_by_child("ID").equal_to(player_id).get())
    if bool(player.keys()):
        pass
    else:
        player = dict(db.reference('Player_STATS').child("ODI_STATS").order_by_child("ID").equal_to(str(player_id)).get())
    key = []
    field_list = []
    player_detail = []
    stats = {}
    for i in player.keys():
        key.append(i)
    for i in key:
        for j in player[i].keys():
            field_list.append(j)
    for i in key:
        for j in field_list:
            player_detail.append(player[i][j])
        stats = dict(zip(field_list, player_detail))
    if request.method == "POST":

        odi = {
                "odi_matches":request.POST["odi_matches"],
                "odi_runs":request.POST["odi_runs"],
                "odi_fours":request.POST["odi_fours"],
                "odi_sixes":request.POST["odi_sixes"],
                "odi_ducks":request.POST["odi_ducks"],
                "ID" : request.POST["Player_id"],
                "odi_balls": request.POST["odi_balls"],
                "odi_wicket": request.POST["odi_wicket"],
                "odi_economy": request.POST["odi_economy"],
                "odi_5w": request.POST["odi_5w"],
            }
        db.reference("Player_STATS").child("ODI_STATS").child(key[0]).update(odi)
        return redirect("/firebase/playersdetail")
    else:
        return render(request, 'firebase/odistats.html', context=stats)
#
#
#
#
def test(request, player_id):
    player = dict(db.reference('Player_STATS').child("TEST_STATS").order_by_child("ID").equal_to(player_id).get())
    if bool(player.keys()):
        pass
    else:
        player = dict(db.reference('Player_STATS').child("TEST_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    key = []
    field_list = []
    player_detail = []
    stats = {}
    for i in player.keys():
        key.append(i)
    for i in key:
        for j in player[i].keys():
            field_list.append(j)
    for i in key:
        for j in field_list:
            player_detail.append(player[i][j])
        stats = dict(zip(field_list, player_detail))

    if request.method == "POST":

        test = {
                "test_matches":request.POST["test_matches"],
                "test_runs":request.POST["test_runs"],
                "test_fours":request.POST["test_fours"],
                "test_sixes":request.POST["test_sixes"],
                "test_ducks":request.POST["test_ducks"],
                "ID": request.POST["Player_id"],
                "test_balls": request.POST["test_balls"],
                "test_wicket": request.POST["test_wicket"],
                "test_economy": request.POST["test_economy"],
                "test_5w": request.POST["test_5w"],
            }
        db.reference("Player_STATS").child("TEST_STATS").child(key[0]).update(test)
        return redirect("/firebase/playersdetail")
    else:
        return render(request, 'firebase/teststats.html', context=stats)
# # delete the data from database
#
#
#
#
#
#
#
#
def delete(request, player_id):
    key = {}

    player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(player_id).get())
    player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to(player_id).get())
    player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to(player_id).get())
    player_t20i = dict(db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to(player_id).get())
    player_test = dict(db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to(player_id).get())
    if bool(player_profile.keys()):
        pass
    else:
        player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(str(player_id)).get())

    if bool(player_ipl.keys()):
        pass
    else:

        player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    if bool(player_odi.keys()):
        pass
    else:
        player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    if bool(player_t20i.keys()):
        pass
    else:
        player_t20i = dict(
            db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to(str(player_id)).get())
    if bool(player_test.keys()):
        pass
    else:
        player_test = dict(
            db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    for i in player_profile.keys():
        key["Profile"] = i
    for i in player_ipl.keys():
        key["IPL"] = i
    for i in player_odi.keys():
        key["ODI"] = i
    for i in player_t20i.keys():
        key["T20I"] = i
    for i in player_test.keys():
        key["TEST"] = i

    db.reference("Player").child(key["Profile"]).delete()
    db.reference("Player_STATS").child("IPL_STATS").child(key["IPL"]).delete()
    db.reference("Player_STATS").child("ODI_STATS").child(key["ODI"]).delete()
    db.reference("Player_STATS").child("T20I_STATS").child(key["T20I"]).delete()
    db.reference("Player_STATS").child("TEST_STATS").child(key["TEST"]).delete()

    return redirect("/firebase/playersdetail", {'message': "You have deleted this player detail successfully"})














def userdetail(request, uid):
    user = dict(db.reference('Users').order_by_child("LID").equal_to(uid).get())

    key = ""
    field_list = []
    user_detail = []
    details = {}
    for i in user.keys():
        key = i
    for j in user[key].keys():
        field_list.append(j)
    
    for j in field_list:
        user_detail.append(user[key][j])
    details = dict(zip(field_list, user_detail))
    player = dict(db.reference('Player').order_by_child('User').equal_to(uid).get())
    keys = []
    player_field = ["Name","ID"]
    player_details = []
    player_store = {}
    K = 1
    if player.keys():
        for i in player.keys():
            keys.append(i)
        for i in keys:
            for j in player_field:
                player_details.append(player[i][j])
            player_1 = dict(zip(player_field, player_details))
            player_store["A" + str(K)]=namedtuple("Player", player_1.keys())(*player_1.values())
            player_details.clear()
            K = K + 1
        details["Players"] = namedtuple("Player", player_store.keys())(*player_store.values())
            
    if request.method == "POST":

        test = {
                "Name": request.POST["Name"],
                "STATUS": request.POST["STATUS"],
                "Money": request.POST["Money"]
            }
        db.reference("Users").child(key).update(test)
        return redirect("/firebase/userlist")
    else:
        return render(request, 'firebase/User Profile.html', context=details)


















def userlist(request):
    player = db.reference('Users').get()
    player = dict(player)
    key = []
    field_list = ["Name","LID"]
    player_detail = []
    player_store = {}
    K = 1
    for i in player.keys():
        key.append(i)
    for i in key:
        for j in field_list:
            player_detail.append(player[i][j])
        print(player_detail)
        player_1 = dict(zip(field_list, player_detail))
        player_store["A" + str(K)] = namedtuple("Player", player_1.keys())(*player_1.values())
        K = K + 1
        player_detail.clear()

    player_output = {"Player": namedtuple("Player", player_store.keys())(*player_store.values())}

    print(player_output)
    return render(request, 'firebase/user list.html', context=player_output)














def delete(request, player_id):
    key = {}

    player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(player_id).get())
    player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to(player_id).get())
    player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to(player_id).get())
    player_t20i = dict(db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to(player_id).get())
    player_test = dict(db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to(player_id).get())
    if bool(player_profile.keys()):
        pass
    else:
        player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(str(player_id)).get())

    if bool(player_ipl.keys()):
        pass
    else:

        player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    if bool(player_odi.keys()):
        pass
    else:
        player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    if bool(player_t20i.keys()):
        pass
    else:
        player_t20i = dict(
            db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to(str(player_id)).get())
    if bool(player_test.keys()):
        pass
    else:
        player_test = dict(
            db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to(str(player_id)).get())

    for i in player_profile.keys():
        key["Profile"] = i
    for i in player_ipl.keys():
        key["IPL"] = i
    for i in player_odi.keys():
        key["ODI"] = i
    for i in player_t20i.keys():
        key["T20I"] = i
    for i in player_test.keys():
        key["TEST"] = i

    db.reference("Player").child(key["Profile"]).delete()
    db.reference("Player_STATS").child("IPL_STATS").child(key["IPL"]).delete()
    db.reference("Player_STATS").child("ODI_STATS").child(key["ODI"]).delete()
    db.reference("Player_STATS").child("T20I_STATS").child(key["T20I"]).delete()
    db.reference("Player_STATS").child("TEST_STATS").child(key["TEST"]).delete()

    return redirect("/firebase/playersdetail", {'message': "You have deleted this player detail successfully"})



def deleteuser(request, uid):
    key = ''

    player_profile = dict(db.reference("Users").order_by_child("LID").equal_to(uid).get())
    

    for i in player_profile.keys():
        key = i
    

    db.reference("Users").child(key).delete()
    auth.delete_user(uid)

    return redirect("/firebase/userlist", {'message': "You have deleted this player detail successfully"})




















def resetplayer(request):
    player = db.reference('Player').get()
    player = dict(player)
    
    bp = {}
    a = 'A'
    b = 1 
    for i in player.keys():
        bp[a + str(b)] = player[i]["BasePrice"]
        b = b + 1
    b =1
    for i in player.keys():
        db.reference("Player").child(i).update({"CurrentPrice":bp[a + str(b)],"User":""})
        b = b + 1 
    
    return redirect("/firebase/playersdetail")
def resetuser(request):
    player = db.reference('Users').get()
    player = dict(player)
    key = []
    
    
    for i in player.keys():
        key.append(i)
    for i in key:
        db.reference("Users").child(i).update({"Money":1000000})
    
    return redirect("/firebase/userlist")

def resetpp(request,player_id):
    player = db.reference('Player').order_by_child("ID").equal_to(player_id).get()
    key = ""
    if player.keys():
        pass
    else:
        player = db.reference('Player').order_by_child("ID").equal_to(str(player_id)).get()
    player = dict(player)
    
    for i in player.keys():
        key = i    
    bp = player[key]["BasePrice"]
    db.reference("Player").child(key).update({"CurrentPrice":bp,"User":""})
    
    
    return redirect("/firebase/playersdetail",{'message': "You have reset the value of player "+str(player_id)})