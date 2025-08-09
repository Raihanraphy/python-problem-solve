class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)

        def backtrack(index, current_parts):
            # Base case: 4 parts formed and string fully consumed
            if len(current_parts) == 4:
                if index == n:
                    result.append(".".join(current_parts))
                return

            # Iterate through possible lengths for the current part (1 to 3 digits)
            for length in range(1, 4):
                if index + length > n:  # Check if substring goes beyond string length
                    continue

                part_str = s[index : index + length]
                
                # Validate the part
                if (len(part_str) > 1 and part_str[0] == '0') or int(part_str) > 255:
                    continue
                
                # Add part and recurse
                current_parts.append(part_str)
                backtrack(index + length, current_parts)
                current_parts.pop()  # Backtrack

        backtrack(0, [])
        return result
