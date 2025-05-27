from collections import defaultdict

def groupAnagrams(strs):
    anagrams_group = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))
        anagrams_group[sorted_word].append(word)
    return list(anagrams_group.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

