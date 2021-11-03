str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + wai_time
print(time_when_alarm_go_off) #The error was The line 6 was wait_time isntead of wai_time so I took away the t part
#and run it
