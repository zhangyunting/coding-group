#encoding=utf-8
from  random import randint

def buildWordDic(text):
    text = text.replace("\n", "")
    text = text.replace("\"", "")
    punctuation = [",", ".", "?", ";", ":"]
    for punc in punctuation:
        text = text.replace(punc, " " + punc + "")

    words = text.split(" ")
    word = [word for word in words if word != "" ]

    wordDic = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDic:
            wordDic[words[i-1]] = {}
        if words[i] not in wordDic[words[i-1]]:
            wordDic[words[i-1]][words[i]] = 0
        wordDic[words[i - 1]][words[i]] += 1
    return wordDic

def wordlistSum(wordlist):
    sum = 0
    for word, value in wordlist.items():
        sum += value
    return sum

def retrieveRandomWork(wordlist):
    randIndex = randint(1, wordlistSum(wordlist)) #在[1,n)区间内取随机整数
    for word, value in wordlist.items():
        randIndex -= value
        if randIndex <= 0:
            return word


file = str(open("F:\\研究生\\研一\\编程小组\\03-马尔科夫自然语言处理\\Genesis.txt").read())
wordDict = buildWordDic(file)
print(wordDict)

length = 100
chain = ""
currentWord = "The"
for i in range(length):
    chain += currentWord + " "
    currentWord = retrieveRandomWork(wordDict[currentWord])

print(chain)