from icalendar import Calendar
from datetime import datetime, timedelta
from collections import defaultdict

# 读取并解析ICS文件
with open('your_calendar.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())

# 使用defaultdict来存储每个月的时间总和
monthly_durations = defaultdict(timedelta)

# 遍历所有事件
for component in cal.walk('vevent'):
    dtstart = component.get('dtstart').dt
    dtend = component.get('dtend').dt
    # 确保dtstart和dtend是datetime对象
    if isinstance(dtstart, datetime) and isinstance(dtend, datetime):
        duration = dtend - dtstart
        # 使用年份和月份作为键
        month_year = (dtstart.year, dtstart.month)
        monthly_durations[month_year] += duration

# 按月份排序并打印总时间
for month_year in sorted(monthly_durations):
    year, month = month_year
    duration = monthly_durations[month_year]
    print(f'{year}-{month:02d}: Total duration of events: {duration}')
