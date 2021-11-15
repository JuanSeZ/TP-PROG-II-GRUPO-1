from Citizen_record import Citizen_record
from User import Citizen, Admin
from utilities import user_searcher, user_validation
from ABM import ABM
import math
from Event import Event


class Zone:
    def __init__(self, origin_of_zone, width):
        self.origin_of_zone = origin_of_zone
        self.width = width


    def is_in_zone(self, event_or_citizen):
        # Verifica si el evento o un ciudadano esta en la zona descripta.
        return self.origin_of_zone[0] < event_or_citizen.coordinates[0] < self.origin_of_zone[0] + self.width and self.origin_of_zone[1] < event_or_citizen.coordinates[1] < self.origin_of_zone[1] + self.width


class RankingInZone:
    def __init__(self, zone):
        self.zone = zone

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

