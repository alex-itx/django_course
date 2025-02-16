from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()  # связываем с моделью
        try:
            user = user_model.objects.get(email=username)  # логика подмены username на еmail
            if user.check_password(password):  # проверка пароля
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None


    def get_user(self, user_id):  # возврат объекта пользователя (без этого мы не авторизуемся)
        user_model = get_user_model()  # получаем объект юзера
        try:
            return user_model.objects.get(pk=user_id)  # возвращаем объект
        except user_model.DoesNotExist:
            return None