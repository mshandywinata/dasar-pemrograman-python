import flet as ft

_dark: str = ft.colors.with_opacity(0.5, "white")
_light: str = ft.colors.with_opacity(1, "black")

toggle_style_sheet: dict = {"icon": ft.icons.DARK_MODE_ROUNDED, "icon_size": 18}
add_style_sheet: dict = {"icon": ft.icons.ADD_ROUNDED, "icon_size": 18}

item_style_sheet: dict = {
    "height": 50,
    "expand": True,
    "border_color": _dark,
    "hint_text": "Tambahkan daftar tugasmu di sini...",
    "content_padding": 15,
}

todo_item_style_sheet: dict = {
    "height": 50,
    "border_radius": 4,
}

class ToDoItem(ft.Container):
    def __init__(self, hero: object, description: str, theme: str) -> None:
        if theme == "dark":
            todo_item_style_sheet["border"] = ft.border.all(1, _dark)
        else:
            todo_item_style_sheet["border"] = ft.border.all(1, _light)
        
        super().__init__(**todo_item_style_sheet)
        self.hero: object = hero
        self.description: str = description
        
        self.tick = ft.Checkbox(on_change = lambda e: self.strike(e))
        self.text: ft.Text = ft.Text(
            spans = [ft.TextSpan(text = self.description)], size = 14
        )
        self.delete: ft.IconButton = ft.IconButton(
            icon = ft.icons.DELETE_ROUNDED,
            icon_color = "red700",
            on_click = lambda e: self.delete_text(e)
        )
        
        self.content: ft.Row = ft.Row(
            alignment = "spaceBetween",
            controls = [
                ft.Row(controls = [self.tick, self.text]),
                self.delete
            ],
        )
        
    def strike(self, e) -> None:
        if e.control.value is True:
            self.text.spans[0].style = ft.TextStyle(
                decoration = ft.TextDecoration.LINE_THROUGH, decoration_thickness = 2
            )
            
        else:
            self.text.spans[0].style = ft.TextStyle()
            
        self.text.update()
        
    def delete_text(self, e):
        self.hero.todo_area.controls.remove(self)
        self.hero.todo_area.update()
        self.hero.item_size()
        ...

class Hero(ft.SafeArea):
    def __init__(self, page: ft.page) -> None:
        super().__init__(minimum = 10, maintain_bottom_view_padding = True)
        self.page = page
        self.title: ft.Text = ft.Text("Daftar Tugas", size = 20, weight = "w800")
        self.toggle : ft.IconButton = ft.IconButton(**toggle_style_sheet, on_click = lambda e: self.switch(e))
        self.item: ft.TextField = ft.TextField(**item_style_sheet)
        self.add: ft.IconButton = ft.IconButton(
            **add_style_sheet,
            on_click = lambda e: self.add_item(e)
        )
        
        self.todo_area: ft.Column = ft.Column(expand = True, spacing = 18)
        self.counter: ft.Text = ft.Text("0 tugas", italic = True)
        
        self.main: ft.Column = ft.Column(
            controls = [
                ft.Row(
                    alignment = "spaceBetween",
                    controls = [self.title, self.toggle],
                ),
                ft.Divider(height = 20),
                ft.Divider(height = 10, color = "transparent"),
                ft.Text("1. Tambahkan daftar tugasmu di bawah ini."),
                ft.Row(controls = [self.item, self.add], alignment = "spaceBetween"),
                ft.Divider(height = 10, color = "transparent"),
                ft.Row(
                    alignment = "spaceBetween",
                    controls = [
                        ft.Text("2. Daftar tugas yang harus dikerjakan."),
                        self.counter,
                    ]
                ),
                self.todo_area,
            ]
        )
        
        self.content = self.main
        
    def item_size(self) -> None:
        # if len(self.todo_area.controls[:]) == 1:
        self.counter.value = f"{len(self.todo_area.controls[:])} tugas"
            
        # else:
        #     self.counter.value = f"{len(self.todo_area.controls[:])} items"
            
        self.counter.update()
        
    def add_item(self, e):
        if self.item.value != "":
            if self.page.theme_mode == ft.ThemeMode.DARK:
                self.todo_area.controls.append(ToDoItem(self, self.item.value, "dark"))
            else:
                self.todo_area.controls.append(ToDoItem(self, self.item.value, "light"))
                
            self.todo_area.update()
            self.item_size()
            self.item.value = ""
            self.item.update()
            
        else:
            pass
        
    def switch(self, e) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.toggle.icon = ft.icons.LIGHT_MODE_ROUNDED
            self.item.border_color = _light
            
            for item in self.todo_area.controls[:]:
                item.border = ft.border.all(1, _light)
            
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.toggle.icon = ft.icons.DARK_MODE_ROUNDED
            self.item.border_color = _dark
            
            for item in self.todo_area.controls[:]:
                item.border = ft.border.all(1, _dark)
        
        self.page.update()

def main(page: ft.page) -> None:
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    page.theme = theme
    
    hero: object = Hero(page)
    page.add(hero)
    page.update()
    
if __name__ == '__main__':
    ft.app(target = main)
