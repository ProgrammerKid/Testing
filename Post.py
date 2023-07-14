import flet as ft

class card(ft.UserControl):
    def __init__(self, data):
        super().__init__()
        self.data = data
        
    def open_close(self, e):
        if e.control.data == 'closed' :
            e.control.data = 'opened'
            e.control.icon = ft.icons.ARROW_DROP_DOWN_CIRCLE
            Card.content.content.controls.append(ft.Markdown(self.data["details"]))
        elif e.control.data == 'opened':
            e.control.data = 'closed'
            e.control.icon = ft.icons.ARROW_DROP_DOWN_CIRCLE_OUTLINED
            Card.content.content.controls.pop(-1)

        self.update()
            
    def build(self):
        global Card
        Card = ft.Card(
            ft.Container(
                ft.Column(
                    [   
                        ft.Row([
                                ft.Text(self.data['title'], 
                                    size=18,
                                    weight='bold',
                                    width=200,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                    ),
                                ft.IconButton(icon=ft.icons.ARROW_DROP_DOWN_CIRCLE_OUTLINED,
                                              on_click=self.open_close, icon_color='black', data='closed')
                            ], 
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(),
                        ft.Text(spans=[
                            ft.TextSpan('Date: ', style=ft.TextStyle(weight='bold')),
                            ft.TextSpan(self.data["currentTimestamp"].split()[0])
                        ]),
                        ft.Text(spans=[
                            ft.TextSpan('Subject: ', style=ft.TextStyle(weight='bold')) if self.data["subject"] != None else ft.TextSpan('No subject', style=ft.TextStyle(weight='bold')),
                            ft.TextSpan(self.data["subject"])
                        ]),
                        ft.Row(height= 15),
                        
                    ],
                    spacing=5
                ),
                padding=10,
                width=280,
                ink=True,
            ),
        )
        return Card
    
        
    
