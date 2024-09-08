from typing import List


class Node:

    def __init__(self, val=None, childs=None, is_last=False):
        self.val = val
        self.childs = childs if childs else {}
        self.is_last = is_last

    def add_child(self, val):
        child = self.childs.get(val)
        if child:
            return child
        child = Node(val)
        self.childs[val] = child
        return child


class MySolution:
    def __init__(self):
        self.root = Node()
        self.board_cache = {}

    def create_prefix_tree(self, words):
        def rec(node, word):
            if not word:
                node.is_last = True
                return
            letter = word[0]
            child = node.add_child(letter)
            rec(child, word[1:])

        for word in words:
            rec(self.root, word)
        return

    def create_board_cache(self, board):
        self.X = len(board)
        self.Y = len(board[0])
        for x in range(self.X):
            for y in range(self.Y):
                val = board[x][y]
                if val not in self.board_cache:
                    self.board_cache[val] = []
                self.board_cache[val].append((x, y))
        return

    def find_word(self, node, x, y, visited, word):
        if (x, y) in visited:
            return False
        if x < 0 or x > self.X - 1:
            return False
        if y < 0 or y > self.Y - 1:
            return False
        if self.board[x][y] != node.val:
            return False
        if node.is_last:
            result = word + node.val
            if result not in self.results:
                self.results.append(result)
        for child in node.childs.values():
            self.find_word(child, x + 1, y, visited | {(x, y)}, word + node.val)
            self.find_word(child, x - 1, y, visited | {(x, y)}, word + node.val)
            self.find_word(child, x, y + 1, visited | {(x, y)}, word + node.val)
            self.find_word(child, x, y - 1, visited | {(x, y)}, word + node.val)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.create_board_cache(board)
        self.create_prefix_tree(words)
        self.results = []
        for node in self.root.childs.values():
            if node.val not in self.board_cache:
                continue
            for x, y in self.board_cache[node.val]:
                self.find_word(node, x, y, set(), '')
        return self.results


class BestSolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            # Get the letter at the current position on the board
            letter = board[x][y]
            # Traverse the trie to the next node
            cur = root[letter]
            # Check if the node has a word in it
            word = cur.pop('#', False)
            if word:
                # If a word is found, add it to the results list
                res.append(word)
            # Mark the current position on the board as visited
            board[x][y] = '*'
            # Recursively search in all four directions
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # Check if the next position is within the board and the next letter is in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            # Restore the original value of the current position on the board
            board[x][y] = letter
            # If the current node has no children, remove it from the trie
            if not cur:
                root.pop(letter)

        # Build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word

        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        # Initialize a list to store the results
        res = []

        # Traverse the board and search for words
        for i in range(m):
            for j in range(n):
                # Check if the current letter is in the trie
                if board[i][j] in trie:
                    dfs(i, j, trie)

        # Return the list of results
        return res


class OptimizedSolution:
    def __init__(self):
        self.root = Node()
        self.board_cache = {}

    def create_prefix_tree(self, words):
        def rec(node, word):
            if not word:
                node.is_last = True
                return
            letter = word[0]
            child = node.add_child(letter)
            rec(child, word[1:])

        for word in words:
            rec(self.root, word)
        return

    def find_word(self, node, x, y, visited, word):
        if (x, y) in visited:
            return False
        if node.is_last:
            result = word + node.val
            if result not in self.results:
                self.results.append(result)
        for child in node.childs.values():
            if x + 1 < self.X and self.board[x + 1][y] == child.val:
                self.find_word(child, x + 1, y, visited | {(x, y)}, word + node.val)
            if x - 1 > -1 and self.board[x - 1][y] == child.val:
                self.find_word(child, x - 1, y, visited | {(x, y)}, word + node.val)
            if y + 1 < self.Y and self.board[x][y + 1] == child.val:
                self.find_word(child, x, y + 1, visited | {(x, y)}, word + node.val)
            if y - 1 > -1 and self.board[x][y - 1] == child.val:
                self.find_word(child, x, y - 1, visited | {(x, y)}, word + node.val)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.X = len(board)
        self.Y = len(board[0])
        self.board = board
        self.create_prefix_tree(words)
        self.results = []
        for x in range(self.X):
            for y in range(self.Y):
                if board[x][y] in self.root.childs:
                    node = self.root.childs[board[x][y]]
                    self.find_word(node, x, y, set(), '')
        return self.results


if __name__ == '__main__':
    BestSolution().findWords(
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain"])
