# 3_bars

Скрипт для нахождения ближайшего, самого большого и самого маленького бара
в наборе [открытых данных](http://data.mos.ru/opendata/7710881420-bary) о барах.


## База данных баров

Для работы со скриптом нужно скачать актуальную базу данных московский или других баров с
[портала открытых данных](http://data.mos.ru/opendata/7710881420-bary).


## Использование

```{r, engine='bash'}
$ python bars.py -f json_bars.json                                                          
BIGGEST BAR: Ночной клуб «Орфей» (1000 seats)                                                                     
SMALLEST BAR: БАР. СОКИ (0 seats)                                                                                 

Do you want to know the closest bar? (y/n) y                                                                      
Enter your coordinates (longitude and latitude): 37.607242 55.757926                                              

CLOSEST BAR: Бар «Стабильная линия» (Большая Никитская улица, дом 12, строение 2)
```

У скрипта есть единственный обязательный аргумент - `-f/--filename` - путь до файла с базой баров.

> Скрипт использует python 3 версии.


## Лицензия

[Creative Commons Attribution License](http://creativecommons.org/licenses/by/2.0/)
