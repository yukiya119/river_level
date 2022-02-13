from linebot import LineBotApi
from linebot.models import TextSendMessage

access_token = 'PM5nQhcEi9x28QElIhEMvCuc0OqOKyNkg6gn2spIF6HZvRuJh5gGQvj+BrXkPJPyT6tgT/VSwuJANTQboljjvQ1AXHL+9sDxmWgl4jiJdhyXGbnA6g/VLVMPnyos0J4q3gf8umL1tvoPczzVH7gitAdB04t89/1O/w1cDnyilFU='

# 送りたい内容
f = open('WATERLEVEL1.txt', 'r')
data = f.read()
send_message = data
send_contents = data
f.close()

line_bot_api = LineBotApi(access_token)
line_bot_api.broadcast(TextSendMessage(data))
