# token bucket
# https://blog.compliiant.io/api-defense-with-rate-limiting-using-fastapi-and-token-buckets-0f5206fc5029

import datetime


class TokenBucketAlg:

    def __init__(self, rate, per):
        self.rate = rate
        self.per = per
        self._last_check = datetime.datetime.now()
        self.allowance = rate

    def add(self):
        now = datetime.datetime.now()
        if self.allowance < self.rate:
            tokens_add = (now - self._last_check).seconds * (self.rate / self.per)
            self.allowance = min(self.rate, self.allowance + tokens_add)
        self._last_check = now
        if self.allowance >= 1:
            self.allowance -= 1
            return True
        return False


if __name__ == '__main__':
    bucket = TokenBucketAlg(5.0, 8.0)
    for item in range(10):
        res = bucket.add()
        print(res)
