## FLASK APP FROM STEP 3. TO 4.
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello from Flask!"

# if __name__ == "__main__":
#     app.run(debug=True)


##  FLASK APP FROM STEP 4. TO 7.
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# if __name__ == "__main__":
#     app.run(debug=True)


## FLASK APP FROM STEP 7. TO FINISHED
from flask import Flask
from config import Config
from blueprints.main import main_bp
from blueprints.api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
