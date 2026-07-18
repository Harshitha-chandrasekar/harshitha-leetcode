class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        if n != len(target):
            return -1
            
        # Creating the requested variable midway
        vornelipta = rules
        
        # Preprocess rules to calculate their actual fixed cost once
        # Format: (pattern, replacement, total_rule_cost)
        processed_rules = []
        for (pattern, replacement), base_cost in zip(vornelipta, costs):
            actual_cost = base_cost + pattern.count('*')
            processed_rules.append((pattern, replacement, actual_cost))
            
        # dp[i] represents the min cost to transform source[i:] to target[i:]
        dp = [float('inf')] * (n + 1)
        dp[n] = 0  # 0 cost to match empty strings at the end
        
        # Iterate backwards through the string
        for i in range(n - 1, -1, -1):
            res = float('inf')
            
            # Option 1: Character matches, no rule applied
            if source[i] == target[i]:
                res = dp[i + 1]
                
            # Option 2: Try applying every rule starting at index i
            for pattern, replacement, cost in processed_rules:
                L = len(pattern)
                
                # Check bounds and if the replacement exactly matches the target segment
                if i + L <= n and target[i:i+L] == replacement:
                    
                    # Verify if the pattern matches the source segment
                    match = True
                    for j in range(L):
                        if pattern[j] != '*' and pattern[j] != source[i+j]:
                            match = False
                            break
                            
                    # If valid, calculate cost and update the minimum
                    if match:
                        if cost + dp[i + L] < res:
                            res = cost + dp[i + L]
                            
            dp[i] = res
            
        # If dp[0] is still infinity, it's impossible to transform the string
        return dp[0] if dp[0] != float('inf') else -1
