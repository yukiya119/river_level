"""
今後の拡張を考慮し、10分ごとに定期実行するためのスケジュールモジュールを別に作成した。
"""

import time

import schedule


def task():
    pass

schedule.every(10).minutes.do(task)


def main():
    while True:
        task()
        schedule.run_pending()
        time.sleep(1)
