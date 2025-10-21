from sqlmodel import SQLModel, Field, Relationship,  Session,  select
from datetime import datetime, timezone, timedelta
from typing import List, Optional
import uuid


class Challenge(SQLModel, table=True):
   __tablename__ = 'challenges'
   challenge_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
   problem: str
   solution: str
   challenge_hint: str
   difficulty_level: str
   challenge_source: str = Field(default='Hackerboard')
   date_added: datetime = Field(default_factory=datetime.utcnow)
   attempts: List["Alchemy"] = Relationship(back_populates="challenge")


   def add_challenge(self):
       pass

   def update_challenge(self):
       #can only update challenges added by yourself
       pass

   def remove_challenge(self):
       #can only remove challenges that you've created
       pass

   def challenges(self, session: Session):
        '''This returns a limited number(10) of
        challenges to display'''
        try:
           challenges = session.exec(select(Challenge).limit(10))
           result = [challenge for challenge in challenges]
           return result
        except Exception as e:
           raise ValueError('Unable to access challenges') from e

   def next_challenge_set(self, session: Session, challenges: List['challenges']):
       '''Exclude UUID's of previous results and return another
       10 challenges'''
       challenge_uuids = [challenge.challenge_id for challenge in challenges]
       challenges = session.exec(select(Challenge).where(~Challenge.challenge_id.in_(challenge_uuids)).limit(10))
       return [challenge.challenge_id for challenge in challenges]


   def get_challenge(self):
       pass

   def toggle_challenge(self):
       '''Star or unstar challenge'''
       pass

   def challenge_solution(self):
       pass

   def filter_challenges(self):
       '''Filter by date added and difficulty level'''
       pass

class Hacker(SQLModel, table=True):
   __tablename__ = 'hackers'
   hacker_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
   fullname: str = Field(default='Anon')
   handle: str = Field(unique=True)
   email: str = Field(unique=True)
   password: str
   image: str
   ranking: int | None = None
   score: int = Field(default=0)
   date_created: datetime = Field(default_factory=datetime.now(timezone.utc))
   last_active: datetime = Field(default_factory=datetime.now(timezone.utc))
   country: str = Field(default='United States')
   bio: str
   team: Optional["Team"] = Relationship(back_populates="hackers_team")
   attempts: List["Alchemy"] = Relationship(back_populates="hacker")
   team_events: List["Event"] = Relationship(back_populates="team_admin")

   def get_hacker(self):
       pass

   def update_hacker(self):
       '''This will update the hackers profile'''
       pass

   def add_hacker(self):
       pass

   def remove_hacker(self):
       pass

   def top_ranked(self):
       pass


class Alchemy(SQLModel, table=True):
   __tablename__ = 'alchemy'
   alchemy_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
   answer: str
   correct: bool | None = None
   date_submitted: datetime = Field(default_factory=datetime.now(timezone.utc))
   challenge_id: uuid.UUID = Field(foreign_key="challenges.challenge_id", nullable=False)
   hacker_id: uuid.UUID = Field(foreign_key="hackers.hacker_id", nullable=False)
   challenge: Challenge = Relationship(back_populates="attempts")
   hacker: Hacker = Relationship(back_populates="attempts")

   def submit_answer(self):
       pass

   def mark_as_completed(self):
       '''This will mark the challenge as completed by a hacker'''
       pass

   def challenge_results(self):
       '''Return the number of all challenges solved and attempted by a hacker'''
       pass

   @classmethod
   def solution_calculator(cls):
       '''Calculate and return all the challenges solved and attempted by a hacker'''
       pass


# class Message(SQLModel, table=True):
#    __tablename__ = 'messages'
#    message_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
#    message: str
#    message_date: datetime = Field(default_factory=datetime.now(timezone.utc))
#    message_status: str = Field(default='unread')
#    archived: bool = Field(default=False)
#    sender_id: uuid.UUID = Field(foreign_key='hacker.hacker_id')
#    recipient_id: Optional[uuid.UUID] = Field(foreign_key='hacker.hacker_id')
#    sender: Hacker = Relationship(back_populates='sent_messages')
#    recipient: Optional[Hacker] = Relationship(back_populates='recieved_messages')

#    def get_all_messages(self):
#        pass

#    def get_message(self):
#        pass

#    def send_message(self):
#        pass

#    def archive_message(self):
#        '''If you delete messages, they will be archived'''
#        pass

#    def archive_messages(self):
#        pass


class Event(SQLModel, table=True):
   __tablename__ = 'events'
   event_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
   name: str = Field(index=True)
   description: str
   event_date: datetime = Field(default_factory=datetime.now(timezone.utc))
   winning_team: str | None = None
   duration: int
   invite_only: str = Field(default='No')
   admin_id: uuid.UUID = Field(foreign_key="hackers.hacker_id", nullable=False)
   team_admin: Hacker = Relationship(back_populates="team_events")


   def send_reminder(self):
       '''Send users registered for events a reminder'''
       pass

   def duration_to_time(self):
       '''Convert duration int to hours and minutes'''
       pass

   def tally_scores(self):
       '''Tally up the scores at the end of an event to determine the winning team'''
       pass

   def join_event(self):
       '''Add a team to the event'''
       pass

   def cancel_event(self):
       '''Whomever created the event can cancel it (or if no team joins in it will be canceled)'''
       pass

   def send_invite(self):
       '''Send another team an invite to join event'''
       pass

   def add_event(self):
       '''Add an event'''
       pass

   def update_event(self):
       '''Update event'''
       pass

   def get_event(self):
       '''Retrieve event by its UUID'''
       pass

   def get_all_events(self):
       '''Get all public events'''
       pass

class Team(SQLModel, table=True):
   __tablename__ = 'teams'
   team_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
   name: str = Field(unique=True, index=True)
   date_created: datetime = Field(default_factory=datetime.now(timezone.utc))
   ranking: int | None = None
   status: str = Field(default='active')
   score: int = Field(default=0)
   hacker_id: uuid.UUID = Field(foreign_key="hackers.hacker_id", nullable=False)
   hackers_team: Hacker = Relationship(back_populates="team")


   def add_team(self):
       pass

   def update_team(self):
       pass

   def get_all_teams(self):
       pass

   def get_team(self):
       pass

   def top_ranked(self):
       '''Get top ranked teams'''
       pass
