import glob, os

# каталог текстовых файлов
# измените на свой
path = './sorted/'
# паттерн поиска файлов по расширению
pattern = '*.txt'

glob_path = os.path.join(path, pattern)
list_files = glob.glob(glob_path)
# расширение нового файла установим как '.all'
new_file = 'new_file.all'

# чтение и запись
if list_files:
    for file_name in list_files:
        # открываем файл из 'list_files' на чтение
        # а новый общий файл 'new_file' на дозапись
        with open(file_name, 'r') as fr, open(new_file, 'a') as fw:
            # дописываем строку с названием файла
            fw.write(f'\n\n------------ {file_name}\n\n')

            # читаем данные построчно
            for line in fr:
                # если нужно, то здесь обрабатываем каждую строку 'line'
                # после обработки дописываем в общий файл
                fw.write(line)