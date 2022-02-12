from bs4 import BeautifulSoup

from selenium import webdriver

"""
10分に１回情報を取得するスケジュールを組みたい
def job():
        get()

schedule.every(10).minutes.do(job) # 10分間隔で定期実行？

while True:
        schedule.run_pending()
        time.sleep(1) # １秒間のスリープを挿入
"""


def chromedriver_options():
        # オプション設定
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # ヘッドレスモード
        # options.add_argument("--blink-settings=imagesEnabled=false") # 画像無効
        return options


URL = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204440'


def search_by_waterlevel(driver, waterlevel):
        driver.get(f'{URL}')

        # ブラウザの読み込みが終わるのを待つ
        driver.implicitly_wait(10)

        iframe = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(iframe)

        # iframeのソースを取得し表データの'tr'タグの１番目（最新[0]）のみ取得する
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find_all("tr")[0]
        driver.close()

        dates = table.find_all("td")[0].text
        times = table.find_all("td")[1].text
        waterlevels = table.find_all("td")[2].text

        print(f'日時:{dates} {times}／水位:{waterlevels}')
        f = open('WATERLEVEL.txt', 'w')
        f.write(f'【通報】\n{dates} {times}に水防団待機水位を超過し、水位:{waterlevels}を観測しました')
        f.close()

        if (1.7 <= float(waterlevels)):
                print("水防団待機水位(1.7m)を超過しています！")
                import push.py
                push.py

        else:
                print("平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel(driver, 1)
