import re
import unittest


### 1)  Write a function sumNums(filename) to read from a file when given 
## the filename and look for integers (that are not phone numbers) using the 
## re.findall(), and then convert the extracted strings to integers and 
## return the sum of the integers. 

## 2)   Write a function countWord(filename,word) to return a count of the 
## number of times a specified word appears in a file.  It should match the 
## word when it starts a sentence also (starts with a capital letter). It 
## should not match any additional letters after the word.  For example, if 
## called on “computer” it should match “Computer” and “computer” but not 
## “computers”.  For file regex_sum_42.txt it will return 21 when called 
## with the word “computer”.   

## 3)   Write a function listURLs(fileName) to return a list of the URLs 
## in the file when given the file name.  It should match URLs like 
## www.cnn.com.  It doesn’t have to return the http:// part or the https:// 
## part of the URL, but it can.  For file regex_sum_42.txt it will return a 
## list of three URLs. 


def sumNums(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    totalTextSum = 0

    while line:
        L = re.findall('[0-9]+', line)
        for number in L:
            totalTextSum += int(number)
        line = inFile.readline()

    inFile.close()
    return totalTextSum



def countWord(fileName, word):
    inFile = open(fileName, 'r')
    line = inFile.readline()









def listURLs(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()

    listURL = []
    while line:
        L = re.findall('\\b(www.[a-z0-9].\S+)\\b', line)
        listURL.extend(L)
        line = inFile.readline()

    inFile.close()
    newList = [c for c in listURL if c]
    return newList


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
