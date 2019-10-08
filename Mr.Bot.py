import requests
from bs4 import BeautifulSoup
import smtplib
URL = '#Product URL from amazon Website'
headers = {
    "User-Agent":
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def check_p():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    ##print(title.strip())
    converted_price = float(price[1:5]) ##this variable can only has 5 digit i.e 999.99

    if (converted_price < 999.00):
        send_mail()
    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('#source email id', '#source email password')
    subject = 'Loot Started'
    body = '##alert price has dropped to desire value'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('#source email id', '#recevier email id', msg)
    print("Mail Sent")

    server.quit()


check_p()
