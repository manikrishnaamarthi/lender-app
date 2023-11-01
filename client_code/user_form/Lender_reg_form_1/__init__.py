from ._anvil_designer import Lender_reg_form_1Template
from anvil import *

class Lender_reg_form_1(Lender_reg_form_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
