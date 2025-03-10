from abc import ABC, abstractmethod

# Defining the product
class Localizer(ABC):
  @abstractmethod
  def localize(self, msg):
    pass


# Creating concrete products
class FrenchLocalizer(Localizer):
  def __init__(self):
    self.translations = {
      "car": "voiture",
      "bike": "bicyclette",
      "cycle": "cyclette"
    }

  def localize(self, msg):
    return self.translations.get(msg, msg)

class SpanishLocalizer(Localizer):
  def __init__(self):
    self.translations = {
      "car": "coche",
      "bike": "bicicleta",
      "cycle": "ciclo"
    }

  def localize(self, msg):
    return self.translations.get(msg, msg)

class EnglishLocalizer(Localizer):
  def localize(self, msg):
    return msg


# Define creator
def create_localizer(language = "English"):
  localizers = {
    "French": FrenchLocalizer,
    "Spanish": SpanishLocalizer,
    "English": EnglishLocalizer,
  }
  return localizers[language]()

if __name__ == "__main__":
  french_localizer = create_localizer("French")
  spanish_localizer = create_localizer("Spanish")
  english_localizer = create_localizer("English")

  message = ["car", "bike", "cycle"]

  for msg in message:
    print(french_localizer.localize(msg))
    print(spanish_localizer.localize(msg))
    print(english_localizer.localize(msg))