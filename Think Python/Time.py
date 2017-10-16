class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second))
    
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def mul_time(t1,x):
    seconds = time_to_int(t1)*x
    return int_to_time(seconds)

def average_pace(finish, dist):
    try:
        return print_time(mul_time(finish,1/float(dist)))
    except TypeError:
        print('Enter distance as a number')

def main():
    finish = Time
    finish.hour, finish.minute, finish.second = 2, 45, 36
    print(average_pace(finish,10))
    

if __name__ == '__main__':
    main()

