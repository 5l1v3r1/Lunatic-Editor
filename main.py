import os
from datetime import datetime
import time as tm
import subprocess
import requests
import threading
import json as js

auth_url = '' 
adwsd = ''

def get_id():
    hwid = str(subprocess.check_output(
        'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    return hwid

if not os.path.exists('result'):
    os.mkdir('result')
if not os.path.exists('put txt for merge here'):
    os.mkdir('put txt for merge here')
if not os.path.exists('Data'):
    os.mkdir('Data')
if not 'Config.txt' in os.listdir('Data'):
    open('Data/Config.txt', 'w', encoding='utf-8').write('{\n    "Counter":"True",\n    "AutoLogin":{\n        "Status":"False",\n        "Username":"",\n        "Password":""\n    },\n    "UppercaseLowercase":"False",\n    "Strip":"False",\n    "Repeat":"1"\n}')
if not 'custom1.txt' in os.listdir('Data'):
    open('Data/custom1.txt', 'w', encoding='utf-8').write('1\n!\n$\n123')
if not '/custom2.txt' in os.listdir('Data'):
    open('Data/custom2.txt', 'w', encoding='utf-8').write('1\n!\n$\n123')
if not 'custom3.txt' in os.listdir('Data'):
    open('Data/custom3.txt', 'w', encoding='utf-8').write('1\n!\n$\n123')




def loaddata():
    return js.loads(str(open('Data/Config.txt', 'r', encoding='utf-8').read()).replace('\n', '').replace(' ', ''))

def loadalldata():
    global Counter, AutoLogin, Username, Password, UppercaseLowercase, strip, repeat
    Counter = loaddata()['Counter']
    AutoLogin = loaddata()['AutoLogin']['Status']
    Username = loaddata()['AutoLogin']['Username']
    Password = loaddata()['AutoLogin']['Password']
    UppercaseLowercase = loaddata()['UppercaseLowercase']
    strip = loaddata()['Strip']
    repeat = int(loaddata()['Repeat'])

Counter = loaddata()['Counter']
AutoLogin = loaddata()['AutoLogin']
Username = loaddata()['AutoLogin']['Username']
Password = loaddata()['AutoLogin']['Password']
UppercaseLowercase = loaddata()['UppercaseLowercase']
strip = loaddata()['Strip']
repeat = int(loaddata()['Repeat'])

temp = []

title = ("""\n\n\n    \033[1;37;40m                       .-') _    ('-.     .-') _                     
                          ( OO ) )  ( OO ).-.(  OO) )                    
 \033[95m ,--.     ,--. ,--.  ,--.\033[1;37;40m/\033[95m ,--,\033[1;37;40m'   / . \033[95m--.\033[1;37;40m //     '._ ,-.-')\033[95m   .-----.  
  |  |\033[1;37;40m.-')\033[95m |  | |  |  |   \ |  |\033[1;37;40m\   \033[95m| \033[1;37;40m\\\033[95m-.  \ |\033[1;37;40m'--...__)\033[95m|  |\033[1;37;40mOO) \033[95m'  .--./  
  |  |\033[1;37;40m OO )\033[95m|  | |\033[1;37;40m .-')\033[95m|    \|  |\033[1;37;40m ).-\033[95m(\033[1;37;40m-'\033[95m__)  |'--.  .--'|  |\033[1;37;40m  \ \033[95m|  |\033[1;37;40m('-.  
\033[95m  |  |\033[1;37;40m`-' |\033[95m|  |_|\033[1;37;40m( OO ) \033[95m .     |\033[1;37;40m/  \\\033[95m|       | | |  |   |  |\033[1;37;40m(_//_) \033[95m|\033[1;37;40mOO  ) 
 (\033[1;36;40m|  '---.\033[1;37;40m'\033[1;36;40m|  | | \033[1;37;40m`-' /  \033[1;36;40m|\    |    |  .-.  |_| |  |  \033[1;37;40m,\033[1;36;40m|  |\033[1;37;40m_.'|\033[1;36;40m|  |\033[1;37;40m`-'|  
\033[1;36;40m  |      |\033[1;37;40m(\033[1;36;40m'  '-'\033[1;37;40m(_.-'\033[1;36;40m|  | \   |    |  | |  |   |  |\033[1;37;40m (_\033[1;36;40m|  | \033[1;37;40m (_\033[1;36;40m'  '--'\  
  `------'  `-----'   `--'  `--'    `--' `--'   `--'   `--'     `-----'  SUS EDITOR\n\n\n\n\n""")



def iseven(number):
    return number % 2 == 0

def counterslowsorter():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mLoaded Lines : {total_lines}\n Sorted Lines : {all_domain}\n Hits : {sorted_domain}\n Unique Domain : {listed_domain}\n')
            if status == 'done':
                break
        else:
            break

def counterfastsorter():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mLdoaded Lines : {s}\n Sorted Lines : {all_domain}\n Hits : {sorted_domain}\n')
            if status == 'done':
                break
        else:
            break

def counterhitremover():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mCombo Loaded : {combo_len}\n Hits Loaded : {hit_len}\n Combo Checked : {combo_checked}\n Hits Removed : {hits}\n\n')
            if status == 'done':
                break
        else:
            break

def countertxtmerger():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mTxt files loaded : {txt_len}\n Txt Merged : {txt_count}\n Lines Merged : {lines}\n Remaining Txt Files : {txt_len - txt_count}\n')
            if status == 'done':
                break
        else:
            break


def countertxtsplitter():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mSplited Files : {e}\n Files Remaining : {o - e}\n')
            if status == 'done':
                break
        else:
            break

def counterbadlinesremover():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mLines Loaded : {combo_len}\n Lines Checked : {combo_checked}\n Badlines Removed : {combo_checked - hits}\n')
            if status == 'done':
                break
        else:
            break

def counterslowcaptureremover():
    while True:
        if Counter == 'True':
            tm.sleep(0.5)
            os.system('cls')
            print(title)
            print(f' \033[1;36;40mLines Loaded : {open_path_len}\n Lines Checked : {all_lines}\n Hits/Cap Removed : {cap_removed}\n Without Capture : {without_cap}\n Invalids Lines : {invalid}')
            if status == 'done':
                break
        else:
            break

def slowsorter(path, domain):
    global all_domain, sorted_domain, listed_domain, total_lines, status, count_done
    os.system('title This Damn Shit Slow asf - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    try:
        start_time = tm.time()
        print(' \033[1;36;40mLoading...')
        open_path = open(path, 'rb')
        total_lines = len(open_path.readlines())
        open_path.close()
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        os.mkdir(f'result/{time}/Extra')
        sorted_file = open(f'result/{time}/{domain}.txt', 'w', encoding='utf-8')
        all_domain = 0
        sorted_domain = 0
        listed_domain = 0
        listed_domain_list = []
        status = 'busy'
        x = threading.Thread(target=counterslowsorter)
        x.start()
        with open(path, 'rb') as open_path:
            for x in range(total_lines):
                single_line = str(open_path.readline()).replace("b'", '').replace("\\r\\n'", '')
                single_domain_raw = single_line.split(':')[0].split('@')[-1].lower()
                single_domain = str(single_domain_raw).replace("b'", '').replace("\\r\\n'", '').replace('\\r\\n', '').replace(';', ':').strip('<,>.?/"[{]]\\|=+-_)(*&^%$\'#@!~')
                if f'@{domain}' in f'@{single_domain}':
                    sorted_file.write(f'{single_line}\n')
                    sorted_domain += 1
                    if single_domain in listed_domain_list:
                        try:
                            open(f'result/{time}/Extra/{single_domain}.txt', 'a', encoding='utf-8').write(f'{single_line}\n')
                        except:
                            pass
                    else:
                        listed_domain_list.insert(0, single_domain)
                        listed_domain += 1
                all_domain += 1
            open_path.close()
            sorted_file.close()
            status = 'done'
            tm.sleep(2)
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def slowsorterwithoutcounter(path, domain):
    global status, count_done
    os.system('title Well not that slow without counter - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    try:
        open_path = open(path, 'rb')
        total_lines = len(open_path.readlines())
        open_path.close()
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        sorted_file = open(f'result/{time}/{domain}.txt', 'w', encoding='utf-8')
        p = []
        start_time = tm.time()
        with open(path, 'rb') as open_path:
            print(' \033[1;36;40mSorting...')
            for x in range(total_lines):
                single_line = str(open_path.readline()).replace("b'", '').replace("\\r\\n'", '').replace("\\r\\n", '').replace(';', ':').strip('<,>.?/"[{]]\\|=+-_)(*&^%$\'#@!~')
                single_domain = single_line.split(':')[0].split('@')[-1].lower().strip('\n')
                if f'@{domain}' in f'@{single_domain}':
                    sorted_file.write(f'{single_line}\n')
                    if not single_domain in p:
                        p.insert(0, single_domain)
            open_path.close()
            sorted_file.close()
        print(' \033[1;36;40mDone!!!.. Sorting Extra Stuff Now')
        status = 'busy'
        os.mkdir(f'result/{time}/Extra')
        total_domains_file = len(p)
        count_done = 0
        for i in range(total_domains_file):
            domain_extra = p[i].replace('/', '')
            x = threading.Thread(target=domain_sorter_withoutcounter, args=(time, domain_extra, path, total_lines,))
            x.start()
        while True:
            if status == f'done{total_domains_file}':
                break
            else:
                tm.sleep(0.1)
                pass
        os.system('title Bruh took me a while - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()

    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def domain_sorter_withoutcounter(time, domain_extra, path, total_lines):
    global status, count_done
    try:
        try:
            open_domain_extra = open(f'result/{time}/Extra/{domain_extra}.txt', 'w', encoding='utf-8')
        except:
            pass
        open_path = open(path, 'rb')
        for _ in range(total_lines):
            single_line = str(open_path.readline()).replace("b'", '').replace("\\r\\n'", '\n').replace("\\r\\n", '\n')
            single_domain = single_line.split(':')[0].split('@')[-1].lower().strip('\n')
            if f'{domain_extra}' == single_domain:
                try:
                    open_domain_extra.write(f'{single_line}\n')
                except:
                    pass
        open_domain_extra.close()
        open_path.close()
        count_done += 1
        tm.sleep(1)
        status = f'done{count_done}'
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def fastsorter(path, domain):
    global s, sorted_domain, all_domain, status
    os.system('title Same sorter without Extra File and lighter script - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    try:
        start_time = tm.time()
        status = 'busy'
        f = open(path, 'rb')
        s = len(f.readlines())
        f.close()
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        c = open(f'result/{time}/{domain}.txt', 'w', encoding='utf-8')
        sorted_domain = 0
        all_domain = 0
        x = threading.Thread(target=counterfastsorter)
        x.start()
        with open(path, 'rb') as f:
            for x in range(s):
                ae = str(f.readline()).replace("b'", '').replace("\\r\\n'", '\n').replace("\\r\\n", '\n')
                a = ae.split(':')[0].split('@')[-1].lower().strip()
                if f'@{domain}' in f'@{a}':
                    c.write(f'{ae}')
                    sorted_domain = sorted_domain + 1
                all_domain = all_domain + 1
            f.close()
        status = 'done'
        tm.sleep(0.5)
        os.system('title Bruh....still slow - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()

    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def fastsorterwithoutcounter(path, domain):
    os.system('title Faster!!!!!! - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    try:
        print(' \033[1;36;40mSorting...')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        c = open(f'result/{time}/{domain}.txt', 'w', encoding='utf-8')
        start_time = tm.time()
        with open(path, 'rb') as f:
            for x in range(len(open(path, 'rb').readlines())):
                ae = str(f.readline()).replace("b'", '').replace("\\r\\n'", '\n')
                a = ae.split(':')[0].split('@')[-1].lower().strip()
                if f'@{domain}' in f'@{a}':
                    c.write(f'{ae}')
            f.close()
        os.system('title Fast asf - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def domainsortermenu(speed):
    os.system('title Sort ur shit - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    domain = str(input(' \033[1;36;40mdomain, .com etc or both\n \033[1;33;40m')).lower().strip('@')
    os.system('cls')
    print(title)
    path = input(' \033[1;36;40mDrop file here\n \033[1;33;40m').strip('"')
    if speed == 'slow':
        if Counter == 'False':
            slowsorterwithoutcounter(path, domain)
        else:
            slowsorter(path, domain)
    elif speed == 'fast':
        if Counter == 'False':
            fastsorterwithoutcounter(path, domain)
        else:
            fastsorter(path, domain)

def hitremover(hit_path, combo_path):  #make the hits remover remove hits from the list
    os.system('title I see... - Lunatic Editor - Made by Nami#7789')
    global combo_len, hit_len, combo_checked, hits, status
    try:
        os.system('cls')
        print(title)
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        hit = str(open(hit_path, 'rb').read()).replace("b'", '').split("\\r\\n")
        hit_len = len(open(hit_path, 'rb').readlines())
        combo_len = len(open(combo_path, 'rb').readlines())
        combo = open(combo_path, 'rb')
        os.mkdir(f'result/{time}')
        hits = 0
        combo_checked = 0
        status = 'busy'
        x = threading.Thread(target=counterhitremover)
        x.start()
        start_time = tm.time()
        for _ in range(combo_len):
            ae = str(combo.readline()).replace("b'", '').replace("\\r\\n'", '').strip('\n')
            if not ae in hit:
                open(f'result/{time}/Hits Remover.txt', 'a', encoding='utf-8').write(f'{ae}\n')
            else:
                hit.remove(ae)
                hits = hits + 1
            combo_checked = combo_checked + 1
        status = 'done'
        tm.sleep(1)
        os.system('title Finally! Done! btw I gonna change this script(Maybe Not) - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()
def hitremoverwithoutcounter(hit_path, combo_path):
    os.system('title I see... - Lunatic Editor - Made by Nami#7789')
    try:
        os.system('cls')
        print(title)
        print(' \033[1;36;40mRemoving...')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        hit = str(open(hit_path, 'rb').read()).replace("b'", '').split("\\r\\n")
        combo_len = len(open(combo_path, 'rb').readlines())
        combo = open(combo_path, 'rb')
        os.mkdir(f'result/{time}')
        w = open(f'result/{time}/Hits Remover.txt', 'w', encoding='utf-8')
        start_time = tm.time()
        for x in range(combo_len):
            ae = str(combo.readline()).replace("b'", '').replace("\\r\\n'", '').replace("\\r\\n", '').strip('\n')
            if not ae in hit:
                w.write(f'{ae}\n')
            else:
                hit.remove(ae)
        os.system('title Finally! Done! - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()


def hitremovermenu():
    os.system('title Hmmm... - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    hits_path = input(' \033[1;36;40mDrop hitlist here\n \033[1;33;40m').strip('"')
    os.system('cls')
    print(title)
    combo_path = input(' \033[1;36;40mDrop combolist here\n \033[1;33;40m').strip('"')
    if Counter == 'False':
        hitremoverwithoutcounter(hits_path, combo_path)
    else:
        hitremover(hits_path, combo_path)

def txtmerger():
    global txt_len, txt_count, lines, status
    os.system('title Transformers! - Lunatic Editor - Made by Nami#7789')
    try:
        os.system('cls')
        print(title)
        txt = os.listdir('put txt for merge here')
        txt_len = len(txt)
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        lines = 0
        txt_count = 0
        status = 'busy'
        lq = threading.Thread(target=countertxtmerger)
        lq.start()
        start_time = tm.time()
        for x in range(txt_len):
            ae = open(f'result/{time}/Merged.txt', 'a', encoding='utf-8')
            single_txt = open(f'put txt for merge here/{txt[x]}', 'rb')
            single_txt_len = len(single_txt.readlines())
            single_txt.close()
            another_txt = open(f'put txt for merge here/{txt[x]}', 'rb')
            for y in range(single_txt_len):
                line = str(another_txt.readline()).strip('\n').replace("b'", '').replace("\\r\\n'", '')
                ae.write(f'{line}\n')
                lines = lines + 1
            txt_count = txt_count + 1
            ae.close()
            single_txt.close()
            another_txt.close()
        status = 'done'
        tm.sleep(1)
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def txtmergerwithoutcounter():
    os.system('title Transformers! - Lunatic Editor - Made by Nami#7789')
    try:
        os.system('cls')
        print(title)
        txt = os.listdir('put txt for merge here')
        print(' \033[1;36;40mMerging...')
        txt_len = len(txt)
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        start_time = tm.time()
        for x in range(txt_len):
            ae = open(f'result/{time}/Merged.txt', 'a', encoding='utf-8')
            single_txt = open(f'put txt for merge here/{txt[x]}', 'rb')
            single_txt_len = len(single_txt.readlines())
            another_txt = open(f'put txt for merge here/{txt[x]}', 'rb')
            for y in range(single_txt_len):
                line = str(another_txt.readline()).replace("b'", '').replace("\\r\\n'", '').strip('\n')
                ae.write(f'{line}\n')
            ae.close()
            single_txt.close()
            another_txt.close()
        os.system('title Nothing much - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def textmergermenu():
    if Counter == 'False':
        txtmergerwithoutcounter()
    else:
        txtmerger()

def duplicateremover(path):
    os.system('title Duplicate Remover Doing his Job(Fuck duplicate hits!) - Lunatic Editor - Made by Nami#7789')
    try:
        os.system('cls')
        print(title)
        print(' \033[1;36;40mWait For a moment...:)')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        f = open(path, 'rb').readlines()
        f_len = len(f)
        start_time = tm.time()
        result_txt = open(f'result/{time}/Duplicate Remover.txt', 'w', encoding='utf-8')
        s = list(dict.fromkeys(f))
        s_len = len(s)
        for x in range(s_len):
            result_txt.write(str(s[x]).replace("b'", '').replace("\\r\\n'", '\n'))
        tm.sleep(0.05)
        os.system('cls')
        print(title)
        print(f' \033[1;36;40mLines Loaded : {f_len}\n \033[1;36;40mRemoved Duplicates : {f_len - s_len}')
        result_txt.close()
        os.system('title Done... - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()


def duplicateremovermenu():
    os.system('title Duplicate Remover - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    path = input(' \033[1;36;40mDrop txt file here\n \033[1;33;40m').strip('"')
    duplicateremover(path)

def txtsplitter(lines, path):
    global e, o, f_len, status, t
    try:
        os.system('title Splitter!! Chop - Lunatic Editor - Made by Nami#7789')
        os.system('cls')
        print(title)
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        f_len = len(open(path, 'rb').readlines())
        f = open(path, 'rb')
        o = round((f_len / lines) + 0.5)
        t = lines
        u = 0
        e = 0
        i = 0
        m = 0
        start_time = tm.time()
        status = 'busy'
        lq = threading.Thread(target=countertxtsplitter)
        lq.start()
        for x in range(o):
            q = open(f'result/{time}/{x}.txt', 'w', encoding='utf8')
            m = f_len - t
            if m >= t:
                for x in range(t):
                    q.write(str(f.readline()).replace("b'", '').replace("\\r\\n'", '\n').strip("'"))
                u = u + lines
            else:
                for x in range(m):
                    q.write(str(f.readline()).replace("b'", '').replace("\\r\\n'", '\n').strip("'"))
                    f_len = f_len - t
            e = e + 1
            tm.sleep(0.05)
            q.close()
        status = 'done'
        tm.sleep(1)
        os.system('title Done Splitted ur ass... - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def txtsplitterwithoutcounter(lines, path):
    try:
        os.system('title Splitter!! Chop - Lunatic Editor - Made by Nami#7789')
        os.system('cls')
        print(title)
        print(' \033[1;36;40mSplitting....')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        f_len = len(open(path, 'rb').readlines())
        f = open(path, 'rb')
        o = round((f_len / lines) + 0.5)
        t = lines
        u = 0
        start_time = tm.time()
        for x in range(o):
            q = open(f'result/{time}/{x}.txt', 'w', encoding='utf8')
            m = f_len - t
            if m >= t:
                for x in range(t):
                    q.write(str(f.readline()).replace("b'", '').replace("\\r\\n'", '\n').strip("'"))
                u = u + lines
            else:
                for x in range(m):
                    q.write(str(f.readline()).replace("b'", '').replace("\\r\\n'", '\n').strip("'"))
                    f_len = f_len - t
            tm.sleep(0.05)
            q.close()
        os.system('cls')
        print(title)
        os.system('title Done Splitted ur ass... - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(
            f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def txtsplittermenu():
    os.system('title Split!! - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    lines = int(input(' \033[1;36;40mAmount of lines in each file\n \033[1;33;40m'))
    os.system('title Duplicate Remover - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    path = input(' \033[1;36;40mDrop txt file here\n \033[1;33;40m').strip('"')
    if Counter == 'False':
        txtsplitterwithoutcounter(lines, path)
    else:
        txtsplitter(lines, path)

def removebadlines(path):
    global combo_len, combo_checked, hits, status
    os.system('title I see... - Lunatic Editor - Made by Nami#7789')
    try:
        os.system('cls')
        print(title)
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        combo_len = len(open(path, 'rb').readlines())
        combo = open(path, 'rb')
        os.mkdir(f'result/{time}')
        w = open(f'result/{time}/Badlines Remover EmailPass.txt', 'w', encoding='utf-8')
        w1 = open(f'result/{time}/Badlines Remover UserPass.txt', 'w', encoding='utf-8')
        w2 = open(f'result/{time}/Badlines.txt', 'w', encoding='utf-8')
        hits = 0
        combo_checked = 0
        start_time = tm.time()
        status = 'busy'
        x = threading.Thread(target=counterbadlinesremover)
        x.start()
        for _ in range(combo_len):
            ae = str(combo.readline()).replace("b'", '').replace("\\r\\n'", '').strip('\n').replace(' ', '').replace(';', ':')
            combo_checked = combo_checked + 1
            if ':' in ae:
                if '@' in ae:
                    w.write(f'{ae}\n')
                    hits = hits + 1
                else:
                    w1.write(f'{ae}\n')
                    hits = hits + 1
            else:
                w2.write(f'{ae}\n')
        w1.close()
        w.close()
        w2.close()
        status = 'done'
        tm.sleep(1)
        os.system('title Finally! Done! btw I gonna change this script(Maybe Not) - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def removebadlineswithoutcounter(path):
    os.system('title I see... - Lunatic Editor - Made by Nami#7789')
    try:
        os.system('cls')
        print(title)
        print(' \033[1;36;40mRemoving...')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        combo_len = len(open(path, 'rb').readlines())
        combo = open(path, 'rb')
        os.mkdir(f'result/{time}')
        w = open(f'result/{time}/Badlines Remover EmailPass.txt', 'w', encoding='utf-8')
        w1 = open(f'result/{time}/Badlines Remover UserPass.txt', 'w', encoding='utf-8')
        w2 = open(f'result/{time}/Badlines.txt', 'w', encoding='utf-8')
        start_time = tm.time()
        for x in range(combo_len):
            ae = str(combo.readline()).replace("b'", '').replace("\\r\\n'", '').strip('\n').replace(' ', '').replace(';', ':')
            if ':' in ae:
                if '@' in ae:
                    w.write(f'{ae}\n')
                else:
                    w1.write(f'{ae}\n')
            else:
                w2.write(f'{ae}\n')
        w1.close()
        w.close()
        w2.close()
        combo.close()
        os.system('title Finally! Done! btw I gonna change this script(Maybe Not) - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def removebadlinessmenu():
    os.system('title Duplicate Remover - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    path = input(' \033[1;36;40mDrop txt file here\n \033[1;33;40m').strip('"')
    if Counter == 'False':
        removebadlineswithoutcounter(path)
    else:
        removebadlines(path)

def slowremovecapture(path, split_between):
    global all_lines, cap_removed, without_cap, invalid, open_path_len, status
    try:
        print(' \033[1;36;40mLoading...')
        open_path_len = len(open(path, 'rb').readlines())
        open_path = open(path, 'rb')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        w = open(f'result/{time}/Capture Removed EmailPass.txt', 'w', encoding='utf-8')
        q = open(f'result/{time}/No Capture.txt', 'w', encoding='utf-8')
        ps = open(f'result/{time}/Invalid.txt', 'w', encoding='utf-8')
        all_lines = 0
        cap_removed = 0
        without_cap = 0
        invalid = 0
        start_time = tm.time()
        status = 'busy'
        lq = threading.Thread(target=counterslowcaptureremover)
        lq.start()
        for _ in range(open_path_len):
            single_line_splitted_raw = str(open_path.readline()).replace("b'",  '').replace("\\r\\n'", '').replace(';', ':')
            single_line_splitted = single_line_splitted_raw.split(split_between)
            single_line_splitted_len = len(single_line_splitted)
            if not ':' in single_line_splitted_raw:
                ps.write(f'{single_line_splitted_raw}\n')
                invalid += 1
            elif not split_between in single_line_splitted_raw:
                q.write(str(single_line_splitted_raw).strip(' ') + '\n')
                without_cap += 1
            elif len(single_line_splitted) > 0:
                for x in range(single_line_splitted_len):
                    scan = str(single_line_splitted[x]).replace(' ', '')
                    if ':' in scan:
                        if '@' in scan:
                            w.write(f'{scan}\n')
                            cap_removed += 1
                            break

                        else:
                            open(f'result/{time}/Capture Removed Other.txt', 'a', encoding='utf-8').write(f'{scan}\n')

            else:
                ps.write(f'{single_line_splitted_raw}\n')
                invalid += 1
            all_lines += 1
        open_path.close()
        ps.close()
        w.close()
        q.close()
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        os.system('title Done!! Now go rape the hits - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        tm.sleep(0.6)
        status = 'done'
        tm.sleep(0.6)
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def slowremovecapturewithoutcounter(path, split_between):
    try:
        os.system('cls')
        print(title)
        print(' \033[1;36;40mLoading...')
        open_path_len = len(open(path, 'rb').readlines())
        open_path = open(path, 'rb')
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        cap_removed = 0
        os.mkdir(f'result/{time}')
        w = open(f'result/{time}/Capture Removed EmailPass.txt', 'w', encoding='utf-8')
        q = open(f'result/{time}/No Capture.txt', 'w', encoding='utf-8')
        ps = open(f'result/{time}/Invalid.txt', 'w', encoding='utf-8')
        print(' \033[1;36;40mRemoving...')
        start_time = tm.time()
        for _ in range(open_path_len):
            single_line_splitted_raw = str(open_path.readline()).replace("b'", '').replace("\\r\\n'", '').replace(';', ':')
            single_line_splitted = single_line_splitted_raw.split(split_between)
            single_line_splitted_len = len(single_line_splitted)
            if not ':' in single_line_splitted_raw:
                ps.write(f'{single_line_splitted_raw}\n')
            elif not split_between in single_line_splitted_raw:
                q.write(str(single_line_splitted_raw).strip(' ') + '\n')
            elif len(single_line_splitted) > 0:
                for x in range(single_line_splitted_len):
                    scan = single_line_splitted[x]
                    if ':' in scan:
                        if '@' in scan:
                            w.write(f'{scan}\n')
                            cap_removed += 1
                            break

                        else:
                            open(f'result/{time}/Capture Removed Other.txt', 'a', encoding='utf-8').write(f'{scan}\n')

            else:
                ps.write(f'{single_line_splitted_raw}\n')
        open_path.close()
        ps.close()
        w.close()
        q.close()
        os.system('title Done!! Now go rape the hits - Lunatic Editor - Made by Nami#7789')
        print(" \033[1;31;40m%s seconds\n" % (tm.time() - start_time))
        print('\n \033[1;36;40mFinish!\n Press Enter for Main Menu')
        input()
        mainmenu()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        os.system('cls')
        print(title)
        print(f' \033[1;31;40mError\n\n {e}\n\n The Error Saved in Error Logs.txt\n\n \033[1;36;40mPress Enter for Main Menu')
        input()
        mainmenu()

def capremoversmenu():
    os.system('title Capture Remover - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    path = input(' \033[1;36;40mDrop txt file here\n \033[1;33;40m').strip('"')
    os.system('cls')
    print(title)
    split_between = str(input(' \033[1;36;40mSplit Between\n \033[1;33;40m'))
    if Counter == 'False':
        slowremovecapturewithoutcounter(path, split_between)
    else:
        slowremovecapture(path, split_between)

def loweruppercase(ae, option):
    global temp
    first_letter = ae[0]
    if first_letter in ('1234567890~`!@#$%^&*()_-+=|\\}]{["\';:/?.>,<'):
        ae = ae.replace(f'{first_letter}', '')
        try:
            if not ae[0] in 'QWERTYIOPASDFGHJKLZXCVBNM':
                resp = f'{first_letter}{ae.capitalize()}'
            else:
                res = lambda ae: ae[:1].lower() + ae[1:] if ae else ''
                resp = f'{first_letter}{str(res(ae))}'
        except:
            resp = ae
        ae = f'{first_letter}{ae}'
    else:
        if not ae[0] in 'QWERTYIOPASDFGHJKLZXCVBNM':
            resp = ae.capitalize()
        else:
            res = lambda ae: ae[:1].lower() + ae[1:] if ae else ''
            resp = str(res(ae))
    if option == '1':
        option1(ae=ae)
        option1(ae=resp)
        return temp
    elif option == '2':
        option2(ae=ae)
        option2(ae=resp)
        return temp
    elif option == '3':
        option3(ae=ae)
        option3(ae=resp)
        return temp

def option1(ae): #add custom at the end of the string
    global temp
    custom = open('Data/custom1.txt', 'r').readlines()
    if strip == 'True':
        ae = ae.rstrip('1234567890~`!@#$%^&*()_-+=|\\}]{["\';:/?.>,<')
    temp.append(f'{ae}')
    for y in range(len(custom)):
        a = custom[y].strip("\n")
        temp.append(f'{ae}{a}')
    return temp

def option2(ae): #option 1 & replace the last speacial character
    global temp
    custom = open('Data/custom2.txt', 'r').readlines()
    if strip == 'True':
        ae = ae.rstrip('1234567890')
    for x in range(len(ae)):
        if ae[-x] in ('~`!@#$%^&*()_-+={[}]|\\"\';:/?.>,<'):
            temp.append(f'{ae}')
            for y in range(len(custom)):
                a = custom[y].strip("\n")
                temp.append(f'{ae}{a}')
                temp.append(f'{ae.replace(str(ae[-x]), f"{a}")}')
    return temp

def option3(ae): #option 1 & replace the last digit
    global temp
    custom = open('Data/custom3.txt', 'r').readlines()
    if strip == 'True':
        ae = ae.rstrip('~`!@#$%^&*()_-+=|\\}]{["\';:/?.>,<')
    for x in range(len(ae)):
        if ae[-x].isdigit() == True:
            temp.append(f'{ae}')
            for xr in range(repeat):
                temp.append(f'{ae.replace(str(ae[-x]), f"{int(ae[-x]) + (xr + 1)}")}')
            for y in range(len(custom)):
                a = custom[y].strip("\n")
                temp.append(f'{ae}{a}')
                for xr in range(repeat):
                    temp.append(f'{ae.replace(str(ae[-x]), f"{int(ae[-x]) + (xr + 1)}")}{a}')
    return temp



def fixcombomenu(path, option):
    global temp
    os.system('title ae - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    os.mkdir(f'result/{time}')
    w_len = len(open(path, 'rb').readlines())
    w = open(path, 'rb')
    print('Fixing your combo...')
    edited_write = open(f'result/{time}/Edited.txt', 'w', encoding='utf-8')
    if UppercaseLowercase == 'True':
        for _ in range(w_len):
            singe_line = str(w.readline()).replace("b'", '').replace("\\r\\n'", '')
            if ':' in singe_line:
                ae = singe_line.split(':')[-1]
                if not ae in ['', ' ']:
                    loweruppercase(ae=ae, option=option)
                    email = singe_line.split(':')[0]
                    b = option1(ae=ae)
                    b = list(dict.fromkeys(b))
                    b_len = len(b)
                    for x in range(b_len):
                        edited_write.write(f'{email}:{b[x]}\n')
                    temp = []
    else:
        if option == '1':
            for _ in range(w_len):
                singe_line = str(w.readline()).replace("b'", '').replace("\\r\\n'", '')
                if ':' in singe_line:
                    ae = singe_line.split(':')[-1]
                    if not ae in ['', ' ']:
                        email = singe_line.split(':')[0]
                        b = option1(ae=ae)
                        b = list(dict.fromkeys(b))
                        b_len = len(b)
                        for x in range(b_len):
                            edited_write.write(f'{email}:{b[x]}\n')
                        temp = []

        elif option == '2':
            for _ in range(w_len):
                singe_line = str(w.readline()).replace("b'", '').replace("\\r\\n'", '')
                if ':' in singe_line:
                    ae = singe_line.split(':')[-1]
                    if not ae in ['', ' ']:
                        email = singe_line.split(':')[0]
                        b = option2(ae=ae)
                        b = list(dict.fromkeys(b))
                        b_len = len(b)
                        for x in range(b_len):
                            edited_write.write(f'{email}:{b[x]}\n')
                        temp = []
        elif option == '3':
            for _ in range(w_len):
                singe_line = str(w.readline()).replace("b'", '').replace("\\r\\n'", '')
                if ':' in singe_line:
                    ae = singe_line.split(':')[-1]
                    if not ae in ['', ' ']:
                        email = singe_line.split(':')[0]
                        b = option3(ae=ae)
                        b = list(dict.fromkeys(b))
                        b_len = len(b)
                        for x in range(b_len):
                            edited_write.write(f'{email}:{b[x]}\n')
                        temp = []
    os.system('cls')
    print(title)
    print(' done...')
    print(' Press Enter for main menu')
    input()
    mainmenu()

def fixcombomenu_():
    os.system('title Duplicate Remover - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    print(' \033[1;36;40medit uppercase and lowercase can be disable in settings\n Strip can be disable and enable in settings\n repeat in settings for option3, u can make an experiment by urself\n option1 = add custom1 at the end of the pass\n option2 = replace the last special character in password with custom2\n option3 = replace the last digit in pass wih custom3\n---------------------------------------------------')
    option = str(input(f' \033[1;35;40m[\033[1;36;40m1\033[1;35;40m]  \033[1;36;40mOption 1\n \033[1;35;40m[\033[1;36;40m2\033[1;35;40m]  \033[1;36;40mOption 2\n \033[1;35;40m[\033[1;36;40m3\033[1;35;40m]  \033[1;36;40mOption 3\n\n '))
    if not option in '123':
        fixcombomenu_()
    os.system('cls')
    print(title)
    path = input(' \033[1;36;40mDrop txt file here\n \033[1;33;40m').strip('"')
    fixcombomenu(path, option=option)

def settings():
    global Counter
    try:
        os.system('title Settings!! - Lunatic Editor - Made by Nami#7789')
        os.system('cls')
        print(title)
        Counter = loaddata()['Counter']
        AutoLogin = loaddata()['AutoLogin']['Status']
        Username = loaddata()['AutoLogin']['Username']
        Password = loaddata()['AutoLogin']['Password']
        UppercaseLowercase = loaddata()['UppercaseLowercase']
        strip = loaddata()['Strip']
        repeat = int(loaddata()['Repeat'])
        if Counter == 'True':
            m_Counter = '\033[1;32;40mTrue'
        else:
            m_Counter = '\033[1;31;40mFalse'
        if AutoLogin == 'True':
            m_AutoLogin = '\033[1;32;40mTrue'
        else:
            m_AutoLogin = '\033[1;31;40mFalse'
        if UppercaseLowercase == 'True':
            m_UppercaseLowercase = '\033[1;32;40mTrue'
        else:
            m_UppercaseLowercase = '\033[1;31;40mFalse'
        if strip == 'True':
            m_strip = '\033[1;32;40mTrue'
        else:
            m_strip = '\033[1;31;40mFalse'
        choice = str(input(f' \033[1;35;40m[\033[1;36;40m1\033[1;35;40m]  \033[1;36;40mCounter : {m_Counter} \033[1;36;40m(Faster without counter)\n \033[1;35;40m[\033[1;36;40m2\033[1;35;40m]  \033[1;36;40mAutoLogin : {m_AutoLogin}\n \033[1;35;40m[\033[1;36;40m3\033[1;35;40m]  \033[1;36;40mUppercaseLowercase (fixcombo) : {m_UppercaseLowercase}\n \033[1;35;40m[\033[1;36;40m4\033[1;35;40m]  \033[1;36;40mstrip (fixcombo) : {m_strip}\n \033[1;35;40m[\033[1;36;40m5\033[1;35;40m]  \033[1;36;40mrepeat (fixcombo) : {loaddata()["Repeat"]}\n\n \033[1;36;40mEnter for Main Menu\n '))
        if choice == '1':
            if Counter == 'True':
                Counter = 'False'
            else:
                Counter = 'True'
            open('Data/Config.txt', 'w', encoding='utf-8').write(
                f'{str("{")}\n    "Counter":"{Counter}",\n    "AutoLogin":{str("{")}\n        "Status":"{AutoLogin}",\n        "Username":"{Username}",\n        "Password":"{Password}"\n    {str("}")},\n    "UppercaseLowercase":"{UppercaseLowercase}",\n    "Strip":"{strip}",\n    "Repeat":"{repeat}"\n{str("}")}')
        elif choice == '2':
            if AutoLogin == 'True':
                open('Data/Config.txt', 'w', encoding='utf-8').write(
                    f'{str("{")}\n    "Counter":"{Counter}",\n    "AutoLogin":{str("{")}\n        "Status":"False",\n        "Username":"",\n        "Password":""\n    {str("}")},\n    "UppercaseLowercase":"{UppercaseLowercase}",\n    "Strip":"{strip}",\n    "Repeat":"{repeat}"\n{str("}")}')
            else:
                AutoLogin = 'True'
                os.system('title Settings!! - Lunatic Editor - Made by Nami#7789')
                os.system('cls')
                print(title)
                Username = input(' \033[1;36;40mUsername : ')
                Password = input(' \033[1;36;40mPassword : ')
                open('Data/Config.txt', 'w', encoding='utf-8').write(
                    f'{str("{")}\n    "Counter":"{Counter}",\n    "AutoLogin":{str("{")}\n        "Status":"{AutoLogin}",\n        "Username":"{Username}",\n        "Password":"{Password}"\n    {str("}")},\n    "UppercaseLowercase":"{UppercaseLowercase}",\n    "Strip":"{strip}",\n    "Repeat":"{repeat}"\n{str("}")}')
        elif choice == '3':
            if UppercaseLowercase == 'True':
                UppercaseLowercase = 'False'
            else:
                UppercaseLowercase = 'True'
            open('Data/Config.txt', 'w', encoding='utf-8').write(
                f'{str("{")}\n    "Counter":"{Counter}",\n    "AutoLogin":{str("{")}\n        "Status":"{AutoLogin}",\n        "Username":"{Username}",\n        "Password":"{Password}"\n    {str("}")},\n    "UppercaseLowercase":"{UppercaseLowercase}",\n    "Strip":"{strip}",\n    "Repeat":"{repeat}"\n{str("}")}')
        elif choice == '4':
            if strip == 'True':
                strip = 'False'
            else:
                strip = 'True'
            open('Data/Config.txt', 'w', encoding='utf-8').write(
                f'{str("{")}\n    "Counter":"{Counter}",\n    "AutoLogin":{str("{")}\n        "Status":"{AutoLogin}",\n        "Username":"{Username}",\n        "Password":"{Password}"\n    {str("}")},\n    "UppercaseLowercase":"{UppercaseLowercase}",\n    "Strip":"{strip}",\n    "Repeat":"{repeat}"\n{str("}")}')
        elif choice == '5':
            repeat = str(input('\033[1;36;40m How Much Fix Combo Option 3 Gonna add number\n ')).replace('~`!@#$%^&*()_-+=\\|]}[{"\';:/?.>,<qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM', '')
            open('Data/Config.txt', 'w', encoding='utf-8').write(
                f'{str("{")}\n    "Counter":"{Counter}",\n    "AutoLogin":{str("{")}\n        "Status":"{AutoLogin}",\n        "Username":"{Username}",\n        "Password":"{Password}"\n    {str("}")},\n    "UppercaseLowercase":"{UppercaseLowercase}",\n    "Strip":"{strip}",\n    "Repeat":"{repeat}"\n{str("}")}')

        elif choice == '':
            loadalldata()
            mainmenu()
        else:
            settings()
        settings()
    except Exception as e:
        open('Error Logs.txt', 'a', encoding='utf-8').write(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} - {e}\n")
        mainmenu()


def mainmenu():
    os.system('title Main Menu - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    choice = str(input(f' \033[1;35;40m[\033[1;36;40m1\033[1;35;40m]  \033[1;36;40mDomain/.com Sorter (Slow)\n \033[1;35;40m[\033[1;36;40m2\033[1;35;40m]  \033[1;36;40mDomain/.com Sorter (Fast)\n \033[1;35;40m[\033[1;36;40m3\033[1;35;40m]  \033[1;36;40mHits Remover\n \033[1;35;40m[\033[1;36;40m4\033[1;35;40m]  \033[1;36;40mtxt merger\n \033[1;35;40m[\033[1;36;40m5\033[1;35;40m]  \033[1;36;40mDuplicate Remover\n \033[1;35;40m[\033[1;36;40m6\033[1;35;40m]  \033[1;36;40mTxt Splitter\n \033[1;35;40m[\033[1;36;40m7\033[1;35;40m]  \033[1;36;40mRemove Bad Lines (E:P)\n \033[1;35;40m[\033[1;36;40m8\033[1;35;40m]  \033[1;36;40mCapture Remover\n \033[1;35;40m[\033[1;36;40m9\033[1;35;40m]  \033[1;36;40mFix Combo\n\n \033[1;35;40m[\033[1;36;40m10\033[1;35;40m]  \033[1;36;40mSettings\n\n'))

    if choice == '1':
        domainsortermenu('slow')
    elif choice == '2':
        domainsortermenu('fast')
    elif choice == '3':
        hitremovermenu()
    elif choice == '4':
        textmergermenu()
    elif choice == '5':
        duplicateremovermenu()
    elif choice == '6':
        txtsplittermenu()
    elif choice == '7':
        removebadlinessmenu()
    elif choice == '8':
        capremoversmenu()
    elif choice == '9':
        fixcombomenu_()
    elif choice == '10':
        settings()
    else:
        mainmenu()

def login():
    os.system('title Login - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    Username = str(input(' \033[1;36;40mUsername : '))
    Password = str(input(' \033[1;36;40mPassword : '))
    json = {
        'Username':Username,
        'Password':Password,
        'HWID':get_id()
    }
    resp = (str(requests.post(f'{auth_url}login', json=json).content)).strip("b'")
    if '-' in resp:
        Duration = resp.split(' - ')[1]
        os.system('title Login - Lunatic Editor - Made by Nami#7789')
        os.system('cls')
        message = f' \033[1;36;40mWelcome,\n \033[1;36;40mExpire Date : \033[1;32;40m{Duration}\n\n \033[1;36;40mPress Enter for Main Menu'
        os.system('title Login - Lunatic Editor - Made by Nami#7789')
        os.system('cls')
        print(title)
        print(message)
        input()
        mainmenu()
    else:
        os.system('cls')
        print(title)
        print(f' \033[1;31;40m{resp}\n\n \033[1;36;40mPress Enter for Login Page')
        input()
        loginpage()

def register():
    os.system('title Register - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    Username = str(input(' \033[1;36;40mUsername : '))
    Password = str(input(' \033[1;36;40mPassword : '))
    Key = str(input(' \033[1;36;40mKey : '))
    json = {
        'Username': Username,
        'Password': Password,
        'HWID': get_id(),
        'Key':Key
    }
    resp = (str(requests.post(f'{auth_url}register', json=json).content)).strip("b'")
    if '-' in resp:
        os.system('cls')
        print(title)
        print(f' \033[1;32;40m{resp}\n\n \033[1;36;40mPress Enter for Login Page')
        input()
        login()
    else:
        os.system('cls')
        print(title)
        print(f' \033[1;31;40m{resp}\n\n \033[1;36;40mPress Enter for Login Page')
        input()
        loginpage()

def showHWID():
    os.system('title HWID - Lunatic Editor - Made by Nami#7789')
    os.system('cls')
    print(title)
    print(f' \033[1;32;40m{get_id()}\n\n \033[1;36;40mPress Enter for Login Page')
    input()
    loginpage()

def dcserver():
    os.system('title Discord - Lunatic Editor - Made by Nami#7789')
    resp = (str(requests.get(f'{auth_url}discord').content)).strip("b'").split('\\n')
    resp_len = len(resp)
    os.system('cls')
    print(title)
    for x in range(resp_len):
        print(resp[x])
    print(f'\n\n \033[1;36;40mPress Enter for Login Page')
    input()
    loginpage()

def loginpage():
    os.system('cls')
    print(title)
    choice = str(input(' \033[1;35;40m[\033[1;36;40m1\033[1;35;40m]  \033[1;36;40mLogin\n \033[1;35;40m[\033[1;36;40m2\033[1;35;40m]  \033[1;36;40mRegister\n \033[1;35;40m[\033[1;36;40m3\033[1;35;40m]  \033[1;36;40mShow HWID\n \033[1;35;40m[\033[1;36;40m4\033[1;35;40m]  \033[1;36;40mDiscord Server\n\n '))
    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        showHWID()
    elif choice == '4':
        dcserver()
    else:
        loginpage()

if loaddata()['AutoLogin']['Status'] == 'True':
    Username = loaddata()['AutoLogin']['Username']
    Password = loaddata()['AutoLogin']['Password']
    json = {
        'Username': Username,
        'Password': Password,
        'HWID': get_id()
    }
    resp = (str(requests.post(f'{auth_url}login', json=json).content)).strip("b'")
    if '-' in resp:
        Duration = resp.split(' - ')[1]
        os.system('title Login - Lunatic Editor - Made by Nami#7789')
        os.system('cls')
        message = f' \033[1;36;40mWelcome,\n \033[1;36;40mExpire Date : \033[1;32;40m{Duration}\n\n \033[1;36;40mPress Enter for Main Menu'
        print(title)
        print(message)
        input()
        mainmenu()
    else:
        os.system('cls')
        print(title)
        print(f' \033[1;31;40m{resp}\n\n \033[1;36;40mPress Enter for Login Page')
        input()
        loginpage()
else:
    mainmenu()
    #loginpage()
input()
