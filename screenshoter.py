import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from PIL import Image, ImageDraw, ImageFont
from auth import TOKEN, ID




def take_screenshot():
    options = Options()
    options.add_argument('--no-sandbox')
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=options)
    driver.get('https://cgpeers.to/')
    driver.save_screenshot('picture.png')
    driver.close()
    add_watermark()


def send_screenshot():
        files = {
            'photo': open('picture.png', 'rb')
        }
        params = {
            'chat_id': ID
            }
        url = 'https://api.telegram.org/bot'+TOKEN+'/sendphoto'
        requests.get(url, data=params, files=files)




def add_watermark():
    im = Image.open('picture.png')
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = str(datetime.datetime.now())

    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(text, font)


    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x,y),text,(255,0,0),font=font)
    im.save('picture.png')
    send_screenshot()

