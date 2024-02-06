import requests
from lxml import etree
import sys
import io

# 确保标准输出能够处理UTF-8编码的输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fetch_content_with_cookies_and_headers(url, cookies, headers):
    # 发送GET请求获取网页内容，带入cookie和自定义头部
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
        return None

def extract_content_from_html(html_content, xpath):
    tree = etree.HTML(html_content)
    content = tree.xpath(xpath)
    if content:
        return content[0].text  # 假设我们只关注第一个匹配项的文本内容
    else:
        return "No content found for the provided XPath."

if __name__ == "__main__":
    url = "https://www.citexs.com/nsfcDetail?leader=%E5%88%98%E6%B6%9B&institution=%E6%B2%B3%E5%8D%97%E8%B4%A2%E7%BB%8F%E6%94%BF%E6%B3%95%E5%A4%A7%E5%AD%A6&title=%3Cmark%3E%E5%9F%BA%E4%BA%8E%3C%2Fmark%3E%3Cmark%3E%E5%B9%BF%E4%B9%89%3C%2Fmark%3E%E5%9C%B0%E6%A0%87%E7%9A%84%3Cmark%3E%E5%AE%A4%E5%86%85%E8%A1%8C%E4%BA%BA%3C%2Fmark%3E%3Cmark%3E%E6%B7%B7%E5%90%88%3C%2Fmark%3E%3Cmark%3E%E6%84%9F%E7%9F%A5%3C%2Fmark%3E%3Cmark%3E%E5%AF%BC%E8%88%AA%3C%2Fmark%3E%3Cmark%3E%E6%96%B9%E6%B3%95%3C%2Fmark%3E&key=%E5%9F%BA%E4%BA%8E%E5%B9%BF%E4%B9%89%E5%9C%B0%E8%A1%A8%E7%9A%84%E5%AE%A4%E5%86%85%E8%A1%8C%E4%BA%BA%E6%B7%B7%E5%90%88%E6%84%9F%E7%9F%A5%E5%AF%BC%E8%88%AA%E6%96%B9%E6%B3%95&CnKey=&xueke=&isOverseas=false"  # 请替换为目标网页的URL
    cookies = {
        # 替换为实际的cookie名和值
        'Hm_lvt_21490b61879a03667587a4b7869f9b95': '1707023211',
        'temporaryToken': '674c16a8-7ca4-460b-8994-a17931b55d2f',
        'webIdentifier': '48e25624c871bf4f8469fce59160b420',
        'IsLimit': 'true',
        'update': 'true',
        'userlist': 'C4+T+wnyxE2C92g6wlYDlP2RqBew35Gb1Z44OVKWyz7chN9vyH9wBIVXqee6qaEdk0TSTZTEznPUS+AF5zDIomwRk83ElJNCMmBIvCUJFIHHRij9YjVQi3IUQl7y2BY4',
        'isdot': 'true',
        'isRemove': 'false',
        'Hm_lpvt_21490b61879a03667587a4b7869f9b95': '1707024142',
        'verifyLoginTime': '1707029994962'
    }
    headers = {
        # 添加完整的请求头
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Source': 'PC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    html_content = fetch_content_with_cookies_and_headers(url, cookies, headers)
    if html_content:
        xpath = "/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/h2"
        extracted_content = extract_content_from_html(html_content, xpath)
        print(extracted_content)
