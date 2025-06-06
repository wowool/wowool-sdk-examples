from wowool.sdk import LanguageIdentifier

document = """
La juventud no es más que un estado de ánimo.

Record de chaleur battu dans une cinquantaine de villes en France

"""
# Initialize a language identification engine
lid = LanguageIdentifier(sections=True, section_data=True)
# Process the data
doc = lid(document)
if lid_results := doc.lid:
    for section in doc.lid.sections:
        assert section.text
        print(
            f"({section.begin_offset},{section.end_offset}): language= {section.language} text={section.text[:20].strip('\n')}..."
        )
