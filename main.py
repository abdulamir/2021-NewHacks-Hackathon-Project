import tkinter as tk
from tkinter import ttk

storage = {}
display_storage = []
week_days = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7, "Due Date": 8}


def get_info():
    #Gets info from input fields and stores in dic
    n1 = input_field.get()
    n2 = input_field2.get()
    n3 = n3_list[0]
    if n1 != "Activity" and n2 != "Priority (1-10)" and n3 != "":
        if n1 in storage: 
            stop = tk.Tk()
            stop.geometry("400x70")
            stop.title("Error")
            error = tk.Label(stop, text = "You have already entered this activity")
            error.pack()
        elif int(n2) > 10 or int(n2) < 1:
            stop = tk.Tk()
            stop.geometry("400x70")
            stop.title("Error")
            error = tk.Label(stop, text = "Please enter a number between 1 and 10")
            error.pack()
        else:
            storage[n1] = [int(n2), week_days[n3]]
            temp = tk.Label(display_inputs, text = n1 + ", " + n2 + ", " + n3)
            display_storage.append(temp)
            temp.pack()


# invoked whenever the due date selection is changed
def day_changed(event):
    n3_list[0] = f'{day_cb.get()}'


def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def manage_cal():
  # user inputs (assignment name), (when it is due), (priority level)
  #dictionary prior[priority level] = [amount of days to spend, time to spend each day]
  # 3 elements per key
  # 0 element: # of days to complete task
  # 1 element: # time it takes per day
  # 2 element: The date that it is due
  #sunday:1
  #monday:2
  #tuesday:3
  #wednesday:4
  #thursday:5
  #friday:6
  #saturday:7
  #activity name:[the threat level, the day its due, how many days to work, mins each day]
  for activity in storage:
    if storage[activity][0] == 1:
        storage[activity].append(1) #append the number of days to spend
        storage[activity].append(15) #append the number of mins to spend each day

    elif storage[activity][0] == 2:
        storage[activity].append(1) #append the number of days to spend
        storage[activity].append(30) #append the number of mins to spend each day
    
    elif storage[activity][0] == 3:
        storage[activity].append(1)#append the number of days to spend
        storage[activity].append(45)#append the number of mins to spend each day
  #------------------------------------------------------------------------------------

    elif storage[activity][0] == 4:
        if storage[activity][1] == 2:
            storage[activity].append(1)#append the number of days to spend
            storage[activity].append(60)#append the number of mins to spend each day
        else:
            storage[activity].append(2)#append the number of days to spend
            storage[activity].append(30)#append the number of mins to spend each day
    
    elif storage[activity][0] == 5:
      
        if storage[activity][1] == 2:
            storage[activity].append(1)#append the number of days to spend
            storage[activity].append(90)#append the number of mins to spend each day
        else:
            storage[activity].append(2)#append the number of days to spend
            storage[activity].append(45)#append the number of mins to spend each day

    elif storage[activity][0] == 6:
        if storage[activity][1] == 2:
            storage[activity].append(1)#append the number of days to spend
            storage[activity].append(120)#append the number of mins to spend each day
        else:
            storage[activity].append(2)#append the number of days to spend
            storage[activity].append(60)#append the number of mins to spend each day
#---------------------------------------------------------------------------------------
    elif storage[activity][0] == 7:
      
        if storage[activity][1] == 2: # 2 = monday
            storage[activity].append(1)
            storage[activity].append(180)
        elif storage[activity][1] == 3: # 3 = tuesday
            storage[activity].append(2)
            storage[activity].append(90)
        else:
            storage[activity].append(3)#append the number of days to spend
            storage[activity].append(60)#append the number of mins to spend each day

    elif storage[activity][0] == 8:
      
      if storage[activity][1] == 2:
        storage[activity].append(1)
        storage[activity].append(240)
      elif storage[activity][1] == 3:
        storage[activity].append(2)
        storage[activity].append(120)
      else:
        storage[activity].append(3)#append the number of days to spend
        storage[activity].append(80)#append the number of mins to spend each day

    elif storage[activity][0] == 9:

      if storage[activity][1] == 2:
        storage[activity].append(1)
        storage[activity].append(300)
      elif storage[activity][1] == 3:
        storage[activity].append(2)#append the number of days to spend
        storage[activity].append(150)#append the number of mins to spend each day
      else:
        storage[activity].append(3)
        storage[activity].append(100)

    elif storage[activity][0] == 10:
      
      if storage[activity][1] == 1:
        storage[activity].append(1)
        storage[activity].append(360)
      elif storage[activity][1] == 2:
        storage[activity].append(2)
        storage[activity].append(180)
      else:
        storage[activity].append(3)
        storage[activity].append(120)
  day_mins_arr = [["Sunday", 0], ["Monday", 0], ["Tuesday", 0], ["Wednesday", 0], ["Thursday", 0], ["Friday", 0], ["Saturday", 0]]
  avail_dict = storage.copy()

  # sorting alogrithm
  for activity in avail_dict:
    if avail_dict[activity][1] == 1: # if it's due on Sunday
      avail_dict[activity] = day_mins_arr[:1]
      avail_dict[activity] = Sort(avail_dict[activity])
    elif avail_dict[activity][1] == 2: # if it's due on Monday...
      avail_dict[activity] = day_mins_arr[:2]
      avail_dict[activity] = Sort(avail_dict[activity])
    elif avail_dict[activity][1] == 3:
      avail_dict[activity] = day_mins_arr[:3]
      avail_dict[activity] = Sort(avail_dict[activity])
    elif avail_dict[activity][1] == 4:
      avail_dict[activity] = day_mins_arr[:4]
      avail_dict[activity] = Sort(avail_dict[activity])
    elif avail_dict[activity][1] == 5:
      avail_dict[activity] = day_mins_arr[:5]
      avail_dict[activity] = Sort(avail_dict[activity])
    elif avail_dict[activity][1] == 6:
      avail_dict[activity] = day_mins_arr[:6]
      avail_dict[activity] = Sort(avail_dict[activity])
    elif avail_dict[activity][1] == 7:
      avail_dict[activity] = day_mins_arr[:7]
      avail_dict[activity] = Sort(avail_dict[activity])
    
   
    # inputting the current taks in the storage dictionary for future calculations
    for activity in storage:
        temp = storage.get(activity) # temp = activity
        
        if temp[1] == 1: # checking what day the activity (temp) is due
            day_mins_arr[0][1] += temp[3] # temp[3] is the time (in min)

        elif temp[1] == 2:
            day_mins_arr[1][1] += temp[3]

        elif temp[1] == 3:
            day_mins_arr[2][1] += temp[3]

        elif temp[1] == 4:
            day_mins_arr[3][1] += temp[3]

        elif temp[1] == 5:
            day_mins_arr[4][1] += temp[3]

        elif temp[1] == 6:
            day_mins_arr[5][1] += temp[3]

        elif temp[1] == 7:
            day_mins_arr[6][1] += temp[3]

  return avail_dict


def generate_calendar():
    calendar = tk.Tk()
    calendar.title("Calendar")
    calendar.geometry("900x400")
    calendar.grid_columnconfigure(0, weight=1)
    calendar.grid_columnconfigure(1, weight=1)
    calendar.grid_columnconfigure(2, weight=1)
    calendar.grid_columnconfigure(3, weight=1)
    calendar.grid_columnconfigure(4, weight=1)
    calendar.grid_columnconfigure(5, weight=1)
    calendar.grid_columnconfigure(6, weight=1)
    sunday = tk.Label(calendar, text="Sunday")
    monday = tk.Label(calendar, text="Monday")
    tuesday = tk.Label(calendar, text="Tuesday")
    wednsday = tk.Label(calendar, text="Wednsday")
    thursday = tk.Label(calendar, text="Thursday")
    friday = tk.Label(calendar, text="Friday")
    saturday = tk.Label(calendar, text="Saturday")
    sunday.grid(row = 0, column = 0)
    monday.grid(row = 0, column = 1)
    tuesday.grid(row = 0, column = 2)
    wednsday.grid(row = 0, column = 3)
    thursday.grid(row = 0, column = 4)
    friday.grid(row = 0, column = 5)
    saturday.grid(row = 0, column = 6)
    dic_to_calendar(manage_cal(), calendar)
    row1 = ttk.Separator(calendar, orient='horizontal')
    row1.grid(row = 1, columnspan = 7,  sticky = "ew")

    
def dic_to_calendar(dic, calendar):
    c = 2
    for x in dic:
        count = 0
        while count != storage[x][2]:
            block = tk.Label(calendar, text = x + " - " + str(storage[x][3]) + " minutes", pady = 15)
            if dic[x][count][0] == "Sunday":
                block.grid(row = c, column = 0)
            elif dic[x][count][0] == "Monday":
                block.grid(row = c, column = 1)
            elif dic[x][count][0] == "Tuesday":
                block.grid(row = c, column = 2)
            elif dic[x][count][0] == "Wednsday":
                block.grid(row = c, column = 3)
            elif dic[x][count][0] == "Thursday":
                block.grid(row = c, column = 4)
            elif dic[x][count][0] == "Friday":
                block.grid(row = c, column = 5)
            elif dic[x][count][0] == "Saturday":
                block.grid(row = c, column = 6)
            count += 1
        c += 1     


def restart_handler(): 
    for x in display_storage:
        x.destroy()
    for x in display_storage:
        display_storage.pop()
    storage.clear()
    


base = tk.Tk()
base.title("Input Window")
display_inputs = tk.Tk()
display_inputs.title("Current Stuff")
display_inputs.geometry("300x500")
restart = tk.Button(display_inputs, text = "Clear", command = restart_handler)
restart.pack()
#Input field block
input_field = tk.Entry(base)
input_field.insert(0, "Activity")
input_field.grid(row = 0, column = 1, sticky='')
input_field2 = tk.Entry(base)
input_field2.insert(0, "Priority (1-10)")
input_field2.grid(row = 1, column = 1, sticky='')
input_field3 = tk.Entry(base)
n3_list = [""]
base.geometry("300x200")
base.grid_columnconfigure(1, weight=1)



# displays the "combobox" for due date
#due_date = tk.StringVar()
day_cb = ttk.Combobox(base, height=8) #textvariable=due_date
day_cb.grid(row=3, column=1)
day_cb['values'] = ("Due Date", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_cb['state'] = 'readonly'
day_cb.current(0)

day_cb.bind('<<ComboboxSelected>>', day_changed)


input_button = tk.Button(base, text="Enter", command=get_info)
input_button.grid(row = 4, column = 1)

done = tk.Button(base, text = "Done", command=generate_calendar)
done.grid(row = 5, column = 1)
tk.mainloop()