from sqlalchemy import Column, String
from models import DecBase


class Prism(DecBase):
    """ A prism is a node in the network.
        Attributes:
            url: url to nodes server
            beams: list of beams this prism is hosting
    """
    __tablename__ = 'prism'
    url = Column(String, primary_key=True, nullable=False)
    beams = Column(String)