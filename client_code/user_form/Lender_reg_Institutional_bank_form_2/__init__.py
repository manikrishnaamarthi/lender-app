from ._anvil_designer import Lender_reg_Institutional_bank_form_2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_bank_form_2(Lender_reg_Institutional_bank_form_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('user_form.Lender_reg_Institutional_bank_form_1')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    alert("Institutional Registration Completed!")
    open_form("user_form.Dashboard")
    """This method is called when the button is clicked"""
    
