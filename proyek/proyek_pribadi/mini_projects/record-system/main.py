import flet as ft 
import os
import csv

data_table_style: dict = {
    "main": {
        "expand": 3,
        "bgcolor": "#fdfdfe",
    },
    "data_table": {
        "heading_row_color": "#e3e4ea",
        "expand": True,
        "heading_row_height": 35,
        "data_row_max_height": 40,
    },
}

class DataTable(ft.Container):
    def __init__(self) -> None:
        super().__init__(**data_table_style["main"])
        
        self.table = ft.DataTable(
            **data_table_style["data_table"],
        )
        
        headers: list = ["Nama Lengkap", "Alamat Surel", "Peran"]
        
        self.table.columns = [
            ft.DataColumn(
                ft.Text(title, weight = "w600", size = 12)
            ) for title in headers
        ]
        
        self.content = ft.Column(
            scroll = "hidden",
            controls = [ft.Row(controls = [self.table])]
        )

form_style: dict = {
    "main": {
        "expand": 2,
        "bgcolor": "#fdfdfe",
        "padding": ft.padding.only(left = 35, right = 35),
    },
    "input": {
        "height": 38,
        "border_color": "#aeaeb3",
        "focused_border_color": "black",
        "border_radius": 5,
        "cursor_height": 16,
        "cursor_color": "black",
        "content_padding": 10,
        "border_width": 1.5,
        "text_size": 12,
    }
}

class Form(ft.Container):
    def __init__(self) -> None:
        super().__init__(**form_style["main"])
        
        self.name = ft.TextField(**form_style["input"])
        self.email = ft.TextField(**form_style["input"])
        self.role = ft.TextField(**form_style["input"])
        
        data: list = ["Nama Lengkap", "Alamat Surel", "Peran"]
        fields: list = [self.name, self.email, self.role]
        
        items: list = [
            ft.Column(
                expand = True,
                spacing = 4,
                controls = [
                    ft.Text(title, size = 12, weight = "w500"),
                    fields[index]
                ]
            ) for index, title in enumerate(data)
        ]
        
        self.content = ft.Column(
            controls = [
                ft.Divider(height = 10, color = "transparent"),
                ft.Text("Record System", size = 28, weight = "w900"),
                ft.Divider(height = 30, color = "transparent"),
                ft.Row(spacing = 20, expand = True, controls = items),   
            ]
        )

def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    
    dataTable: ft.Container = DataTable()
    form: ft.Container = Form()
    
    page.add(
        ft.Row(
            expand = True,
            spacing = 0,
            controls = [
                ft.Column(
                    expand = 5,
                    controls = [form, dataTable],
                )
            ],
        )
    )
    
    page.update()
    
if __name__ == "__main__":
    ft.app(target = main)