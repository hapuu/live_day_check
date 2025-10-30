import datetime

today = datetime.date.today()
user_brith = (input("\n請輸入你的出生年份(範例:19850125)\n"))
date_user_brith = datetime.datetime.strptime(user_brith, "%Y%m%d")
live_day = (today-date_user_brith.date()).days
print("你已經活了",live_day,"天了!")
input("\n輸入任意鍵關閉視窗")

# """
# ヽ(=^･ω･^=)丿
#
# """