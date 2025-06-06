# This sample script processes sentences from a text file using the Wowool SDK,
# focusing on extracting and preparing text from each sentence with linguistic normalization.
# Takes a Sentence object and returns a processed string.
# Skips punctuation, determiners, conjunctions, prepositions, and adverbs.
# Can use either the stem or literal form of tokens, depending on parameters.
# For concepts (like named entities), it tries to use their canonical form.
# Handles noun/verb phrases by collecting their stems.
# ----------------------------------------------------------------------------------------------
# Usage: python english-rag-sentences.py <file_descriptor>
# ----------------------------------------------------------------------------------------------
from wowool.sdk import Pipeline
from wowool.document import Document
from wowool.annotation import Sentence, Token, Concept
from typing import cast
from pathlib import Path


GUESSER_PROPERTIES = {"cleanup", "guess", "typo"}


def get_pos(annotation):
    return annotation.pos.split("-")[0]


def prepare_text(sentence: Sentence, stem: bool = False, spelling: bool = True) -> str:
    """
    replace the literal or the stem by there canonical.

    :param sentence: the sentence to be converted.
    :type obj: Sentence
    :param stem: replace using the stem or the literal.
    :type stem: bool

    :rtype: str
    """

    output = ""
    skip_until_offset = 0
    annotation_count = len(sentence.annotations)
    prev_token = None
    for annotation_idx in range(annotation_count):
        annotation = sentence.annotations[annotation_idx]
        if annotation.begin_offset < skip_until_offset:
            prev_token = annotation
            continue
        else:
            skip_until_offset = 0

        if annotation.is_token:
            token = cast(Token, annotation)
            # skip the token if it is a punctuation, determiner, conjunction or preposition or adverb
            pos = get_pos(token)
            if pos in ["Punct", "Det", "Conj", "Prep", "Adv"]:
                continue
            if prev_token:
                # insert space if required.
                if prev_token.end_offset != token.begin_offset:
                    output += " "
            if stem:
                output += token.stem
            elif spelling and bool(GUESSER_PROPERTIES.intersection(token.properties)):
                # use the stem only it it's not guessed.
                output += token.stem
            else:
                # use the literal
                output += token.literal

            prev_token = token

        elif annotation.is_concept:
            # A Concept is a Entity like a Person, Location, Organization
            concept = cast(Concept, annotation)
            if "canonical" in concept.attributes:
                if prev_token:
                    if prev_token.end_offset != concept.begin_offset:
                        output += " "
                output += concept.attributes["canonical"][0]
                skip_until_offset = concept.end_offset
            elif concept.uri in ["NP", "VP"]:
                # collection the stem for Noun Phrase or Verb Phrase and
                # skipping "Punct", "Det", "Conj", "Prep", "Adv" inside the VP or NP
                for tk in concept.tokens:
                    pos = get_pos(tk)
                    if pos in ["Punct", "Det", "Conj", "Prep", "Adv"]:
                        continue

                    if prev_token:
                        if prev_token.end_offset != tk.begin_offset:
                            output += " "
                    output += tk.stem
                    prev_token = tk
                skip_until_offset = concept.end_offset

    return output


def main(file_descriptor: Path):
    """
    Main function to run the pre-sentence processing.

    :param file: The input file containing sentences.
    :type file: str
    """
    if not file_descriptor.exists():
        raise FileNotFoundError(f"File not found: {file_descriptor}")

    pipeline = Pipeline("english,entity")
    for input_provider in Document.glob(file_descriptor):
        doc = pipeline(input_provider)
        # print(f"Processing document: {doc}")

        for sentence in doc.sentences:
            processed_text = prepare_text(sentence, stem=True)
            print("-", processed_text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No file descriptor provided. Using default: english-default.txt")
        fn = Path(__file__).parent / "english-default.txt"
        main(fn)
    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Usage: python pre-sentence.py <file_descriptor>")
            print("Example: python pre-sentence.py english-default.txt")
            sys.exit(0)
        fn = Path(sys.argv[1])
        main(fn)
