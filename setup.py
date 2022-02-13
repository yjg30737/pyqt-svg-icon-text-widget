from setuptools import setup, find_packages

setup(
    name='pyqt-svg-icon-text-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt widget consists of svg icon label and text label',
    url='https://github.com/yjg30737/pyqt-svg-icon-text-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-label @ git+https://git@github.com/yjg30737/pyqt-svg-label.git@main'
    ]
)