import flet as ft
from sample_data import data
import Post

def main(page: ft.Page):
    page.scroll = 'always'
    page.add(Post.card(data))
    page.add(Post.card(data))
ft.app(main)