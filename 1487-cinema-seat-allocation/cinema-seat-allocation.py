from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Bitmasks representing the 4-seat blocks (for seats 2 to 9)
        # Left block:   seats 2, 3, 4, 5 -> 0b11110000 (0xF0)
        # Right block:  seats 6, 7, 8, 9 -> 0b00001111 (0x0F)
        # Middle block: seats 4, 5, 6, 7 -> 0b00111100 (0x3C)
        left_mask = 0b11110000
        right_mask = 0b00001111
        middle_mask = 0b00111100
        
        occupied_rows = defaultdict(int)
        
        # Build bitmask for each row containing reserved seats
        for row, seat in reservedSeats:
            # Ignore seats 1 and 10 as they are not part of any 4-person group
            if seat in (1, 10):
                continue
            # Map seats 2..9 to bit indices 0..7
            occupied_rows[row] |= (1 << (9 - seat))
            
        # Empty rows can each fit 2 groups
        ans = (n - len(occupied_rows)) * 2
        
        # Check non-empty rows for at most 1 group
        for reserved_mask in occupied_rows.values():
            if (reserved_mask & left_mask) == 0:
                ans += 1
            elif (reserved_mask & right_mask) == 0:
                ans += 1
            elif (reserved_mask & middle_mask) == 0:
                ans += 1
                
        return ans