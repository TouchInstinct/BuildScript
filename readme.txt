Добавить символьную ссылку на скрипт сборки. Заменить <builder_path> на абсолютный путь к корню репозитория билд скрипта
sudo ln -s <builder_path>/scripts/TouchinBuild/taskRunner.py /user/local/bin/tibuild



Чтобы работала система сборки необходимо выполнить формальные шаги:
0. Убедиться что в собираемом проекте выбор профиля обеспечения и сертификата производится автоматически.
Так следует сделать чтобы любой разработчик мог собрать проект, на билд сервере будут подставлены необоходимы значения автоматически

1. Убедиться что в названии проекта нет пробелов.

1. В корне репозитория создать папку scripts
mkdir scripts

2. Положить в папку scripts профили обеспечения со следующими названиями
development.mobileprovision
distribution.mobileprovision 

2. В папке scripts создать папку settings.txt
touch scripts/settings.txt

3. Скопировать содержимое примера scripts/common/setting.txt в свой файл settings.txt и переопределить все необходимые настройки
Стоит обратить внимание на комментации 
# required – эти настройки необходимо задать, иначе ничего не будет работать
# dont change – это можно менять если есть четкое осознание того что происходит

4. вызвать скрипт, заменив параметры
на сервере
tibuild --settings=scripts/settings.txt build="0.0" builder_path=<builder_path>

локально. path_to_local_direcotry – путь к папке вне репозитория проекта (чтобы ничего не потерлось) или добавить папку в настройку
tibuild --settings=scripts/settings.txt build="0.0" builder_path=<builder_path> publish_path=<path_to_local_direcotry>