from sqlalchemy import Column, String
from models import DecBase


class Prism(DecBase):
    """ A prism is a node in the network.
        Attributes:
		URL: Base URL of prism.
        beams: string of beams hosted on the prism, separated by commas.
    """
    __tablename__ = 'prism'
    url = Column(String, primary_key=True, nullable=False)
    beams = Column(String)