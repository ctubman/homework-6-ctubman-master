import re
import unittest

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
    numOfWordAppearances = 0

    for c in inFile:
        collectedWords = re.findall(r'\b'+ word + r'\b', c.lower())
        numOfWordAppearances += len(collectedWords)
    inFile.close()
    return numOfWordAppearances



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

##### TEST CASES DON'T EDIT #####

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
