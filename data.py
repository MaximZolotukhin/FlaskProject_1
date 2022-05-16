from flask import url_for

title = 'Russia Travel'
subtitle = "Для тех, кого отвлекают дома"
description = """Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, 
дизайн, разработку игр и управление продуктами """
departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
              "kazan": "Из Казани"}


tours = {
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description": "Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями.  "
                       "Высокие округлые окна добавляют общий стиль дома и были добавлены в дом в довольно "
                       "симметричном образце.",
        "departure": "nsk",
        "picture": "/static/img/Marina_Lake_Hotel_&_Spa.jpg",
        "price": 62000,
        "stars": "4",
        "country": "Куба",
        "nights": 6,
        "date": "2 марта",
    },
    2: {
        "title": "Baroque Hotel",
        "description": "Здание отеля имеет форму короткой буквы U. Два расширения связаны стеклянными нависающими "
                       "панелями. Второй этаж такого же размера, как и первый, который был построен точно над полом "
                       "под ним. Этот этаж имеет совершенно другой стиль, чем этаж ниже.",
        "departure": "ekb",
        "picture": "/static/img/Baroque_Hotel.jpg",
        "price": 85000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 8,
        "date": "12 января",
    },
    3: {
        "title": "Voyager Resort",
        "description": "Снаружи отель выглядит красиво и традиционно. Он был построен с белыми камнями и имеет еловые "
                       "деревянные украшения. Высокие, большие окна добавляют к общему стилю дома и были добавлены в "
                       "дом в основном симметричным способом.",
        "departure": "nsk",
        "picture": "/static/img/Voyager_Resort.jpg",
        "price": 63000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 11,
        "date": "7 февраля",
    },
    4: {
        "title": "Orbit Hotel",
        "description": "Каждый домик оборудован средней кухней и одной небольшой ванной комнатой, в нем также есть "
                       "уютная гостиная, две спальни, скромная столовая и большой подвал.  Небольшие треугольные окна "
                       "добавляют к общему стилю дома и были добавлены в дом в основном симметричным способом.",
        "departure": "msk",
        "picture": "/static/img/Orbit_Hotel.jpg",
        "price": 62000,
        "stars": "4",
        "country": "Индия",
        "nights": 9,
        "date": "22 января",
    },
    5: {
        "title": "Atlantis Cabin Hotel",
        "description": "Этот дом среднего размера имеет футуристический вид и находится в среднем состоянии. Интерьер "
                       "выполнен в насыщенных тонах. Двор небольшой и выглядит очень формально. Кроме того, "
                       "странные огни были замечены движущимися в доме ночью.",
        "departure": "msk",
        "picture": "/static/img/Atlantis_Cabin_Hotel.jpg",
        "price": 68000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "18 января",
    },
    6: {
        "title": "Light Renaissance Hotel",
        "description": "Этот крошечный дом выглядит довольно современно и находится в ужасном состоянии. Интерьер "
                       "выполнен в цветах, которые напоминают вам о тропическом лесу. Двор небольшой и заросший "
                       "дикими растениями. Кроме того, это было однажды показано в телесериале, демонстрирующем "
                       "необычно украшенные дома.",
        "departure": "spb",
        "picture": "/static/img/Light_Renaissance_Hotel.jpg",
        "price": 53000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 13,
        "date": "15 февраля",
    },
    7: {
        "title": "King's Majesty Hotel",
        "description": "Этот дом средних размеров выглядит немного старомодно и находится в среднем состоянии. "
                       "Интерьер выполнен в цветах, которые напоминают о весеннем цветнике. Двор среднего размера и "
                       "напоминает луг. Кроме того, он был построен над остатками дома, который был разрушен в "
                       "результате пожара.",
        "departure": "ekb",
        "picture": "/static/img/King's_Majesty_Hotel.jpg",
        "price": 72000,
        "stars": "5",
        "country": "Мексика",
        "nights": 9,
        "date": "22 января",
    },
    8: {
        "title": "Crown Hotel",
        "description": "Этот огромный дом почти выглядит инопланетянином и находится в среднем состоянии. Интерьер "
                       "выполнен в цветах, напоминающих апельсиновое дерево. Двор среднего размера и напоминает луг. "
                       "Кроме того, это место печально известного убийства.",
        "departure": "kazan",
        "picture": "/static/img/Crown_Hotel.jpg",
        "price": 44000,
        "stars": "4",
        "country": "Тайланд",
        "nights": 7,
        "date": "3 февраля",
    },
}

