from chiplotle import *

text = 'Your name\n\rwww.yourwebsite.net\n\ryouremail@xxx.net\n\ryour phone'
l1 = Label((1500, -550), text, charsize=(.1, .1), origin=7)
text = 'your title here'
l2 = Label((0, -300), text, charsize=(.1, .1), origin=4)
log = Cube((0, 200), width = 500, height = 500, depth = 500,  
   rotation=(1.1, 2.9, 2.3))
p = BusinessCard((0,0), log, [l1, l2], pen=1)

io.view(p)
