'''
Timer overflow calculation
'''
resolution=int(input("enter timer resolution: "))
system_freq=int(input("enter cpu freq: "))
prescaler=int(input("enter timer prescaler: "))

ticktime=prescaler/(system_freq*(10**6))
overflow=(ticktime* (2**resolution))*1000

print(f"the timer would overflow after {overflow} milliseconds")
