class Zone:
    def __init__(self, center_of_zone, width):
        self.center_of_zone = center_of_zone
        self.width = width


    def is_in_zone(self, event_or_citizen):
        # Verifica si el evento o un ciudadano esta en la zona descripta.


        pass






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


class ZoneRecord:
    def __init__(self):
        self.zones = []