
# function модуль для импорта ф-ции для работы


# TODO - import 
from docx import Document

def retrieves_goods(file_path): # функция для извлечения названий товаров из документа
    document = Document(file_path)
    product_names = []
    for paragraph in document.paragraphs:
        for run in paragraph.runs:  # Проверка каждого текстового фрагмента
            if run.font.size and run.font.size.pt == 12:
                text = run.text.strip()
                if len(text.split()) <= 6:  # Условие для названия товара
                    product_names.append(text)
                
    return product_names

    



def displays_names_in_a_table_format(product_names):
    """"Выводит названия товаров в табличном виде"""
    for i, name in enumerate(product_names, start=1):
        print(f'{i}. {name}')

  