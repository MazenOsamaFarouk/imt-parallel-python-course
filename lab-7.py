# string concatenation
# 'Mazen' + 'Osama' = 'MazenOsama'
# int + int = int
# int + float = float
# int + str   = error
# str + str  = concat.
'''
mazen = "Mazen"
osama = "Osama"

#fullname = mazen  + osama + ' '

fullname = mazen
fullname += osama
fullname += ' '
'''

# print(fullname)

sentence=input("please input your sentence: ")
reversed_sent=""

for ch in sentence:
    reversed_sent = ch + reversed_sent

print(f"the sentence mirrored is {reversed_sent}")


'''
"Mazen"

ch | reversed_sent
-------------------
'M'| 'M'
'a'| 'a' + 'M' -> 'aM'
'z'| 'z' + 'aM' -> 'zaM'


'''