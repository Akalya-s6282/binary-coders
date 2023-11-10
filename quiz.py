import flet as ft

def main(page: ft.Page):
    questions = ["What is the capital of France?", "Which planet is nearest to the Sun?"]
    optionsa = ["a. New York","a. Mercury"]
    optionsb = [ "b. Paris", "b. Venus"]
    optionsc = [ "c. Madrid", "c. Earth"]
    optionsd = ["c. Madrid", "c. Earth"]
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Container(
           
                 
            ft.Stack(
                [
                    ft.Container(
                        content=ft.OutlinedButton("optionsa[i]"),
                        width=300,
                        height=50, 
                        bgcolor=ft.colors.RED, 
                        border_radius=5,
                        right=150,
                        bottom=200,
                    ),
                    ft.Container(
                         content=ft.OutlinedButton("optionsb[i]"),
                         
                        width=300,
                        height=50,
                       
                        border_radius=5,
                        right=150,
                        bottom=50,
                    ),
                    ft.Container(
                         content=ft.OutlinedButton("optionsc[i]"),
                        width=300,
                        height=50,
                        
                        left=150,
                        bottom=200,
                    ),
                    ft.Container(
                         content=ft.OutlinedButton("options[i]"),
                        width=300,
                        height=50,
                        
                        
                        left=150,
                        bottom=50,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Text("questions[i]"),
                                alignment=ft.alignment.center,
                                width=1000,
                                height=50,
                                
                                border_radius=5,
                            )
                        ],
                        left=100,
                        top=150,
                    ),
                ]
            ),
            border_radius=8,
            padding=5,
            width=1200,
            height=600,
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLUE, ft.colors.YELLOW],),
        )
    )
    
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
                        