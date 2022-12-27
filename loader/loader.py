# photo upload
from flask import Blueprint, render_template, request, send_from_directory
from utils import *

# создаем блюпринт с настройкой папки шаблонов
loader_blueprint = Blueprint(
	'loader_blueprint',
	__name__,
  template_folder='templates')

@loader_blueprint.route("/post")
def loader_page():
    """
    Обработка запрос при обращении к GET /post
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"]) # запрос при обращении к POST /post
def page_add():
    """
    PОбработка запроса при обращении к POST /post
    """
    try: #1 обработка ошибки "Ошибка при загрузке файла"
        photo = request.files.get("picture")
        filename_photo = photo.filename
        if save_photo(filename_photo): #2 обработка ошибки "Загруженный файл - не картинка (расширение не jpeg, png, gif)"
            text = request.form["content"]
            photo.save(f"./static/uploads/{filename_photo}")
            if save_text_in_jsonfile(filename_photo, text): #3 обработка ошибки "Файл posts.json отсутствует или не хочет превращаться в список"
                return render_template("post_uploaded.html", picture=filename_photo, content=text)
            else:
                return save_text_in_jsonfile(filename_photo, text)
        else:
            return save_photo(filename_photo)
    except:
        return "Ошибка при загрузке файла"

