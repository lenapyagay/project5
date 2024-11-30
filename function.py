
# function модуль для импорта ф-ции для работы


# TODO - import 
from docx import Document

def retrieves_goods(file_path): # функция для извлечения названий товаров из документа
    """" Функция 1 """
    document = Document(file_path)
    product_names = []
    for paragraph in document.paragraphs:
        if paragraph.text.strip(): # проверка на наличие текста
            if len(paragraph.text.split()) < 5: #название короче 5 слов
                product_names.append(paragraph.text.strip())
    return product_names



def displays_names_in_a_table_format(product_names):
    """"Выводит названия товаров в табличном виде"""
    for i, name in enumerate(product_names, start=1):
        print(f'{i}. {name}')

  