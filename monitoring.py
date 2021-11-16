from Citizen_record import Citizen_record
from User import Citizen, Admin
from utilities import user_searcher, user_validation
from ABM import ABM
import math
from Event import Event
from Event_type import Event_type

class Zone:
    def __init__(self, origin_of_zone, width):
        self.origin_of_zone = origin_of_zone
        self.width = width


    def is_in_zone(self, event_or_citizen):
        # Verifica si el evento o un ciudadano esta en la zona descripta.
        return self.origin_of_zone[0] < event_or_citizen.coordinates[0] < self.origin_of_zone[0] + self.width and self.origin_of_zone[1] < event_or_citizen.coordinates[1] < self.origin_of_zone[1] + self.width

    def get_center_of_point(self):
        return self.origin_of_zone

    def get_width(self):
        return self.width


class RankingInZone:
    def __init__(self, zone):
        self.zone = zone
        self.ranking = []


    def get_ranking(self):
        # Ordena el ranking en base a la concurrencia
        ranking_in_zone = []
        for event_type in Admin.get_event_type_list():
            for event in event_type.get_event_list():
                if self.zone.is_in_zone(event):
                    ranking_in_zone.append(event)
        ranking_in_zone.sort(reverse=True)
        return ranking_in_zone




    def record_ranking(self):
        # Pasarlo a un archivo el ranking
        pass


class ZoneRecord:
    def __init__(self):
        self.zones = []

Pilar = Zone((0,0), 10)
Tigre = Zone((0, 10), 10)
San_Isidro = Zone((10, 0), 10)
Escobar = Zone((10, 10), 10)
Concerts = Event_type("Concert")
Concierto = Event(Concerts, (2, 2))
Ranking_In_Zone = RankingInZone(Pilar)
Ranking_In_Zone.ranking = [[10, Concierto]]

