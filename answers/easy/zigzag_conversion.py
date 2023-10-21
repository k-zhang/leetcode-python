class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        group_size = 1 if num_rows * 2 - 2 == 0 else num_rows * 2 - 2
        n = len(s)
        group_base_index = list(range(0, n, group_size))

        res = []
        for i in range(num_rows):
            for base_index in group_base_index:
                index_of_char1 = base_index + i
                if index_of_char1 < n:
                    selected = s[index_of_char1]
                    res.append(selected)

                if i != 0 and i != num_rows - 1:
                    index_of_char2 = base_index + 2 * (num_rows - 1) - i
                    if index_of_char2 < n:
                        res.append(s[index_of_char2])

        return ''.join(res)
