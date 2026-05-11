class TimeMap:

    def __init__(self):
        self.hm = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.hm[key])-1

        if not self.hm[key] or timestamp < self.hm[key][l][0]:
            return ""

        if timestamp >= self.hm[key][r][0]:
            return self.hm[key][r][1]

        maxindex = -1
        while l <= r:
            m = (l+r)//2

            if self.hm[key][m][0] <= timestamp:
                maxindex = m
                l = m+1
            else:
                r = m-1

        return self.hm[key][maxindex][1] if maxindex != -1 else ""