from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase
from sqlalchemy.orm import relationship


class Post(DecBase):
    """ A post is a type of content that can be submitted. 
        Attributes:
            beam: Name of beam (community)
    """
    __tablename__ = 'post'
    id = Column(Integer, ForeignKey('content.id'), primary_key=True)
    comments = relationship("Comments", backref="post")
    beam = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':'post',
    }
