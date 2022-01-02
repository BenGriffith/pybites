from __future__ import annotations

import string

EOL_PUNCTUATION = ".!?"


class Document:
    def __init__(self) -> None:
        # it is up to you how to implement this method
        # feel free to alter this method and its parameters to your liking
        self.document_strings = []

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        if index == None:
            self.document_strings.append(line)
        else:
            self.document_strings.insert(index, line)

        return self

    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        temp_index = self.document_strings[index_two]
        self.document_strings[index_two] = self.document_strings[index_one]
        self.document_strings[index_one] = temp_index
        return self

    def merge_lines(self, indices: list) -> Document:
        """Merge several lines into a single line.

        If indices are not in a row, the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        in_row = True

        for i in range(len(indices) -1):
            if i == 0:
                continue
            difference = indices[i] - indices[i -1]
            if difference != 1:
                in_row = False

        merged_line = ""
        removed_line = []
        for i in indices:
            merged_line += self.document_strings[i]
            removed_line.append(self.document_strings[i])

        while len(removed_line) > 0:
            self.document_strings.remove(removed_line.pop())

        if in_row:
            self.document_strings.append(merged_line)
        else:
            self.document_strings[0] = merged_line        
        return self


    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """
        line = self.document_strings[index]
        new_line = line[:len(line)]
        self.document_strings[index] = new_line + punctuation
        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        return sum([len(line.split(" ")) for line in self.document_strings])

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""
        unique_words = set()

        for line in self.document_strings:

            for word in line.split(" "):
                if word == "":
                    continue

                if word != "" and word[-1] in EOL_PUNCTUATION:
                    unique_words.add(word[:len(word) -1].lower())
                else:
                    unique_words.add(word.lower())

        return sorted([*unique_words])

    def _remove_punctuation(line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        pass

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        line_count = 0
        for line in self.document_strings:
            line_count += 1
        return line_count

    def __str__(self):
        """Return the content of the document as string."""
        content = ""
        for line in self.document_strings:
            content += line
        return content


if __name__ == "__main__":

    d = (
        Document()
        .add_line("My second sentence.")
        .add_line("My first sentence.")
        .swap_lines(0, 1)
        .add_line("Introduction", 0)
        .add_punctuation("!", 0)
        .add_line("")
        .add_line("My second paragraph.")
        .merge_lines([1, 2])
    )

    #print(d)
    #print(len(d))
    print(d.word_count())
    print(d.words)