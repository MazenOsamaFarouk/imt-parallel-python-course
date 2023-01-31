# print pyramid
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
'''
i=0
j=0
line=""

while i<6:
    while j<i+1:
        line += "*"
        j+=1
    print(line)
    i+=1
    j=0
    line=""
j=0
while i>1:
    while j<i-1:
        line += "*"
        j+=1
    print(line)
    i-=1
    j=0
    line=""
'''
i=0
while i<6:
    print("*"*(i+1))
    i+=1

while i>1:
    print("*"*(i-1))
    i-=1
   
# get pip script: https://bootstrap.pypa.io/get-pip.py 