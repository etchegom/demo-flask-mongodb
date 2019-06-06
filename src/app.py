from flask import Flask
from flask_mongoengine import MongoEngine
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object("settings")

db = MongoEngine()
db.init_app(app)

app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
admin = Admin(app, name="microblog", template_mode="bootstrap3")


@app.route("/")
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


if __name__ == "__main__":
    app.run(debug=True)
