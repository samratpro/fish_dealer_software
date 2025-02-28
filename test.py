from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys

class BanglaKeyboard(QLineEdit):
    def __init__(self, target_input: QLineEdit):
        super().__init__()
        self.target_input = target_input  # Reference to existing input field

    def keyPressEvent(self, event: QKeyEvent):
        shift_pressed = event.modifiers() & Qt.KeyboardModifier.ShiftModifier
        ctrl_pressed = event.modifiers() & Qt.KeyboardModifier.ControlModifier

        key_mappings = {
            Qt.Key.Key_Q: "ং" if shift_pressed else "ঙ",
            Qt.Key.Key_W: "য়" if shift_pressed else "য",
            Qt.Key.Key_E: "ঢ" if shift_pressed else "ড",
            Qt.Key.Key_R: "ফ" if shift_pressed else "প",
            Qt.Key.Key_T: "ঠ" if shift_pressed else "ট",
            Qt.Key.Key_Y: "ছ" if shift_pressed else "চ",
            Qt.Key.Key_U: "ঝ" if shift_pressed else "জ",
            Qt.Key.Key_I: "ঞ" if shift_pressed else "হ",
            Qt.Key.Key_O: "ঘ" if shift_pressed else "গ",
            Qt.Key.Key_P: "ঢ়" if shift_pressed else "ড়",
            Qt.Key.Key_A: "র্" if shift_pressed else "ৃ",
            Qt.Key.Key_S: "ূ" if shift_pressed else "ু",
            Qt.Key.Key_D: "ী" if shift_pressed else "ি",
            Qt.Key.Key_F: "অ" if shift_pressed else "া",
            Qt.Key.Key_G: "।" if shift_pressed else "্",
            Qt.Key.Key_H: "ভ" if shift_pressed else "ব",
            Qt.Key.Key_J: "খ" if shift_pressed else "ক",
            Qt.Key.Key_K: "থ" if shift_pressed else "ত",
            Qt.Key.Key_L: "ধ" if shift_pressed else "দ",
            Qt.Key.Key_Z: "্য" if shift_pressed else "্র",
            Qt.Key.Key_X: "ৗ" if shift_pressed else "ও",
            Qt.Key.Key_C: "ৈ" if shift_pressed else "ে",
            Qt.Key.Key_V: "ল" if shift_pressed else "র",
            Qt.Key.Key_B: "ণ" if shift_pressed else "ন",
            Qt.Key.Key_N: "ষ" if shift_pressed else "স",
            Qt.Key.Key_M: "শ" if shift_pressed else "ম",
            Qt.Key.Key_QuoteDbl: "”" if shift_pressed else "’",
            Qt.Key.Key_Space: " ",
        }

        if ctrl_pressed:
            super().keyPressEvent(event)  # Process Ctrl key combinations normally
        elif event.key() in key_mappings:
            char = key_mappings[event.key()]
            cursor_position = self.target_input.cursorPosition()

            if char in ["া", "ি", "ী", "ু", "ূ", "ে", "ৈ", "ো", "ৌ", "ৃ", "্র", "্য"]:
                if cursor_position > 0:
                    previous_char = self.target_input.text()[cursor_position - 1]
                    combined_char = self.combine_vowel_sign(previous_char, char)
                    self.target_input.setText(self.target_input.text()[:cursor_position - 1] + combined_char + self.target_input.text()[cursor_position:])
                    self.target_input.setCursorPosition(cursor_position)
                else:
                    self.target_input.insert(char)
                    self.target_input.setCursorPosition(cursor_position + 1)
            else:
                self.target_input.insert(char)
                self.target_input.setCursorPosition(cursor_position + 1)
        else:
            super().keyPressEvent(event)

    def combine_vowel_sign(self, consonant: str, vowel_sign: str) -> str:
        combinations = {
            ("অ", "া"): "আ",
            ("্", "ি"): "ই",
            ("্", "ী"): "ঈ",
            ("্", "ু"): "উ",
            ("্", "ূ"): "ঊ",
            ("্", "ৃ"): "ঋ",
            ("্", "ে"): "এ",
            ("্", "ৈ"): "ঐ",
            ("ও", "ো"): "ও",
            ("ও", "ৗ"): "ঔ"
        }
        return combinations.get((consonant, vowel_sign), consonant + vowel_sign)

class BanglaTypingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bangla Keyboard - PyQt6")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.sellerNameInput = QLineEdit()
        self.sellerNameInput.setPlaceholderText("Seller Name Input")

        # Attach the BanglaKeyboard behavior to the existing input field
        self.banglaKeyboard = BanglaKeyboard(self.sellerNameInput)

        layout.addWidget(self.sellerNameInput)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BanglaTypingApp()
    window.show()
    sys.exit(app.exec())
