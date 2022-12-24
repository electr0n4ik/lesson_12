# photo upload

from flask import Blueprint

# импортируем класс блюпринта
from flask import Blueprint

# создаем блюпринт
loader_blueprint = Blueprint('loader_blueprint', __name__)

# вьюшка, использую блюпринт вместо app
@loader_blueprint.route('/loader/<photo>')
def loader_page(photo):
    return f"Я страничка {photo}"
