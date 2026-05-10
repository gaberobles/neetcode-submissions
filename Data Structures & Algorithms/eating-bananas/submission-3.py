class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = 1
        maxk = max(piles)
        res = maxk+1

        while mink <= maxk:
            midk = (mink+maxk)//2

            hours = 0
            for bananas in piles:
                if midk >= bananas:
                    hours += 1
                else:
                    hours += math.ceil(bananas/midk)
            
            if res == midk:
                return res
            elif hours > h:
                mink = midk+1
            else:
                maxk = midk-1
                res = min(res, midk)
        return res