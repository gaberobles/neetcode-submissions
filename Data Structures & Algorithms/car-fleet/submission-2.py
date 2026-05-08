class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleets = 0
        while cars:
            fleetArrival = (target-cars[-1][0])/cars[-1][1]
            cars.pop()
            while cars and (target-cars[-1][0])/cars[-1][1] <= fleetArrival:
                cars.pop()
            fleets += 1
        return fleets