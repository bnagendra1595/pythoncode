def calculate_survival_duration():
  print("what is your age?")
  age=int(input())
  print("please choose the time unit: months, weeks, days, hours, minutes, seconds")
  # Split by comma and space to allow for more flexible user input
  time_units=input().lower().split(", ")  
  # calculate survival duration in seconds
  survival_duration_seconds = age*365.25*24*60*60  # This line was moved inside the function
  # convert seconds to different time units
  survival_duration_months = survival_duration_seconds//(30*24*60*60)
  survival_duration_weeks = survival_duration_seconds//(7*24*60*60)
  survival_duration_days = survival_duration_seconds//(24*60*60)
  survival_duration_hours = survival_duration_seconds//(60*60)
  survival_duration_minutes = survival_duration_seconds//60
  # print the results based on user selection
  print("you have lived for.")
  if 'months'in time_units:
     print(f"{survival_duration_months}months")
  if 'weeks' in time_units:
     print(f"{survival_duration_weeks}weeks")
  if 'days' in time_units:
    print(f"{survival_duration_days}days")
  if 'hours'in time_units:
    print(f"{survival_duration_hours}hours")
  if 'minuts' in time_units: #Typo here, should be 'minutes'
    print(f"{survival_duration_minutes}minutes")
  if 'seconds' in time_units:
    print(f"{round(survival_duration_seconds)}seconds")

calculate_survival_duration() # Call the function to execute it
