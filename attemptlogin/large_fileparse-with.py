#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
login = 0 # for successful log ins
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed log in attempts is", loginfail)


with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as jfile:
    for line in jfile:
        if " -] Authorization" in line:
            login += 1
print("the number of successful log in attempts is", login)

print(line.split(" ")[-1])
