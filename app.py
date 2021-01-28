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
              "corpus.custom.random",
              "corpus.custom.gettingtoknowyou")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg")
     return str(chatbot.get_response(userText))

@app.route("/blog")
def blog_page():
    return render_template("blogs.html", section_title='Brendan Ferris | Blog')

@app.route("/projects")
def projects_page():
    return render_template("projects.html", section_title='Brendan Ferris | Projects')

@app.route("/datasets")
def datasets_page():
    return render_template("datasets.html", section_title='Brendan Ferris | Datasets')

@app.route("/implementing_a_face_mask_detector_in_opencv")
def article1_page():
    return render_template("face_mask_detector.html", article_title='Brendan Ferris | Implementing a face mask detector in OpenCV.')

if __name__ == "__main__":
    app.run()
