from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        temp = [0] * (len(words) + 1)
        for index, word in enumerate(words):
            temp[index + 1] = temp[index]
            if word[0] in vowels and word[-1] in vowels:
                temp[index + 1] += 1
        result = []
        for start, stop in queries:
            result.append(temp[stop + 1] - temp[start])
        return result


if __name__ == '__main__':
    query = ["bzmxvzjxfddcuznspdcbwiojiqf", "mwguoaskvramwgiweogzulcinycosovozppl",
             "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs", "uivcdsboxnraqpokjzaayedf", "yalc",
             "bbhlbmpskgxmxosft", "vigplemkoni", "krdrlctodtmprpxwditvcps", "gqjwokkskrb",
             "bslxxpabivbvzkozzvdaykaatzrpe", "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
             "siqbezhkohmgbenbkikcxmvz", "ddmaireeouzcvffkcohxus", "kjzguljbwsxlrd",
             "gqzuqcljvcpmoqlnrxvzqwoyas", "vadguvpsubcwbfbaviedr", "nxnorutztxfnpvmukpwuraen",
             "imgvujjeygsiymdxp", "rdzkpk", "cuap", "qcojjumwp", "pyqzshwykhtyzdwzakjejqyxbganow",
             "cvxuskhcloxykcu", "ul", "axzscbjajazvbxffrydajapweci"]
    Solution().vowelStrings(query, [[6, 17]])
