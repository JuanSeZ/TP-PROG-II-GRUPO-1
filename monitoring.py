class Zone:
    def __init__(self, lower_left_vertex, lower_right_vertex, upper_left_vertex, upper_right_vertex):
        self.lower_left_vertex = lower_left_vertex
        self.lower_right_vertex = lower_right_vertex
        self.upper_left_vertex = upper_left_vertex
        self.upper_right_vertex = upper_right_vertex

    def is_in_zone(self):
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