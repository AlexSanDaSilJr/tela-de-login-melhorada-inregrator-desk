import flet as ft
from ping3 import ping


def main(page: ft.Page):

    page.padding = 0
    page.scroll = True
    page.window_height = 467
    page.window_width = 349
    page.window_always_on_top = True
    page.window_title_bar_hidden = True
    page.window_left = 850
    page.window_top = 400

    conteudo_barra_banner = ft.Row(
        [ft.Text("LOGIN", color="WHITE", weight=ft.FontWeight.BOLD),
        ft.Text("ISP INTEGRATOR", color="WHITE", weight=ft.FontWeight.BOLD),],
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )

    barra_banner = ft.Container(
        content=conteudo_barra_banner,
        bgcolor="#22438a",
        padding=10,
    )

    imagem_logo = ft.Image(src=r"C:\Users\FHP0087\Desktop\logo_banner.png")
    logo_banner = ft.Row(controls=[imagem_logo], alignment=ft.MainAxisAlignment.CENTER, height=185)

    campo_leitura = ft.Row(controls=[ft.Container(width=6, bgcolor="BLUE"), ft.Column(
        [ft.TextField(label="Usuário", height=40, border_radius=5, border_color="GREY", capitalization= ft.TextCapitalization.CHARACTERS),
        ft.TextField(label="Senha", height=40, border_radius=5, border_color="GREY", can_reveal_password=True, password=True), ],
        spacing=5,
    ), ft.Container(width=10, bgcolor="BLUE")])

    botoes = ft.Row(
        [ft.ElevatedButton("Entrar"),
        ft.ElevatedButton("Sair")],
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
    )

    informacoes = ft.Row([ft.Column(
        [ft.Text("@ 2021 Elitesoft informática Ltda", text_align=ft.TextAlign.CENTER),
        ft.Text("Versão 6.11.11", text_align=ft.TextAlign.CENTER),
        ft.Text("[Web5] [Web6]", text_align=ft.TextAlign.CENTER, color="#1f2fff", weight=ft.FontWeight.BOLD)],
        horizontal_alignment="CENTER",
        spacing=2
    )],
    alignment= ft.MainAxisAlignment.CENTER,
    )
    
    page.add(
        ft.Row(height=1),
        barra_banner,
        logo_banner,
        campo_leitura,
        botoes,
        informacoes,
    )
    

ft.app(target=main)