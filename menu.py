__author__='Centusk'

from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input('Enter your author name')
        self.user_blog = None
        if self._user_has_account():
            print('Welcome back {}'.format(self.user))
        else:
            self._promt_user_for_account()
        pass

    def _user_has_account(self):
        blog = Database.findOne('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            return False

    def _promt_user_for_account(self):
        title = input('Enter blog title : ')
        description = input('Enter Blog description : ')
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def _list_blogs(self):
        blogs = Database.find(collection="blogs", query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        id_blog = input("Enter ID of the blog you'd like to read: ")
        blog = Blog.get_from_mongo(id_blog)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, Title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))

    def run_menu(self):
        read_or_write = input('Do you want tu read (R) or write (W) blogs ?')
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blogs()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            pass


