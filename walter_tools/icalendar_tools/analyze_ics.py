from icalendar import Calendar

# 从文件中读取日历数据
with open('my_calendar.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())

for component in cal.walk():
    if component.name == "VEVENT":
        print("Summary: ", component.get('summary'))
        print("Start: ", component.get('dtstart').dt)
