from ._anvil_designer import Lender_reg_individual_bank_form_2Template
from anvil import *

class Lender_reg_individual_bank_form_2(Lender_reg_individual_bank_form_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('user_form.Lender_reg_individual_bank_form_1')
    

  def button_2_click(self, **event_args):
    alert("Individual Lendor registration Compelted!")
    open_form("user_form.Dashboard")
    """This method is called when the button is clicked"""
    
