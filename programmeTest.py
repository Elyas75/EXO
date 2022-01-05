from unittest import main

import programme
import programme as mp
import unittest

class TestMonProgramme(unittest.TestCase):

    def testCheckPwd(self):
        self.assertTrue(programme.checkPwd('HelloPari$75'))

        #test le nombre de caractère du mdp qui doit être => 10 et =<25
        self.assertTrue(programme.checkPwd('Hell12'))


        #vérifier si le mdp contient des caractères spéciaux
        self.assertTrue(main.checkPwd("Helloo123"));

        # vérifier si le mdp contient des Majuscules
        self.assertTrue(main.checkPwd("helloo123"));

        # vérifier si le mdp contient des minuscules
        self.assertTrue(main.checkPwd("HELLO123"));

if __name__ == "__main__":
    unittest.main()