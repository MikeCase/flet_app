import json
import flet as ft
from flet import UserControl
import requests


class VinDecoder(UserControl):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.symmetric(1, 5)
        self.label_text_style = ft.TextStyle(size=10, weight=ft.FontWeight.NORMAL)

        self.decoded = ''


        self.veh_vin = ft.TextField(
            value='1B7MC3364XJ592341', # Default for testing
            border="none",
            
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Identification Number (VIN)",
            height=30,
            text_size=10,
            label_style=self.label_text_style,
            content_padding=self.padding
        )

        self.container = ft.Container(
            content=ft.Row(
                controls=[
                    self.veh_vin,
                    ft.IconButton(ft.icons.SEARCH, on_click=lambda x: self.decodeVin(self.veh_vin.value)),
                ],
            ),
            expand=True,
            bgcolor=ft.colors.BLUE_GREY_900,
            padding=5,
            border_radius=ft.border_radius.all(5)
        )

        self.decoded_txt = ft.Text(
            value=self.decoded,
        )

    def decodeVin(self, vin):
        self.decoded = ''

        r = requests.get(
            f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvaluesextended/{vin}?format=json'
        )

        result = r.json()['Results'][0]
        with open('results.json', "w") as f:
            json.dump(result, f)

        result = {k:v for (k, v) in result.items() if v != ""}
        for k,v in result.items():
            self.decoded += f"{k}: {result[k]}\n"
        
        self.decoded_txt.value = self.decoded
        self.update()

    def build(self):

        return ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        self.container,
                    ],
                ),
                ft.ResponsiveRow(
                    controls= [
                        self.decoded_txt
                    ],
                ),
            ],
        )
    