from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 指定ChromeDriver的路径（如果没有将WebDriver添加到PATH）
# driver_path = '/path/to/chromedriver'
# driver = webdriver.Chrome(driver_path)

# 如果WebDriver已添加到PATH，可以直接创建WebDriver实例
driver = webdriver.Chrome()

try:
    # 打开网页
    driver.get('https://www.citexs.com/nsfc')

    # 等待页面加载完成
    time.sleep(5)  # 根据网速和页面响应时间调整等待时长
    print(driver.title)
    # 定位输入框并输入文本'111'
    input_element = driver.find_element(By.CSS_SELECTOR, 'input.el-input__inner')
    input_element.send_keys('111')

    # 如果需要提交表单，可以模拟按下Enter键
    # input_element.send_keys(Keys.RETURN)

finally:
    # 等待一段时间后关闭浏览器窗口，以便你可以看到输入结果
    time.sleep(10)  # 观察结果，然后关闭
    driver.quit()
