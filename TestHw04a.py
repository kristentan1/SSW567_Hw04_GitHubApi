'''
Created on Sep 18, 2018

@author: Kristen Tan
I pledge my Honor that I have abided by the Stevens Honor System. Kristen Tan
'''

import unittest
from Hw04a import getGitHubInfo

class TestHw04a(unittest.TestCase):
        
    def testValidInput1(self):
        self.assertEqual(getGitHubInfo('bsb226'), [['GuessingGame', 3], ['GuessingGame2', 2], ['hello-world', 3], ['HelloJava', 4], ['ud851-Exercises', 30]],
                         'bsb226 has the following repos and commits: GuessingGame - 3, GuessingGame2 - 2, hello-world - 3, HelloJava - 4, ud851-Exercises - 30.')
        
    def testValidInput2(self):
        self.assertEqual(getGitHubInfo('richkempinski'), [['hellogitworld', 30], ['helloworld', 2], ['Project1', 2], ['threads-of-life', 1]], 
                         'richkempinski has the folllowing repos and commits: hellogitworld - 30, helloworld - 2, Project1 - 2, threads-of-life - 1.')
        
    def testValidInput3(self):
        self.assertEqual(getGitHubInfo('Simoa33'), [['LaundryDetector', 2], ['uunite', 8]], 
                         'Simoa33 has the folllowing repos and commits: LaundryDetector - 2, uunite - 8.')
        
    def testInvalidInput1(self):
        self.assertEqual(getGitHubInfo(77), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
        
    def testInvalidInput2(self):
        self.assertEqual(getGitHubInfo(False), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
        
    def testInvalidInput3(self):
        self.assertEqual(getGitHubInfo(9.5), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
        
    def testInvalidInput4(self):
        self.assertEqual(getGitHubInfo([1, 2, 3, 4, 5]), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
        
    def testInvalidInput5(self):
        self.assertEqual(getGitHubInfo((1, 2, 3, 4, 5)), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')

    def testInvalidInput6(self):
        self.assertEqual(getGitHubInfo({'kristen':'junior', 'kevin':'freshman'}), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')

        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()