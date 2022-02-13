from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from pyqt_svg_label import SvgLabel


class SvgIconTextWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__svgIconLbl = SvgLabel()

        self.__textLbl = QLabel()

        # get the point size of the self.__textLbl's font
        title_lbl_size = self.__textLbl.font().pointSize()

        # to match the self.__svgIconLbl's size with self.__textLbl's font size (usually double size is appropriate)
        self.__svgIconLbl.setFixedSize(title_lbl_size * 2, title_lbl_size * 2)

        lay = QHBoxLayout()
        lay.addWidget(self.__svgIconLbl)
        lay.addWidget(self.__textLbl)

        self.setLayout(lay)

    def setSvgFile(self, filename: str):
        self.__svgIconLbl.setSvgFile(filename)

    def setText(self, text: str):
        self.__textLbl.setText(text)
