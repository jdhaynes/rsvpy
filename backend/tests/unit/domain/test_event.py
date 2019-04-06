from random import randint
from datetime import datetime
from backend.domain.event import Event

def test_event_model_init():
    rand_id = randint(1, 10000)
    rand_owner_id = randint(1, 10000)
    close_date_dt = datetime.strptime('21/03/19 13:55', '%d/%m/%y %H:%M')
    event_date_dt = datetime.strptime('22/03/19 14:55', '%d/%m/%y %H:%M')
    created_date_dt = datetime.strptime('23/03/19 15:55', '%d/%m/%y %H:%M')

    event = Event(rand_id, event_name = 'Test Event', 
                    allow_tentative=True, owner_id=rand_owner_id, 
                    close_date=close_date_dt, event_date=event_date_dt, 
                    created_date=created_date_dt)

    assert event.id == rand_id
    assert event.event_name == 'Test Event'
    assert event.allow_tentative == True
    assert event.owner_id == rand_owner_id
    assert event.close_date == close_date_dt
    assert event.event_date == event_date_dt
    assert event.created_date == created_date_dt