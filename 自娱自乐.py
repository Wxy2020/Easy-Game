#-*- coding=utf=8 -*-
import random
from PIL import Image
import time

def randon_pic(num):
    p1 = Image.open("D:/自娱自乐/1.png","r")
    p2 = Image.open("D:/自娱自乐/2.png","r")
    p3 = Image.open("D:/自娱自乐/3.png","r")
    p4 = Image.open("D:/自娱自乐/4.png","r")
    p5 = Image.open("D:/自娱自乐/5.png","r")
    p6 = Image.open("D:/自娱自乐/6.png","r")
    p7 = Image.open("D:/自娱自乐/7.png","r")
    p8 = Image.open("D:/自娱自乐/8.png","r")
    p9= Image.open("D:/自娱自乐/9.png","r")
    p10 = Image.open("D:/自娱自乐/10.png","r")
    p11 = Image.open("D:/自娱自乐/11.png","r")
    p12 = Image.open("D:/自娱自乐/12.png","r")
    p13 = Image.open("D:/自娱自乐/13.png","r")
    p14 = Image.open("D:/自娱自乐/14.png","r")
    p15 = Image.open("D:/自娱自乐/15.png","r")
    p16 = Image.open("D:/自娱自乐/16.png","r")
    p17 = Image.open("D:/自娱自乐/17.png","r")
    p18 = Image.open("D:/自娱自乐/18.png","r")
    p19 = Image.open("D:/自娱自乐/19.png","r")
    p20 = Image.open("D:/自娱自乐/20.png","r")
    p21 = Image.open("D:/自娱自乐/21.png","r")
    p22 = Image.open("D:/自娱自乐/22.png","r")
    p23 = Image.open("D:/自娱自乐/23.png","r")
    p24 = Image.open("D:/自娱自乐/24.png","r")
    p25 = Image.open("D:/自娱自乐/25.png","r")
    p26 = Image.open("D:/自娱自乐/26.png","r")
    p27 = Image.open("D:/自娱自乐/27.png","r")
    p28 = Image.open("D:/自娱自乐/28.png","r")
    p29 = Image.open("D:/自娱自乐/29.png","r")
    p30 = Image.open("D:/自娱自乐/30.png","r")

    plist = {"1":p1,"2":p2,"3":p3,"4":p4,"5":p5,"6":p6,"7":p7,"8":p8,"9":p9,"10":p10,
    "11":p11,"12":p12,"13":p13,"14":p14,"15":p15,"16":p16,"17":p17,"18":p18,"19":p19,"20":p20,
    "21":p21,"22":p22,"23":p23,"24":p24,"25":p25,"26":p26,"27":p27,"28":p28,"29":p29,"30":p30,
    }
    

    print(num)
    img = plist.get(num)
    img.show()

def other_condition1(num):
    if num == 4:
        print(random.randint(1,3))
    
    elif num == 5:
        p10 = Image.open("D:/自娱自乐/10.png","r")
        time.sleep(4)
        p10.show()

    elif num == 6:
        print(random.randint(1,4))

    elif num == 9:
        print(random.randint(1,3))

    elif num == 11:
        print(random.randint(1,3))

    elif num == 13:
        a = random.randint(1,20)
        print(a)
        if a>=16 and a<=18:
            end = Image.open("D:/自娱自乐/结局3.png",'r')
            end.show()

    elif num == 19:
        print(random.randint(1,6))   

    elif num == 22:
        print(random.choice([10,13]))

    elif num == 23:
        print(random.randint(1,7))

    elif num == 24:
        print(random.randint(1,3))

def main():
    while True:
        for i in range(5):
            rd = random.randint(1,30)
            #rd = 13
            r1 = str(rd)
            randon_pic(r1)
            other_condition1(rd)
            print("是否跳过")
            shuru = input()
            if shuru  == "y":
                time.sleep(0)
            else:
                time.sleep(40)
            
        for i in range(4):
            rd = random.randint(1,30)
            #rd = 5
            r1 = str(rd)
            randon_pic(r1)
            other_condition1(rd)
            print("是否跳过")
            shuru = input()
            if shuru  == "y":
                time.sleep(0)
            else:
                time.sleep(60)

        for i in range(3):
            rd = random.randint(1,30)
            #rd = 5
            r1 = str(rd)
            randon_pic(r1)
            other_condition1(rd)
            print("是否跳过")
            shuru = input()
            if shuru  == "y":
                time.sleep(0)
            else:
                time.sleep(80)
main()