from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys

class BanglaKeyboard(QLineEdit):
    def __init__(self):
        super().__init__()
        # Set a larger font size using stylesheet
        self.setStyleSheet("font-size: 20px;")  # Adjust the font size as needed

    def keyPressEvent(self, event: QKeyEvent):
        # Check if Shift is pressed
        shift_pressed = event.modifiers() & Qt.KeyboardModifier.ShiftModifier

        # Check if Ctrl is pressed
        ctrl_pressed = event.modifiers() & Qt.KeyboardModifier.ControlModifier

        # Bangla key mappings (updated based on your input)
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
            Qt.Key.Key_Space: " ",  # Space key
        }

        # Ignore Ctrl key combinations
        if ctrl_pressed:
            super().keyPressEvent(event)  # Process Ctrl key combinations normally
        elif event.key() in key_mappings:
            # Get the mapped character
            char = key_mappings[event.key()]

            # Handle space key separately
            if event.key() == Qt.Key.Key_Space:
                # Insert a space at the cursor position
                self.insert(" ")
                # Move the cursor to the right after inserting the space
                self.setCursorPosition(self.cursorPosition() + 1)
            else:
                # Handle vowel signs (া, ি, ী, ু, ূ, ে, ৈ, ো, ৌ, etc.)
                if char in ["া", "ি", "ী", "ু", "ূ", "ে", "ৈ", "ো", "ৌ", "ৃ", "্র", "্য"]:
                    # Combine the vowel sign with the previous character
                    cursor_position = self.cursorPosition()
                    if cursor_position > 0:
                        # Get the character before the cursor
                        previous_char = self.text()[cursor_position - 1]
                        combined_char = self.combine_vowel_sign(previous_char, char)
                        # Replace the previous character with the combined character
                        self.setText(self.text()[:cursor_position - 1] + combined_char + self.text()[cursor_position:])
                        # Move the cursor to the right after inserting the vowel sign
                        self.setCursorPosition(cursor_position + 1)
                    else:
                        # If there's no previous character, just insert the vowel sign
                        self.insert(char)
                        # Move the cursor to the right after inserting the vowel sign
                        self.setCursorPosition(self.cursorPosition() + 1)
                else:
                    # Insert the character at the cursor position
                    self.insert(char)
        else:
            super().keyPressEvent(event)  # Process other keys normally

    def combine_vowel_sign(self, consonant: str, vowel_sign: str) -> str:
        """
        Combine a consonant with a vowel sign.
        """
        # Mapping of consonant + vowel sign combinations
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

        # Return the combined character if found, otherwise return consonant + vowel sign
        return combinations.get((consonant, vowel_sign), consonant + vowel_sign)

class BanglaTypingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bangla Keyboard - PyQt6")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.line_edit = BanglaKeyboard()
        self.line_edit.setPlaceholderText("Type Bangla here...")

        layout.addWidget(self.line_edit)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BanglaTypingApp()
    window.show()
    sys.exit(app.exec())