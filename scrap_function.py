import time
from selenium import webdriver

# Aller sur le profil de tous les amis et renvoyer la liste de leurs amis
def go_profile(pause, browser):
    
    my_friends = ami_list(pause, browser)
    wesh = browser.find_elements_by_xpath("//ul[@data-pnref='friends']/li/div/a")
    length = len(wesh)
    print('J ai ', length, ' amis')
    amis_damis = []
    z=0
    for i in range(length):
        
        if((i+1)%20==0):
            print('i = ', i+1)
            z=z+1
        for j in range(z):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause+2)

        browser.find_elements_by_xpath("//ul[@data-pnref='friends']/li/div/a")[i].click()
        voir_amis(pause, browser)
        print('searching', my_friends[i] ,"'s friends") 
        som1_friends = ami_list(pause, browser)
        print(my_friends[i], 'has ', len(som1_friends), ' friends')
        amis_damis.append(som1_friends)

        preced(browser)
        preced(browser)
    return amis_damis, my_friends

#return a friends' list of someone
def ami_list(pause, browser):
 
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(pause)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True

    liste = []
    liste_webel = browser.find_elements_by_xpath("//ul[@data-pnref='friends']/li/div/div/div[@class='uiProfileBlockContent']/div/div/div")
    length = len(liste_webel)
    for z in range(length):
        liste.append(liste_webel[z].text)
    return liste

# Go to last page
def preced(browser):
    browser.execute_script("window.history.go(-1)")

# See a friends' friends list
def voir_amis(pause, browser):
    time.sleep(pause)
    browser.find_elements_by_xpath("//a[@class='_39g6']/span")[1].click()

def nb_common_friends(nom, a):
    nb=0
    for i in range(162):
        if(nom in a[i]):
            nb=nb+1
    return nb

def split_name(pre_nom):
    wesh = pre_nom.split(' ')[0][0] + '. '+pre_nom.split(' ')[-1]
    return wesh