from icalendar import Calendar
from datetime import datetime, timedelta

# 读取并解析ICS文件
with open('your_calendar.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())

total_duration = timedelta(0)  # 初始化总时间

# 遍历所有事件
for component in cal.walk('vevent'):
    dtstart = component.get('dtstart').dt
    dtend = component.get('dtend').dt
    # 确保dtstart和dtend是datetime对象
    if isinstance(dtstart, datetime) and isinstance(dtend, datetime):
        duration = dtend - dtstart
        total_duration += duration

# 打印所有日程总时间
print(f'Total duration of all events: {total_duration}')
