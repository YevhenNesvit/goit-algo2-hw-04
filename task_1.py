from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str) or not pattern:
            raise TypeError(f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a non-empty string")

        def _collect_words_with_suffix(node, path, result):
            if node.value is not None and "".join(path).endswith(pattern):
                result.append("".join(path))
            for char, next_node in node.children.items():
                path.append(char)
                _collect_words_with_suffix(next_node, path, result)
                path.pop()

        result = []
        self._collect(self.root, [], result)
        return sum(1 for word in result if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(f"Illegal argument for has_prefix: prefix = {prefix} must be a non-empty string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
