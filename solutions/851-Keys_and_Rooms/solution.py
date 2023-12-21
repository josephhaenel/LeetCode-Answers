'''
Time Complexity: O(N)
Space Complexity: O(N)
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlockedRooms, stack = set(), list()

        if rooms[0]: # True if rooms[0] is not an empty list
            stack.append((0,rooms[0])) # (Room #, Keys in Room)

        while stack: # True while stack is not empty
            room, keys = stack.pop()
            unlockedRooms.add(room)
            for key in keys:
                if key not in unlockedRooms:
                    stack.append((key, rooms[key]))
        
        return len(rooms) == len(unlockedRooms)


        

