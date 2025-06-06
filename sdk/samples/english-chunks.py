from wowool.sdk import Pipeline

text = """# List of Authors and Their Books

## J.R.R. Tolkien

J.R.R. Tolkien was an English writer, poet, and professor known for his high fantasy works. He created the richly detailed world of Middle-earth, a place inhabited by hobbits, elves, dwarves, and orcs.

### The Hobbit

- Published: 1937
- Genre: Fantasy
- **Abstract**: 
  *The Hobbit* is a classic tale of adventure and self-discovery. Bilbo Baggins, a reluctant hobbit, is recruited by the wizard Gandalf and a group of thirteen dwarves to help them reclaim their homeland and treasure from the fearsome dragon Smaug. Along the way, Bilbo encounters trolls, goblins, giant spiders, and a mysterious creature named Gollum. The novel explores themes of bravery, friendship, and the unexpected heroism that lies within ordinary individuals. This book also serves as a prelude to *The Lord of the Rings*, setting up the history of Middle-earth.

### The Lord of the Rings
- Published: 1954
- Genre: Epic Fantasy
- **Abstract**: 
  *The Lord of the Rings* is a monumental epic fantasy trilogy that follows the journey of Frodo Baggins as he attempts to destroy the One Ring, a powerful artifact created by the dark lord Sauron. The ring grants immense power but also corrupts those who possess it. With the help of friends like Samwise Gamgee, Aragorn, Gandalf, and others, Frodo travels across Middle-earth, facing tremendous challenges and internal struggles. The novel delves into themes of good versus evil, the corrupting influence of power, and the importance of hope and perseverance in the face of overwhelming odds. Tolkien's world-building and intricate mythology make this one of the most beloved and influential works of fantasy literature.

## George Orwell

George Orwell was an English novelist, essayist, and critic whose works often focused on social issues, particularly those related to politics, totalitarianism, and personal freedoms. Orwell's keen insights into human nature and government have made his works enduringly relevant.

### 1984
- Published: 1949
- Genre: Dystopian, Political Fiction
- **Abstract**: 
  *1984* is a chilling portrayal of a dystopian future where the government, led by the omnipresent Big Brother, controls every aspect of life. Citizens are constantly watched through telescreens, and any hint of rebellion or independent thought is ruthlessly suppressed by the Thought Police. The novel follows Winston Smith, a low-ranking government employee who becomes disillusioned with the oppressive regime and secretly longs for freedom. Orwell's work explores themes such as the dangers of totalitarianism, the manipulation of truth, and the loss of individual identity. The novel remains a powerful critique of oppressive governments and the dangers of surveillance and propaganda.

### Animal Farm
- Published: 1945
- Genre: Allegory, Satire
- **Abstract**: 
  *Animal Farm* is an allegorical novella that uses a group of farm animals to represent the events leading up to the Russian Revolution of 1917 and the subsequent rise of the Soviet Union. The animals, led by the pigs Napoleon and Snowball, overthrow their human farmer in a bid for equality and freedom. However, as time goes on, the pigs become indistinguishable from the humans they replaced, and the farm’s original ideals are betrayed. Orwell uses the fable to critique the corruption of socialist ideals and the rise of totalitarianism, demonstrating how power can corrupt even the most well-intentioned leaders. The famous line, \"All animals are equal, but some animals are more equal than others,\" captures the central theme of the story.
"""
pipeline = Pipeline(
    [
        "english",
        "entity",
        "topics",
        "semantic-theme",
        {
            "name": "chunks.app",
            "options": {
                "add_outline": True,
                "add_themes": True,
                "add_topics": True,
                "header_level": 3,
                "canonicalize": True,
                "cleanup": True,
                "lowercase": True,
                "fix_spelling_mistakes": True,
            },
        },
    ]
)
document = pipeline(text)

for chunk in document.chunks:
    print("Offsets:", chunk.begin_offset, chunk.end_offset)
    print("Outline:", chunk.outline)
    print("Themes:", chunk.themes)
    print("Topics:", chunk.topics)
    print("Sentences:")
    for sentence in chunk.sentences:
        print("  ", sentence)

    print("-" * 30)
