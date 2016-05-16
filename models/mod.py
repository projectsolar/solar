from sqlalchemy import Column, String, Integer
from models import DecBase


class Moderator(DecBase):
    """ A moderator (mod) is a user or collection of users that filter content in the community
        Users will be able to subscribe to groups of mods or individual mods to filter their 
        content as they see fit.
        Attributes:
            mod_type: 'list': a collection of mods which the user can subscribe to
                      'user':    
            url: address of user page of the mod or group of mod
    """
    __tablename__ = 'moderator'
    mod_type = Column(String)
    url = Column(String, primary_key=True, nullable=False)
