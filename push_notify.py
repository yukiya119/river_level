import requests

# 必要な変数を設定
# 取得したトークン
TOKEN = 'T9lIdJSQ0Gk2w6N9FL7SR5rUFuk3RLCSS9T5eDhiTve'
# APIのURL
api_url = 'https://notify-api.line.me/api/notify'
# 送りたい内容
f = open('WATERLEVEL1.txt', 'r')
data = f.read()
send_message = data
send_contents = data
f.close()

# 情報を辞書型にする
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}
print(TOKEN_dic)
print(send_dic)

# LINE通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
requests.post(api_url, headers=TOKEN_dic, data=send_dic)
