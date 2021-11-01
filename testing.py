from User import user, citizen,admin,sensor
import unittest


class test_user(unittest.TestCase):

    def test_send_friend_request(self):
        citizen_1 = citizen(1, 123)
        citizen_2 = citizen(2, 456)

        citizen_1.send_friend_request(citizen_2)
        self.assertEqual(citizen_2.get_friend_requests()[0], citizen_1)

    def test_accept_friend_request(self):
        citizen_1 = citizen(1, 123)
        citizen_2 = citizen(2, 456)
        citizen_3 = citizen(3, 789)

        citizen_1.send_friend_request(citizen_2)
        citizen_3.send_friend_request(citizen_2)

        citizen_2.accept_friend_request(citizen_3)
        self.assertEqual(citizen_2.get_friend_list()[0], citizen_3)

    def test_reject_friend_request(self):
        citizen_1 = citizen(1, 123)
        citizen_2 = citizen(2, 456)
        citizen_3 = citizen(3, 789)

        citizen_1.send_friend_request(citizen_2)
        citizen_3.send_friend_request(citizen_2)

        citizen_2.accept_friend_request(citizen_3)
        citizen_2.reject_friend_request(citizen_1)
        self.assertEqual(len(citizen_2.get_friend_requests()), 0)
        self.assertEqual(citizen_1.get_strikes(), 1)

    def test_report_citizen(self):
        citizen_1 = citizen(1, 123)
        citizen_2 = citizen(2, 456)
        citizen_1.report_citizen(citizen_2)
        self.assertEqual(citizen_2.get_strikes(), 1)
        citizen_1.report_citizen(citizen_2)
        self.assertEqual(citizen_2.get_strikes(), 2)


if __name__ == '__main__':
    unittest.main()
