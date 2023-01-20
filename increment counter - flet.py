import flet as ft


def main(page: ft.Page):
    page.title = "Increment Counter"
    page.window_width = 270
    page.window_height = 240
    page.window_resizable = False
    # page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def increment(e):
        label.value = str(int(label.value) + 1)
        if int(label.value) > 0:
            btn_reset.opacity = 1
        page.update()

    def reset(e):
        label.value = "0"
        btn_reset.opacity = 0
        page.update()

    label = ft.Text(
        value="0", text_align=ft.TextAlign.CENTER, width=150, font_family="Helvetic bold", size=26)

    btn_increment = ft.ElevatedButton(
        text="Increment", on_click=increment, width=150,
        icon="plus_one", icon_color="green400"
    )
    btn_reset = ft.ElevatedButton(
        text="Reset", on_click=reset, width=150,
        icon="refresh", icon_color="red800",  opacity=0
    )

    page.add(
        ft.Column(
            controls=[
                label,
                btn_increment,
                btn_reset
            ],  width=150)
    )


ft.app(target=main)
