from datetime import *

birthdate= datetime.strptime(input("Your birthday(d.m.y): "),"%d.%m.%Y")
age = datetime.now()-birthdate

print("Excellent! You survived {} seconds. ".format(age.total_seconds()))