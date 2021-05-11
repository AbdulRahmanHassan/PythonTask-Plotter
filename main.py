# import main libraries
from  PySide2.QtWidgets  import * 
from  PySide2.QtUiTools  import  QUiLoader 
from  PySide2.QtCore  import  QFile

from  matplotlib.backends.backend_qt5agg  import  ( 
        FigureCanvas ,  NavigationToolbar2QT  as  NavigationToolbar )

from  matplotlib.figure  import  Figure

import  numpy  as  np 
import  random



# create widget to hold plots, MplWidget 
class  MplWidget ( QWidget ):
    
    def  __init__ ( self ,  parent  =  None ):
        
        QWidget . __init__ ( self ,  parent )
        
        self . canvas  =  FigureCanvas ( Figure ())
        
        vertical_layout  =  QVBoxLayout () 
        vertical_layout . addWidget ( self . canvas ) 
        vertical_layout . addWidget ( NavigationToolbar ( self . canvas ,  self ))
        
        self . canvas . axes  =  self . canvas . figure . add_subplot ( 111 ) 
        self . setLayout ( vertical_layout )    



# main program, MainWidget 
class  MainWidget ( QWidget ):

    def  __init__ ( self ):
        
        QWidget . __init__ ( self )

        designer_file  =  QFile ( "FunctionPlotter.ui" ) 
        designer_file . open ( QFile . ReadOnly )

        loader  =  QUiLoader () 
        loader . registerCustomWidget ( MplWidget ) 
        self . ui  =  loader . load ( designer_file ,  self )

        designer_file . close ()

        # define GUI pushbutton and related function
        self.ui.Button_0.pressed.connect(self.btn_0)
        self.ui.Button_1.pressed.connect(self.btn_1)
        self.ui.Button_2.pressed.connect(self.btn_2)
        self.ui.Button_3.pressed.connect(self.btn_3)
        self.ui.Button_4.pressed.connect(self.btn_4)
        self.ui.Button_5.pressed.connect(self.btn_5)
        self.ui.Button_6.pressed.connect(self.btn_6)
        self.ui.Button_7.pressed.connect(self.btn_7)
        self.ui.Button_8.pressed.connect(self.btn_8)
        self.ui.Button_9.pressed.connect(self.btn_9)
        self.ui.Button_X.pressed.connect(self.btn_X)
        self.ui.Button_X_2.pressed.connect(self.update_graph)
        self.ui.Button_divid.pressed.connect(self.btn_divid)
        self.ui.Button_dot.pressed.connect(self.btn_dot)
        self.ui.Button_end.pressed.connect(self.btn_end)
        self.ui.Button_clear.pressed.connect(self.btn_clear)
        self.ui.Button_minus.pressed.connect(self.btn_minus)
        self.ui.Button_mul.pressed.connect(self.btn_mul)
        self.ui.Button_plus.pressed.connect(self.btn_plus)
        self.ui.Button_power.pressed.connect(self.btn_power)
        self.ui.Button_start.pressed.connect(self.btn_start)
        
        self . setWindowTitle ( "Plotter" )

        grid_layout  =  QGridLayout () 
        grid_layout . addWidget ( self . ui ) 
        self . setLayout ( grid_layout )


    # define buttons functions
    
    def btn_0(self):
        expr = self.ui.EquationDisplay.text()                                   # see current user expression
        expr += '0'                                                             # add the specific button letter to the expression
        self.ui.EquationDisplay.setText(expr)                                   # display the new expression


    def btn_1(self):
        expr = self.ui.EquationDisplay.text()
        expr += '1'
        self.ui.EquationDisplay.setText(expr)


    def btn_2(self):
        expr = self.ui.EquationDisplay.text()
        expr += '2'
        self.ui.EquationDisplay.setText(expr)

    def btn_3(self):
        expr = self.ui.EquationDisplay.text()
        expr += '3'
        self.ui.EquationDisplay.setText(expr)


    def btn_4(self):
        expr = self.ui.EquationDisplay.text()
        expr += '4'
        self.ui.EquationDisplay.setText(expr)


    def btn_5(self):
        expr = self.ui.EquationDisplay.text()
        expr += '5'
        self.ui.EquationDisplay.setText(expr)


    def btn_6(self):
        expr = self.ui.EquationDisplay.text()
        expr += '6'
        self.ui.EquationDisplay.setText(expr)


    def btn_7(self):
        expr = self.ui.EquationDisplay.text()
        expr += '7'
        self.ui.EquationDisplay.setText(expr)


    def btn_8(self):
        expr = self.ui.EquationDisplay.text()
        expr += '8'
        self.ui.EquationDisplay.setText(expr)


    def btn_9(self):
        expr = self.ui.EquationDisplay.text()
        expr += '9'
        self.ui.EquationDisplay.setText(expr)


    def btn_X(self):
        expr = self.ui.EquationDisplay.text()
        expr += 'x'
        self.ui.EquationDisplay.setText(expr)


    def btn_divid(self):
        expr = self.ui.EquationDisplay.text()
        expr += '/'
        self.ui.EquationDisplay.setText(expr)


    def btn_dot(self):
        expr = self.ui.EquationDisplay.text()
        expr += '.'
        self.ui.EquationDisplay.setText(expr)


    def btn_end(self):
        expr = self.ui.EquationDisplay.text()
        expr += ')'
        self.ui.EquationDisplay.setText(expr)

        
    def btn_clear(self):
        expr = ''
        self.ui.EquationDisplay.setText(expr)
        

    def btn_minus(self):
        expr = self.ui.EquationDisplay.text()
        expr += '-'
        self.ui.EquationDisplay.setText(expr)


    def btn_mul(self):
        expr = self.ui.EquationDisplay.text()
        expr += '*'
        self.ui.EquationDisplay.setText(expr)


    def btn_plus(self):
        expr = self.ui.EquationDisplay.text()
        expr += '+'
        self.ui.EquationDisplay.setText(expr)


    def btn_power(self):
        expr = self.ui.EquationDisplay.text()
        expr += '**'
        self.ui.EquationDisplay.setText(expr)


    def btn_start(self):
        expr = self.ui.EquationDisplay.text()
        expr += '('
        self.ui.EquationDisplay.setText(expr)

    def update_graph ( self ):
        
        expr = self.ui.EquationDisplay.text()                       # inseart user final expression as final input
        self.ui.EquationDisplay.clear()                             # clear line edit after insertion
        Xmax = self.ui.lineEdit.text()                              # inseart maximum x range
        Xmin = self.ui.lineEdit_2.text()                            # inseart minimum x range
        No_of_points = self.ui.lineEdit_3.text()                    # inseart No of points to plot

        try:
            Xmax = float(Xmax)                                      # check if Xmax, Xmin and no of points are available and transform it to numbers
            Xmin = float(Xmin)
            No_of_points = int(No_of_points)
            x = np.linspace(Xmin, Xmax, No_of_points)               # create numpy array for x range

            if Xmax > Xmin:                                         # check the range validation
                try:
                    result = eval(expr)                             # try to evaluate the final expression
                    self.ui.MplWidget.canvas.axes.clear()           # clear the line edit display 
                    self.ui.MplWidget.canvas.axes.plot(x, result)   # plot the evaluated expression Vs the X range 
                    self.ui.MplWidget.canvas.axes.set_title(expr)   # make the expression as plot title 
                    self.ui.MplWidget.canvas.axes.grid()
                    self.ui.MplWidget.canvas.draw()

                except:
                    result = expr + ' : Expression Error; usual suspect forgetting * 🙂:   5x instead of 5*x'   # if the evaluation failed this means expression error
                    self.ui.EquationDisplay.setText(result)     
            else:
                result = 'range Error; Xmax < Xmin'                 # if the range validation failed means range error
                self.ui.EquationDisplay.setText(result)
        except :
            result = 'Please enter Range and No of points'          # if transformation failed means missing data 
            self.ui.EquationDisplay.setText(result)

        

app  =  QApplication ([]) 
window  =  MainWidget () 
window . show () 
app . exec_ ()
