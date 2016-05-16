
from sqlalchemy import Column, Integer, String, Text
from models import DecBase
from sqlalchemy.orm import relationship
]
class Content(DecBase):
    """ A content object represents all relevent information for a submission.
        Attributes:
            poster_address: address of poster where points will be sent to
            payload: actual content in text form (can be url to image, video, article etc)
            content_type: Content type: 'post' or 'comment'
            btc_like: address keeping track of points given directly to the poster ('up-votes')
            btc_host: {"prism_url", "like", "dislike"}
            			prism_url: url of prism hosting content 
            			like: address keeping track of percentage 
            				  of point given to prism from number of 'upvotes'
            			dislike: address keeping track of points given directly to prism
            					from number of'down-votes'
            sig: 
    """
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    poster_address = Column(String)
    payload = Column(Text)
    content_type = Column(String)
    btc_like = Column(String)
    btc_host = Column(String)
    sig = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':'content',
        'polymorphic_on':type
    }
