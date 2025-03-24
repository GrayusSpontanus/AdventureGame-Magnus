class Character:
  def __init__(self, name):
      self.name = name
      self.health = 50
      self.fear = 5
      self.inventory = []
      self.marks = []


  def __str__(self):
      return f"{self.name}\nHealth: {self.health}\nFear: {self.fear}"

