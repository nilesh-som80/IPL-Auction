from django.shortcuts import render, redirect
from django.http import JsonResponse


from collections import namedtuple
from firebase_admin import auth,db


# Create your views here.


# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        try:
            user = auth.get_user_by_email(email)
        except:
            message = "invalid credentials"
            return render(request, "sign-in.html", {"message": message})
        print(user)
        session_id = user.uid
        request.session['uid'] = str(session_id)
        return redirect("/user/main")
    return render(request, 'sign-in.html')


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect("/user/login")


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        passw = request.POST['password']
        try:
            user = auth.create_user(email=email, password=passw, display_name=name)
            print(user)
        except:
            message = "User Id not created as you have either used a weak password or the email id is registered"
            return render(request, "sign-up.html", {"message": message})

        data = {"Name": name, "STATUS": "1", "LID":user.uid , "Money":1000000}

        db.reference("Users").push(data)
        return redirect("/user/login")
    else:
        return render(request, 'sign-up.html')


def batsman(request):
    try:
        user = request.session['uid']
        player = db.reference("Player").order_by_child("Type").equal_to("Batsman").get()
        player_1 = db.reference("Player").order_by_child("Type").equal_to("Batsmen").get()
        player = dict(player)
        player_1 = dict(player_1)
        player.update(player_1)
        field_list = ["ID", "Name", "Player_img", "BasePrice"]
        key = []
        player_field_detail = []
        player_dict = {}
        player_output = {}

        k = 1
        for i in player.keys():
            key.append(i)
        for i in key:
            for j in field_list:
                player_field_detail.append(player[i][j])
            player_com = dict(zip(field_list, player_field_detail))
            player_dict["P" + str(k)] = namedtuple("Player", player_com.keys())(*player_com.values())
            player_field_detail.clear()
            k = k + 1

        player_output["Player"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
        player_output["Type"] = "Batsman"
        print(player_output)
        return render(request, 'MAIN PAGE/product.html', context=player_output)
    except KeyError:
        message = "OOPS! you have logged out please SignIn again"
        return render(request, "sign-in.html", {"message": message})


def bowler(request):
    try:
        user = request.session['uid']
        player = db.reference("Player").order_by_child("Type").equal_to("Bowler").get()
        player = dict(player)
        field_list = ["ID", "Name", "Player_img", "BasePrice"]
        key = []
        player_field_detail = []
        player_dict = {}
        player_output = {}

        k = 1
        for i in player.keys():
            key.append(i)
        for i in key:
            for j in field_list:
                player_field_detail.append(player[i][j])
            player_com = dict(zip(field_list, player_field_detail))
            player_dict["P" + str(k)] = namedtuple("Player", player_com.keys())(*player_com.values())
            player_field_detail.clear()
            k = k + 1

        player_output["Player"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
        print(player_output)
        player_output["Type"] = "Bowler"
        return render(request, 'MAIN PAGE/product.html', context=player_output)
    except KeyError:
        message = "OOPS! you have logged out please SignIn again"
        return render(request, "sign-in.html", {"message": message})


def keeper(request):
    try:
        user = request.session['uid']
        player = db.reference("Player").order_by_child("Type").equal_to("Wicket Keeper").get()
        player = dict(player)
        field_list = ["ID", "Name", "Player_img", "BasePrice"]
        key = []
        player_field_detail = []
        player_dict = {}
        player_output = {}

        k = 1
        for i in player.keys():
            key.append(i)
        for i in key:
            for j in field_list:
                player_field_detail.append(player[i][j])
            player_com = dict(zip(field_list, player_field_detail))
            player_dict["P" + str(k)] = namedtuple("Player", player_com.keys())(*player_com.values())
            player_field_detail.clear()
            k = k + 1

        player_output["Player"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
        print(player_output)
        player_output["Type"] = "Wicket Keeper"
        return render(request, 'MAIN PAGE/product.html', context=player_output)
    except KeyError:
        message = "OOPS! you have logged out please SignIn again"
        return render(request, "sign-in.html", {"message": message})


def allrounder(request):
    try:
        user = request.session['uid']
        player = db.reference("Player").order_by_child("Type").equal_to("All Rounder").get()
        player = dict(player)
        field_list = ["ID", "Name", "Player_img", "BasePrice"]
        key = []
        player_field_detail = []
        player_dict = {}
        player_output = {}

        k = 1
        for i in player.keys():
            key.append(i)
        for i in key:
            for j in field_list:
                player_field_detail.append(player[i][j])
            player_com = dict(zip(field_list, player_field_detail))
            player_dict["P" + str(k)] = namedtuple("Player", player_com.keys())(*player_com.values())
            player_field_detail.clear()
            k = k + 1

        player_output["Player"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
        print(player_output)
        player_output["Type"] = "All Rounder"
        return render(request, 'MAIN PAGE/product.html', context=player_output)
    except KeyError:
        message = "OOPS! you have logged out please SignIn again"
        return render(request, "sign-in.html", {"message": message})


def profile(request, player_id):

    user = request.session['uid']
    key = {}
    player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(str(player_id)).get())
    player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to(str(player_id)).get(
        ))
    player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to(str(player_id)).get(
        ))
    player_t20i = dict(db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to(str(player_id)).get(
        ))
    player_test = dict(db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to(str(player_id)).get(
        ))
    if bool(player_profile.keys()):
        pass
    else:
        player_profile = dict(db.reference("Player").order_by_child("ID").equal_to((player_id)).get())
    if bool(player_ipl.keys()):
        pass
    else:
        player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to((player_id)).get())
        if bool(player_ipl.keys()):
            pass
        else:
            player_ipl = dict(db.reference("Player_STATS").child("IPL_STATS").order_by_child("ID").equal_to(0).get())
    if bool(player_odi.keys()):
        pass
    else:
        player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to((player_id)).get())
        if bool(player_odi.keys()):
            pass
        else:
            player_odi = dict(db.reference("Player_STATS").child("ODI_STATS").order_by_child("ID").equal_to(0).get())
    if bool(player_t20i.keys()):
        pass
    else:
        player_t20i = dict(db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to((player_id)).get())
        if bool(player_t20i.keys()):
            pass
        else:
            player_t20i = dict(db.reference("Player_STATS").child("T20I_STATS").order_by_child("ID").equal_to(0).get())
    if bool(player_test.keys()):
        pass
    else:
        player_test = dict(db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to((player_id)).get())
        if bool(player_test.keys()):
            pass
        else:
            player_test = dict(db.reference("Player_STATS").child("TEST_STATS").order_by_child("ID").equal_to(0).get())
    for i in player_profile.keys():
        key["Profile"] = i
    for i in player_ipl.keys():
        key["IPL"] = (i)
    for i in player_odi.keys():
        key["ODI"] = (i)
    for i in player_t20i.keys():
        key["T20I"] = (i)
    for i in player_test.keys():
        key["TEST"] = (i)
    stats = {}

    field_list_test = []
    for i in player_test[key["TEST"]].keys():
        field_list_test.append(i)
    for i in field_list_test :
        stats[i] = player_test[key["TEST"]][i]
    field_list_odi = []
    for i in player_odi[key["ODI"]].keys():
        field_list_odi.append(i)
    for i in field_list_odi:
        stats[i] = player_odi[key["ODI"]][i]
    field_list_t20i = []
    for i in player_t20i[key["T20I"]].keys():
        field_list_t20i.append(i)
    for i in field_list_t20i:
        stats[i] = player_t20i[key["T20I"]][i]
    field_list_ipl = []
    for i in player_ipl[key["IPL"]].keys():
        field_list_ipl.append(i)
    for i in field_list_ipl:
        stats[i] = player_ipl[key["IPL"]][i]
    field_list = []
    for i in player_profile[key["Profile"]].keys():
        field_list.append(i)
    for i in field_list:
        if i == "User" :
            user_list = dict(db.reference("Users").order_by_child("LID").equal_to(player_profile[key["Profile"]][i]).get())
            if user_list.keys():
                for j in user_list.keys():
                    key["User Detail"] = j
                stats[i] = user_list[key["User Detail"]]['Name']
            else:
                pass        
        else:
            stats[i] = player_profile[key["Profile"]][i]
    player = {}
    player.update(stats)
    if request.is_ajax():
        player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(str(player_id)).get())
        if player_profile[key["Profile"]]["active"] :
            user_list = dict(db.reference("Users").order_by_child("LID").equal_to(user).get())
            for i in user_list.keys():
                key["User Detail"] = i
            print(player_profile[key["Profile"]]["CurrentPrice"])
            print(user_list[key["User Detail"]]["Money"])
            if int(user_list[key["User Detail"]]["Money"]) >= (int(player_profile[key["Profile"]]["CurrentPrice"])+1000):
                i = int(player_profile[key["Profile"]]["CurrentPrice"])
                i = i + 1000
                print(i)
                db.reference("Player").child(key["Profile"]).update({"CurrentPrice":i,"User":user})
                player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(str(player_id)).get())
                print(player_profile[key["Profile"]]["CurrentPrice"])
                return JsonResponse({"price":player_profile[key["Profile"]]["CurrentPrice"],"current":i,"Name":user_list[key["User Detail"]]["Name"]})
            else:
                player['active'] = False
                return JsonResponse({"err":"You dont have enough amount for this bid","price":player_profile[key["Profile"]]["CurrentPrice"],"Name":user_list[key["User Detail"]]["Name"],"price":player_profile[key["Profile"]]["CurrentPrice"]})
        else:
            return JsonResponse({"price":player_profile[key["Profile"]]["CurrentPrice"],"current":i,"Name":user_list[key["User Detail"]]["Name"],"err":"bidding is closed for this player"})

    return render(request, 'PRODUCT/product-details.html', context=player)

    # except KeyError:
    #      message = "OOPS! you have logged out please SignIn again"
    #      return render(request, "sign-in.html", {"message": message})


def main_page(request):
    try:
        user = request.session['uid']
        type = ["Batsman", "Bowler", "Wicket Keeper", "All Rounder"]
        field_list = ["ID", "Name", "Player_img"]
        player_details = []
        player_dict = {}
        player_output = {}
        j = "A"

        k = 1
        for i in type:
            player = dict(db.reference("Player").order_by_child("Type").equal_to(i).get())
            for key in player.keys():
                if k > 3:
                    pass
                else:
                    for l in field_list:
                        player_details.append(player[key][l])
                    player_1 = dict(zip(field_list, player_details))
                    player_dict[j + str(k)] = namedtuple("Player", player_1.keys())(*player_1.values())
                    k = k + 1
                    player_details.clear()
            k = 1
            if i == "Wicket Keeper":
                player_output["WicketKeeper"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
            elif i == "All Rounder":
                player_output["AllRounder"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
            else:
                player_output[i] = namedtuple("Player", player_dict.keys())(*player_dict.values())

        print(player_output)
        user_detail = dict(db.reference("Users").order_by_child("LID").equal_to(user).get())
        for i in user_detail.keys():
            player_output["UserName"] = user_detail[i]["Name"]
        active_player = dict(db.reference("Player").order_by_child("active").equal_to(True).get())
        field_list.append("CurrentPrice")
        field_list.append("active")
        for i in active_player.keys():
            for j in field_list:
                if j == "active":
                    player_output[j] = active_player[i][j]
                else:
                    player_output["Active" + j] = active_player[i][j]

        print(player_output)

        return render(request, 'AUCTION/index.html', context=player_output)

    except :
        message = "OOPS! you have logged out please SignIn again"
        return render(request, "sign-in.html", {"message": message})

def users_dashboard(request):
    
        user = request.session['uid']
        player = dict(db.reference("Player").order_by_child("User").equal_to(user).get())
        user_details = dict(db.reference("Users").order_by_child("LID").equal_to(user).get())
        user_key = "a"
        field_list = ["ID", "Name", "Player_img", "BasePrice"]
        user_fields = []
        key = []
        player_field_detail = []
        player_dict = {}
        player_output = {}

        k = 1
        for i in user_details.keys():
            user_key = i
        for i in user_details[user_key].keys():
            user_fields.append(i)
        for i in user_fields:
            player_output[i] = user_details[user_key][i] 
        if player.keys() :    
            for i in player.keys():
                key.append(i)
            
                for j in field_list:
                    player_field_detail.append(player[i][j])
                player_com = dict(zip(field_list, player_field_detail))
                player_dict["P" + str(k)] = namedtuple("Player", player_com.keys())(*player_com.values())
                player_field_detail.clear()
                k = k + 1
        else:
            pass

        player_output["Player"] = namedtuple("Player", player_dict.keys())(*player_dict.values())
        print(player_output)
        return render(request, 'Users/product.html', context=player_output)
    # except :
    #     message = "OOPS! you have logged out please SignIn again"
    #     return render(request, "sign-in.html", {"message": message})
def bid_load_data(request,player_id):
    user = request.session['uid']
    key = {}

    player_profile = dict(db.reference("Player").order_by_child("ID").equal_to(str(player_id)).get())
    if bool(player_profile.keys()):
        pass
    else:
        player_profile = dict(db.reference("Player").order_by_child("ID").equal_to((player_id)).get())
    
    
    for i in player_profile.keys():
        key["Profile"] = i
    user_list = dict(db.reference("Users").order_by_child("LID").equal_to(player_profile[key["Profile"]]["User"]).get())
    if user_list.keys():
        for i in user_list.keys():
            key["User"] = i
    
        return JsonResponse({"price":player_profile[key["Profile"]]["CurrentPrice"],"Name":user_list[key["User"]]["Name"]})

    else:
        return JsonResponse({"price":player_profile[key["Profile"]]["CurrentPrice"]})