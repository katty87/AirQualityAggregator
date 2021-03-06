# AirQualityAggregator

## Цели проекта

 1. Собрать данные о качестве воздуха в Москве из различных источников в одном месте
 2. Настраивать отслеживаемые станции для конкретного пользователя
 3. Обеспечить объективное отображение данных 
 4. Возможность сравнивать данные из различных источников на графиках
 5. Обеспечить масштабируемость с перспективой расширения на большее количество сервисов
 
 ## Что планировалось
 
 Знания до курса: отсутствие опыта разработки на Python
 Значительную часть времени заняла подготовка к проекту: анализ различных сервисов оценки качества воздуха и способов получения данных.
 Время, затраченное на проект: 3 недели, порядка 50 часов
 
 ## Используемые технологии
 
 1. Python
 2. Django
 3. PostgreSQL
 4. Django ORM
 5. Celery 
 6. Redis
 7. MatPlotLib
 8. FactoryBoy
 9. Docker-compose
 
 ## Результат
 
 Сайт, агрегирующий данные с официального сайта Мосэкомониторинга (скраппинг) и независимого мониторинга AirCms
 
 Настройки пользователя
 
 ![Alt text](img/User_settings.png?raw=true)
 
 Настройка станций 
 
 ![Alt text](img/My_stations_settings_all.png?raw=true )
 
 Избранные станции 
 
 ![Alt text](img/My_stations_settings.png?raw=true)
  
  
 Ситуация в городе 
 
 ![Alt text](img/Main_screen_by_service.png?raw=true)  
 
 График изменения за последние сутки
 
 ![Alt text](img/Graph_station_substance.png?raw=true) 
 
 Группировка по загрязняющему веществу
 
 ![Alt text](img/Main_screen_by_substance.png?raw=true)  
 
 График изменения за последние сутки
 
 ![Alt text](img/Graph_by_services.png?raw=true)   
 
 Данные только избранных станций
 
 ![Alt text](img/My_stations_by_service.png?raw=true)     
 
 ![Alt text](img/My_stations_by_substance.png?raw=true)  
 
 График изменения концентрации загрязняющего вещества на избранных станциях
 
 ![Alt text](img/My_stations_graph_by_substance.png?raw=true) 
 
 ## Схемы

Схема БД

![Alt text](img/ErScheme.png?raw=true)
 
 ## Дальнейшее развитие
  1. Интернационализация
  2. Отображение графиков за неделю и за месяц
  3. Просмотр истории за произвольный период
  4. Отображение и выбор станцией на карте 
  5. Секционирование таблицы с измерениями