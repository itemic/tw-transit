import json
import urllib.request

trains = "http://ptx.transportdata.tw/MOTC/v2/Rail/TRA/DailyTrainInfo?%24format=JSON"
trains_data = json.loads(urllib.request.urlopen(trains).read().decode('utf8'))

delay = "http://ptx.transportdata.tw/MOTC/v2/Rail/TRA/LiveTrainDelay?%24format=JSON"
delay_data = json.loads(urllib.request.urlopen(delay).read().decode('utf8'))

train_listing = []
for train in trains_data:
    #all the trains!
    train_listing.append(train["TrainNo"])
active_trains = {}
for train in delay_data:
    #current trains that have delay data
    active_trains[train["TrainNo"]] = int(train["DelayTime"])

valid = False
while (not valid):
    train_input = input("Search by train number: ")
    if train_input not in train_listing:
        print("That train doesn't exist right now")
    else:
        if train_input not in active_trains.keys():
            print("That train is not running right now.")
        else:
            valid = True
            if active_trains[train_input] == 0:
                print("Train {} is running on schedule!".format(train_input))
            else:
                print("Train {} is running {} minute(s) late!".format(train_input, active_trains[train_input]))


