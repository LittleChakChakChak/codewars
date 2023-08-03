# 4kyu
def format_duration(seconds):
    time = ''
    if seconds == 0:
        time = 'now'
# год
    if seconds >= 31536000:
        year = seconds // 31536000
        word = plural(year, 'year')
        time += f'{year} {word}'
        seconds -= 31536000 * year
        time += end(seconds, 86400)
# день
    if seconds >= 86400:
        days = seconds // 86400
        seconds -= 86400 * days
        word = plural(days, 'day')
        time += f'{days} {word}'
        time += end(seconds, 3600)
# час
    if seconds >= 3600:
        hours = seconds // 3600
        word = plural(hours, 'hour')
        time += f'{hours} {word}'
        seconds -= 3600 * hours
        time += end(seconds, 60)
# минута
    if seconds >= 60:
        minutes = seconds // 60
        word = plural(minutes, 'minute')
        time += f'{minutes} {word}'
        seconds -= 60 * minutes
        time += end(seconds, 1)
# секунда
    if seconds != 0:
        word = plural(seconds, 'second')
        time += f'{seconds} {word}'
    return time

def plural(time, word):
    if time != 1:
        word += 's'
    return word

def end(seconds, divider):
    if seconds % divider == 0 and seconds != 0:
        return ' and '
    elif seconds % divider != 0 and seconds != 0:
        return ', '
    else:
        return ''





print(format_duration(1)) # "1 second")
print(format_duration(62)) # "1 minute and 2 seconds")
print(format_duration(120)) # "2 minutes")
print(format_duration(3600)) # "1 hour")
print(format_duration(3662)) # "1 hour, 1 minute and 2 seconds")