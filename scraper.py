import asyncio
from pyppeteer import launch

async def scraper():
    # launch the browser and a new page instance
    browser =await launch({"headless": False})
    page = await browser.newPage()

    # set the viewport of the page
    await page.setViewport({"width": 1280, "height": 720})

    # visit the target website
    await page.goto("https://www.scrapingcourse.com/infinite-scrolling")

    # scroll the page vertically
    await page.evaluate("""{window.scrollBy(0, document.body.scrollHeight);}""")

    # wait for page to load
    await page.waitFor(5000)

    # close the browser
    await browser.close()

# run the scraper function
asyncio.run(scraper())
