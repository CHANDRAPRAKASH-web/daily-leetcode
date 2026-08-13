class ST:
    def __init__(self, s: str):
        self.n = len(s)
        self.st = [None] * (4 * self.n)
        self.build(0, self.n - 1, 1, s)

    def build(self, left, right, node, s):
        if left == right:
            # State structure: [prefix, suffix, best, left_char, right_char, length]
            self.st[node] = [1, 1, 1, s[left], s[left], 1]
            return self.st[node]

        mid = left + (right - left) // 2
        left_child = self.build(left, mid, node * 2, s)
        right_child = self.build(mid + 1, right, node * 2 + 1, s)

        self.st[node] = self.merge(left_child, right_child)
        return self.st[node]

    def merge(self, left, right):
        (lp, ls, lb, lc, lrc, llen) = left
        (rp, rs, rb, rlc, rrc, rlen) = right

        prefix = lp
        suffix = rs
        best = max(lb, rb)

        # If adjacent characters match across the boundary
        if lrc == rlc:
            best = max(best, ls + rp)
            if lp == llen:
                prefix = llen + rp
            if rs == rlen:
                suffix = rlen + ls

        return [prefix, suffix, best, lc, rrc, llen + rlen]

    def update(self, left, right, node, idx, val):
        if left == right:
            self.st[node] = [1, 1, 1, val, val, 1]
            return self.st[node]

        mid = left + (right - left) // 2
        if idx <= mid:
            self.update(left, mid, node * 2, idx, val)
        else:
            self.update(mid + 1, right, node * 2 + 1, idx, val)

        self.st[node] = self.merge(self.st[node * 2], self.st[node * 2 + 1])
        return self.st[node]


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        n = len(s)
        q = len(queryCharacters)
        st = ST(s)
        res = []

        for i in range(q):
            st.update(0, n - 1, 1, queryIndices[i], queryCharacters[i])
            # st.st[1][2] contains the 'best' max repeating segment length for the entire string
            res.append(st.st[1][2])

        return res