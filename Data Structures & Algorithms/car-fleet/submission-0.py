class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        p_time = 0.0
        ct = 0
        for c,s in cars:
            c_t = (target-c)/s
            if(c_t > p_time):
                p_time = c_t
                ct += 1
        return ct