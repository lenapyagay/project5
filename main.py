# Основная функция
def main():
    files = ["reviews1.docx", "reviews2.docx", "reviews3.docx"]
    all_product_names = []
    
    for file in files:
        product_names = retrieves_goods(file)
        all_product_names.extend(product_names)
    
    displays_names_in_a_table_format(all_product_names)

# Инициализованный скрипт
if __name__ == "main":
    main()
