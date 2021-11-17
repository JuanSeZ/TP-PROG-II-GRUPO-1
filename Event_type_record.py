class EventTypeRecord:
    def __init__(self):
        self.event_types = []# ["Robo", "Concierto"]

    def get_event_types(self):
        return self.event_types

    def add_event_type(self, event_type):
        self.event_types.append(event_type)

event_type_record = EventTypeRecord()
