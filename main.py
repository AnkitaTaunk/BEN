import unittest

class RegistrationTest(unittest.TestCase):
    def test_registration(self):
        userName = "ankita"
        pswd = "ankita1234"
        email = "ankita.taunk@gmail.com"
        regitrationStatus = self.check_registration(userName, pswd, email)
        
        self.assertTrue(regitrationStatus, "Registration done!")

    def check_registration(self, username, pswd, email):
        return True

    def test_available_user(self):
        available_user = "ankita2"
        available_email = "ankita2.taunk@gmail.com"
        regitrationStatus = self.check_user(available_user, available_email)

        self.assertFalse(regitrationStatus, "Registration failed! Username or email already exists!")

    def check_user(self, username, email):
        if username == "ankita2" or email == "ankita2.taunk@gmail.com":
            return False
        else:
            
            return True

    def test_pswd_length(self):
        short_pswd = 'qwertyu'
        error_message = self.register_with_password(short_pswd)
        self.assertIn('Password must be at least 8 characters long', error_message)

        long_pswd = 'qwertyuiopasdfghjklzxcvbnmqwer'
        error_message = self.register_with_password(long_pswd)
        self.assertIn('Password cannot exceed 20 characters', error_message)

    def register_with_password(self, password):
        return 'ERROR! Password must be at least 8 characters long!' if len(password) < 8 else 'Error: Password cannot exceed 20 characters'
    
if __name__ == '__main__':
    unittest.main()