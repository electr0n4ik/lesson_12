# photo upload
from flask import Blueprint, render_template, request, send_from_directory
from utils import *

# создаем блюпринт с настройкой папки шаблонов
loader_blueprint = Blueprint(
	'loader_blueprint',
	__name__,
  template_folder='templates')
# вьюшка, использую блюпринт вместо app
@loader_blueprint.route("/post")
def loader_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def page_add():
    photo = request.files["picture"]
    filename_photo = photo.filename

    if save_photo(filename_photo):
        text = request.form["content"] #request.form
        photo.save(f"loader/uploads/images/{filename_photo}")
        filepath = f"loader/uploads/images/{filename_photo}"
        save_text_in_jsonfile(filename_photo, text)
        return render_template("post_uploaded.html", picture=filename_photo, content=text)
    else:
        return save_photo(filename_photo)

