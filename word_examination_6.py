__author__ = 'TakuyaSakaguchi'


from bs4 import BeautifulSoup
import requests
from random import randint


def getAllLink(givensoup):
    #put soup and return all links in the soup as a list.
    tempLinkList = []

    for link in givensoup.find_all('a'):
    # print(link.get('href'))
        if link.get('href') != None:
            tempLinkList.append(link.get('href'))

    return tempLinkList


def makeWordAndLinkList(givenList):
    # input all URL list and return word and their url lists.
    tempWordList = []
    tempLinkList = []
    for item in givenList:
        if "dictionary.reference" in item:
        #print (item)

            if "%20?" in item:
                trimmed_word = item[item.rindex("/")+1:item.rindex("%")]
            elif "+?" in item:
                trimmed_word = item[item.rindex("/")+1:item.rindex("+")]
            elif "?" in item:
                trimmed_word = item[item.rindex("/")+1:item.rindex("?")]
            else:
                trimmed_word = item[item.rindex("/")+1:]

            tempLinkList.append(item)
            tempWordList.append(trimmed_word)

    return(tempWordList, tempLinkList)


def wordTest(repeatNumber, given_dictionary_list, given_word_list):
    fo = open("unknown_words.txt","a")
    counter = 1
    while counter <= repeatNumber:
        n = randint(0,len(given_dictionary_list))
        print(given_dictionary_list[n])
        print(given_word_list[n])
        answer = input("do you know this word, y/n:")
        if answer == "y":
            print ("good")
        elif answer == "n":
            print ("bad")
            #word_not_know.append(word_list[n])
            #dictionary_list_not_know.append(dictionary_list[n])
            fo.write(given_word_list[n] + "\n")
        else:
            print("push y or n only please!!")
        counter +=1
    fo.close()


def makeDictionary(given_dictionary_list, given_word_list):
    # return as a dictionary
    tempDic = {}
    for i in range (len(given_word_list)):
        tempDic[given_word_list[i]]=given_dictionary_list[i]
    return tempDic


def obtainUnkownWordList():
    # open file and return unremembered words as a list
    fo = open("unknown_words.txt","r")
    temp_list = fo.readlines()
    uk_wordList = []
    for item in temp_list:
        uk_wordList.append(item.replace("\n",""))
    #print (uk_wordList)
    return uk_wordList

def getLinkOfOlderPost(givenSoup):
    temp_old_link_html= None
    for i in givenSoup.find_all("a"):
        if "Older Post" in str(i):
            temp_old_link_html = i.get("href")
    return temp_old_link_html

def getSoupFromLink(givenhtml):

    temp_html_source = requests.get(givenhtml)
    temp_html_txt = str(temp_html_source.text)
    temp_soup = BeautifulSoup(temp_html_txt, "html.parser")
    return temp_soup


def main():

    url = 'http://wordyn.blogspot.com'

    soup = getSoupFromLink(url)

    linkList_All = getAllLink(soup)

    word_list, word_link_list = makeWordAndLinkList(linkList_All)

    #print(soup.text)



    old_link_html = getLinkOfOlderPost(soup)

    soup_old = getSoupFromLink(old_link_html)

    oldLinkList_All = getAllLink(soup_old)
    #print (oldLinkList)
    word_old_list, word_link_old_list = makeWordAndLinkList(oldLinkList_All)
    #print (word_old_list)
    #print(dictionary_old_list)

    word_list += word_old_list
    word_link_list += word_link_old_list

    #print(soup_old.text)


    wordTest(3, word_link_list, word_list)

    addressDic = makeDictionary(word_link_list, word_list)


    unknownWordList = obtainUnkownWordList()
    unknownDictionarylist = []
    for item in unknownWordList:
        unknownDictionarylist.append(addressDic[item])


    wordTest(1, unknownDictionarylist,unknownWordList)

    print(len(unknownWordList))


if __name__ == "__main__":
    main()
