import random


def authenticate(user, password):
    session_id = random.randint(1000, 9999)
    print('User authorized: {} {}'.format(user, password))
    print('Session ID: {}'.format(session_id))
    return session_id


def call_api(endpoint, session_id):
    print('Called {} with {}...'.format(endpoint, session_id))
    return 1  # Пока что всегда будем возвращать единицу как успешный ответ


def create_test(user, password):
    session_id = authenticate(user, password)  # Предположим, что функция authenticate возвращает

    # идентификатор сессии после аутентификации
    # В этом моменте у нас есть идентификатор сессии, который мы хотим использовать в наших тестах.
    def test_func(endpoint, expected_result):
        # Предположим, что функция call_api вызывает API с заданным идентификатором сессии
        response = call_api(endpoint, session_id)
        # Здесь мы используем идентификатор сессии, полученный на первом шаге.
        assert response == expected_result, f"Expected {expected_result}, got {response}"

    return test_func  # Возвращаем функцию теста


# Создаем функцию теста для определенного пользователя
test = create_test('user', 'password')

# Запускаем тесты
test('/endpoint1', 1)
test('/endpoint2', 1)
# И теперь все эти тесты используют тот же идентификатор сессии, который был получен при вызове функции create_test!
