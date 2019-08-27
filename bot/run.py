from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os

arr = os.listdir("data")

try:
	os.remove("db.sqlite3")
	os.remove("db.sqlite3-shm")
	os.remove("db.sqlite3-wal")
except:
	print("some thing went wrong")
chatbot = ChatBot('buddy',
	logic_adapters=[
        "chatterbot.logic.BestMatch",
		"chatterbot.logic.MathematicalEvaluation"
    ]
)
trainer = ListTrainer(chatbot)
for i in arr:
	file=open('data/'+i, 'r').readlines();
	#trainer.train('chatterbot.corpus.english')
	trainer.train(file)

while True:

	
	#req=input("Enter:");
	print(req);
	if req=="Could not understand please try again":
	
	elif req=="Something went wrong":
		voiceEngine.say(req)
		voiceEngine.runAndWait()
		break;
	else:
		response = str(chatbot.get_response(req))
		print(response)
		if response=="%ex%":
			response="have a nice day"
			voiceEngine.say(response)
			voiceEngine.runAndWait()
			break;
		
		voiceEngine.say(response)
		voiceEngine.runAndWait()
		
