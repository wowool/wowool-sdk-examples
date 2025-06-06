from wowool.sdk import LanguageIdentifier

document = """
Moi je dis: l'intelligence artificielle,
c'est bien sauf quand elle se met au service de la connerie naturelle
"""
# Initialize a language identification engine
lid = LanguageIdentifier()
# Process the data
doc = lid(document)
print(doc.language)
