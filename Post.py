import flet as ft

class card(ft.UserControl):
    def __init__(self, data):
        super().__init__()
        self.data = data # set self.data equal to the diary data
        
    def open_close(self, e):# called when dropdown button is pressed
        if e.control.data == 'closed' : # If the post is closed open it, change the icon of the dropdown button and append the details of the post in the card
            e.control.data = 'opened'
            e.control.icon = ft.icons.ARROW_DROP_DOWN_CIRCLE
            Card.content.content.controls.append(ft.Markdown(self.data["details"])) # get details from data dictionary
        elif e.control.data == 'opened': # If the post is opened close it, change the icon of the dropdown button and remove the details of the post from the card
            e.control.data = 'closed'
            e.control.icon = ft.icons.ARROW_DROP_DOWN_CIRCLE_OUTLINED
            Card.content.content.controls.pop(-1)

        self.update()
            
    def build(self):
        global Card # Set card as a global variable to use it in the open_close function
        Card = ft.Card(
            ft.Container(
                ft.Column(
                    [   
                        ft.Row([
                                ft.Text(self.data['title'], # get title from diary data
                                    size=18,
                                    weight='bold',
                                    width=200,
                                    overflow=ft.TextOverflow.ELLIPSIS 
                                    ),
                                ft.IconButton(icon=ft.icons.ARROW_DROP_DOWN_CIRCLE_OUTLINED, # button for opening and closing the post Card
                                              on_click=self.open_close, icon_color='black', data='closed')
                            ], 
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(),
                        ft.Text(spans=[
                            ft.TextSpan('Date: ', style=ft.TextStyle(weight='bold')), # date
                            ft.TextSpan(self.data["currentTimestamp"].split()[0])# get the timestamp(list) from diary data and get only the date (not time)
                        ]),
                        ft.Text(spans=[
                            ft.TextSpan('Subject: ', style=ft.TextStyle(weight='bold')) if self.data["subject"] != None else ft.TextSpan('No subject', style=ft.TextStyle(weight='bold')),
                            ft.TextSpan(self.data["subject"])# get subject from diary data
                        ]),
                        ft.Row(height= 15),
                        
                    ],
                    spacing=5
                ),
                padding=10,
                width=280,
            ),
        )
        return Card
    
        
    
