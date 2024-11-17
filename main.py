# Импортируем библиотеку json для работы с JSON-файлами
import json

# Запрашиваем у пользователя номер квалификации и преобразуем в целое число
number = int(input("Введите номер квалификации: ")) 

# Флаг, указывающий на то, найдена ли квалификация
find = False

# Открываем файл dump.json в режиме чтения с указанием кодировки UTF-8
with open("dump.json", 'r', encoding='utf-8') as file: 
  # Загружаем данные из JSON-файла в переменную data
  data = json.load(file) 
  # Проходим циклом по каждому элементу в загруженных данных
  for skill in data:
    # Проверяем, является ли текущий элемент квалификацией (model == "data.skill")
    if skill.get("model") == "data.skill": 
      # Проверяем, совпадает ли specialty текущей квалификации с номером, введенным пользователем
      if skill["fields"].get("specialty") == number: 
        # Если совпадает, сохраняем код и название квалификации
        skill_code = skill["fields"].get("code")
        skill_title = skill["fields"].get("title")
        # Устанавливаем флаг find в True, так как квалификация найдена
        find = True
      
        # Вложенный цикл для поиска информации о специальности
        for profession in data:
          # Проверяем, является ли текущий элемент специальностью (model == "data.specialty")
          if profession.get("model") == "data.specialty":
            # Получаем код специальности
            specialty_code = profession["fields"].get("code")
            # Проверяем, содержится ли код специальности в коде квалификации
            if specialty_code in skill_code: 
              # Если содержится, сохраняем название и тип образования специальности
              specialty_title = profession["fields"].get("title")
              specialty_educational = profession["fields"].get("c_type")


# Проверяем флаг find. Если квалификация не найдена, выводим соответствующее сообщение
if not find:
  print("=============== Не Найдено ===============") 
  
# Иначе выводим информацию о найденной квалификации и специальности
else:
  print("=============== Найдено ===============") 
  print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
  print(f"{skill_code} >> Квалификация '{skill_title}'")

