
from chiplotle.interfaces.interface import _Interface

class ParentageInterface(_Interface):
   def __init__(self, _client):
      _Interface.__init__(self, _client)
      self.__parent = None

   ## PROPERTIES ##

   @property
   def parent(self):
      return self.__parent


   ## PRIVATE METHODS ##

   def _cut(self):
      '''Cut all ties with parent.'''
      self._cut_from_parent( )
      self._cut_parent( )

   def _cut_from_parent(self):
      '''Remove client from parent.'''
      client, parent = self._client, self.parent
      if parent is not None:
         parent._shapes.remove(client)

   def _cut_parent(self):
      '''Set parent of client to None.'''
      self.__parent = None

   def _switch(self, new_parent):
      '''Remove client from parent and give client to new parent.'''
      self._cut( )
      self.__parent = new_parent
