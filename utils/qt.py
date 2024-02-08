from PySide2.QtWidgets import QGroupBox, QRadioButton


def get_checked_radio_text_in_groupbox(groupbox: QGroupBox):
    selected_radio = None
    for button in groupbox.findChildren(QRadioButton):
        if button.isChecked():
            selected_radio = button
            break
    return selected_radio.text() if selected_radio else None


def set_checked_radio_text_in_groupbox(groupbox: QGroupBox, text: str):
    for button in groupbox.findChildren(QRadioButton):
        if button.text() == text:
            button.setChecked(True)
            break
