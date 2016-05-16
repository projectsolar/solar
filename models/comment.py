from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase
from sqlalchemy.orm import relationship



class Comment(DecBase):
    """ A post is a type of content that can be submitted. 
        Attributes:
            post_id: ID of the content which the comment was made about 
    """
    __tablename__ = 'comment'
    id = Column(Integer, ForeignKey('content.id'), primary_key=True)
    post = relationship("Post", back_ref="comment")
    post_id = Column(Integer, ForeignKey('post.id'))

    __mapper_args__ = {
        'polymorphic_identity':'comment',
    }