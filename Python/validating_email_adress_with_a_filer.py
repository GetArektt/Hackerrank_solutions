import re
import string

def fun(s):
    flag = True
    try:
        username, websitename, extension = re.split("\@|\.",s)
    except ValueError:
        return False
    #print(username, websitename, extension)
    if username.isalnum() or re.search("-", s) or re.search("_",s): pass
    else: flag = False
    if websitename.isalnum(): pass
    else: flag = False
    if extension.isalpha() and len(extension) <= 3: pass
    else: flag = False
    
    if flag:
        return s

    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)