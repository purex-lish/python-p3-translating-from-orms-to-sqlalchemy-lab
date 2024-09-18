from sqlalchemy import create_engine
from models import Dog, Base
from sqlalchemy.orm import sessionmaker

def create_table(base, engine ):
    """Create the database tables."""
    #engine = create_engine(database_url)
    base.metadata.create_all(engine)

def save(session, dog):
    """Save a Dog instance to the database."""
    session.add(dog)
    session.commit()

def get_all(session):
    """Return all Dog instances from the database."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Find a Dog by its name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Find a Dog by its ID."""
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    """Find a Dog by its name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Update a Dog's breed."""
    dog.breed = breed
    session.commit()


