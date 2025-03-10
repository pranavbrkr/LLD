from abc import ABC, abstractmethod

# Base game character
class Character(ABC):
  @abstractmethod
  def get_description(self):
    pass

  @abstractmethod
  def get_damage(self):
    pass


# Concrete component - base game character
class BasicCharacter(Character):
  def get_description(self):
    return "Basic Character"
  
  def get_damage(self):
    return 10


# Decorator - abstract decorator class
class CharacterDecorator(Character, ABC):
  def __init__(self, character):
    self._character = character

  @abstractmethod
  def get_description(self):
    pass

  @abstractmethod
  def get_damage(self):
    pass


# Concrete decorators
class DoubleDamageDecorator(CharacterDecorator):
  def get_description(self):
    return self._character.get_description() + " with Double Damage"

  def get_damage(self):
    return self._character.get_damage() * 2

class FireballDecorator(CharacterDecorator):
  def get_description(self):
    return self._character.get_description() + " with Fireball"

  def get_damage(self):
    return self._character.get_damage() + 20

class InvisibilityDecorator(CharacterDecorator):
  def get_description(self):
    return self._character.get_description() + " with Invisibility"

  def get_damage(self):
    return self._character.get_damage()
  

# Client
if __name__ == "__main__":
  character = BasicCharacter()
  print(character.get_description())
  print(character.get_damage())

  # Create different decorators
  double_damage_decorator = DoubleDamageDecorator(character)
  fireball_decorator = FireballDecorator(character)
  invisibility_decorator = InvisibilityDecorator(character)

  # Apply decorators individually
  print(double_damage_decorator.get_description())
  print(double_damage_decorator.get_damage())
  
  print(fireball_decorator.get_description())
  print(fireball_decorator.get_damage())
  
  print(invisibility_decorator.get_description())
  print(invisibility_decorator.get_damage())

  # Combine decorators
  double_fireball_character = DoubleDamageDecorator(FireballDecorator(character))
  print(double_fireball_character.get_description())
  print(double_fireball_character.get_damage())

  invisibility_double_fireball_character = InvisibilityDecorator(double_fireball_character)
  print(invisibility_double_fireball_character.get_description())
  print(invisibility_double_fireball_character.get_damage())