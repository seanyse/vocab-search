import time
import datetime
import sys
import eel
import tkinter
from tkinter import Tk
from tkinter import filedialog
from tkinter import *
import requests
from bs4 import BeautifulSoup
import threading
import pyperclip


global kill

eel.init('web')

list = ['',]


# some code in search function sourced and cited
@eel.expose
def normalSearch():
    fout = open('result.txt', 'w')
    result = ''
    count = 1
    
    x = 1
    
    
    # request headers
    # headers taken from https://requests.readthedocs.io/en/master/user/quickstart/
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Encoding': 'identity'
    }

    start_time = time.time()
    
    fin = open('vocab.txt', 'r')
    

    for line in fin:
        
        count = count + 1
        query = line.strip()
        query = query.replace("►", "").replace(".", "").replace("•", "")
        global parameters

        print(query + "in test")
        print(parameters + "in test")

        url = ("https://www.google.com/search?q=" + query + "+definition+" + parameters)
        print("url = " + url)
        x = 0
        while True:

            try:
                # get session 
                status = f"{datetime.datetime.now()} Requesting Query"
                eel.setstatus(status)
                request = requests.Session()
                result = request.get(url, headers=headers,)
                break
            
            except:
                eel.setstatus(f'{datetime.datetime.now()} An Internal Error Occured Retrying ...')
                time.sleep(1)
     
        while True:
            try:
                # beutiful soup to find text by class
                eel.setstatus(f"{datetime.datetime.now()} Parsing Query")
                
                soup = BeautifulSoup(result.text, "html.parser")
                result_soup = soup.find('span', {'class':"FCUp0c"})
                
                result_str = str(result_soup.parent.text)
                # result_soup = soup.find_all(class_="hgKElc")
                # result_str = str(result_soup)
                status = result_str
                eel.setstatus(status)
                break

            except Exception as e:
                
                eel.setstatus(f"Internal Error Occured, {e} {x}/3")
                time.sleep(1)
                x = x+1
                if x == 3:
                    eel.setstatus(f"Internal Error Occured, {e} FATAL")
                    x = 0
                    result_str = "None"
                    break

        # beutify text, remove all useless html
        result = result_str.replace('[<span class="hgKElc"><b>',"").replace("</b>", "").replace("</span>]","").replace('[<span class="hgKElc">',"").replace("<b>","").replace(query,"")
        # instead of result being an empty bracket, its query does not exist
        global fallback_status
        if result == '[]' and fallback_status == False:
            
            status = 'Query does not exist, manual search required'
            eel.setstatus(status)
            result = 'Query does not exist, manual search required'

        print("lets ssee")
        print(len(result))
        
        print(fallback_status)
        if len(result) < 20 and fallback_status == "True":

            eel.setstatus("Proper Result Not Found, Reattempting 2")
            
            url = ("https://www.google.com/search?q=" + query + "+definition")
            print(f"url 2 = {url}")
            eel.setstatus(f"{datetime.datetime.now()} Parsing Query 2")
            request = requests.Session()
            result1 = request.get(url, headers=headers, )
            
            result_soup = soup.find('span', {'class':"FCUp0c"})
            
            try:
                result_str = str(result_soup.parent.text)
            except Exception as e:
                result_str = result_str.replace('[<span class="hgKElc"><b>',"").replace("</b>", "").replace("</span>]","").replace('[<span class="hgKElc">',"").replace("<b>","").replace(query,"")

            print(f"result_str = {result_str}")
            # result_soup = soup.find_all(class_="hgKElc")
            # result_str = str(result_soup)
            result = result_str.replace('[<span class="hgKElc"><b>',"").replace("</b>", "").replace("</span>]","").replace('[<span class="hgKElc">',"").replace("<b>","").replace(query,"")
            result = "*fb1" + result

            if len(result) < 20 and fallback_status == "True":
                eel.setstatus("Proper Result Still Not Found, Reattempting 3")

                url = ("https://www.google.com/search?q=" + query)
                request = requests.Session()
                result = request.get(url, headers=headers, )
                # fin1 = open("googlehtml.txt", "w")
                soup = BeautifulSoup(result.text, "html.parser")
                data = soup.prettify()
                # fin1.write(data)
                # fin1.close
                result_soup = soup.findAll('div', {'class':"BNeawe s3v9rd AP7Wnd"})[-1].string
                result = "*fb2 " + str(result_soup)


        # write to file and list, and repeat
        try:
            parsed = (f"{count-1}){query}:{result}\n")
            fout.write(parsed)
            list.append(parsed)
        except:
            pass

        global kill
        if kill == True:
            # quit function if user wants to stop
            # sys.exit()
            break
        
        
        # parsed.append(list[cocount_l = count_l + 1
    # execution time
    status = (f"-- Execution Complete, Thread Kill = {kill}, Took %s Seconds --" % (time.time() - start_time))
    eel.setstatus(status)
    fout.close()
    with open('result.txt','r') as read:
        output = read.read()
        
        read.close()
        print(output)
    eel.setOutput(output)

@eel.expose
def proxySearch():
    fout = open('result.txt', 'w')
    result = ''
    count = 1
    
    x = 1
    fout.write("VocabSearch v1.0\n")
    # request headers
    # headers taken from https://requests.readthedocs.io/en/master/user/quickstart/
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Encoding': 'identity'
    }
    proxy_list = eel.proxy_list()()
    print(f"proxy_list = {proxy_list}")

    try:
        proxiesDict = {
        "http" : "http://" + proxy_list,    
        "https" : "https://" + proxy_list,
        }
    except TypeError:
        eel.setstatus("Invalid Proxy")

    start_time = time.time()
    
    fin = open('vocab.txt', 'r')
    

    for line in fin:
        
        count = count + 1
        query = line.strip()
        query = query.replace("►", "").replace(".", "").replace("•", "")
        url = ("https://www.google.com/search?q=" + query + "+" + "definition+" + parameters)
        print(url)
        status = url
        eel.setstatus(status)
        x = 0
        while True:

            try:
                # get session 
                status = f"{datetime.datetime.now()} Requesting Query"
                eel.setstatus(status)
                request = requests.Session()
                result = request.get(url, headers=headers, proxies=proxiesDict)
                break
            
            except Exception as e:
                eel.setstatus('Proxy Error or IP Banned')
                print(e)
                time.sleep(5)
                global kill
                if kill == True:
                    eel.setstatus("Stopped")
                    sys.exit()
     
        while True:
            try:
                # beutiful soup to find text by class
                eel.setstatus(f"{datetime.datetime.now()} Parsing Query")
                
                soup = BeautifulSoup(result.text, "html.parser")
                result_soup = soup.find('span', {'class':"FCUp0c"})
                
                result_str = str(result_soup.parent.text)
                print(result_str)
                # result_soup = soup.find_all(class_="hgKElc")
                # result_str = str(result_soup)
                break

            except Exception as e:
                
                eel.setstatus(f"Internal Error Occured, {e} {x}/3")
                time.sleep(1)
                x = x+1
                if x == 3:
                    eel.setstatus(f"Internal Error Occured, {e} FATAL")
                    x = 0
                    result_str = "None"
                    break


        # beutify text, remove all useless html
        try:
            result = result_str.replace('[<span class="hgKElc"><b>',"").replace("</b>", "").replace("</span>]","").replace('[<span class="hgKElc">',"").replace("<b>","").replace(query,"")
        except:
            pass
        # instead of result being an empty bracket, its query does not exist
    
        if len(result) < 20 and fallback_status == "True":

            eel.setstatus("Proper Result Not Found, Reattempting 2")
            
            url = ("https://www.google.com/search?q=" + query + "+definition")
            print(f"url 2 = {url}")
            eel.setstatus(f"{datetime.datetime.now()} Parsing Query 2")
            request = requests.Session()
            result1 = request.get(url, headers=headers, proxies=proxiesDict)
            
            result_soup = soup.find('span', {'class':"FCUp0c"})
            try:
                result_str = str(result_soup.parent.text)
            except Exception as e:
                result_str = result_str.replace('[<span class="hgKElc"><b>',"").replace("</b>", "").replace("</span>]","").replace('[<span class="hgKElc">',"").replace("<b>","").replace(query,"")

            print(f"result_str = {result_str}")
            # result_soup = soup.find_all(class_="hgKElc")
            # result_str = str(result_soup)
            result = result_str.replace('[<span class="hgKElc"><b>',"").replace("</b>", "").replace("</span>]","").replace('[<span class="hgKElc">',"").replace("<b>","").replace(query,"")
            result = "*fb1" + result

            if len(result) < 20 and fallback_status == "True":
                eel.setstatus("Proper Result Still Not Found, Reattempting 3")

                url = ("https://www.google.com/search?q=" + query)
                request = requests.Session()
                result = request.get(url, headers=headers, proxies=proxiesDict)
                # fin1 = open("googlehtml.txt", "w")
                soup = BeautifulSoup(result.text, "html.parser")
                data = soup.prettify()
                # fin1.write(data)
                # fin1.close
                result_soup = soup.findAll('div', {'class':"BNeawe s3v9rd AP7Wnd"})[-1].string
                result = "*fb2 " + str(result_soup)
                
        
            

        # write to file and list, and repeat
        try:
            parsed = (f"{count-1}){query}:{result}\n")
            fout.write(parsed)
            list.append(parsed)
        except:
            pass
        
    
        if kill == True:
            # quit function if user wants to stop
            # sys.exit()
            break
        else:
            pass
        
        # parsed.append(list[cocount_l = count_l + 1
    # execution time
    
    
    fout.close()
    with open('result.txt','r') as read:
        output = read.read()
        
        read.close()
        print(output)
    eel.setOutput(output)
    eel.setstatus(f"-- Execution Complete, Thread Kill = {kill}, Took %s Seconds --" % (time.time() - start_time))
@eel.expose
# transfers data in list into result.txt
def save(result):

    fout =  open('result.txt', 'w')
    # transverse a list
    for item in list:
        fout.write(item)
    fout.close()
    eel.setstatus("File Explorer Opened, Waiting for User Response")

    export = Tk()
    export.attributes("-topmost", True)
    export.withdraw()
    filename = filedialog.asksaveasfilename(initialdir='/', title='Save As', filetypes=(('Text Documents', '*.txt'), ))
    item = ''
    
    # to test
    eel.setstatus("Results Successfully Exported")

    fout2 = open(filename + '.txt', 'w')
    for item in list:
        fout2.write(item)
    fout2.close()
    export.destroy()

    return(result)
    
@eel.expose
def stop():
    stop = threading.Thread(target=stop_1, args=()) 
    stop.start()

@eel.expose

def stop_1():
    global kill
    kill = True
    status = "Stopping"
    eel.setstatus(status)
@eel.expose
def start():
    global kill
    kill = False
    start = threading.Thread(target=start_1, args=()) 
    start.start()
@eel.expose
def start_1():
    eel.setstatus("Checking Data")
    input_i = eel.getInput()()
    input_py = str(input_i)
    print(input_py)
    fin = open("vocab.txt", 'w+')
    # checks to see if there is data in input field or file
    if len(input_py) > 0:
        fin = open("vocab.txt", 'w')
        fin.write(input_py)
        fin.close()
    elif len(input_py) and len(fin) == 0:
        eel.setstatus("Input Must Not Be Blank")
        stop()
    global parameters
    global fallback_status
    parameters = eel.parameters()()
    if parameters == None:
        parameters = "quizlet"
    try:
        parameters = parameters.replace(" ","+")
    except:
        pass

    print(f"parameter = {parameters}")
    fallback_status = eel.fallback_status()()
    print(f"fallback_status = {fallback_status}")
    proxy_status = eel.proxy_status()()
    print(f"proxy_status = {proxy_status}")
    
    
    if proxy_status == False:
        eel.setstatus("Data Collected, Starting Search")
        threading.Thread(target=normalSearch(), args=(), daemon=True).start()
    else:
        eel.setstatus("Data Collected, Starting Search")
        threading.Thread(target=proxySearch(), args=(), daemon=True).start()
    # except:
    #     status = f"{datetime.datetime.now()} Chromedriver Not Found"
    #     eel.setstatus(status)


@eel.expose
def getPathToFile():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    path = filedialog.askopenfilename()
    print(path)

    loadDataToTextin(path)


    # return path

def loadDataToTextin(file_path):
    data = None
    with open(file_path,'r') as read:
        data = read.read()

    print(data)
    eel.setDataFromFile(data)

@eel.expose
# copy function used in this program cited below
def copy():
    # copies to clipboard, copy pasted from stack overflow https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard
    with open("result.txt", "r") as read:
        output = read.read()
        read.close()

    pyperclip.copy(output)
    spam = pyperclip.paste()

    eel.setstatus("Successfully Copied To Clipboard")
    
@eel.expose
def py_find():
    kew = eel.getKeyWord()()
    kw = str(kew)
    kw = kw.lower()
    
    fin = open("result.txt", "r")
    count = 0
    for line in fin:
        if line != "\n":
            count = count + 1
    fin.close()
    lines = count
    count1 = 0 
    with open("result.txt", "r") as data:
        while count1 < lines:
            line = data.readline()
            line = line.lower()

            if kw in line: 
                eel.setOutput(line)
                eel.setstatus("Search Results Found")
                break

            else:
                eel.findSetOutput("No Search Results Found")
                eel.setstatus("No Search Results Found")
               

            count1 = count1 + 1
    if kw == '':
        with open('result.txt', 'r') as file:
            data = file.read().replace('\n', '')
        
        eel.setOutput(data)
        eel.setstatus("Search Parameters Cleared")

                
@eel.expose
def printnow(print):
    print(print)
    
# sets gui size
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')
eel.start(mode='electron', size=(1075, 550), port=1904)

