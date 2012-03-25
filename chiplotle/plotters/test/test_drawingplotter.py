from chiplotle import *
from chiplotle.hpgl.commands import *
from chiplotle.tools.plottertools.instantiate_virtual_plotter \
   import instantiate_virtual_plotter

## goto ##

def test_goto_01():
   p = instantiate_virtual_plotter( )
   p.goto(10, 10)
   assert p._serial_port.get_received_commands() == [IN(), PA([(10, 10)])]

def test_gotocenter_01():
   p = instantiate_virtual_plotter( )
   p.goto_center()
   assert p._serial_port._received_commands_string == 'IN;PA5160.00,3960.00;'
   assert p._serial_port.get_received_commands() == [IN(), PA([(5160.0,3960.0)])]

def test_goto_bottom_left():
   p = instantiate_virtual_plotter( )
   p.goto_bottom_left()

def test_goto_bottom_right():
   p = instantiate_virtual_plotter( )
   p.goto_bottom_right()

def test_goto_bottom_right():
   p = instantiate_virtual_plotter( )
   p.goto_bottom_right()

def test_goto_origin():
   p = instantiate_virtual_plotter( )
   p.goto_origin()

def test_goto_top_left():
   p = instantiate_virtual_plotter( )
   p.goto_top_left()

def test_goto_top_right():
   p = instantiate_virtual_plotter( )
   p.goto_top_right()

def test_nudge():
   p = instantiate_virtual_plotter( )
   p.nudge(1, 2)


## set origin ##

def test_set_origin_bottom_left():
   p = instantiate_virtual_plotter( )
   p.set_origin_bottom_left()

def test_set_origin_top_left():
   p = instantiate_virtual_plotter( )
   p.set_origin_top_left()

def test_set_origin_bottom_right():
   p = instantiate_virtual_plotter( )
   p.set_origin_bottom_right()

def test_set_origin_top_right():
   p = instantiate_virtual_plotter( )
   p.set_origin_top_right()

def test_set_origin_center():
   p = instantiate_virtual_plotter( )
   p.set_origin_center()

def test_set_origin_current_location():
   p = instantiate_virtual_plotter()
   p.set_origin_current_location()

def test_set_origin_to_point():
   p = instantiate_virtual_plotter()
   p.set_origin_to_point(Coordinate(1, 2))

## transforms ##

def test_rotate():
   p = instantiate_virtual_plotter()
   p.rotate(90)
   
def test_scale():
   p = instantiate_virtual_plotter()
   p.scale(0, 0, 2, 2)
   
## window setting ##

def test_set_plot_window_01():
   '''Arguments as tuples.'''
   p = instantiate_virtual_plotter()
   p.set_plot_window((0, 0), (1, 2))

def test_set_plot_window_02():
   '''Arguments as coordinates.'''
   p = instantiate_virtual_plotter()
   p.set_plot_window(Coordinate(0, 0), Coordinate(1, 2))

