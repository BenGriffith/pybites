from __future__ import annotations

import string

EOL_PUNCTUATION = ".!?"


class Document:
    def __init__(self) -> None:
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
            self.document_strings.append(f"{line}\n")
        else:
            self.document_strings.insert(index, f"{line}\n")

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

        merged_line = []
        for i in range(len(indices)):
            if i == 0:
                merged_line.append(self.document_strings[indices[i]].strip("\n"))
            else:
                merged_line.append(self.document_strings[indices[i]])

        if in_row and len(indices) > 1:
            self.document_strings[indices[0]] = " ".join(merged_line)
            self.document_strings.pop(indices[1])
        else:
            self.document_strings[0] = " ".join(merged_line)
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
        line = list(self.document_strings[index])
        if len(line) == 1:
            if line[0] == "\n":
                line.insert(0, punctuation)
        elif len(line) == 0:
            line.append(punctuation)
        elif len(line) > 1 and line[-2] not in EOL_PUNCTUATION:
            line.insert(-1, punctuation)
        else:
            line[0] = punctuation

        self.document_strings[index] = "".join(line)
        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        return len(self._remove_punctuation())

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""
        return self._remove_punctuation("unique")


    def _remove_punctuation(self, values = None):
        """Remove punctuation from a line. Return unique or non-unique structures."""
        words = []

        for line in self.document_strings:
            line = line.translate(str.maketrans("", "", EOL_PUNCTUATION + ","))

            for word in line.split(" "):
                if word == "\n" or word == "":
                    continue
                if word != "" and word[-1] in EOL_PUNCTUATION:
                    words.append(word[:len(word) -1].lower())
                else:
                    words.append(word.strip(",").lower())

        if values == "unique":
            return sorted([*set(word.strip("\n") for word in words)])
        else:
            return sorted(words)

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        line_count = 0
        for _ in self.document_strings:
            line_count += 1
        return line_count

    def __str__(self):
        """Return the content of the document as string."""
        content = ""
        for i in range(len(self.document_strings)):
            if i == len(self.document_strings) -1:
                line = self.document_strings[i].strip("\n")
                content += f"{line}"
            else:
                content += f"{self.document_strings[i]}"
        return content


if __name__ == "__main__":

    e = (
        # Document()
        # .add_line("This is the tale of a dwarf.")
        # .add_line("")
        # .add_line("A dwarf you ask?")
        # .add_line("Yes, a dwarf and not any dwarf, so you know!")
        Document().add_line("").swap_lines(0, 0).merge_lines([0]).add_punctuation(".", 0)
    )

    print(e)
    print(e.word_count())
    print(e.words)