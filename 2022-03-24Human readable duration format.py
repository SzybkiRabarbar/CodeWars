'''
https://www.codewars.com/kata/52742f58faf5485cae000b9a/solutions/python
'''

def format_duration(seconds:int):
    if not seconds: return 'now'
    content = []
    years = int(seconds/31536000)
    if years == 1:
        content.append('1 year')
    elif years:
        content.append(str(years)+' years')
    days = int((seconds-(31536000*years))/86400)
    if days == 1:
        content.append('1 day')
    elif days:
        content.append(str(days)+' days')
    hh = int((seconds-(31536000*years)-(86400*days))/3600)
    if hh == 1:
        content.append('1 hour')
    elif hh:
        content.append(str(hh)+' hours')
    mm = int((seconds-(31536000*years)-(86400*days)-(3600*hh))/60)
    if mm == 1:
        content.append('1 minute')
    elif mm:
        content.append(str(mm)+' minutes')
    ss = int(seconds-(31536000*years)-(86400*days)-(3600*hh)-(60*mm))
    if ss == 1:
        content.append('1 second')
    elif ss:
        content.append(str(ss)+' seconds')
    if len(content) > 1: content.insert(-1, "and")
    if len(content) >= 4: content[-4] += ','
    if len(content) >= 5: content[-5] += ','
    if len(content) >= 6: content[-6] += ','

    return " ".join(content)

print(format_duration(11113601))