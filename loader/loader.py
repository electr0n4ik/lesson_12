# photo upload

from flask import Blueprint, render_template

# создаем блюпринт с настройкой папки шаблонов
loader_blueprint = Blueprint(
	'loader_blueprint',
	__name__,
  template_folder='templates2')
# вьюшка, использую блюпринт вместо app
@loader_blueprint.route('/loader/<photo>')
def loader_page(photo):
    return f"Я страничка {photo}"
