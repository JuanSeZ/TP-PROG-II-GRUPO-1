from Event import Event
from Event_type import Event_type
class Zone:
    def __init__(self, center_of_zone, width):
        self.center_of_zone = center_of_zone
        self.width = width


    def is_in_zone(self, event_or_citizen):
        # Verifica si el evento o un ciudadano esta en la zona descripta.


        pass

    def get_center_of_point(self):
        return self.center_of_zone

    def get_width(self):
        return self.width

class RankingInZone:
    def __init__(self, zone):
        self.zone = zone
        self.ranking = []

    def update_ranking(self, event):
        # Ordena el ranking en base a la concurrencia

        pass

    def record_ranking(self):
        # No nos acordamos que poronga hace esto
        pass

    def get_ranking(self):
        return self.ranking

class ZoneRecord:
    def __init__(self):
        self.zones = []


Pilar = Zone((0, 0), 5)
Tigre = Zone((0, 5), 5)
San_Isidro = Zone((5, 0), 5)
Escobar = Zone((5, 5), 5)
Concerts = Event_type("Concert")
Concierto = Event(Concerts,  (0, 3))
Ranking_In_Zone = RankingInZone(Pilar)
Ranking_In_Zone.ranking = [[10, Concierto]]

