from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
import os
# 指定ChromeDriver的路径（如果没有将WebDriver添加到PATH）
# 如果WebDriver已添加到PATH，可以直接创建WebDriver实例
# driver_path = '/path/to/chromedriver'
# driver = webdriver.Chrome(driver_path)

# 创建ChromeOptions对象
options = Options()
# 设置浏览器启动时的参数，防止被网站检测到使用了自动化工具
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument("--headless")  # 无头模式，不显示浏览器窗口


# 编写函数，读取projectName.txt文件，遍历每一行
def readProjectName():
    with open('projectName.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)

# 对每一行的文字执行如下操作：
# 打开网页，找到//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/input输入框，将文字输入，点击搜索按钮,等待2s后找到//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[2]/h2并点击，打开网页后复制该网页链接并输出到output1.txt文件中
def searchForProject():
    with open('projectName.txt', 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            driver.get('https://www.citexs.com/nsfc')
            time.sleep(3)
            element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/input')
            element.send_keys(line)
            element.send_keys(Keys.RETURN)
            time.sleep(3)
            element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[2]/h2').click()
            time.sleep(3)
            # 切换网页到打开的新窗口
            driver.switch_to.window(driver.window_handles[-1])
            # 获取当前url
            current_url = driver.current_url
            print(current_url)
            time.sleep(2)
            print('opened')
            
            with open('output1.txt', 'a',encoding='utf-8') as file:
                file.write(current_url)
                file.write('\n')
            print('searchingProjectFinished')
            time.sleep(2)
            

# 打开output1.txt文件，遍历每一行的链接，打开并调用copyingProjectInformation()函数，将相关文献的链接保存到output2.txt文件中
def searchForRelevantLiterature():
    if os.path.exists('output1.txt'):
        with open('output1.txt', 'r') as file:
            lines = file.readlines()
    else:
        lines = []
        openProjectUrl = 'https://www.citexs.com/nsfcDetail?leader=%E5%BC%A0%E7%90%B3&institution=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6&title=%3Cmark%3E%E9%9D%A2%E5%90%91%E5%BA%94%E6%80%A5%3C%2Fmark%3E%3Cmark%3E%E4%BA%A4%E9%80%9A%3C%2Fmark%3E%3Cmark%3E%E7%96%8F%E6%95%A3%3C%2Fmark%3E%3Cmark%3E%E7%9A%84%3C%2Fmark%3E%3Cmark%3E%E9%A9%BE%E9%A9%B6%3C%2Fmark%3E%3Cmark%3E%E8%A1%8C%E4%B8%BA%3C%2Fmark%3E%3Cmark%3E%E5%BC%82%E8%B4%A8%E6%80%A7%3C%2Fmark%3E%3Cmark%3E%E5%BB%BA%E6%A8%A1%3C%2Fmark%3E%3Cmark%3E%E5%8F%8A%3C%2Fmark%3E%3Cmark%3E%E5%86%B3%E7%AD%96%3C%2Fmark%3E%E6%94%AF%E6%8C%81%E6%96%B9%E6%B3%95%E7%A0%94%E7%A9%B6&key=%E9%9D%A2%E5%90%91%E5%BA%94%E6%80%A5%E4%BA%A4%E9%80%9A%E7%96%8F%E6%95%A3%E7%9A%84%E9%A9%BE%E9%A9%B6%E8%A1%8C%E4%B8%BA%E5%BC%82%E8%B4%A8%E6%80%A7%E5%BB%BA%E6%A8%A1%E5%8F%8A%E5%86%B3%E7%AD%96&CnKey=&xueke=&isOverseas=false'
        line = openProjectUrl
        lines.append(line)
    
    for line in lines:
        print(line)
        driver.get(line)
        time.sleep(2)
        i = 1
        elements = []
        while True:
            try:
                element = driver.find_element(By.XPATH, f'//*[@id="pane-Search"]/div[{i}]/h2/a[1]')
                href = element.get_attribute('href')
                elements.append(href)
                i += 1
            except NoSuchElementException:
                break
        with open('output2.txt', 'a') as file:
            for element in elements:
                file.write(element + '\n')
            # file.write('\n') #输出完当前项目相关文献后是否需要空行
    
        print('searchingFinished')

# 遍历output2.txt里每一行的链接，打开并调用copyingLiteratureInformation()函数，将文献信息保存到output3.txt文件中
def startCopyLiteratureInformation():
    with open('output2.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            driver.get(line)
            time.sleep(2)
            copyingLiteratureInformation()

# 对当前文献网页的信息进行复制并输出
def copyingLiteratureInformation():
    
    element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[1]')
    content1 = element.text

    element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[2]')
    content2 = element.text

    element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[3]')
    content3 = element.text

    content = f'Content 1: {content1}\nContent 2: {content2}\nContent 3: {content3}\n'
    with open('output3.txt', 'a',encoding='utf-8') as file:
        file.write(content)
        file.write('\n')
    
    print('copyingFinished')
    return content



# 创建WebDriver实例
driver = webdriver.Chrome(options=options)



if __name__ == "__main__":

    # driver.get('https://www.citexs.com/nsfc')
    # time.sleep(20)
    # print('20秒内自行扫码登陆')
    
    # searchForProject()

    # 测试项目url
    searchForRelevantLiterature()

    # 测试相关文献url
    # openArticleUrl = 'https://www.citexs.com/allSearchDetail?wid=2165005617'
    # driver.get(openArticleUrl)
    # time.sleep(5)   
    startCopyLiteratureInformation()

    # 等待一段时间后关闭浏览器窗口
    time.sleep(1000) 
    driver.quit()
    