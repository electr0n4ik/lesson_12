# photo show

from flask import Blueprint

# импортируем класс блюпринта
from flask import Blueprint

# создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__)

# вьюшка, использую блюпринт вместо app
@main_blueprint.route('/')
def main_page(name):
    return f"Я main страничка!"
