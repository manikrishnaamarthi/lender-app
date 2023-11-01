from ._anvil_designer import user_formTemplate
from anvil import *

class user_form(user_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
