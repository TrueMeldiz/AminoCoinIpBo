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
print("Telegram: @NowNameBo")
print("▄▀▄ ██▄██ ▀█▀ █▄░█ ▄▀▀▄ ▄▀▀ ▄▀▀▄ ▀█▀ █▄░█ ▀█▀ █▀▄ █▀▄ ▄▀▀▄")
print("█▄█ █░▀░█ ░█░ █▀██ █░░█ █░░ █░░█ ░█░ █▀██ ░█░ █▀░ █▀▄ █░░█")
print("▀░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░▀▀░ ░▀▀ ░▀▀░ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░ ▀▀░ ░▀▀░")
import amino
client = amino.Client()
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]

sub_client=amino.SubClient(comId=communityid, profile=client.profile)

wallet=sub_client.get_wallet_history(size=50)
print("Получаем ip людей которые перевели вам монеты!")
for i in range(50): 
    if wallet.changedCoins[i] > 0:
        if wallet.description[i]!=None:
            print(wallet.description[i])
            print("IP/Айпи = " + wallet.sourceIp[i])
