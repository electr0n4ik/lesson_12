# 1
def get_posts():
    """
    Загрузка списка постов из файла
    """
    import json

    with open("posts.json", encoding="utf-8") as file:
        posts = json.load(file)
    return posts


# 2
def find_post(search):
    """
    Получает запрос и возвращает список постов по данному запросу
    """

    list_posts = []
    for post in get_posts():
        if search.lower() in post["content"].lower():
            list_posts.append(post)

    if len(search) == 0 or len(list_posts) == 0:
        return "Пост не найден!"
    else:
        return list_posts

# 3
def save_photo(filename_photo):
    """
    Проверка картинки поста
    """
    extension = filename_photo.split(".")[-1]

    if extension in ['jpg', 'jpeg', 'gif', 'png']:
        return True
    else:
        return False

# 4
def save_text_in_jsonfile(filename, text):
    """
    Сохранение текста поста и адрес картинки в файл json
    """
    import json

    try:
        dict = {"content": text, "pic":filename}
        with open("posts.json", "r", encoding="utf-8") as file:
            posts = json.load(file)
            posts.append(dict)

        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False)

        return True
    except:
        return "Файл posts.json отсутствует или не хочет превращаться в список"