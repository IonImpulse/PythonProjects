from pyautogui import press, typewrite, hotkey
import random
import time
import pydirectinput
locations = [
    "[20:47:45] [Async Chat Thread - #2/INFO]: <IonImpulse> 1436 81 -361[m",
    "[20:47:49] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1393, 73, -43[m",
    "[20:47:54] [Async Chat Thread - #2/INFO]: <IceCaptain> 1391, 73, -365[m",
    "[20:47:54] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1385 73 -381[m",
    "[20:48:00] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1385, 73, -435[m",
    "[20:48:10] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1389, 73, -434[m",
    "[20:48:19] [Async Chat Thread - #2/INFO]: <IceCaptain> 1385 73 -365[m",
    "[20:48:23] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1373 73 -413[m",
    "[20:48:30] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1385, 73, -444[m",
    "[20:48:37] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1373 78 -412[m",
    "[20:48:40] [Async Chat Thread - #2/INFO]: <IceCaptain> 1385 73 -381[m",
    "[20:48:40] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1391, 73, -444[m",
    "[20:49:01] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1374, 77, 418[m",
    "[20:49:08] [Async Chat Thread - #2/INFO]: <IceCaptain> 1391 73 -385[m",
    "[20:49:14] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1419 71 -442[m",
    "[20:49:15] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1366, 83, -395[m",
    "[20:49:31] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1328, 71, -363[m",
    "[20:49:47] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1366, 83, -395[m",
    "[20:49:55] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1437 73 -447[m",
    "[20:50:00] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1351, 83, -402[m",
    "[20:50:03] [Async Chat Thread - #2/INFO]: <IceCaptain> 1432 80 -446[m",
    "[20:50:14] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1335. 73, -438[m",
    "[20:50:20] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1437 73 -418[m",
    "[20:50:23] [Async Chat Thread - #2/INFO]: <IceCaptain> 1419 71 -442[m",
    "[20:50:33] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1386, 73, -414[m",
    "[20:50:54] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1391, 71, -408[m",
    "[20:51:10] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1391, 75, -407[m",
    "[20:51:11] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1438 73 -408[m",
    "[20:51:27] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1395, 75, -421[m",
    "[20:51:39] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1412. 79, -418[m",
    "[20:51:47] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1418 80 -385[m",
    "[20:51:59] [Async Chat Thread - #2/INFO]: <IceCaptain> 1420 72 -402[m",
    "[20:52:01] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1419, 76, -430[m",
    "[20:52:10] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1411 73 -367[m",
    "[20:52:17] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1419, 71, -442[m",
    "[20:52:46] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1385, 73, -365[m",
    "[20:52:47] [Async Chat Thread - #2/INFO]: <Fozzy623> 1366 82 -394[m",
    "[20:52:54] [Async Chat Thread - #2/INFO]: <ColonelJJHawkins> 1336 84 -442[m",
    "[20:52:56] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1385, 73, -381[m",
    "[20:53:15] [Async Chat Thread - #2/INFO]: <DMR_Rocks> 1411, 73, -367[m",
    "[20:54:52] [Async Chat Thread - #3/INFO]: <ColonelJJHawkins> 1418 73 -4199[m",
    "[20:55:16] [Async Chat Thread - #3/INFO]: <ColonelJJHawkins> 1420 72 -402[m",
    "[21:25:00] [Async Chat Thread - #8/INFO]: <DMR_Rocks> 1411 73 -367[m",
    "[21:27:17] [Async Chat Thread - #9/INFO]: <DMR_Rocks> 1412 60 -411[m",
    "[21:27:59] [Async Chat Thread - #9/INFO]: <IonImpulse> 1428 73 -383[m",
    "[21:28:27] [Async Chat Thread - #9/INFO]: <DMR_Rocks> 1386 71 -393[m",
    "[21:28:34] [Async Chat Thread - #9/INFO]: <DMR_Rocks> 1386 73 -392[m",
    "[21:32:20] [Async Chat Thread - #10/INFO]: <DMR_Rocks> 1335 70 -379[m"

]

locations2 = [
    "[21:24:17] [Async Chat Thread - #8/INFO]: <arimeffie> 1424 73 -406",
    "[21:24:34] [Async Chat Thread - #8/INFO]: <DMR_Rocks> 1373 73 -412",
    "[21:24:40] [Async Chat Thread - #8/INFO]: <ehawk08> 1412 80 -411",
    "[21:24:41] [Async Chat Thread - #8/INFO]: <IonImpulse> 1351 83 -402",
    "[21:24:43] [Async Chat Thread - #8/INFO]: <DodgerThePuppis> 1400 73 -435",
    "[21:24:51] [Async Chat Thread - #8/INFO]: <DMR_Rocks> 1385 73 -435",
    "[21:24:56] [Async Chat Thread - #8/INFO]: <IonImpulse> 1366 83 -395",
    "[21:25:04] [Async Chat Thread - #8/INFO]: <DMR_Rocks> 1393 73 -436",
    "[21:25:07] [Async Chat Thread - #8/INFO]: <IonImpulse> 1366 82 -394",
    "[21:25:07] [Async Chat Thread - #8/INFO]: <arimeffie> 1424 73 -406",
    "[21:25:24] [Async Chat Thread - #8/INFO]: <DMR_Rocks> 1336 84 -442",
    "[21:25:28] [Async Chat Thread - #8/INFO]: <ColonelJJHawkins> 1437 73 -418",
    "[21:25:30] [Async Chat Thread - #8/INFO]: <Ch1cChak> 1418 73 -419",
    "[21:25:31] [Async Chat Thread - #8/INFO]: <IonImpulse> 1385 73 -381",
    "[21:25:40] [Async Chat Thread - #8/INFO]: <arimeffie> 1410 73 -389",
    "[21:25:46] [Async Chat Thread - #8/INFO]: <Fozzy623> 1351,",
    "[21:25:53] [Async Chat Thread - #8/INFO]: <ehawk08> 1412 79 -418",
    "[21:25:54] [Async Chat Thread - #8/INFO]: <IonImpulse> 1391 73 -385",
    "[21:25:55] [Async Chat Thread - #8/INFO]: <Fozzy623> 1351,83, -401",
    "[21:26:11] [Async Chat Thread - #8/INFO]: <DMR_Rocks> 1385 73 -365",
    "[21:26:12] [Async Chat Thread - #8/INFO]: <arimeffie> 1399 73 -410",
    "[21:26:12] [Async Chat Thread - #8/INFO]: <ColonelJJHawkins> 1420 72 -402",
    "[21:26:36] [Async Chat Thread - #8/INFO]: <arimeffie> 1373 73 -411",
    "[21:26:49] [Async Chat Thread - #8/INFO]: <ehawk08> 1423 78 -407",
    "[21:27:02] [Async Chat Thread - #8/INFO]: <arimeffie> 1369 73 -419",
    "[21:27:24] [Async Chat Thread - #8/INFO]: <arimeffie> 1374 77 -417",
    "[21:27:34] [Async Chat Thread - #8/INFO]: <ehawk08> 1411 74 -390"
]
loot_table = [
    "end_city_treasure",
    "woodland_mansion",
    "spawn_bonus_chest"
]

time.sleep(5)
for index, msg in enumerate(locations) :
    temp = msg.replace("[m", "").replace(",", "").replace(".", "")
    temp = temp.split("> ")[1]

    coords = temp.split(" ")
    
    loot = loot_table[random.randint(0, len(loot_table) - 1)]
    
    print(coords, loot)

    output = "/setblock {} {} {} ".format(coords[0], coords[1], coords[2])
    output += "minecraft:chest{LootTable:\"minecraft:chests/" + loot + "\"}"
    pydirectinput.press('t')
    typewrite(output)
    pydirectinput.press('enter')
