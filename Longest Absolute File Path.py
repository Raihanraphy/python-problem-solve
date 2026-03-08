class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # depth 0 has length 0

        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1  # add '/' length

        return max_len
