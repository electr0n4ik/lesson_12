# photo show

from flask import Blueprint, render_template

# создаем блюпринт с настройкой папки шаблонов
main_blueprint = Blueprint(
	'main_blueprint',
	__name__,
  template_folder='templates')

# вьюшка, использую блюпринт вместо app
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")
