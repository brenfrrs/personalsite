from flask import Flask, render_template, request, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)


chatbot = ChatBot(
    'Bren', storage_adapter="chatterbot.storage.SQLStorageAdapter")
# chatbot.storage.drop()
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


@app.route("/about")
def about_page():
    return render_template("about.html", section_title='Brendan Ferris | About')


@app.route("/implementing_a_face_mask_detector_in_opencv")
def article1_page():
    return render_template("face_mask_detector.html", article_title='Brendan Ferris | Implementing a face mask detector in OpenCV.')


@app.route("/scraping_amazon_results_with_selenium_and_python")
def article2_page():
    return render_template("scraping_amazon_selenium.html", article_title='Brendan Ferris | Scraping Amazon results with Selenium and Python')


@app.route("/a_brief_introduction_to_sed")
def article3_page():
    return render_template("intro_to_sed.html", article_title='Brendan Ferris | A Brief Introduction to Sed.')


@app.route("/cracking_the_zoom_host_code")
def article4_page():
    return render_template("zoom_host_code.html", article_title='Brendan Ferris | Cracking the Zoom Host Code (Theoretically)')


@app.route("/survival_analysis")
def article5_page():
    return render_template("survival_analysis.html", article_title='Brendan Ferris | Survival analysis: censoring, survival functions, hazard functions.')


@app.route("/postgres_basics")
def article6_page():
    return render_template("survival_analysis.html", article_title='Brendan Ferris | PostgreSQL: basics to get you up and running.')


if __name__ == "__main__":
    app.run()
