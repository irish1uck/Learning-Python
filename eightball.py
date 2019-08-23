import random
def eightball():
	answers = ["It is certain.", "As I see it, yes.", "Reply hazy, try again.", "Don't count on it.", "It is decidely so.", "Most likely.", "Ask again later.", "My reply is no.", "Without a dout.", "Outlook good.", "Better not tell you now.", "My sources say no.", "Yes, definitely.", "Yes.", "Cannot predict now.", "Outlook not so good.", "You may rely on it.", "Signs point to yes.", "Concentrate and ask again.", "Very doubtful."]
	b = input("What do you want to know? ")
	a = random.randint(0, 19)
	print(answers[a])
