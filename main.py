import asyncio
from pyppeteer import launch

async def main():
    # Запускаем браузер в фоновом режиме
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://example.com')  # Переходим на сайт
    await page.screenshot({'path': 'example.png'})  # Делаем скриншот
    await browser.close()

# Запуск асинхронного цикла
asyncio.get_event_loop().run_until_complete(main())
