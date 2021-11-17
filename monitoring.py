import csv

from Event_type_record import event_type_record
from Event import Event
# from Event_type import Event_type

class Zone:
    def __init__(self, origin_of_zone, width, description):
        self.origin_of_zone = origin_of_zone
        self.width = width
        self.description = description

    def is_in_zone(self, event_or_citizen):
        # Verifica si el evento o un ciudadano esta en la zona descripta.
        return self.origin_of_zone[0] < event_or_citizen.coordinates[0] < self.origin_of_zone[0] + self.width and self.origin_of_zone[1] < event_or_citizen.coordinates[1] < self.origin_of_zone[1] + self.width

    def get_center_of_point(self):
        return self.origin_of_zone

    def get_width(self):
        return self.width

    def get_descprition(self):
        return self.description



class RankingInZone:
    def __init__(self, zone):
        self.zone = zone

    def get_ranking(self):
        # Ordena el ranking en base a la concurrencia
        ranking_in_zone = []
        for event_type in event_type_record.get_event_types():
            for event in event_type.get_event_list():
                if self.zone.is_in_zone(event):
                    ranking_in_zone.append(event)
        ranking_in_zone.sort(key=lambda event:event.concurrence, reverse=True)
        return ranking_in_zone

class GeneralRanking:
    def get_ranking(self):
        ranking = []
        for event_type in event_type_record.get_event_types():
            for event in event_type.get_event_list():
                ranking.append(event)
        ranking.sort(key=lambda event:event.concurrence, reverse=True)
        return ranking



    def add_user_to_csv(self):
        with open("Users.csv", "a") as r:
            writer = csv.writer(r)
            for citizen in self.citizen_list:
                writer.writerow([citizen.cuil, citizen.cellphone, citizen.password])

    def import_ranking(self):
        with open("Eventos.csv") as f:
            reader = csv.reader(f)
            next(reader)
        for row in reader:
            evento = Event(row[0], row[1])
            evento.concurrence = row[2]
            for event_type in event_type_record:
                if event_type == evento.get_type():
                    event_type.get_event_list().append(evento)





class ZoneRecord:
    def __init__(self):
        self.zones = []

Pilar = Zone((0,0), 10, "Pilar")
Tigre = Zone((0, 10), 10, "Tigre")
San_Isidro = Zone((10, 0), 10, "San Isidro")
Escobar = Zone((10, 10), 10, "Escobar")

rankingInPilar = RankingInZone(Pilar)
rankingInTigre = RankingInZone(Tigre)
rankingInSanIsidro = RankingInZone(San_Isidro)
rankingInEscobar = RankingInZone(Escobar)

ranking_list = [rankingInPilar, rankingInEscobar, rankingInSanIsidro, rankingInTigre]

general_ranking = GeneralRanking()
