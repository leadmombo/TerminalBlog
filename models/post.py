import datetime
import uuid
from database import Database

__author__ = "centusk"


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

        #
    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @staticmethod
    def form_mongo(id):
        return Database.findOne(collection="posts", query= {'id': id})

    @staticmethod
    def form_blog(id):
        return [ post for post in Database.find(collection='post', query= {'blog_id': id})]
