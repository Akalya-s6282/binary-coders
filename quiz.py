import flet as ft

def main (page: ft.Page):
    def button_clicked(e):
        page.add(
            ft.Text("Clicked"))
        page.add(ft.ElevatedButton(text = "Play")) 
    page.title = "Test your knowledge"
    c = ft.Container(
        width=1200,
        height=600,
        bgcolor=ft.colors.SURFACE_VARIANT,
       
        content=ft.ElevatedButton("PLay",on_click = button_clicked),
        padding= 250
    )
    page.update()
    page.add(c)
    
ft.app(target=main, view=ft.AppView.WEB_BROWSER)