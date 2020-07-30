import datetime
from sys import argv
def dateToString(date):
    fmt = '%d.%m.%Y'
    dt = datetime.datetime.strptime(date, fmt)
    julian = dt.timetuple()
    return julian.tm_year*1000 + julian.tm_yday

def stringToDate(string):
    date = string[0]
    if(string[1].isnumeric()):
        date = date+string[1]
    #date = int(date)
    year = string[-4:]
   # year = int(year)
    months = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    i=1
    while not string[i].isalpha():
        i+=1
    month = months[string[i:i+3].lower()]
    return '.'.join([str(date), str(month), str(year)])

def convert(date):
    return dateToString(stringToDate(date))
print (convert(argv[1]))
