from datetime import datetime

from . import db


ACTIVITIES = {
    'create_user': 'User {user} created',
    'update_user': 'Profile of user {user} updated',
    'update_event': 'Event {event} updated',
    'create_event': 'Event {event} created',
    'delete_event': 'Event {event} deleted',
    'create_role': 'Role {role} created for user {user} in event {event}',
    'update_role': 'Role updated to {role} for user {user} in event {event}',
    'delete_role': 'User {user} removed from role {role} in event {event}',
    'create_session': 'Session {session} was created in event {event}'
}


class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.String)  # user email + id
    time = db.Column(db.DateTime)
    action = db.Column(db.String)

    def __init__(self, actor=None, time=None, action=None):
        self.actor = actor
        self.time = time
        if self.time is None:
            self.time = datetime.now()
        self.action = action

    def __repr__(self):
        return '<Activity by %s>' % (self.actor)
