# Меню

### Домашняя страница - http://127.0.0.1:8000/base/
Использовал только django и стандартные библиотеки пайтона, sqlite (могу подмять всё под postgres, дело 5 минут)

Ссылки-заглушки введут по slug'ам (get_absolute_url), путь можно поменять в views,
изначально все ведется на ту же страницу.
Ссылки подсвечиваются в зависимости от выбранной категории.
Данные хранятся в бдшке sqlite, редактирование через админку.


Данные выводятся как через simple_tag, так и через inclusion,
функции идентичны, за исключением названия


    
```html
    {% draw_menu_inclusion 'имя' %}

    или 
    
    {% draw_menu_simple 'имя' %}
```
![img.png](images/img.png)
![img_2.png](images/img_2.png)
![img_3.png](images/img_3.png)


