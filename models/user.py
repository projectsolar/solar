from sqlalchemy import Column, String
from models import DecBase


class User(DecBase):
    """ A mod (moderator) is a user or collection of users that filter content in the community
        Users will be able to subscribe to groups of mods or individual mods to filter their 
        content as they see fit.
        Attributes:
            seed: 
            url: address of users personal page
    """
    __tablename__ = 'user'
    seed = Column(String)
    url = Column(String, primary_key=True, nullable=False)
