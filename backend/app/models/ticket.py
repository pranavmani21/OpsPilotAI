from sqlalchemy import Column, Integer, String, Text

from app.db.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    department = Column(String)
    priority = Column(String)
