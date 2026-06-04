class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in ("(", "{", "["):
                st.append(char)
            elif char in (")", "}", "]"):
                if not st:
                    return False
                if char == ")" and st.pop() != "(":
                        return False
                elif char == "}" and st.pop() != "{":
                        return False
                elif char == "]" and st.pop() != "[":
                        return False
                else:
                    continue
        if st:
            return False
        return True


        