# What is the difference between the year attribute and the isocalendar method?
from datetime import date

today = date.today()

today_year = today.year # returns year
iso_year = today.isocalendar()[0] # isocalendar returns a tupe with iso year, iso week and iso weekday

print(today_year)
print(iso_year)