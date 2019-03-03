import unittest
import account as AccountClass


class Test(unittest.TestCase):
    accInfo = AccountClass.account()

    def test_check_password_length(self):
        print("Checking possible passwords\n")
        passwordList = ['abeautifulday', 'astrictboss', 'alovelyhopuse']

        for passwd in passwordList:
            print("Checking password " + passwd)
            passInfo = self.accInfo.check_password_length(passwd)
            self.assertTrue(passInfo)


if __name__ == '__main__':
    unittest.main()
