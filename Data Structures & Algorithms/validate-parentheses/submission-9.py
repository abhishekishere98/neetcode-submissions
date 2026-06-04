class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in ("(", "{", "["):
                st.append(char)
            elif char in (")", "}", "]"):
                if len(st) == 0:
                    return False
                if char == ")":
                    if st.pop() != "(":
                        return False
                elif char == "}" :
                    if  st.pop() != "{":
                        return False
                elif char == "]":
                    if st.pop() != "[":
                        return False
                else:
                    continue
        if len(st) != 0:
            return False
        return True


        