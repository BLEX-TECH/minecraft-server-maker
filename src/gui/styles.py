"""GUI Styles and Themes"""

DARK_THEME = """
QMainWindow {
    background-color: #1e1e1e;
    color: #ffffff;
}

QWidget {
    background-color: #1e1e1e;
    color: #ffffff;
}

QPushButton {
    background-color: #0d47a1;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: bold;
    font-size: 12px;
}

QPushButton:hover {
    background-color: #1565c0;
}

QPushButton:pressed {
    background-color: #0d3a8f;
}

QPushButton:disabled {
    background-color: #555555;
    color: #999999;
}

QLineEdit, QSpinBox, QDoubleSpinBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #444444;
    border-radius: 4px;
    padding: 6px;
    font-size: 11px;
}

QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {
    border: 1px solid #0d47a1;
}

QComboBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #444444;
    border-radius: 4px;
    padding: 6px;
}

QComboBox::drop-down {
    border: none;
    background-color: #1e1e1e;
}

QComboBox QAbstractItemView {
    background-color: #2d2d2d;
    color: #ffffff;
    selection-background-color: #0d47a1;
}

QLabel {
    color: #ffffff;
    font-size: 12px;
}

QGroupBox {
    color: #ffffff;
    border: 1px solid #444444;
    border-radius: 4px;
    margin-top: 10px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px 0 3px;
}

QTabWidget::pane {
    border: 1px solid #444444;
}

QTabBar::tab {
    background-color: #2d2d2d;
    color: #ffffff;
    padding: 8px 20px;
    border: 1px solid #444444;
}

QTabBar::tab:selected {
    background-color: #0d47a1;
    color: white;
}

QTextEdit, QPlainTextEdit {
    background-color: #2d2d2d;
    color: #00ff00;
    border: 1px solid #444444;
    font-family: Courier New;
    font-size: 10px;
}

QScrollBar:vertical {
    background-color: #2d2d2d;
    width: 12px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #555555;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #777777;
}

QStatusBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border-top: 1px solid #444444;
}

QMenuBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border-bottom: 1px solid #444444;
}

QMenuBar::item:selected {
    background-color: #0d47a1;
}

QMenu {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #444444;
}

QMenu::item:selected {
    background-color: #0d47a1;
}
"""

SPINBOX_STYLE = """
QSpinBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #444444;
    border-radius: 4px;
}
QSpinBox::up-button, QSpinBox::down-button {
    border: none;
    background-color: #444444;
}
QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background-color: #0d47a1;
}
"""
