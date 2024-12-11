from flet import*


class MyApp(UserControl):
    def __init__(self,page,primary_color,secondary_color,background_color,text_color,padding_value,margin_value):
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.background_color = background_color
        self.text_color = text_color
        self.padding_value = padding_value
        self.margin_value = margin_value
        self.build()