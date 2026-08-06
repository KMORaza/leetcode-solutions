class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        class SegmentTree:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (4 * n)
                self.lazy = [0] * (4 * n)

            def push(self, node, start, end):
                if self.lazy[node] != 0:
                    self.tree[node] += self.lazy[node] * (end - start + 1)
                    if start != end:
                        self.lazy[2 * node] += self.lazy[node]
                        self.lazy[2 * node + 1] += self.lazy[node]
                    self.lazy[node] = 0

            def update_range(self, node, start, end, l, r, val):
                self.push(node, start, end)
                if start > end or start > r or end < l:
                    return
                if start >= l and end <= r:
                    self.lazy[node] += val
                    self.push(node, start, end)
                    return
                mid = (start + end) // 2
                self.update_range(2 * node, start, mid, l, r, val)
                self.update_range(2 * node + 1, mid + 1, end, l, r, val)
                self.push(2 * node, start, mid)
                self.push(2 * node + 1, mid + 1, end)
                self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

            def query_range(self, node, start, end, l, r):
                if start > end or start > r or end < l:
                    return 0
                self.push(node, start, end)
                if start >= l and end <= r:
                    return self.tree[node]
                mid = (start + end) // 2
                return self.query_range(2 * node, start, mid, l, r) + self.query_range(2 * node + 1, mid + 1, end, l, r)

        n = len(s)
        seg_tree = SegmentTree(n)

        for start, end, direction in shifts:
            if direction == 1:
                seg_tree.update_range(1, 0, n - 1, start, end, 1)
            else:
                seg_tree.update_range(1, 0, n - 1, start, end, -1)

        result = []
        for i in range(n):
            shift_val = seg_tree.query_range(1, 0, n - 1, i, i)
            new_char_code = (ord(s[i]) - ord('a') + shift_val) % 26
            if new_char_code < 0:
                new_char_code += 26
            new_char = chr(new_char_code + ord('a'))
            result.append(new_char)

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for ch in word:
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                node.is_end = True

            def search(self, word):
                node = self.root
                for ch in word:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
                return node.is_end

        trie = Trie()
        trie.insert(''.join(result))

        def validate_result_string(res_str):
            if len(res_str) != n:
                return False
            for i in range(len(res_str)):
                if not ('a' <= res_str[i] <= 'z'):
                    return False
            return True

        final_result = ''.join(result)
        if validate_result_string(final_result):
            return final_result
        else:
            raise ValueError("Invalid result string generated")