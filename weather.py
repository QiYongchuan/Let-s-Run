import requests
from sys import exit
# r = requests.get('https://wttr.in/beijing', verify=False，proxies={"http": "http://111.233.225.166:1234"})
# input city name
# proxies={"http": "http://111.233.225.166:1234"}
#, verify=False
#  直接在powerShell中输入：Invoke-RestMethod https://wttr.in/qindao?lang=zh
def ask():
  print("请输入你要查询天气的城市:")
  city = input(">>  ")
  print(city)
  return city
# city = "nanjing"
# Display the message
# print('展示天气： ' + city)


# y = True  

def showWeather(city):
  #fetch the weather details
  show2 = '' if y == True else 'v2.'
  url = 'https://{}wttr.in/{}?lang=zh'.format(show2,city)
# url = 'https://baidu.com/{}'.format(city)
  res = requests.get(url)
  # display the result
  print(res.text)


menu= '''
\t****************菜单************************
\t*                                          *
\t*        1.天气视角1 💻                    *
\t*        2.天气视角2 📱                    *
\t*        3.继续查询其它城市天气 🌡️          *
\t*        4.退出    ⏏️                      *
\t*                                          *
\t********************************************       '''



def Corefunction():
  global y,city  # 声明全局变量
  city = ''
  y = True
  while True:
    print(menu)
    choice = input(">>")
    if choice.isdigit():
      choice = int(choice)
      if choice == 1:
        if city == '':
            city = ask()
        showWeather(city)
      elif choice ==2:
        if city == '':
            city = ask()
        y = False
        showWeather(city)
      elif choice ==3:
        Corefunction()
      elif choice ==4:
        print("Have a nice day! 🎈")
        exit(0)

    else:
      print("Man,learn to type a number  🔢 😠")  

def main():
  Corefunction()

main()