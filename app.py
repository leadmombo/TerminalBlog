from database import Database
from models.post import Post

__author__ = "Centusk"

Database.initialize()


post = Post(blog_id='123',
            title='Herve vs Jenifa',
            content="Herve a dit a jenifa de montrer ses seins",
            author='Baizman')
post.save_to_mongo()
