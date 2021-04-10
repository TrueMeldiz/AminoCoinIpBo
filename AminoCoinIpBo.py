from colorama import init, Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.GREEN)
print(Style.NORMAL)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ ██▄██ ▀█▀ █▄░█ ▄▀▀▄ ▄▀▀ ▄▀▀▄ ▀█▀ █▄░█ ▀█▀ █▀▄ █▀▄ ▄▀▀▄")
print("█▄█ █░▀░█ ░█░ █▀██ █░░█ █░░ █░░█ ░█░ █▀██ ░█░ █▀░ █▀▄ █░░█")
print("▀░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░▀▀░ ░▀▀ ░▀▀░ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░ ▀▀░ ░▀▀░")
import amino
client = amino.Client()
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
client.login(email=email, password=password)
for z, name in enumerate(client.sub_clients().name, 1):
    print(f"{z}.{name}")

comid = input("Выберите Сообщество/Select community: ")

sub_client=amino.SubClient(comId=comid, profile=client.profile)

wallet=sub_client.get_wallet_history(size=50)
print("Получаем ip людей которые перевели вам монеты!")
for i in range(50): 
    if wallet.changedCoins[i] > 0:
        if wallet.description[i]!=None:
            print(wallet.description[i])
            print("IP/Айпи = " + wallet.sourceIp[i])