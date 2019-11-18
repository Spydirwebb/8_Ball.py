""" magic 8-ball from STP
credit for ascii art to unknown at https://www.asciiart.eu/sports-and-outdoors/billiards
"""
#dependencies
import random

#art
ball = ["        ____",
"    ,dP9CGG88@b,",
"  ,IP  _   Y888@@b,",
" dIi  (_)   G8888@b",
"dCII  (_)   G8888@@b",
"GCCIi     ,GG8888@@@",
"GGCCCCCCCGGG88888@@@",
"GGGGCCCGGGG88888@@@@...",
"Y8GGGGGG8888888@@@@P.....",
" Y88888888888@@@@@P......",
" `Y8888888@@@@@@@P'......",
"    `@@@@@@@@@P'.......",
"        \"\"\"\"........"]

answers = ["As I see it, yes",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don’t count on it",
"It is certain",
"It is decidedly so",
"Most likely",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Outlook good",
"Reply hazy, try again",
"Signs point to yes",
"Very doubtful",
"Without a doubt",
"Yes",
"Yes – definitely",
"You may rely on it"]
#functions
def print_ball():
    for i in ball:
        print(i)
def shake():
    rando = random.randint(0,len(answers)-1)
    print(rando)
    print(answers[rando])

#main
while(True):
    print("\nHere is your Magic 8 Ball")
    print_ball();
    print("Ask the Fates a question")
    choice = input("Give it a Shake?(y/n): ")
    if (choice == 'y'):
        while(True):
            shake()
            choice2 = input("Satisfied with your answer?(y/n): ")
            if(choice2 == 'y'):
                break
            else:                
                continue
    else:
        choice3 = input("Quit?(y/n): ")
        if (choice2 == 'y'):
            print("Putting it away. Goodbye")
            break
        else:
            continue


