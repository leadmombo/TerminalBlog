from database import Database
from menu import Menu
from models.blog import Blog
from models.post import Post

__author__ = "Centusk"

Database.initialize()

menu = Menu()

menu.run_menu()
