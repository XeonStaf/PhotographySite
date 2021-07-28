
States = [
    (1, "Отправлено", "#3ea635"),
    (2, "Обработка", "#b10006"),
    (3, "Выбрано", "#0091ff"),
    (4, "Необходимо Выбрать", "#fa6400"),
    (5, "Съемка назачена", "#8c00dd"),
    (6, "Создание мудборда", "#f7b500"),
]

States_for_model = []
for i in States:
    States_for_model.append((i[0], i[1]))


def permission(obj, request):
    return request.user and request.user.is_authenticated and (obj.linkUser == request.user or request.user.is_superuser)
