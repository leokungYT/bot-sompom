    
def adbbot1(devicsX):
    config = configparser.ConfigParser()
    config.read('bin/config.ini')
    gachaselect = config.getint('SETTINGS', 'gachaselect')
    herowant = config.getint('SETTINGS', 'herowant')
    name1 = config.get('SETTINGS', 'name1')
    name2 = config.get('SETTINGS', 'name2')
    name3 = config.get('SETTINGS', 'name3')
    name4 = config.get('SETTINGS', 'name4')
    name5 = config.get('SETTINGS', 'name5')
    name6 = config.get('SETTINGS', 'name6')
    name7 = config.get('SETTINGS', 'name7')
    name8 = config.get('SETTINGS', 'name8')
    name9 = config.get('SETTINGS', 'name9')
    name10 = config.get('SETTINGS', 'name10')
    if herowant == 1:
        all_hero_name = [name1]
        pic_hero = ['bin/hero_pic/hero1.png']
    elif herowant == 2:
        all_hero_name = [name1, name2]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png']
    elif herowant == 3:
        all_hero_name = [name1, name2, name3]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png']
    elif herowant == 4:
        all_hero_name = [name1, name2, name3, name4]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png']
    elif herowant == 5:
        all_hero_name = [name1, name2, name3, name4, name5]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png', 'bin/hero_pic/hero5.png']
    elif herowant == 6:
        all_hero_name = [name1, name2, name3, name4, name5, name6]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png', 'bin/hero_pic/hero5.png', 'bin/hero_pic/hero6.png']
    elif herowant == 7:
        all_hero_name = [name1, name2, name3, name4, name5, name6, name7]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png', 'bin/hero_pic/hero5.png', 'bin/hero_pic/hero6.png', 'bin/hero_pic/hero7.png']
    elif herowant == 8:
        all_hero_name = [name1, name2, name3, name4, name5, name6, name7, name8]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png', 'bin/hero_pic/hero5.png', 'bin/hero_pic/hero6.png', 'bin/hero_pic/hero7.png', 'bin/hero_pic/hero8.png']
    elif herowant == 9:
        all_hero_name = [name1, name2, name3, name4, name5, name6, name7, name8, name9]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png', 'bin/hero_pic/hero5.png', 'bin/hero_pic/hero6.png', 'bin/hero_pic/hero7.png', 'bin/hero_pic/hero8.png', 'bin/hero_pic/hero9.png']
    elif herowant == 10:
        all_hero_name = [name1, name2, name3, name4, name5, name6, name7, name8, name9, name10]
        pic_hero = ['bin/hero_pic/hero1.png', 'bin/hero_pic/hero2.png', 'bin/hero_pic/hero3.png', 'bin/hero_pic/hero4.png', 'bin/hero_pic/hero5.png', 'bin/hero_pic/hero6.png', 'bin/hero_pic/hero7.png', 'bin/hero_pic/hero8.png', 'bin/hero_pic/hero9.png', 'bin/hero_pic/hero10.png']

    adb = AdbClient()
    dv = adb.device(devicsX)
    if dv:
        while sw_emu1:
            dv.shell(f"rm -r data/data/com.linecorp.LGRGS/shared_prefs")
            time.sleep(2)
            sw_hero = 0
            hero_name = ""
            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/guestlogin.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/icongame.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipmain.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/signin1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(2) ###################
                            dv.shell("input tap 925 154")
                            time.sleep(1)
                            dv.shell("input tap 926 314")
                            time.sleep(1)
                            dv.shell("input tap 926 402")
                            time.sleep(1)
                            dv.shell("input tap 420 489")
                            time.sleep(1)
                            dv.shell("input keyevent KEYCODE_BACK")
                            time.sleep(2)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/black.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 406 514")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/error1.png')
                        if len(pos_adb) > 0:
                            sw_hero = 3
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z2.png') #############
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/guestlogin.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/login.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(2) ######################
                            dv.shell("input tap 925 154")
                            time.sleep(1)
                            dv.shell("input tap 926 314")
                            time.sleep(1)
                            dv.shell("input tap 926 402")
                            time.sleep(1)
                            dv.shell("input tap 420 489")
                            time.sleep(1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/black.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 532 508")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        pos_adb2 = ImgSearchADB(adb_img, 'bin/pic/z2.png')
                        if len(pos_adb) > 0 and len(pos_adb2) == 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/b5.png') ###########
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/r.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/here1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(2)
                            dv.shell("input tap 478 407")
                            time.sleep(0.1)
                        cap = dv.screencap() ####################### 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        dv.shell("input tap 281 474") ##########
                        time.sleep(0.1)
                        dv.shell("input tap 382 474")
                        time.sleep(0.1)
                        dv.shell("input tap 809 474")
                        time.sleep(0.1)
                        dv.shell("input tap 481 474")
                        time.sleep(0.1)
                        dv.shell("input tap 586 474")
                        time.sleep(0.1)
                        dv.shell("input tap 151 474")
                        time.sleep(0.1)
                        dv.shell("input tap 681 474")
                        time.sleep(0.1)
                        dv.shell("input tap 542 340")
                        time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/b1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/s1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() ####################### 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/freeitem.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/start1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/anf.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 50 44")
                            time.sleep(0.5)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 583 480")
                            time.sleep(0.5)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 282 479")
                            time.sleep(0.5)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/anf.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 476 458")
                            time.sleep(0.5)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onetime.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        dv.shell("input tap 663 113")
                        time.sleep(0.5)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onetime.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(2)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok4.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok3.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        dv.shell("input tap 877 493")
                        time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 400:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/guestlogin.png')
                        if len(pos_adb) > 0:
                            sw_hero = 3
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(2)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/b2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                            dv.shell(f"input swipe 481 192 477 416")
                            time.sleep(0.1)
                            dv.shell(f"input swipe 135 421 482 223")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/save1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/back1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/guestlogin.png')
                        if len(pos_adb) > 0:
                            sw_hero = 3
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop1.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 812 61")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop2.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 726 76")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop4.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 725 75")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop5.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 479 416")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop6.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop7.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop8.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop9.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop10.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop11.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop12.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop13.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop14.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop15.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 478 416")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop16.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 813 62")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop18.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 38")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop19.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 727 75")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop17.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 37")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        if count_loop > 40:
                            dv.shell("input tap 542 340")
                            time.sleep(0.1)
                    except:
                        pass

            ########################## 111 ################################################################
            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/b4.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/s11.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/freeitem.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/start1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/back2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 50 44")
                            time.sleep(0.5)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 380 480")
                            time.sleep(0.5)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        else:
                            dv.shell("input tap 282 479")
                            time.sleep(0.5)
                    except:
                        pass

            ########################################################
            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/back2.png')
                        pos_adb2 = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0 or len(pos_adb2) > 0:
                            dv.shell("input keyevent KEYCODE_APP_SWITCH")
                            time.sleep(0.1)
                            for _ in range(3):
                                dv.shell("input keyevent KEYCODE_DPAD_DOWN")
                                time.sleep(0.1)
                                dv.shell("input keyevent DEL")
                                time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/guestlogin.png')
                        if len(pos_adb) > 0:
                            sw_hero = 3
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/icongame.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop1.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 812 61")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop2.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 726 76")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop4.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 725 75")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop5.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 479 416")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop6.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop7.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop8.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop9.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop10.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop11.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop12.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop13.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop14.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 36")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop15.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 478 416")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop16.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 813 62")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop18.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 38")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop19.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 730 76")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pop17.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 858 37")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/buff1.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 812 35")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                    except:
                        pass

            #############################################################################
            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ygotre.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/skipplay.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/buff1.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 814 35")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/7day.png')
                        time.sleep(0.1)
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
  
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/1day.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 334 436")

                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall3.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall4.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ygotre.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 480 405")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/1day.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 839 32")
                            time.sleep(0.1)
                            
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/box1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall2.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 556 362")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onetime2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 479 361")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall4.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 477 362")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/done1.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 802 35")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/box1.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 664 103")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onetime2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall2.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 565 362")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/acceptall3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 477 362")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/gb.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 803 35")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/mainstage.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 665 142")
                            time.sleep(0.1)
                    except:
                        pass
        
            count_loop = 0
            sw_exit = 0
            if gachaselect == 1:
                dv.shell("input tap 750 180")
                time.sleep(0.1)
            elif gachaselect == 2:
                dv.shell("input tap 747 309")
                time.sleep(0.1)
            elif gachaselect == 3:
                dv.shell("input tap 747 432")
                time.sleep(0.1)
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 827 50")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam4.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 827 50")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ruby.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/gotgpoint.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 478 358")
                            time.sleep(2)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/pgc.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 553 406")
                            time.sleep(2)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onemore.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onetime2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(3)
                            dv.shell("input tap 894 478")
                            time.sleep(0.1)
                            dv.shell("input tap 894 478")
                            time.sleep(0.1)
                            dv.shell("input tap 894 478")
                            time.sleep(0.1)

                    except:
                        pass
            count_loop = 0
            sw_exit = 0

            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break

                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 827 50")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam4.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 827 50")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam2.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ruby.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 399 359")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/onemore.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 783 441")
                            time.sleep(0.1)
                    except:
                        pass

            count_loop = 0
            sw_exit = 0
            hero_name = ""
            while sw_hero != 3 and sw_emu1:
                if sw_exit == 1:
                    break
 
                while sw_hero != 3 and sw_emu1:
                    if count_loop >= 100:
                        sw_hero = 3
                        break
                    count_loop += 1
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            sw_exit = 1
                            sw_hero = 2
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam3.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 827 50")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam4.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 827 50")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam2.png')
                        if len(pos_adb) > 0:
                            hero_c = 0
                            for i in range(len(pic_hero)):
                                pos_hero = ImgSearchADB(adb_img, pic_hero[i])
                                if len(pos_hero) > 0:
                                    hero_c += 1
                                    hero_name = hero_name + all_hero_name[i] ##############################
                            if hero_c > 0:
                                sw_hero = 1
                            else:
                                sw_hero = 2
                        if sw_hero == 1 or sw_hero == 2:
                            sw_exit = 1
                            break
                    except:
                        pass

            if sw_hero == 1:
                while sw_emu1:
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/myteam2.png')
                        if len(pos_adb) > 0:
                            dv.shell("input tap 35 27")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/settings.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/settings2.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/settings3.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                    except:
                        pass

                while sw_emu1:
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/icongame.png')
                        if len(pos_adb) > 0:
                            break
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/ok1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                            dv.shell("input keyevent KEYCODE_APP_SWITCH")
                            time.sleep(0.1)
                            for _ in range(3):
                                dv.shell("input keyevent KEYCODE_DPAD_DOWN")
                                time.sleep(0.1)
                                dv.shell("input keyevent DEL")
                                time.sleep(0.1)

                    except:
                        pass

                while sw_emu1:
                    try:
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/z1.png')
                        if len(pos_adb) > 0:
                            dv.shell(f"input tap {pos_adb[0][0]} {pos_adb[0][1]}")
                            time.sleep(0.1)
                        cap = dv.screencap() 
                        image = np.frombuffer(cap, dtype=np.uint8)
                        adb_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                        pos_adb = ImgSearchADB(adb_img, 'bin/pic/icongame.png')
                        if len(pos_adb) > 0:
                            break
                        dv.shell("input keyevent KEYCODE_APP_SWITCH")
                        time.sleep(0.1)
                        for _ in range(3):
                            dv.shell("input keyevent KEYCODE_DPAD_DOWN")
                            time.sleep(0.1)
                            dv.shell("input keyevent DEL")
                            time.sleep(0.1)
                    except:
                        pass

                game_name = pyperclip.paste()
                subprocess.run(['bin/adb/adb.exe', "-s", devicsX, "pull", "data/data/com.linecorp.LGRGS/shared_prefs/_LINE_COCOS_PREF_KEY.xml", f"backup/{hero_name + game_name}_LINE_COCOS_PREF_KEY.xml"], stdout=subprocess.PIPE)
                time.sleep(2)

            else:
                dv.shell("input keyevent KEYCODE_APP_SWITCH")
                time.sleep(0.1)
                for _ in range(3):
                    dv.shell("input keyevent KEYCODE_DPAD_DOWN")
                    time.sleep(0.1)
                    dv.shell("input keyevent DEL")
                    time.sleep(0.1)


