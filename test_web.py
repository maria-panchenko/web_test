import unittest
from app import login1, password1

class TestStringMethods(unittest.TestCase):

  def logins(self):
      self.assertEqual(login1("Masha"), 'Masha')
      self.assertEqual(login1("Macha"), 'error')

  def password(self):
      self.assertEqual(password1("132"), 'error')
      self.assertEqual(password1("123"), '123')

if __name__ == '__main__':
    unittest.main()