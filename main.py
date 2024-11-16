import asyncio
import os
import logging
from pyppeteer import launch

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Путь к браузеру Chromium или Chrome
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Функция для проверки наличия файла браузера
def check_browser_path(path):
    if not os.path.exists(path):
        logging.error(f"Браузер не найден по пути: {path}")
        return False
    return True

async def main():
    # Проверка пути к браузеру
    if not check_browser_path(CHROME_PATH):
        return
    
    try:
        # Запуск браузера
        logging.info("Запуск браузера...")
        browser = await launch(
            headless=False,  # Установите True для работы без интерфейса
            executablePath=CHROME_PATH,  # Путь к браузеру
            args=['--no-sandbox', '--disable-setuid-sandbox'],  # Дополнительные аргументы для безопасности
        )
        
        # Открытие новой страницы
        page = await browser.newPage()
        
        # Переход на страницу
        logging.info("Переход на сайт...")
        await page.goto('https://www.google.com', {'waitUntil': 'domcontentloaded'})
        
        # Сделать скриншот
        logging.info("Сохранение скриншота...")
        await page.screenshot({'path': 'screenshot.png'})
        
        # Закрытие браузера
        logging.info("Закрытие браузера...")
        await browser.close()
    
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    asyncio.run(main())
