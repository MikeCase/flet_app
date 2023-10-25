from typing import Any, List, Optional, Union
import flet as ft
from flet import UserControl
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

class VehicleInfoBar(UserControl):
    def __init__(self):
        super().__init__()
        
        self.make = ''
        self.model = ''
        self.year = ''
        self.vin = ''
        self.engine = ''
        self.mileage = ''

        self.hint_text_style = ft.TextStyle(size=10)
        self.padding = ft.padding.symmetric(1, 5)
        
        ## Vehicle Make TextField
        self.veh_make = ft.TextField(
            value='',
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Make",
            height=30,
            text_size=10,
            label_style=self.hint_text_style,
            content_padding=self.padding
        )


        self.veh_model = ft.TextField(
            value='',
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Model",
            height=30,
            text_size=10,
            label_style=self.hint_text_style,
            content_padding=self.padding
        )

        self.veh_year = ft.TextField(
            value='',
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Year",
            height=30,
            text_size=10,
            label_style=self.hint_text_style,
            content_padding=self.padding
        )
        
        self.veh_vin = ft.TextField(
            value='',
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Identification Number (VIN)",
            height=30,
            text_size=10,
            label_style=self.hint_text_style,
            content_padding=self.padding
        )

        self.veh_engine = ft.TextField(
            value='',
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Engine Size in Liters",
            height=30,
            text_size=10,
            label_style=self.hint_text_style,
            content_padding=self.padding
        )
        
        self.veh_mileage = ft.TextField(
            value='',
            text_align=ft.TextAlign.LEFT,
            label="Vehicle Mileage",
            height=30,
            text_size=10,
            label_style=self.hint_text_style,
            content_padding=self.padding
        )

    def build(self):
        
        return ft.Row(
            controls=[
                self.veh_make,
                self.veh_model,
                self.veh_year,
                self.veh_vin,
                self.veh_engine,
                self.veh_mileage,
            ]
        )

    