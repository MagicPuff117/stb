import schedule
from screenshoter import take_screenshot

def main():
    # schedule.every(5).seconds.do(take_screenshot)
    schedule.every().day.at("00:30").do(take_screenshot)
    schedule.every().day.at("12:30").do(take_screenshot)
    while True:
        schedule.run_pending()



if __name__ == '__main__':
    main()
