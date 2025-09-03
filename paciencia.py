SLOT_WIDTH = 70
SLOT_HEIGHT = 100

import flet as ft

# Uso do GestureDetector com o evento on_pan_update para arrastar o cartão
# Posicionamento absoluto dos controles dentro da pilha

class Slot(ft.Container):
    def __init__(self, top, left):
        super().__init__()
        self.pile=[]
        self.width=SLOT_WIDTH
        self.height=SLOT_HEIGHT
        self.left=left
        self.top=top
        self.border=ft.border.all(1)
class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0

def main(page: ft.Page):
    def place(card, slot):
        """coloque a carta no slot"""
        card.top = slot.top
        card.left = slot.left

    def bounce_back(game, card):
        """devolve a carta para a posição inicial"""
        card.top = game.start_top
        card.left = game.start_left

    def move_on_top(card, controls):
        """Moves draggable card to the top of the stack"""
        controls.remove(card)
        controls.append(card)
        page.update()

    def start_drag(e: ft.DragStartEvent):
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left
       
    def start_drag(e: ft.DragStartEvent):
        move_on_top(e.control, controls)
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left   

    def drop(e: ft.DragEndEvent):
        for slot in slots:
            if (
                abs(e.control.top - slot.top) < 20
            and abs(e.control.left - slot.left) < 20
        ):
                place(e.control, slot)
                e.control.update()
                return

        bounce_back(solitaire, e.control)
        e.control.update()

    def drag(e: ft.DragUpdateEvent):
        e.control.top += e.delta_y
        e.control.left += e.delta_x
        e.control.update()

    slot0 = ft.Container(
        width=70, height=100, left=0, top=0, border=ft.border.all(1)
)

    slot1 = ft.Container(
        width=70, height=100, left=200, top=0, border=ft.border.all(1)
)

    slot2 = ft.Container(
        width=70, height=100, left=300, top=0, border=ft.border.all(1)
)

    slots = [slot0, slot1, slot2]



    card1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),
)
    card2 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=100,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.YELLOW, width=70, height=100),
   )

    controls = [slot0, slot1, slot2, card1, card2]

    # deal cards
    place(card1, slot0)
    place(card2, slot0)

    solitaire = Solitaire()

    page.add(ft.Stack(controls=controls, width=1000, height=500))

ft.app(target=main)