from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)


chatbot = ChatBot('Bren', storage_adapter="chatterbot.storage.SQLStorageAdapter")
#chatbot.storage.drop()
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("corpus.custom.professionalskills",
              "corpus.custom.oneliners",
              "corpus.custom.selfaware",
              "corpus.custom.help",
              "corpus.custom.random")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg")
     return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
