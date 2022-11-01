import unittest
from api.user_manager import UserManager

class TestUserManger(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        cls.user.login()

    def test_add_user(self):
        self.username = 'testk01'
        self.password = '123456'
        actual_result = self.user.add_user(self.username,self.password)
        self.assertEqual(502,actual_result['errno'])


    def test_edit_username(self):
        pass

    def test_search_username(self):
        pass

    def test_delete_user(self):
        pass

if __name__ == '__main__':
    unittest.main()