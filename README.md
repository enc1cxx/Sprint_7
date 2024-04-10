# Финальный проект 6 спринта по курсу "Автоматизатор тестирования на Python"

## Инструкция по запуску:

1. Создаем виртуальное окружение
   ```
   python -m venv venv
   ```
2. Активируем виртуальное окружение
   ```
   venv\Scripts\activate
   ```
3. Устанавливаем необходимые пакеты
   ```
   pip install -r requirements.txt
   ```
4. Запускаем тесты
   ```
   pytest --alluredir=allure_results
   ```
5. Генерируем отчёты
   ```
   allure serve allure_results
   ```
   

