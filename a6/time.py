def isLeap(year):
    if(year%100 == 0):
        return (year%400 == 0)
    return (year%100 == 0)

def add_time(time, diff):
    time[0] += diff[0]
    time[1] += diff[1]
    if(time[1]>59):
        time[0] += 1
        time[1] -= 60
    carry = 0
    if(time[0]>24):
        carry = 1
        time[0] -= 24
    out = ""
    if(time[0]<10):
        out  = '0'
    out = out + str(time[0]) + ":"
    if(time[1]<10):
        out = out + '0'
    out = out + str(time[1])
    return (out, carry)
    
def add_Day(day, carry, months):
    if(carry==1):
        day[0] += 1
        if(day[0]>months[day[1]][1]):
            if(day[1]=='February' and isLeap(day[2])):
                1
            else:
                day[1] += 1
                day[0] = 1
                if(day[1]==13):
                    day[2] += 1
                    day[1] = 1
    return str(day[2]) + '-' + str(day[1]) + '-' + str(day[0])


def time_difference(city_a, timestamp, city_b):
    # YOUR CODE HERE
    city = {'Los Angeles': [-8, 0], 'New York': [-5, 0], 'Caracas': [-4, 30], 'Buenos Aires': [-3, 0], 'London': [0, 0], 'Rome': [1, 0], 'Moscow': [3, 0], 'Tehran': [3, 30], 'New Delhi':[5, 30], 'Beijing': [8, 0], 'Canberra': [10, 0]}
    time_diff = [city[city_b][0] - city[city_a][0], city[city_b][1] - city[city_a][1]]
    months = {'January': [1, 31], 'February': [2, 28], 'March': [3, 31], 'April': [4, 30], 'May': [5, 30], 'June': [6, 30], 'July': [7 31], 'August': [8,31], 'September': [9, 30], 'October': [10, 31], 'November': [11, 30], 'December': [12, 31]}
    if(time_diff[1] >= 60):
        time_diff[0] += 1
        time_diff[1] = 0

    timestamp.replace(',', ' ')
    day = timestamp.split(" ")


    print 'hello'
    print day
    current_date = [int(day[1]), day[0], int(day[2])
    #day[3].split(":")

time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra")
