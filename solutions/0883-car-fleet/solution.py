class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posspe = [[position[i],speed[i]] for i in range(len(speed))]
        posspe.sort(reverse=True)
        time = []
        for p,s in posspe:
            time.append((target-p)/s)

        stack =[]

        for t in time:
            if not stack:
                stack.append(t)
            if t>stack[-1]:
                stack.append(t)

        return len(stack)
