# pyqt-svg-icon-text-widget
PyQt widget consists of textless `QLabel` which has svg image as an icon on the left and text included `QLabel` on the right. 

This module is useful to set the icon included title bar.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-svg-icon-text-widget`

## Included Package
* <a href="https://github.com/yjg30737/pyqt-svg-label.git">pyqt-svg-label</a>

## Usage
* `setSvgFile(filename: str)` to set svg file
* `setText(text: str)` to set text

## Note
Svg icon `QLabel`'s maximum height is set according to text included `QLabel`'s font height.

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_svg_icon_text_widget import SvgIconTextWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = SvgIconTextWidget()
    ex.setSvgFile('ico/dark-notepad.svg')
    ex.setText('Dark Notepad')
    ex.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/153750415-c9f99eb7-46be-4703-9751-18578e839f4b.png)
