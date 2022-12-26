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
    # if not len(list_posts):
    #     return "Пост не найден!"
    # else:
    return list_posts

