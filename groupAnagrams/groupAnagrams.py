from collections import defaultdict

def groupAnagrams(strs):
    anagrams_group = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))
        anagrams_group[sorted_word].append(word)
    return list(anagrams_group.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

# How I solved it:
# 1. I used a defaultdict to group words by their sorted character representation.
# 2. For each word, I sorted the characters and used the sorted string as a key.
# 3. I appended the original word to the list corresponding to that key.
# 4. Finally, I returned the values of the defaultdict as a list of lists.
# Time Complexity: O(n * k log k), where n is the number of words and k is the maximum length of a word.
# Space Complexity: O(n * k), where n is the number of words and k is the maximum length of a word.