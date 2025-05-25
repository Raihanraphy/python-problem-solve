class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if item == "..":
                if len(stack)>0:
                    stack.pop()
            elif item == ".":
                continue
            else:
                if item != '':
                    stack.append(item)
        if len(stack)==0:
            return "/"
        return "/" + "/".join(stack)
