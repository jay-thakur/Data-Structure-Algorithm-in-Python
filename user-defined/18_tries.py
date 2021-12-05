class Trie:
    head = {}
    
    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur: # then head
                cur[ch] = {}
            cur = cur[ch] # increment statement, make new node
        cur['*'] = True # denotes the Trie has this word as valid given word

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


dictionary = Trie()
dictionary.add("Hi")
dictionary.add("hello")

dictionary.search("hel")


