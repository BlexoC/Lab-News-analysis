import re


def extract_words(text: str) -> list[str]:
    if text is None:
        return []

    return re.findall(r"[A-Za-z']+", text.lower())


def count_specific_word(text: str, word: str) -> int:
    words = extract_words(text)
    if not word:
        return 0

    target = word.lower()
    count = 0
    for current in words:
        if current == target:
            count += 1
    return count


def identify_most_common_word(text: str) -> str | None:
    words = extract_words(text)
    if not words:
        return None

    frequency: dict[str, int] = {}
    order: list[str] = []
    for current in words:
        if current not in frequency:
            frequency[current] = 0
            order.append(current)
        frequency[current] += 1

    most_common = None
    highest_count = 0
    for current in order:
        current_count = frequency[current]
        if most_common is None or current_count > highest_count:
            most_common = current
            highest_count = current_count
    return most_common


def calculate_average_word_length(text: str) -> float:
    words = extract_words(text)
    if not words:
        return 0.0

    total_length = 0
    for current in words:
        total_length += len(current)
    return total_length / len(words)


def count_paragraphs(text: str) -> int:
    if not text or not text.strip():
        return 0

    paragraphs: list[str] = []
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.strip() == "":
            if current_lines:
                paragraphs.append("\n".join(current_lines))
                current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        paragraphs.append("\n".join(current_lines))

    return len(paragraphs)


def count_sentences(text: str) -> int:
    if not text or not text.strip():
        return 0

    count = 0
    i = 0
    while i < len(text):
        if text[i] in ".!?":
            count += 1
            while i + 1 < len(text) and text[i + 1] in ".!?":
                i += 1
        i += 1
    return count
