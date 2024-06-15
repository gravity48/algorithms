

class Solution:

    def transfer(self, mass):
        if len(mass) == 1:
            return
        count = 0
        mass = sorted(mass)
        pay = sum(mass)/len(mass)
        mass = list(map(lambda x: x - pay, mass))
        index1 = 0
        index2 = len(mass) - 1
        while index2 > index1:
            diff = mass[index2] + mass[index1]
            if diff == 0:
                index2 -= 1
                index1 += 1
            if diff < 0:
                mass[index2] = 0
                index2 -= 1
                mass[index1] = diff
            if diff > 0:
                mass[index1] = 0
                index1 += 1
                mass[index2] = diff
            count += 1
        return count


class Solution2:

    def transfer(self, mass):
        k = 0
        pay = sum(mass) / len(mass)
        mass = list(map(lambda x: x - pay, mass))

        def rec(mass, k):
            if len(mass) == 2:
                return k
            maximum = max(mass)
            minimum = min(mass)
            res = maximum + minimum
            mass.pop(mass.index(maximum))
            mass.pop(mass.index(minimum))
            if res:
                mass.append(res)
            return rec(mass, k + 1)

        res = rec(mass, k)
        return res


class Solution3:

    def transfer(self, mass):
        k = 0
        pay = sum(mass) / len(mass)
        mass = list(map(lambda x: x - pay, mass))

        def rec(mass, k, urav):
            if len(mass) == 1:
                return k
            if urav > 0:
                minimum = min(mass)
                mass.pop(mass.index(minimum))
                urav += minimum
            else:
                maximum = max(mass)
                mass.pop(mass.index(maximum))
                urav -= maximum
            k += 1
            return rec(mass, k, urav)
        urav = max(mass)
        mass.pop(mass.index(urav))
        rec(mass, k, urav)
        return k


if __name__ == '__main__':
    mass = [0, 500, 1200, 2300]
    Solution().transfer([5000, 500, 0, 0])
    Solution2().transfer([0, 500, 1200, 2300])
    Solution3().transfer([0, 500, 1200, 2300])