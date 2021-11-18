from User import Citizen, Admin, Sensor
import unittest
from Event_type import Event_type
from monitoring import Zone, RankingInZone, Pilar
from Event import Event
from Event_type_record import event_type_record, EventTypeRecord
from Citizen_record import Citizen_record
from Admin_record import Admin_record
from utilities import user_validation

class test_user(unittest.TestCase):

    def test_send_friend_request(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)

        citizen_1.send_friend_request(citizen_2)
        self.assertEqual(citizen_2.get_friend_requests()[0], citizen_1)

    def test_accept_friend_request(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)
        citizen_3 = Citizen(3, 789, 1)

        citizen_1.send_friend_request(citizen_2)
        citizen_3.send_friend_request(citizen_2)

        citizen_2.accept_friend_request(citizen_3)
        self.assertEqual(citizen_2.get_friend_list()[0], citizen_3)

    def test_reject_friend_request(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)
        citizen_3 = Citizen(3, 789, 1)

        citizen_1.send_friend_request(citizen_2)
        citizen_3.send_friend_request(citizen_2)

        citizen_2.accept_friend_request(citizen_3)
        citizen_2.reject_friend_request(citizen_1)
        self.assertEqual(len(citizen_2.get_friend_requests()), 0)
        self.assertEqual(citizen_1.get_strikes(), 1)

    def test_report_citizen(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)
        citizen_1.report_citizen(citizen_2)
        self.assertEqual(citizen_2.get_strikes(), 1)
        citizen_1.report_citizen(citizen_2)
        self.assertEqual(citizen_2.get_strikes(), 2)

    def test_promote_citizen(self):
        citizen_1 = Citizen(1, 123, 1)
        Citizen_record.register_citizen(citizen_1)
        self.assertEqual(len(Citizen_record.get_citizen_list()), 1)
        admin_1 = Admin(0, 321, 1)
        Admin_record.add_default_admin(admin_1)
        admin_1.promote_citizen(citizen_1)
        self.assertEqual(len(Admin_record.get_admin_list()), 2)
        Citizen_record.citizen_list = []
        Admin_record.admin_list = []

    def test_demote_admin(self):
        citizen_1 = Citizen(1, 123, 1)
        Citizen_record.register_citizen(citizen_1)
        admin_1 = Admin(0, 321, 1)
        Admin_record.add_default_admin(admin_1)
        admin_1.promote_citizen(citizen_1)
        admin_2 = Admin(2, 234, 6)
        Admin_record.add_default_admin(admin_2)
        self.assertEqual(len(Admin_record.get_admin_list()), 3)
        admin_1.demote_citizen(admin_2)
        self.assertEqual(len(Admin_record.get_admin_list()), 2)
        self.assertEqual(len(Citizen_record.get_citizen_list()), 1)
        Citizen_record.citizen_list = []
        Admin_record.admin_list = []


    def test_sensors(self):
        Conciertos = Event_type("Concert")
        event_type_record.add_event_type(Conciertos)
        sensor_1 = Sensor(Conciertos, (1, 2))
        sensor_1.report_event()
        self.assertEqual(len(Conciertos.get_event_list()), 1)


class test_event(unittest.TestCase):

    def test_report_event(self):
        citizen_1 = Citizen(1, 123, 1)
        Conciertos = Event_type("Concert")
        event_type_record.add_event_type(Conciertos)
        citizen_1.report_event(Conciertos, (1, 2))
        self.assertEqual(len(Conciertos.get_event_list()), 1)
        event_type_record.event_types = []

    def test_report_event_two_concurrences(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)
        Conciertos = Event_type("Concert")
        event_type_record.event_types.append(Conciertos)
        citizen_1.report_event(Conciertos, (1,2))
        citizen_2.report_event(Conciertos, (1,2))
        self.assertEqual(Conciertos.get_event_list()[0].get_concurrence(), 2)

    def test_is_in_zone(self):
        Conciertos = Event_type("Concert")

        event = Event(Conciertos, (6, 2))
        event1 = Event(Conciertos, (2, 3))

        new_zone = Zone((0, 0), 5, 'Pilar')
        self.assertEqual(new_zone.is_in_zone(event), False)
        self.assertEqual(new_zone.is_in_zone(event1), True)


    def test_get_ranking(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)

        Concert = Event_type("Concert")
        Robo = Event_type("Robo")
        rankingInPilar = RankingInZone(Pilar)


        event_type_record.add_event_type(Concert)
        event_type_record.add_event_type(Robo)

        citizen_1.report_event(Concert, (1, 1))
        citizen_2.report_event(Robo, (1, 2))
        citizen_2.report_event(Concert, (1, 1))

        self.assertEqual(len(rankingInPilar.get_ranking()), 2)



class test_user(unittest.TestCase):

    def test_validate_data_set(self):
        x = user_validation.validate_registration(9432, 145)
        self.assertEqual(x, True)



if __name__ == '__main__':
    unittest.main()
