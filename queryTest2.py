import asyncio
from pyppeteer import launch

# 定义一个异步函数来获取网页内容
async def get_page_content(url):
    # 指定 Chromium 的执行路径
    browser = await launch(headless=True, executablePath='D:/chromium/chrome-win/chrome.exe')
    page = await browser.newPage()
    
    # 设置请求头
    await page.setExtraHTTPHeaders({
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Source': 'PC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    })
    
    # 设置Cookies，注意Pyppeteer设置cookie的方法略有不同，可能需要分别设置每个cookie
    await page.setCookie({
        'name': 'Hm_lvt_21490b61879a03667587a4b7869f9b95',
        'value': '1707023211',
        'domain': 'www.citexs.com'
    })
    # 根据需要添加更多的cookies

    # 访问URL
    await page.goto(url)
    # await page.waitForSelector('title')  # 等待页面标题加载完成，根据实际情况调整

    # 获取页面的内容
    content = await page.content()
    # title = await page.title()
    print('666')

    # 将内容写入文件
    with open('output3.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    await browser.close()

# 需要爬取的网页URL
url = 'https://www.citexs.com/nsfcDetail?leader=%E5%88%98%E6%B6%9B&institution=%E6%B2%B3%E5%8D%97%E8%B4%A2%E7%BB%8F%E6%94%BF%E6%B3%95%E5%A4%A7%E5%AD%A6&title=%3Cmark%3E%E5%9F%BA%E4%BA%8E%3C%2Fmark%3E%3Cmark%3E%E5%B9%BF%E4%B9%89%3C%2Fmark%3E%E5%9C%B0%E6%A0%87%E7%9A%84%3Cmark%3E%E5%AE%A4%E5%86%85%E8%A1%8C%E4%BA%BA%3C%2Fmark%3E%3Cmark%3E%E6%B7%B7%E5%90%88%3C%2Fmark%3E%3Cmark%3E%E6%84%9F%E7%9F%A5%3C%2Fmark%3E%3Cmark%3E%E5%AF%BC%E8%88%AA%3C%2Fmark%3E%3Cmark%3E%E6%96%B9%E6%B3%95%3C%2Fmark%3E&key=%E5%9F%BA%E4%BA%8E%E5%B9%BF%E4%B9%89%E5%9C%B0%E8%A1%A8%E7%9A%84%E5%AE%A4%E5%86%85%E8%A1%8C%E4%BA%BA%E6%B7%B7%E5%90%88%E6%84%9F%E7%9F%A5%E5%AF%BC%E8%88%AA%E6%96%B9%E6%B3%95&CnKey=&xueke=&isOverseas=false'

# 运行异步主函数
asyncio.get_event_loop().run_until_complete(get_page_content(url))
