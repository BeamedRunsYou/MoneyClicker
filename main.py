import time
import os
import random
import pickle
from colorama import Fore
a=input("would you like to load? y/n")
if a=="y":
  pass
else:
  pickle.dump("0 1 0 15 100 300 1000 5000 10000 100000 1000000 2000000 10000000 50000000 100000000 500000000 1000000000 10000000000 100000000000 200000000000 1000000000000", open("save.p", "wb"))
starter=pickle.load(open("save.p", "rb"))
starter2=starter.split()
money=int(starter2[0])
moneyperclick=int(starter2[1])
moneypersec=int(starter2[2])
shop1 = ["[1] CLICKER", 1, 0, 15]  #name, extra money per click, extra mps, cost
shop2 = ["[2] GRANDMA", 0, 1, 100]
shop3 = ["[3] BANKER", 1, 2, 300]
shop4 = ["[4] THOUSANDARE", 3, 5, 1000]
shop5 = ["[5] FARM", 5, 7, 5000]
shop6 = ["[6] MINE", 10, 10, 10000]
shop7 = ["[7] BANK", 50, 100, 100000]
shop8 = ["[8] MILLIONARE", 300, 300, 1000000]
shop9 = ["[9] BRONZE CLICKER", 1000, 0, 2000000]
shop10 = ["[10] ATM MACHINE", 700, 1000, 10000000]
shop11 = ["[11] MONEY POOL", 5000, 5000, 50000000]
shop12 = ["[12] MONEY GOD", 15000, 7000, 100000000]
shop13= ["[13] SILVER CLICKER", 100000, 0, 500000000]
shop14= ["[14] BILLIONARE", 50000, 75000, 1000000000]
shop15= ["[15] BILL GATES", 450000, 1000000, 10000000000]
shop16= ["[16] JEFF BESOS", 2000000, 10000000, 100000000000]
shop17= ["[17] ELON MUSK", 5000000, 20000000, 200000000000]
shop18= ["[18] TRILLIONARE", 50000000, 200000000, 1000000000000]
shop1[3]=int(starter2[3])
shop2[3]=int(starter2[4])
shop3[3]=int(starter2[5])
shop4[3]=int(starter2[6])
shop5[3]=int(starter2[7])
shop6[3]=int(starter2[8])
shop7[3]=int(starter2[9])
shop8[3]=int(starter2[10])
shop9[3]=int(starter2[11])
shop10[3]=int(starter2[12])
shop11[3]=int(starter2[13])
shop12[3]=int(starter2[14])
shop13[3]=int(starter2[15])
shop14[3]=int(starter2[16])
shop15[3]=int(starter2[17])
shop16[3]=int(starter2[18])
shop17[3]=int(starter2[19])
shop18[3]=int(starter2[20])

while True:
  pickle.dump(str(money)+" " + str(moneyperclick) + " " + str(moneypersec) + " " + str(shop1[3]) + " " + str(shop2[3]) + " " + str(shop3[3]) + " " + str(shop4[3]) + " " + str(shop5[3]) + " " + str(shop6[3]) + " " + str(shop7[3]) + " " + str(shop8[3]) + " " + str(shop9[3]) + " " + str(shop10[3]) + " " + str(shop11[3]) + " " + str(shop12[3]) + " " + str(shop13[3]) + " " + str(shop14[3]) + " " + str(shop15[3]) + " " + str(shop16[3]) + " " + str(shop17[3]) + " " + str(shop18[3]) + " ", open("save.p", "wb"))
  secmoney = time.time()
  print(Fore.GREEN + "You have " + str(money) + '💲 \n')
  print(Fore.WHITE + "money per click: " + str(moneyperclick))
  print("money per second: " + str(moneypersec))
  print("[ENTER] to continue, [W] to wipe save file. Autosave is ON")
  print('')
  print('')
  print("SHOP:")
  print(shop1[0] + " cost: " + str(shop1[3]) + ", " + shop2[0] + " cost: " + str(shop2[3]))
  print(shop3[0] + " cost: " + str(shop3[3]) + ", " + shop4[0] + " cost: " + str(shop4[3]))
  print(shop5[0] + " cost: " + str(shop5[3]) + ", " + shop6[0] + " cost: " + str(shop6[3]))
  print(shop7[0] + " cost: " + str(shop7[3]) + ", " + shop8[0] + " cost: " + str(shop8[3]))
  print(shop9[0] + " cost: " + str(shop9[3]) + ", " + shop10[0] + " cost: " + str(shop10[3]))
  print(shop11[0] + " cost: " + str(shop11[3]) + ", " + shop12[0] + " cost: " + str(shop12[3]))
  print(shop13[0] + " cost: " + str(shop13[3]) + ", " + shop14[0] + " cost: " + str(shop14[3]))
  print(shop15[0] + " cost: " + str(shop15[3]) + ", " + shop16[0] + " cost: " + str(shop16[3]))
  print(shop17[0] + " cost: " + str(shop17[3]) + ", " + shop18[0] + " cost: " + str(shop18[3]))
  print()
  buy = input('[enter]')
  if buy == "":
    pass
  elif str(buy) == "1":
    if money >= shop1[3]:
      money -= shop1[3]
      moneyperclick += shop1[1]
      moneypersec += shop1[2]
      shop1[3]+=round(0.1*shop1[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "2":
    if money >= shop2[3]:
      money -= shop2[3]
      moneyperclick += shop2[1]
      moneypersec += shop2[2]
      shop2[3]+=round(0.1*shop2[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "3":
    if money >= shop3[3]:
      money -= shop3[3]
      moneyperclick += shop3[1]
      moneypersec += shop3[2]
      shop3[3]+=round(0.1*shop3[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "4":
    if money >= shop4[3]:
      money -= shop4[3]
      moneyperclick += shop4[1]
      moneypersec += shop4[2]
      shop4[3]+=round(0.1*shop4[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "5":
    if money >= shop5[3]:
      money -= shop5[3]
      moneyperclick += shop5[1]
      moneypersec += shop5[2]
      shop5[3]+=round(0.1*shop5[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "6":
    if money >= shop6[3]:
      money -= shop6[3]
      moneyperclick += shop6[1]
      moneypersec += shop6[2]
      shop6[3]+=round(0.1*shop6[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "7":
    if money >= shop7[3]:
      money -= shop7[3]
      moneyperclick += shop7[1]
      moneypersec += shop7[2]
      shop7[3]+=round(0.1*shop7[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "8":
    if money >= shop8[3]:
      money -= shop8[3]
      moneyperclick += shop8[1]
      moneypersec += shop8[2]
      shop8[3]+=round(0.1*shop8[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "9":
    if money >= shop9[3]:
      money -= shop9[3]
      moneyperclick += shop9[1]
      moneypersec += shop9[2]
      shop9[3]+=round(0.1*shop9[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "10":
    if money >= shop10[3]:
      money -= shop10[3]
      moneyperclick += shop10[1]
      moneypersec += shop10[2]
      shop10[3]+=round(0.1*shop10[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "11":
    if money >= shop11[3]:
      money -= shop11[3]
      moneyperclick += shop11[1]
      moneypersec += shop11[2]
      shop11[3]+=round(0.1*shop11[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "12":
    if money >= shop12[3]:
      money -= shop12[3]
      moneyperclick += shop12[1]
      moneypersec += shop12[2]
      shop12[3]+=round(0.1*shop12[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "13":
    if money >= shop13[3]:
      money -= shop13[3]
      moneyperclick += shop13[1]
      moneypersec += shop13[2]
      shop13[3]+=round(0.1*shop13[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "14":
    if money >= shop14[3]:
      money -= shop14[3]
      moneyperclick += shop14[1]
      moneypersec += shop14[2]
      shop14[3]+=round(0.1*shop14[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "15":
    if money >= shop15[3]:
      money -= shop15[3]
      moneyperclick += shop15[1]
      moneypersec += shop15[2]
      shop15[3]+=round(0.1*shop15[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "16":
    if money >= shop16[3]:
      money -= shop16[3]
      moneyperclick += shop16[1]
      moneypersec += shop16[2]
      shop16[3]+=round(0.1*shop16[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "17":
    if money >= shop17[3]:
      money -= shop17[3]
      moneyperclick += shop17[1]
      moneypersec += shop17[2]
      shop17[3]+=round(0.1*shop17[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  elif str(buy) == "18":
    if money >= shop18[3]:
      money -= shop18[3]
      moneyperclick += shop18[1]
      moneypersec += shop18[2]
      shop18[3]+=round(0.1*shop18[3])
    else:
      print("not enough money!!!")
      time.sleep(0.5)
  else:
    pass
  money = money + moneyperclick
  secmoneyend = time.time()
  overallmoneysec = (round(secmoneyend) - round(secmoney)) * int(moneypersec)
  money = int(money) + overallmoneysec
  
  os.system("clear")

