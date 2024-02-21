как написать код на python которий должен делать следующее задание:
нужно из каталога D:\time_export вибрать все файли CSV.
дальше нужно прочитать каждий из них. внутри каждого файла есть примерно такое содержимое:
1;Банк;2;2;1720.00;1720.00;0.00;0.00;0;0;0.00;0.00;0.00;0.00;1720.00;1720.00;0.00;0.00;0.00;0.00;1720.00;1720.00;0.00;1720.00;1720.00;0.00;1720.00;1720.00;0.00;0;0.00;2;2;1720.00;0.00;
2;Пошта;0;0;0.00;0.00;0.00;0.00;0;0;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0;0.00;0;0;0.00;0.00;
3;Інтернатні установи;0;0;0.00;0.00;0.00;0.00;0;0;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0;0.00;0;0;0.00;0.00;
4;Інші установи;0;0;0.00;0.00;0.00;0.00;0;0;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0;0.00;0;0;0.00;0.00;
5;Всього (рядки 1+2+3+4);2;2;1720.00;1720.00;0.00;0.00;0;0;0.00;0.00;0.00;0.00;1720.00;1720.00;0.00;0.00;0.00;0.00;1720.00;1720.00;0.00;1720.00;1720.00;0.00;1720.00;1720.00;0.00;0;0.00;2;2;1720.00;0.00;

из чего ми видим что в каждом файле есть 5 строчек. при етом в файле нету строчки которую називают шапкой таблици, а просто сразу дание таблици.
в каждой строчке есть елементи: цифри, текст и числа которие между собой разделени точкой с запятой - ; всего 35 елементов в строке.

наша задача проверить в каждом файле из них следующее:

1) чтоб в первой строке второй елемент бил равен "Банк"
2) чтоб в второй строке второй елемент бил равен "Пошта"
3) чтоб в третей строке второй елемент бил равен "Інтернатні установи"
4) чтоб в четвертой строке второй елемент бил равен "Інші установи"
5) чтоб в пятой строке второй елемент бил равен "Всього (рядки 1+2+3+4)"

и если есть файл в котором найдено несоответствие то виводим пользователю "в файле (имя файла) во втором елементе такойто строки (номер строки) несоответствие".

дальше проверяем следующее:

6) чтоб в пятой строке третий елемент бил равен 30-му елементу и равен 32-му.

и если есть файл в котором найдено несоответствие то виводим пользователю "в файле (имя файла) в 5 строке такойто елемент (номер елемента) несоответствие".

дальше проверяем следующее:

7) чтоб в пятой строке четвертий елемент бил равен 33-му елементу.

и если есть файл в котором найдено несоответствие то виводим пользователю "в файле (имя файла) в 5 строке такойто елемент (номер елемента) несоответствие".

дальше проверяем следующее:

8) чтоб в пятой строке пятий елемент бил равен 31-му елементу и 34-му.

и если есть файл в котором найдено несоответствие то виводим пользователю "в файле (имя файла) в 5 строке такойто елемент (номер елемента) несоответствие".

в итоге ми должни получить список файлов красним цветом и описание к ним в каком из них какое несоответствие.
