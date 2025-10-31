import datetime

today = datetime.date.today() #變數 今天的日期
user_brith = (input("\n請輸入你的出生年份(範例:19850125)\n")) #變數 使用者的出生日期
date_user_brith = datetime.datetime.strptime(user_brith, "%Y%m%d") #變數 這裡透過datetime類別的strptime物件設定格式，確保能與 today變數相減
live_day = (today-date_user_brith.date()).days #想減後取天數屬性
print("你已經活了",live_day,"天了!") #顯示天數
input("\n輸入任意鍵關閉視窗")

# """
# ヽ(=^･ω･^=)丿
#

# """
