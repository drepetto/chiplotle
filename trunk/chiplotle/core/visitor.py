

class Visitor(object):
   
   def visit(self, node, *args, **kwargs):
      for cls in node.__class__.__mro__:
         meth_name = 'visit_' + cls.__name__
         meth = getattr(self, meth_name, None)
         if meth:
            break
      else:
         meth = self.visit_generic
      return meth(node, *args, **kwargs)


   def visit_generic(self, node, *args, **kwargs):
      print '*** In generic Visitor function.'
      print 'Node: %s' % node

