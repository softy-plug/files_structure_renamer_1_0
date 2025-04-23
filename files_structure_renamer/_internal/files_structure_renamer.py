input("Нажмите Enter для запуска программы")

import os

def rename_single_digit_files():
    # Получить текущую директорию
    current_directory = os.getcwd()
    
    # Целевые расширения
    extensions = ['.mp4', '.jpg', '.pdf', '.png', '.pptx', '.ppt']
    
    # Проверка файлов от 1 до 9
    for i in range(1, 10):
        for ext in extensions:
            old_name = f"{i}{ext}"
            new_name = f"0{i}{ext}"
            old_path = os.path.join(current_directory, old_name)
            new_path = os.path.join(current_directory, new_name)
            
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f'Renamed: "{old_name}" to "{new_name}"')

# Запуск функции
rename_single_digit_files()

input("Переименование завершено. Нажмите Enter для закрытия окна")

# softy_plug