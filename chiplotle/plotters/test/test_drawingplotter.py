from chiplotle import *
from chiplotle.hpgl.commands import *
from chiplotle.tools.plottertools.instantiate_virtual_plotter \
   import instantiate_virtual_plotter

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

