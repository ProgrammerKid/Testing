import flet as ft
from sample_data import data
import Post

def main(page: ft.Page):
    page.scroll = 'always' # allow scrolling
    page.add(Post.card(data)) # add the Card control and pass the diary data
    page.add(Post.card(data)) # add the Card control and pass the diary data
ft.app(main)