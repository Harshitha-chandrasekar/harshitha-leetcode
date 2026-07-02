from collections import defaultdict

class FreqStack:
    def __init__(self):
        # Maps the value to its current frequency
        self.freq_map = Counter()
        # Maps a frequency to a stack of values that have that frequency
        self.group_map = defaultdict(list)
        # Keeps track of the highest frequency right now
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increase the frequency of the value
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        
        # Update the max_freq if this value reached a new high
        if freq > self.max_freq:
            self.max_freq = freq
            
        # Add the value to the stack for this specific frequency
        self.group_map[freq].append(val)

    def pop(self) -> int:
        # Get the most recent value from the stack with the highest frequency
        val = self.group_map[self.max_freq].pop()
        
        # Decrease its frequency in our tracker
        self.freq_map[val] -= 1
        
        # If there are no more elements with this max frequency, lower the max_freq
        if not self.group_map[self.max_freq]:
            self.max_freq -= 1
            
        return val
