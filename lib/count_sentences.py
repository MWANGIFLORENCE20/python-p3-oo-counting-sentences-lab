#!/usr/bin/env python3

class MyString:
  def __init__(self):
    self._value=None

  def get_value(self):
    return self._value

  def set_value(self,new_value):
  
      if not isinstance(new_value,str):
         print("The value must be a string.")

      else:
         self._value = new_value

  def is_sentence(self):
    if self.value.endswith('.'):
            return True
    else:
            return False

        
  value=property(get_value,set_value)

