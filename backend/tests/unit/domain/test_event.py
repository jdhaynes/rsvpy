from random import randint
from datetime import datetime
from backend.domain.event import Event

def test_event_model_init():
    rand_id = randint(1, 10000)
    rand_owner_id = randint(1, 10000)
    close_date_dt = datetime.strptime('21/03/19 13:55', '%d/%m/%y %H:%M')
    event_date_dt = datetime.strptime('22/03/19 14:55', '%d/%m/%y %H:%M')
    created_date_dt = datetime.strptime('23/03/19 15:55', '%d/%m/%y %H:%M')

    event = Event(rand_id, event_nameevent_date_dt = datetime.strptime('22/03/19 14:55', '%d/%m/%y %H:%M')='Test Event', close_date=close_date_dt,
                    allow_tentative=True, rand_owner_id=rand_owner_id, 
                    event_date=close_date_dt, created_date=created_date_dt)

    assert event.rand_id == rand_id
    assert event.event_name == 'Test Event'
    assert event.close_date == close_date_dt
    assert event.allow_tentative == True
    assert event.rand_owner_id == rand_owner_id
    assert event.close_date == close_date_dt
    assert event.created_date == created_date_dt