'''
Created on Sep 18, 2018

@author: Kristen Tan
I pledge my Honor that I have abided by the Stevens Honor System. Kristen Tan
'''

import unittest
# import unittest.mock
# from unittest.mock import patch
from unittest import mock
from unittest.mock import Mock
from Hw04a import getGitHubInfo

class DummyObject(object):
    def __init__(self, content):
        self.content = content

class TestHw04a(unittest.TestCase):
        
    @mock.patch('requests.get')
    def testValidInput1(self, mockedReqs):
        mockedResponses = [0, 0, 0, 0, 0, 0]
        # Each nested dictionary below is like an individual repo
        mockedResponses[0] = DummyObject(b'[{"id" : "32808844", "name" : "GuessingGame"}, {"id" : "32816276", "name" : "GuessingGame2"}, {"id" : "31634961", "name" : "hello-world"}, {"id" : "31636381", "name" : "HelloJava"}, {"id" : "134432844", "name" : "ud851-Exercises"}]')
        mockedResponses[1] = DummyObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}]')
        mockedResponses[2] = DummyObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}]')
        mockedResponses[3] = DummyObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}]')
        mockedResponses[4] = DummyObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}]')
        mockedResponses[5] = DummyObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}]')
        
        mockedReqs.side_effect = mockedResponses
        self.assertEqual(getGitHubInfo("bsb226"), [['GuessingGame', 3], ['GuessingGame2', 2], ['hello-world', 3], ['HelloJava', 4], ['ud851-Exercises', 30]],
                         'bsb226 has the following repos and commits: GuessingGame - 3, GuessingGame2 - 2, hello-world - 3, HelloJava - 4, ud851-Exercises - 30.')
    
    @mock.patch('requests.get')
    def testValidInput2(self, mockedReqs):
        mockedResponses = [0, 0, 0, 0, 0]
        mockedResponses[0] = DummyObject(b'[{"id" : "28765791", "name" : "hellogitworld"}, {"id" : "144656027", "name" : "helloworld"}, {"id" : "28765763", "name" : "Project1"}, {"id" : "7468415", "name" : "threads-of-life"}]')
        mockedResponses[1] = DummyObject(b'[{"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}, {"author" : "richkempinski"}]')
        mockedResponses[2] = DummyObject(b'[{"author" : "richkempinski"}, {"author" : "richkempinski"}]')
        mockedResponses[3] = DummyObject(b'[{"author" : "richkempinski"}, {"author" : "richkempinski"}]')
        mockedResponses[4] = DummyObject(b'[{"author" : "richkempinski"}]')
        
        mockedReqs.side_effect = mockedResponses
        self.assertEqual(getGitHubInfo('richkempinski'), [['hellogitworld', 30], ['helloworld', 2], ['Project1', 2], ['threads-of-life', 1]], 
                         'richkempinski has the folllowing repos and commits: hellogitworld - 30, helloworld - 2, Project1 - 2, threads-of-life - 1.')
         
    @mock.patch('requests.get')
    def testValidInput3(self, mockedReqs):
        mockedResponses = [0, 0, 0]
        mockedResponses[0] = DummyObject(b'[{"id" : "134514223", "name" : "LaundryDetector"}, {"id" : "128850081", "name" : "uunite"}]')
        mockedResponses[1] = DummyObject(b'[{"author" : "Simoa33"}, {"author" : "Simoa33"}]')
        mockedResponses[2] = DummyObject(b'[{"author" : "Simoa33"}, {"author" : "Simoa33"}, {"author" : "Simoa33"}, {"author" : "Simoa33"}, {"author" : "Simoa33"}, {"author" : "Simoa33"}, {"author" : "Simoa33"}, {"author" : "Simoa33"}]')
        
        mockedReqs.side_effect = mockedResponses
        self.assertEqual(getGitHubInfo('Simoa33'), [['LaundryDetector', 2], ['uunite', 8]], 
                         'Simoa33 has the folllowing repos and commits: LaundryDetector - 2, uunite - 8.')

#     @mock.patch('requests.get')
#     def testInvalidInput1(self, mockedReq):
#         # The mock never actually gets called, as the exception handling returns before the API call
#         mockedReq.return_value = 'gitHubUserId must be a string'
#         self.assertEqual(getGitHubInfo(77), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
#         
#     @mock.patch('requests.get')
#     def testInvalidInput2(self, mockedReq):
#         # The mock never actually gets called, as the exception handling returns before the API call
#         mockedReq.return_value = 'gitHubUserId must be a string'
#         self.assertEqual(getGitHubInfo(False), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
#            
#     @mock.patch('requests.get')
#     def testInvalidInput3(self, mockedReq):
#         # The mock never actually gets called, as the exception handling returns before the API call
#         mockedReq.return_value = 'gitHubUserId must be a string'
#         self.assertEqual(getGitHubInfo(9.5), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
#            
#     @mock.patch('requests.get')
#     def testInvalidInput4(self, mockedReq):
#         # The mock never actually gets called, as the exception handling returns before the API call
#         mockedReq.return_value = 'gitHubUserId must be a string'
#         self.assertEqual(getGitHubInfo([1, 2, 3, 4, 5]), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
#            
#     @mock.patch('requests.get')
#     def testInvalidInput5(self, mockedReq):
#         # The mock never actually gets called, as the exception handling returns before the API call
#         mockedReq.return_value = 'gitHubUserId must be a string'
#         self.assertEqual(getGitHubInfo((1, 2, 3, 4, 5)), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
#    
#     @mock.patch('requests.get')
#     def testInvalidInput6(self, mockedReq):
#         # The mock never actually gets called, as the exception handling returns before the API call
#         mockedReq.return_value = 'gitHubUserId must be a string'
#         self.assertEqual(getGitHubInfo({'kristen':'junior', 'kevin':'freshman'}), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
         
         
         
         
# The below tests don't actually need mocking, but I wrote them using mocking above
         
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