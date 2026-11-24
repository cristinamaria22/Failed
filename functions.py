#
# Functions section
#
########getters and setters
def set_title(station, title):
    station["title"]= title

def set_category(station, categ):
    station["category"]=categ

def set_minutes(station, minu):
    station["duration"]= minu

def get_title(station):
    return station["title"]

def get_category(station):
    return station["category"]

def get_minutes(station):
    return station["duration"]

### add
def create_station(title, categ, minu):
    station={
    }
    set_title(station, title)
    set_category(station, categ)
    set_minutes(station, minu)
    return station

def add_station(stations, title, categ, minu):
    if len(stations)>0:
        for i in stations:
            if get_title(i)==title:
                raise ValueError("The title already exists")
    if minu<1:
        raise ValueError("The time must be more than a minute")

    station=create_station(title,categ,minu)
    stations.append(station)


####Move to the end = 2
def move_title(stations, title):
    copy_stations= stations.copy()
    stat={}
    okay= False
    for i in copy_stations:
        if get_title(i)== title:
            okay= True
            stat=create_station(get_title(i),get_category(i), get_minutes(i))
            copy_stations.remove(i)
            copy_stations.append(stat)
    if okay ==False:
        raise ValueError("The title was not found")
    return copy_stations

######Sort_by_categ
def sort_by_criterii(stat_list):
    stations= stat_list.copy()
    for i in range(len(stations)-1):
        for j in range (i+1, len(stations)):
            if get_minutes(stations[i])>get_minutes(stations[j]):
                stations[i], stations[j]= stations[j], stations[i]
            else :
                if get_title(stations[i])> get_title(stations[j]):
                    stations[i], stations[j] = stations[j], stations[i]
    return stations

def sort_by_category(stations, categ):
    categ_list=[]
    okay = False
    for i in stations:
        if get_category(i)==categ:
            categ_list.append(i)
            okay=True
    if okay ==False :
        raise ValueError("No segments")
    else :
        categ_list = sort_by_criterii(categ_list)
        return categ_list

#### preview brodcast
def preview_broad( stations, new_list, time, current_time ):
    for i in stations:
        if  (current_time+get_minutes(i)<= time):
            new_list.append(i)
            preview_broad(stations, new_list, time, current_time+ get_minutes(i))
        else:
            return new_list

    return False



