Добавить символьную ссылку на скрипт сборки. Заменить <builder_path> на абсолютный путь к корню репозитория билд скрипта
sudo ln -s <builder_path>/scripts/TouchinBuild/taskRunner.py /usr/local/bin/tibuild



Чтобы работала система сборки необходимо выполнить формальные шаги:
0. [iOS] Убедиться что в собираемом проекте выбор профиля обеспечения и сертификата производится автоматически.
Так следует сделать чтобы любой разработчик мог собрать проект, на билд сервере будут подставлены необоходимы значения автоматически

1. [iOS, Android] Убедиться что в названии проекта нет пробелов.

2. [iOS, Android] В корне репозитория создать папку scripts
mkdir scripts

3. [iOS] Положить в папку scripts профили обеспечения со следующими названиями
development.mobileprovision
distribution.mobileprovision 

4. [iOS, Android] В папке scripts создать файл settings.txt
touch scripts/settings.txt

5. [iOS, Android] Скопировать содержимое примера scripts/common/setting.txt в свой файл settings.txt и переопределить все необходимые настройки
Стоит обратить внимание на комментации 
# required – эти настройки необходимо задать, иначе ничего не будет работать
# dont change – это можно менять если есть четкое осознание того что происходит

6. [iOS, Android] вызвать скрипт, заменив параметры
на сервере. <builder_path> скорее всего это /BuildServer/Scripts
tibuild --settings=scripts/settings.txt build=%build.number% builder_path=<builder_path>

локально. path_to_local_direcotry – путь к папке вне репозитория проекта (чтобы ничего не потерлось) или добавить папку в настройку backup_ignore
tibuild --settings=scripts/settings.txt build=777 builder_path=<builder_path> publish_path=<path_to_local_direcotry>

Пояснение значения некоторых настроек:
publish_step_type – enum(development|distribution) – в зависимости от этого значения будет вызван один из следующих шагов
'ios publish development.txt' – копирование файла ipa в папку @publish_path/
'ios publish distribution.txt' - создание zip архива (app файла) и копирование его в папку @publish_path/
Это значение было введено чтобы поддерживать сборку с разными профилями обеспечения.
Типичный кейс. У нас 2 профайла:
development.mobileprovision – сборка для наших тестировщиков [publish_step_type=development]
distribution.mobileprovision – сборка для апстора [publish_step_type=distribution]
Расширенный кейс. У нас 3 профайла
development.mobileprovision – сборка для наших тестировщиков [publish_step_type=development]
customer.mobileprovision – сборка для тестировщиков заказчиков [publish_step_type=development]
distribution.mobileprovision – сборка для апстора [publish_step_type=distribution]
