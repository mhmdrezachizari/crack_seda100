import requests
from bs4 import BeautifulSoup
import time

# URL صفحه فرم
url = "https://seda100.ir/"

# تابع برای دریافت توکن جدید
def get_new_token(session, url):
    response = session.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find("input", {"name": "token"})['value']
        return token
    else:
        print("خطا در دریافت توکن:", response.status_code)
        return None

try:
    while True:
        session = requests.Session()
        
        token = get_new_token(session, url)
        if not token:
            print("عدم دریافت توکن! تلاش مجدد...")
            continue

        data = {
            "domain": "webdevhub.ir",  
            "token": token,            
            "submitAddNewScore": "1",  
            "score": "20"             
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Referer": url
        }

        response_post = session.post(url, headers=headers, data=data)

        if response_post.status_code == 200:
            print("درخواست با موفقیت ارسال شد!")
        else:
            print("خطا در ارسال درخواست:", response_post.status_code)
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("برنامه متوقف شد!")
