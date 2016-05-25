from sqlalchemy import Column, String
from models import DecBase


class User(DecBase):
    """ A user is a person who interacts with the solar network by browsing, posting, or commenting in beams.
        Attributes:
            seed: BIP32 XPrivKey used to generate Bitcoin wallets
            url: address of users personal page
    """
    __tablename__ = 'user'
    seed = Column(String)
    url = Column(String, primary_key=True, nullable=False)
