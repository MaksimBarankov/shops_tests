# Финальная прямая: готовим код к ревью

Поздравляем, вы уже почти закончили свой финальный проект! В следующем шаге вы отправите его на оценку сокурсникам, а сейчас время немного причесать его и довести до совершенства. Следуйте этим советам, чтобы получить максимальные баллы:

## 1. Убедитесь, что в репозитории есть все нужные файлы.
Все файлы, где хранятся страницы, лежат в отдельной папке `pages`. В итоге структура файлов и папок должна выглядеть так:

```
shops_tests/
├── pages/
│   ├── base_page.py
│   ├── basket_page.py
│   ├── locators.py
│   ├── login_page.py
│   ├── main_page.py
│   ├── product_page.py
│   └── __init__.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── test_main_page.py
├── test_product_page.py
```

Убедитесь, что ничего не потерялось. Обратите внимание обязательно на `conftest.py`.

---

## 2. Проверьте `requirements.txt`

Убедитесь, что там указаны нужные версии пакетов, как минимум:

```
pytest==5.1.1
selenium==3.14.0
```

Желательно, чтобы там не было лишнего. Помните, что задание будут проверять ваши сокурсники, и им вряд ли понравится ставить огромную кучу пакетов.

---

## 3. Проверьте, что все тесты запускаются и проходят

Убедитесь, что все тесты, описанные в `test_main_page.py` и `test_product_page.py`, запускаются и проходят (очевидно, за исключением тех, которые помечены как `xfail`/`skip`).

---

## 4. Проверьте стиль кода

- Представьте, что ваш код будет читать человек, который никогда не программировал и не автоматизировал тестирование — ему должно быть понятно, что происходит.
- Убедитесь, что все переменные, методы и классы, которые вы создаёте, называются осмысленно.
- Удалите весь ненужный закомментированный код, помним, что захламлять репозиторий лишним — плохой тон.

---

## 5. Убедитесь, что в `test_product_page.py` есть следующие тесты

- `test_user_can_add_product_to_basket`
- `test_guest_can_add_product_to_basket`
- `test_guest_cant_see_product_in_basket_opened_from_product_page`
- `test_guest_can_go_to_login_page_from_product_page`

Отмаркируйте эти тесты меткой:

```python
@pytest.mark.need_review
```

Не забудьте зарегистрировать метку, чтобы избежать предупреждений. Добавьте в `pytest.ini`:

```ini
[pytest]
markers =
    need_review: mark tests that need to be reviewed
```

Убедитесь, что при запуске с помощью следующей команды тесты запускаются и успешно проходят:

```bash
pytest -v --tb=line --language=en -m need_review
```

---

## 6. Проверьте, что все тесты написаны в стиле PageObject

- Нет `assert` в теле тестов — все методы действий и проверки выделены в отдельные методы в классах PageObject.
- Все селекторы находятся в `locators.py`.

---

## 7. Зафиксируйте изменения коммитом

- Не добавляйте локальные файлы окружения, файлы IDE и прочие вспомогательные вещи в отслеживаемые. Нужен только код!
- Пример команды для фиксации изменений:

```bash
git add .
git commit -m "Finalized project: cleaned up and added all required tests"
```

---

## 8. Сделайте пуш изменений в свой репозиторий

```bash
git push origin main
```

---

## 9. Откройте репозиторий на GitHub и перепроверьте пункты 1, 2, 4, 5 и 6

---

## 10. Порадуйтесь за себя и переходите к следующему шагу

🎉 Вы великолепны! 😊

# P.S. В тестах test_guest_can_add_product_to_basket добавлена параметризация в соответсвие с заданием, в то же время как для упрощения в тесте test_guest_can_go_to_login_page_from_product_page параметризации нет.