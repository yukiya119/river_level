from bs4 import BeautifulSoup

from selenium import webdriver


def chromedriver_options():
        # オプション設定
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # ヘッドレスモード
        options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
        return options


URL1 = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204440'  # 五串(磐井川)
URL2 = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204450'  # 釣山(磐井川)
URL3 = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204270'  # 狐禅寺(北上川)
URL4 = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204310'  # 諏訪前(北上川)
URL5 = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204490'  # 十二木橋(砂鉄川)
URL6 = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=302041282204460'  # 妻神(砂鉄川)


def search_by_waterlevel_1(driver, waterlevel):
        driver.get(f'{URL1}')

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

        print(f'磐井川\n五串水位観測所\n日時:{dates} {times}\n水位:{waterlevels}')

        if (1.70 <= float(waterlevels)):
                print("五串水位観測所は、水防団待機水位(1.70m)を超過しています！")
                f = open('WATERLEVEL1.txt', 'w')
                f.write(f'【通報】\n磐井川\n五串水位観測所は{dates} {times}に水防団待機水位(1.70m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push1
                push1

        else:
                print("五串水位観測所は、平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel_1(driver, 1)


def search_by_waterlevel_2(driver, waterlevel):
        driver.get(f'{URL2}')

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

        print(f'磐井川\n釣山\n日時:{dates} {times}\n水位:{waterlevels}')

        if 6.50 <= float(waterlevels):
                print("釣山水位観測所は、氾濫危険水位(6.50m)を超過しています！")
                f = open('WATERLEVEL2.txt', 'w')
                f.write(f'【通報】\n磐井川\n釣山水位観測所は{dates} {times}に氾濫危険水位(6.50m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push2
                push2

        elif 5.90 <= float(waterlevels) < 6.50:
                print("釣山水位観測所は、避難判断水位(5.90m)を超過しています！")
                f = open('WATERLEVEL2.txt', 'w')
                f.write(f'【通報】\n磐井川\n釣山水位観測所は{dates} {times}に避難判断水位(5.90m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push2
                push2

        elif 2.60 <= float(waterlevels) < 5.90:
                print("釣山水位観測所は、氾濫注意水位(2.60m)を超過しています！")
                f = open('WATERLEVEL2.txt', 'w')
                f.write(f'【通報】\n磐井川\n釣山水位観測所は{dates} {times}に氾濫注意水位(2.60m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push2
                push2

        elif 1.80 <= float(waterlevels) < 2.60:
                print("釣山水位観測所は、水防団待機水位(1.80m)を超過しています！")
                f = open('WATERLEVEL2.txt', 'w')
                f.write(f'【通報】\n磐井川\n釣山水位観測所は{dates} {times}に水防団待機水位(1.80m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push2
                push2

        else:
                print("釣山水位観測所は、平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel_2(driver, 2)


def search_by_waterlevel_3(driver, waterlevel):
        driver.get(f'{URL3}')

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

        print(f'北上川\n狐禅寺\n日時:{dates} {times}\n水位:{waterlevels}')

        if 17.10 <= float(waterlevels):
                print("狐禅寺水位観測所は、氾濫危険水位(17.10m)を超過しています！")
                f = open('WATERLEVEL3.txt', 'w')
                f.write(f'【通報】\n北上川\n狐禅寺水位観測所は{dates} {times}に氾濫危険水位(17.10m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push3
                push3

        elif 16.80 <= float(waterlevels) < 17.10:
                print("狐禅寺水位観測所は、避難判断水位(16.80m)を超過しています！")
                f = open('WATERLEVEL3.txt', 'w')
                f.write(f'【通報】\n北上川\n狐禅寺水位観測所は{dates} {times}に避難判断水位(16.80m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push3
                push3

        elif 7.00 <= float(waterlevels) < 5.90:
                print("狐禅寺水位観測所は、氾濫注意水位(7.00m)を超過しています！")
                f = open('WATERLEVEL3.txt', 'w')
                f.write(f'【通報】\n北上川\n狐禅寺水位観測所は{dates} {times}に氾濫注意水位(7.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push3
                push3

        elif 4.00 <= float(waterlevels) < 7.00:
                print("狐禅寺水位観測所は、水防団待機水位(4.00m)を超過しています！")
                f = open('WATERLEVEL3.txt', 'w')
                f.write(f'【通報】\n北上川\n狐禅寺水位観測所は{dates} {times}に水防団待機水位(4.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push3
                push3

        else:
                print("狐禅寺水位観測所は、平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel_3(driver, 3)


def search_by_waterlevel_4(driver, waterlevel):
        driver.get(f'{URL4}')

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

        print(f'北上川\n諏訪前\n日時:{dates} {times}\n水位:{waterlevels}')

        if 8.80 <= float(waterlevels):
                print("諏訪前水位観測所は、氾濫危険水位(8.80m)を超過しています！")
                f = open('WATERLEVEL4.txt', 'w')
                f.write(f'【通報】\n北上川\n諏訪前水位観測所は{dates} {times}に氾濫危険水位(8.80m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push4
                push4

        elif 8.60 <= float(waterlevels) < 8.80:
                print("諏訪前水位観測所は、避難判断水位(8.60m)を超過しています！")
                f = open('WATERLEVEL4.txt', 'w')
                f.write(f'【通報】\n北上川\n諏訪前水位観測所は{dates} {times}に避難判断水位(8.60m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push4
                push4

        elif 5.50 <= float(waterlevels) < 8.60:
                print("諏訪前水位観測所は、氾濫注意水位(5.50m)を超過しています！")
                f = open('WATERLEVEL4.txt', 'w')
                f.write(f'【通報】\n北上川\n諏訪前水位観測所は{dates} {times}に氾濫注意水位(5.50m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push4
                push4

        elif 4.00 <= float(waterlevels) < 5.50:
                print("諏訪前水位観測所は、水防団待機水位(4.00m)を超過しています！")
                f = open('WATERLEVEL4.txt', 'w')
                f.write(f'【通報】\n北上川\n諏訪前水位観測所は{dates} {times}に水防団待機水位(4.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push4
                push4

        else:
                print("諏訪前水位観測所は、平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel_4(driver, 4)


def search_by_waterlevel_5(driver, waterlevel):
        driver.get(f'{URL5}')

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

        print(f'砂鉄川\n十二木橋\n日時:{dates} {times}\n水位:{waterlevels}')

        if 5.80 <= float(waterlevels):
                print("十二木橋水位観測所は、氾濫危険水位(5.80m)を超過しています！")
                f = open('WATERLEVEL5.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n十二木橋水位観測所は{dates} {times}に氾濫危険水位(17.10m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push5
                push5

        elif 3.70 <= float(waterlevels) < 5.80:
                print("十二木橋水位観測所は、避難判断水位(3.70m)を超過しています！")
                f = open('WATERLEVEL5.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n十二木橋水位観測所は{dates} {times}に避難判断水位(16.80m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push5
                push5

        elif 3.00 <= float(waterlevels) < 3.70:
                print("十二木橋水位観測所は、氾濫注意水位(3.00m)を超過しています！")
                f = open('WATERLEVEL5.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n十二木橋水位観測所は{dates} {times}に氾濫注意水位(7.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push5
                push5

        elif 2.20 <= float(waterlevels) < 3.00:
                print("十二木橋水位観測所は、水防団待機水位(2.20m)を超過しています！")
                f = open('WATERLEVEL5.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n十二木橋水位観測所は{dates} {times}に水防団待機水位(5.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push5
                push5

        else:
                print("十二木橋水位観測所は、平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel_5(driver, 5)


def search_by_waterlevel_6(driver, waterlevel):
        driver.get(f'{URL6}')

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

        print(f'砂鉄川\n妻神\n日時:{dates} {times}\n水位:{waterlevels}')

        if 8.70 <= float(waterlevels):
                print("妻神水位観測所は、氾濫危険水位(8.70m)を超過しています！")
                f = open('WATERLEVEL6.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n妻神水位観測所は{dates} {times}に氾濫危険水位(17.10m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push6
                push6

        elif 8.10 <= float(waterlevels) < 8.70:
                print("妻神水位観測所は、避難判断水位(8.10m)を超過しています！")
                f = open('WATERLEVEL6.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n妻神水位観測所は{dates} {times}に避難判断水位(16.80m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push6
                push6

        elif 5.60 <= float(waterlevels) < 8.10:
                print("妻神水位観測所は、氾濫注意水位(5.60m)を超過しています！")
                f = open('WATERLEVEL6.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n妻神水位観測所は{dates} {times}に氾濫注意水位(7.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push6
                push6

        elif 3.80 <= float(waterlevels) < 5.60:
                print("妻神水位観測所は、水防団待機水位(3.80m)を超過しています！")
                f = open('WATERLEVEL6.txt', 'w')
                f.write(f'【通報】\n砂鉄川\n妻神水位観測所は{dates} {times}に水防団待機水位(5.00m)を超過し、水位:{waterlevels}を観測しました')
                f.close()
                import push6
                push6

        else:
                print("妻神水位観測所は、平常水位です")


if __name__ == '__main__':
        driver = webdriver.Chrome()
        search_by_waterlevel_6(driver, 6)
