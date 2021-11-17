from User import User, Citizen, Admin, Sensor
import unittest
from Event_type import Event_type
from monitoring import Zone, RankingInZone, Pilar
from Event import Event
from Event_type_record import event_type_record, EventTypeRecord
# class test_user(unittest.TestCase):

#     def test_send_friend_request(self):
#         citizen_1 = Citizen(1, 123, 1)
#         citizen_2 = Citizen(2, 456, 1)
#
#         citizen_1.send_friend_request(citizen_2)
#         self.assertEqual(citizen_2.get_friend_requests()[0], citizen_1)
#
#     def test_accept_friend_request(self):
#         citizen_1 = Citizen(1, 123, 1)
#         citizen_2 = Citizen(2, 456, 1)
#         citizen_3 = Citizen(3, 789, 1)
#
#         citizen_1.send_friend_request(citizen_2)
#         citizen_3.send_friend_request(citizen_2)
#
#         citizen_2.accept_friend_request(citizen_3)
#         self.assertEqual(citizen_2.get_friend_list()[0], citizen_3)
#
#     def test_reject_friend_request(self):
#         citizen_1 = Citizen(1, 123, 1)
#         citizen_2 = Citizen(2, 456, 1)
#         citizen_3 = Citizen(3, 789, 1)
#
#         citizen_1.send_friend_request(citizen_2)
#         citizen_3.send_friend_request(citizen_2)
#
#         citizen_2.accept_friend_request(citizen_3)
#         citizen_2.reject_friend_request(citizen_1)
#         self.assertEqual(len(citizen_2.get_friend_requests()), 0)
#         self.assertEqual(citizen_1.get_strikes(), 1)
#
#     def test_report_citizen(self):
#         citizen_1 = Citizen(1, 123, 1)
#         citizen_2 = Citizen(2, 456, 1)
#         citizen_1.report_citizen(citizen_2)
#         self.assertEqual(citizen_2.get_strikes(), 1)
#         citizen_1.report_citizen(citizen_2)
#         self.assertEqual(citizen_2.get_strikes(), 2)
#
class test_event(unittest.TestCase):
#
#     def test_report_event(self):
#         citizen_1 = Citizen(1, 123, 1)
#         admin_1 = Admin(13, 890, 34)
#         Conciertos = Event_type("Concert")
#         admin_1.event_type_list.append(Conciertos)
#         citizen_1.report_event("Concert", "xy")
#         self.assertEqual(len(Conciertos.get_ocurrence_list()), 1)
#
#     def test_report_event_con_dos_ocurrencias(self):
#         citizen_1 = Citizen(1, 123, 1)
#         citizen_2 = Citizen(2, 456, 1)
#         admin_1 = Admin(13, 890, 34)
#         Conciertos = Event_type("Concert")
#         admin_1.event_type_list.append(Conciertos)
#         citizen_1.report_event("Concert", "xy")
#         citizen_2.report_event("Concert", "xy")
#         self.assertEqual(Conciertos.get_ocurrence_list()[0][0], 2)

    def test_is_in_zone(self):
        Conciertos = Event_type("Concert")

        event = Event(Conciertos, (6, 2))
        event1 = Event(Conciertos, (2, 3))

        new_zone = Zone((0,0), 5)
        self.assertEqual(new_zone.is_in_zone(event), False)
        self.assertEqual(new_zone.is_in_zone(event1), True)


    def test_get_ranking(self):
        citizen_1 = Citizen(1, 123, 1)
        citizen_2 = Citizen(2, 456, 1)
        Concert = Event_type("Concert")
        Robo = Event_type("Robo")
        rankingInPilar = RankingInZone(Pilar)
        eventos = EventTypeRecord()
        eventos.add_event_type(Concert)
        eventos.add_event_type(Robo)
        citizen_1.report_event(Concert, (1, 1))
        citizen_2.report_event(Robo, (1, 2))
        citizen_2.report_event(Concert, (1, 1))
        self.assertEqual(len(rankingInPilar.get_ranking()), 2)





if __name__ == '__main__':
    unittest.main()
