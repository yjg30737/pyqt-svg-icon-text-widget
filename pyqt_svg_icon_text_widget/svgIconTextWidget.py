from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from pyqt_svg_label import SvgLabel


class SvgIconTextWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__svgIconLbl = SvgLabel()

        self.__textLbl = QLabel()
        self.__textLbl.installEventFilter(self)

        title_lbl_size = self.__textLbl.font().pointSize()

        self.__setIconSizeForFontSize()

        lay = QHBoxLayout()
        lay.addWidget(self.__svgIconLbl)
        lay.addWidget(self.__textLbl)

        self.setLayout(lay)

    def setSvgFile(self, filename: str):
        self.__svgIconLbl.setSvgFile(filename)
        title_lbl_size = self.__textLbl.font().pointSize()

    def setText(self, text: str):
        self.__textLbl.setText(text)

    def getSvgLabel(self) -> SvgLabel:
        return self.__svgIconLbl

    def getTextLabel(self) -> QLabel:
        return self.__textLbl

    def __setIconSizeForFontSize(self):
        # get the point size of the self.__textLbl's font
        title_lbl_size = self.__textLbl.font().pointSize()
        # to match the self.__svgIconLbl's size with self.__textLbl's font size
        self.__svgIconLbl.setFixedSize(title_lbl_size * 1.5, title_lbl_size * 1.5)

    def eventFilter(self, obj, e):
        if obj == self.__textLbl:
            # font changed
            if e.type() == 97:
                self.__setIconSizeForFontSize()
        return super().eventFilter(obj, e)