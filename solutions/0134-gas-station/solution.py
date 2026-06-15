class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        i = 0
        if sum(cost)>sum(gas):
            return -1
        current_tank = 0
        starting_station = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                current_tank = 0
                starting_station = i + 1
                
        return starting_station
