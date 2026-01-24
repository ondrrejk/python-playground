from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

languages = [
    {
        "id": "python",
        "title": "Python",
        "description": "High-level, general-purpose programming language known for its emphasis on code readability and simplicity.",
        "experience": "Beginner",
        "link": "/languages/python"
    },
    {
        "id": "golang",
        "title": "Golang",
        "description": "Statically typed, compiled programming language developed at Google and launched in 2009.",
        "experience": "Beginner",
        "link": "/languages/golang"
    },
    {
        "id": "bash",
        "title": "Bash",
        "description": "Unix shell and command-line interpreter primarily used for automating system administration tasks and writing shell scripts.",
        "experience": "Intermediate",
        "link": "/languages/bash"
    }
]

@main_bp.route("/")
def index():
    return render_template("index.html", languages=languages)

@main_bp.route("/about")
def about():
    return render_template("about.html")

@main_bp.route("/languages")
def languages_page():
    return render_template("languages.html", languages=languages)

@main_bp.route("/languages/<lang_id>")
def language_detail(lang_id):
    # Find the language by ID
    for lang in languages:
        if lang["id"] == lang_id:
            return render_template("languages/detail.html", language=lang)

    # If not found, return 404
    return "Language not found", 404
