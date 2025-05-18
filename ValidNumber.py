class Solution:
    def check_float(self, s: str) -> bool:
        parts = s.split(".")
        len_parts = len(parts)

        if len_parts > 2:
            return False
        else:
            part1 = parts[0]

            if len(part1) > 0 and (part1[0] == "-" or part1[0] == "+"):
                part1 = part1[1:]
            
            if len_parts == 1:
                return part1.isdigit()
            else:
                part2 = parts[1]
                
                if len(part1) == 0 and len(part2) == 0:
                    return False

                return ('0' + part1).isdigit() and ('0' + part2).isdigit()
        

    def check_int(self, s: str) -> bool:
        if len(s) > 0 and (s[0] == "-" or s[0] == "+"):
            s = s[1:]
        
        return s.isdigit()

    def isNumber(self, s: str) -> bool:
        s = s.lower()
        parts = s.split("e")

        if len(parts) > 2:
            return False
        else:
            if not self.check_float(parts[0]):
                return False
            
            if len(parts) == 2 and not self.check_int(parts[1]):
                return False
            
        return True
