from pyboy import PyBoy, WindowEvent

class GameBoy(PyBoy):

    def press(self,button):
        mappings = {
            "a": "BUTTON_A",
            "b": "BUTTON_B",
            "start": "BUTTON_START",
            "select": "BUTTON_SELECT",
            "up": "ARROW_UP",
            "down": "ARROW_DOWN",
            "left": "ARROW_LEFT",
            "right": "ARROW_RIGHT",
        }

        button = str(button).lower()
        key = mappings.get(button, None)

        press = getattr(WindowEvent, f"PRESS_{key}")
        release = getattr(WindowEvent, f"RELEASE_{key}")

        self.send_input(press)
        self.tick()
        self.tick()
        self.send_input(release)
