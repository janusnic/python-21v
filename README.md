# python-21v

# Python.

## История
Язык программирования Python был создан в 1991 году голландцем Гвидо ван Россумом. Свое имя - Пайтон - получил от названия телесериала.

Гвидо ван Россум (Guido van Rossum) ( https://www.python.org/~guido ) — голландский программист, прежде всего известный как автор языка программирования Python. Среди разработчиков Python Гвидо известен как «великодушный пожизненный диктатор» - Benevolent Dictator For Life (BDFL) проекта, это означает, что он продолжает наблюдать за процессом разработки Python, принимая окончательные решения, когда это необходимо.

![Guido van Rossum](/img/Guido_van_Rossum_OSCON_2006.jpg)

До разработки Python участвовал в проекте по написанию языка для обучения программированию — ABC. Лауреат «Free Software Award» 2001 года.

Сейчас работает в компании Dropbox Inc, покинув в декабре 2012 года корпорацию Google.

В своем эссе «Заселяя ноосферу» Эрик Рэймонд в частности обсуждает феномен «великодушной диктатуры» в сообществе свободного ПО. Согласно Рэймонду, «диктатор» свободного проекта обязан быть великодушным, поскольку если набирается достаточно разработчиков, несогласных с решениями «диктатора», они в любой момент могут уйти из проекта или создать форк.

## Примеры «великодушных пожизненных диктаторов»

- Адриан Головатый и Джекоб Каплан-Мосс — Django
- Гвидо ван Россум — Python
- Джимми Уэйлс — Wikipedia
- Дрис Бёйтарт — Drupal
- Ларри Уолл — Perl
- Линус Торвальдс — ядро Linux, в интервью согласился с тем, что он великодушный диктатор проекта, но при этом не упомянул слово «пожизненный».
- Марк Шаттлворт — Ubuntu Linux
- Патрик Фолькердинг — Slackware
- Расмус Лердорф — PHP
- Тэо де Раадт — OpenBSD

## Особенности
- Python – это интерпретируемый язык программирования: исходный код частями преобразуется в машинный в процессе выполнения специальной программой — интерпретатором.
- Python характеризуется ясным синтаксисом.
- Python – это полноценный, универсальный, язык программирования. Он разрабатывался как объектно-ориентированный язык.
- Python распространяется свободно на основании лицензии подобной GNU General Public License.

# Python 2 vs Python 3
Python 2 - эта версия предустанавливается на компьютеры с операционными системами семейства Linux.

Создатель языка Python Гвидо ван Россум и другие объединили решения трудных проблем и назвали их Python 3.

Python 2 — это прошлое, а Python 3 — будущее. Последняя версия Python 2 имеет номер 2.7, она еще долго будет поддерживаться, но на ней род заканчивается;
Python 2.8 никогда не выйдет. Новая разработка будет вестись на Python 3.

Самое очевидное изменение — это способ вызова функции print . Самое главное изменение — это обработка символов Unicode.
Преобразование популярного ПО, написанного на Python, выполняется постепенно.

# Установка Python

# Установка Python 3
В операционной системе Windows нет Python, а OS X, Linux и Unix, как правило, имеют старые версии. До тех пор пока это не исправили, вам, скорее всего, придется устанавливать Python 3 самостоятельно.

## Если у вас еще не установлен Python 3 или вы не знаете этого точно:

- определить, какая версия Python установлена на вашем компьютере, если она
есть;
- установить стандартный дистрибутив Python 3, если у вас его нет;
- установить дистрибутив Anaconda, содержащий научные модули Python;
- установить pip и virtualenv, если вы не можете изменять свою систему;
- установить conda в качестве альтернативы pip.

Страница What’s New in Python ( https://docs.python.org/3/whatsnew/ ) представляет информацию о том, что было добавлено в каждой версии.

Если вы хотите установить стандартный интерпретатор и библиотеки, используйте официальный сайт языка ( http://www.python.org/ ).

Если вы хотите использовать и стандартную библиотеку, и научные библиотеки, используйте Anaconda.

## Установка стандартной версии Python

- Перейдите в браузере на страницу загрузки Python ( http://www.python.org/download/ ).
- Она попробует определить вашу операционную систему и предоставить подходящие вам варианты. Если она ошибется, вы можете использовать следующие ссылки:

1. версии Python для Windows ( https://www.python.org/downloads/windows/ );
2. версии Python для Mac OS X ( https://www.python.org/downloads/mac-osx/ );
3. исходные коды Python (Linux и Unix) ( https://www.python.org/downloads/source/ ).

- Выберите ссылку Download (Загрузить) у наиболее свежей версии.
- Выберите ссылку, чтобы перейти на страницу определенной версии.
- Теперь выберите корректную версию для вашего компьютера.

## Mac OS X

- Щелкните на ссылке Mac OS X 64-bit/32-bit installer , чтобы загрузить файл с расширением .dmg для Mac.
- После завершения загрузки дважды щелкните на нем. Появится окно с четырьмя значками.
- Правой кнопкой мыши щелкните на Python.mpkg и затем в появившемся диалоговом окне нажмите кнопку Open (Открыть).
- Нажмите кнопку Continue (Продолжить) три раза, чтобы просмот­реть юридические детали, и затем, когда появится соответствующее диалоговое окно, нажмите кнопку Install (Установить).
- Python 3 будет установлен в каталог /usr/local/bin/python3 , что оставит существующую версию Python 2 нетронутой.

## Windows
Для Windows загрузите один из следующих установщиков:

- Windows x86 MSI installer (32-bit) ( http://bit.ly/win-x86 );
- Windows x86-64 MSI installer (64-bit) ( http://bit.ly/win-x86-64 ).

Чтобы определить, какая версия Windows у вас установлена (32- или 64-битная), сделайте следующее.

1.	 Нажмите кнопку Пуск .
2.	 Щелкните правой кнопкой мыши на пункте Мой компьютер .
3.	 Выберите пункт меню Свойства и найдите битовое значение.
Щелкните на соответствующем установщике (файл с расширением .msi ). После того как он будет загружен, щелкните на нем два раза и следуйте инструкциям.

## Linux или Unix
Пользователи Linux и Unix могут выбрать формат сжатия файлов исходного кода:

- сжатие с помощью XZ ( http://bit.ly/xz-tarball );
- сжатие с помощью Gzipped ( http://bit.ly/gzip-tarball ).

Загружайте любой из этих архивов. Разархивируйте его с помощью tar xJ (для файла с расширением .xz ) или tar xz (для файла с расширением .tgz ), а затем запустите полученный сценарий оболочки.

Python Documentation
==============
- Python Official Website : http://www.python.org/
- Python Documentation Website : www.python.org/doc/
- Марк Лутц, Изучаем Python (4-е издание)
- Марк Саммерфилд, Программирование на Python 3 подробное руководство.

Python Enhancement Proposal
===================

Аббревиатура «PEP» расшифровывается как Python Enhancement Proposal (предложение по расширению Python). Если кто-то желает изменить или дополнить язык Python, и его стремление пользуется широкой поддержкой сообщества, он посылает PEP с подробным описанием своего предложения, чтобы его можно было рассмотреть в официальном порядке; в некоторых случаях, как это произошло с PEP 3131, предложение принимается и реализуется. Все предложения PEP можно найти на странице www.py-thon.org/dev/peps/.

Этот документ создан на основе рекомендаций Гуидо ван Россума с добавлениями от Барри. Если где-то возникал конфликт, мы выбирали стиль Гуидо. И, конечно, этот PEP может быть неполным (фактически, он, наверное, никогда не будет закончен).

Ключевая идея Гуидо такова: код читается намного больше раз, чем пишется. Собственно, рекомендации о стиле написания кода направлены на то, чтобы улучшить читабельность кода и сделать его согласованным между большим числом проектов. В идеале, весь код будет написан в едином стиле, и любой сможет легко его прочесть. Как говорится в PEP 20 «Читабельность имеет значение».

Это руководство о согласованности и единстве. Согласованность с этим руководством очень важна. Согласованность внутри одного проекта еще важнее. А согласованность внутри модуля или функции — самое важное. Но важно помнить, что иногда это руководство неприменимо, и понимать, когда можно отойти от рекомендаций. Когда вы сомневаетесь, просто посмотрите на другие примеры и решите, какой выглядит лучше.

### Две причины, чтобы нарушить правила:
Когда применение правила сделает код менее читабельным даже для того, кто привык читать код, который следует правилам.
Чтобы писать в едином стиле с кодом, который уже есть в проекте и который нарушает правила (может быть, в силу исторических причин) — впрочем, это возможность подчистить чужой код.

# Дзэн Питона

Каждый язык программирования имеет свой стиль. В Python встроен
небольшой текст, который выражает его философию ( Python — это единственный язык программирования, содержащий подобное «пасхальное яйцо»).

Если интерпретатору Питона дать команду import this (импортировать "сам объект"), то выведется так называемый "Дзен Питона", иллюстрирующий идеологию и особенности данного языка. Глубокое понимание этого дзена приходит тем, кто сможет освоить язык Python в полной мере и приобретет опыт практического программирования.

1. Beautiful is better than ugly. Красивое лучше уродливого.
2. Explicit is better than implicit. Явное лучше неявного.
3. Simple is better than complex. Простое лучше сложного.
4. Complex is better than complicated. Сложное лучше усложнённого.
5. Flat is better than nested. Плоское лучше вложенного.
6. Sparse is better than dense. Разрежённое лучше плотного.
7. Readability counts. Удобочитаемость важна.
8. Special cases aren't special enough to break the rules. Частные случаи не настолько существенны, чтобы нарушать правила.
9. Although practicality beats purity. Однако практичность важнее чистоты.
10. Errors should never pass silently. Ошибки никогда не должны замалчиваться.
11. Unless explicitly silenced. За исключением замалчивания, которое задано явно.
12. In the face of ambiguity, refuse the temptation to guess. В случае неоднозначности сопротивляйтесь искушению угадать.
13. There should be one — and preferably only one — obvious way to do it. Должен существовать один — и, желательно, только один — очевидный способ сделать это.
14. Although that way may not be obvious at first unless you're Dutch. Хотя он может быть с первого взгляда не очевиден, если ты не голландец.
15. Now is better than never. Сейчас лучше, чем никогда.
16. Although never is often better than *right* now. Однако, никогда чаще лучше, чем прямо сейчас.
17. If the implementation is hard to explain, it's a bad idea. Если реализацию сложно объяснить — это плохая идея.
18. If the implementation is easy to explain, it may be a good idea. Если реализацию легко объяснить — это может быть хорошая идея.
19. Namespaces are one honking great idea — let's do more of those! Пространства имён — прекрасная идея, давайте делать их больше!

Если Python не будет соответствовать вашим потребностям, альтернативой в таком случае являются языки программирования С, С++ и Java, однако решением может стать и более новый язык программирования — Go ( http://golang.org/, который похож на Python, но имеет более высокую производительность, вроде С).

Онлайн-IDE
========
Pastebin
----------
- Python Fiddle http://pythonfiddle.com/
- ideone http://ideone.com/

облачные IDE
----------------
- Eclipse Orion http://www.eclipse.org/orion/
- Cloud9 IDE http://c9.io/
- Codenvy(eXo) Cloud IDE https://codenvy.com/
