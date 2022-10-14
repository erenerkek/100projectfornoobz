import random
from time import sleep
import random

answers = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.",
"Outlook good.","Yes.","Signs point to yes.","Reply hazy, Try Again.","Ask again later.","Better not tell you now.","Cannot predict now","Concentrate and ask again.",
"Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful." ]

print(("-"*30)+"\nMagic Eight Ball\n"+("-"*30))
sleep(1)
choice="y"
while choice == "y":
    choice = input("Are you ready to ask your question?(y/n)")
    print("Give some time for ball...")
    sleep(2)
    print(random.choice(answers))
    sleep(3)
    choice = input("Do you want to ask again another question?(y/n)")
