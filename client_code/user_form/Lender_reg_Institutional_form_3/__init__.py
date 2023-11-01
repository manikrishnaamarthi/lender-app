from ._anvil_designer import Lender_reg_Institutional_form_3Template
from anvil import *

class Lender_reg_Institutional_form_3(Lender_reg_Institutional_form_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('user_form.Lender_reg_form_6')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
