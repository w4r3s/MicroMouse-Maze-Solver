# modules/views_and_themes.py

class ThemeManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.themes = {
            'Default': {'background': 'white', 'wall_color': 'black'},
            'Dark': {'background': 'black', 'wall_color': 'white'},
            # 可以添加更多主题
        }
        self.current_theme = 'Default'

    def apply_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name
            theme = self.themes[theme_name]
            self.canvas.config(bg=theme['background'])
            # 在绘制时使用 theme['wall_color']
            # 可以在这里更新其他界面元素的颜色

    def get_wall_color(self):
        # 返回当前主题的墙壁颜色
        theme = self.themes.get(self.current_theme, self.themes['Default'])
        return theme['wall_color']
