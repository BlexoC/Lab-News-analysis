import re
from collections import Counter


def extract_words(text: str) -> list[str]:
	"""Return lowercase words from text, ignoring punctuation."""
	return re.findall(r"[A-Za-z']+", text.lower())


def count_specific_word(text: str, word: str) -> int:
	"""Count how many times a specific word appears (case-insensitive)."""
	words = extract_words(text)
	return words.count(word.lower())


def most_common_word(text: str) -> tuple[str | None, int]:
	"""Return the most common word and its frequency."""
	words = extract_words(text)
	if not words:
		return None, 0

	word_counts = Counter(words)
	common_word, frequency = word_counts.most_common(1)[0]
	return common_word, frequency


def average_word_length(text: str) -> float:
	"""Compute the average word length."""
	words = extract_words(text)
	if not words:
		return 0.0

	total_length = sum(len(word) for word in words)
	return total_length / len(words)


def count_paragraphs(text: str) -> int:
	"""Count paragraphs separated by one or more blank lines."""
	paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
	return len(paragraphs)


def count_sentences(text: str) -> int:
	"""Count sentences ending in ., !, or ?."""
	sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
	return len(sentences)


def analyze_text(text: str, target_word: str) -> dict:
	"""Run all required analysis tasks and return the results."""
	common_word, common_count = most_common_word(text)

	return {
		"target_word": target_word,
		"target_word_count": count_specific_word(text, target_word),
		"most_common_word": common_word,
		"most_common_word_count": common_count,
		"average_word_length": average_word_length(text),
		"paragraph_count": count_paragraphs(text),
		"sentence_count": count_sentences(text),
	}


if __name__ == "__main__":
	news_article = """AI adoption is accelerating in many industries. Startups are using NLP to analyze customer feedback and news data.

Teams rely on text analysis to discover trends, risks, and opportunities. Better insights help leaders make faster decisions."""

	word_to_check = "news"
	results = analyze_text(news_article, word_to_check)

	print("News Text Analysis Results")
	print("-" * 32)
	print(f"Count of '{results['target_word']}': {results['target_word_count']}")
	print(
		f"Most common word: {results['most_common_word']} "
		f"({results['most_common_word_count']} times)"
	)
	print(f"Average word length: {results['average_word_length']:.2f}")
	print(f"Paragraphs: {results['paragraph_count']}")
	print(f"Sentences: {results['sentence_count']}")
