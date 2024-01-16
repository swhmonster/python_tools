下面是一些icalendar常见组件和它们对应的属性：

## VCALENDAR
VCALENDAR 是iCalendar数据的根组件，它包含日历的元数据和实际的日历项（如VEVENT、VTODO等）。

常见属性包括：
- PRODID: 产品标识符，指定日历生成产品的唯一标识。 
- VERSION: iCalendar规范的版本号。 
- CALSCALE: 日历尺度（通常是"Gregorian"，即公历）。 
- METHOD: 用于指定日历数据的使用方式，如"REQUEST"、"REPLY"等。
## VEVENT
VEVENT 组件代表一个日历事件。

常见属性包括：
- SUMMARY: 事件的简短描述。 
- DTSTART: 事件开始时间。 
- DTEND: 事件结束时间（如果没有指定，持续时间可以通过DURATION属性来表示）。 
- DTSTAMP: 事件创建的时间戳。 
- UID: 事件的唯一标识符。 
- DESCRIPTION: 对事件的长描述。 
- LOCATION: 事件发生的地点。 
- SEQUENCE: 事件的修改次数。
## VTODO
VTODO 组件代表一个待办事项。

常见属性包括：
- SUMMARY: 待办事项的简短描述。
- DUE: 完成期限。 
- STATUS: 待办项的状态，如“NEEDS-ACTION”，“COMPLETED”，“IN-PROCESS”等。 
- PRIORITY: 优先级。
## VJOURNAL
VJOURNAL 组件代表一个日记或日志条目。

常见属性包括：
- SUMMARY: 日志的标题。 
- DTSTART: 日志的日期。 
- DESCRIPTION: 日志的详细内容。
## VFREEBUSY
VFREEBUSY 组件代表一个时间段的忙闲信息。

常见属性包括：
- DTSTART: 查询开始时间。 
- DTEND: 查询结束时间。 
- FREEBUSY: 忙闲时间信息。
## VALARM
VALARM 组件提供了一种在特定时间触发提醒的机制。

常见属性包括：
- ACTION: 提醒时要采取的动作，如“DISPLAY”（显示一个文本提醒）。 
- TRIGGER: 提醒的触发时间。 
- DESCRIPTION: 提醒的描述。

这些是一些常用的组件和属性，但iCalendar规范定义了更多的组件和属性，详细内容可以参考RFC 5545规范文档。