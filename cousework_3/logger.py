import logging

# Создаем новый логгер
logger = logging.getLogger("api_logs")
logger.setLevel(logging.INFO)
# Cоздаем ему обработчик
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/api_logs.txt', encoding='utf-8')

# Добавляем обработчик к журналу
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# Применяем форматирование к обработчику
console_handler.setFormatter(formatter_one)
file_handler.setFormatter(formatter_one)
