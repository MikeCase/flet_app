import flet as ft
from flet import ControlEvent
from vehicle_info_bar import VehicleInfoBar
from vin_decoder_control import VinDecoder


def main(page: ft.Page):
    page.title = "Vehicle Work Log"
    page.horizontal_alignment = "center"
    # page.vertical_alignment = "center"
    page.scroll = ft.ScrollMode.ADAPTIVE


    view = ft.ResponsiveRow(
        controls = [
            VinDecoder(),
        ],
        # expand=True
        
    )
    page.add(view)


if __name__ == "__main__":
    ft.app(target=main)
