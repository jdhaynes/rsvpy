class Event(object):
    def __init__(self, id, event_name, allow_tentative, owner_id, 
                    close_date, event_date, created_date):

        self.id = id
        self.event_name = event_name
        self.allow_tentative = allow_tentative
        self.owner_id = owner_id
        self.close_date = close_date
        self.event_date = event_date
        self.created_date = created_date