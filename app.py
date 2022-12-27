from flask import Flask, request, render_template, send_from_directory
from utils import *

# Импортируем блюпринты из их пакетов
from main.main import main_blueprint
from loader.loader import loader_blueprint

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False
# Регистрируем первый блюпринт
app.register_blueprint(main_blueprint)
# Регистрируем второй блюпринт
app.register_blueprint(loader_blueprint)

@app.route('/search', methods=["GET", "POST"])
def search_page():
    """
    Поиск и вывод постов при обращении на /search/?s=<ключ поиска>
    """
    s = request.values.get("s") # через адресную строку можно делать поиск и через форму "найти"
    if len(s) == 0 or s.isdigit(): # обработка пустого или с цифрой запроса
        return render_template("search_empty.html")
    else:
        return render_template("post_list.html", s=s, posts=find_post(s))


@app.route("/static/<path:filename>")
def static_dir(filename):
    """
    Для отображения загруженных картинок
    """
    return send_from_directory("static", filename)

app.run(port=5000)
