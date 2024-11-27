# Основная функция
def main():
    files = ["reviews1.docx", "reviews2.docx", "reviews3.docx"]
    all_product_names = []
    
    for file in files:
        product_names = func1(file)
        all_product_names.extend(product_names)
    
    func2(all_product_names)

# Инициализованный скрипт
if __name__ == "main":
    main()
