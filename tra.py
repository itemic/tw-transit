import json
import urllib.request

trains = "http://ptx.transportdata.tw/MOTC/v2/Rail/TRA/DailyTrainInfo?%24format=JSON"
trains_data = json.loads(urllib.request.urlopen(trains).read().decode('utf8'))

train_listing = []
for train in trains_data:
    #all the trains!
    train_listing.append(train["TrainNo"])