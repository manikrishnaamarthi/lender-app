from ._anvil_designer import user_formTemplate
from anvil import *

class user_form(user_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form('user_form.Lender_reg_form_1')
    """This method is called when the button is clicked"""
    
