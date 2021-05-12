# testing codes are under develpoing
import pytest
from PySide2 import QtCore
import main


@pytest.fixture
def app(qtbot):
    test_app = main.MainWidget()
    qtbot.addWidget(test_app)

    return test_app


def test_empty_label(app):
    assert app.ui.EquationDisplay.text() == ''


def test_buttons_click(app, qtbot):
    
    qtbot.mouseClick(app.ui.Button_0, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '0'

    qtbot.mouseClick(app.ui.Button_1, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '1'

    qtbot.mouseClick(app.ui.Button_2, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '2'
    
    qtbot.mouseClick(app.ui.Button_3, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '3'

    qtbot.mouseClick(app.ui.Button_4, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '4'

    qtbot.mouseClick(app.ui.Button_5, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '5'

    qtbot.mouseClick(app.ui.Button_6, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '6'

    qtbot.mouseClick(app.ui.Button_7, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '7'

    qtbot.mouseClick(app.ui.Button_8, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '8'

    qtbot.mouseClick(app.ui.Button_9, QtCore.Qt.LeftButton)
    expr = app.ui.EquationDisplay.text()
    assert expr[-1] == '9'

    


    

    
