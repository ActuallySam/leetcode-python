class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        st, num_st = [], deque()
        ch_list = [""] * n
        vowels = "aeiouAEIOU"
        for idx, ch in enumerate(s):
            if ch not in vowels:
                ch_list[idx] = ch
            else:
                st.append(ch)
        
        for ch in st:
            num_st.append(ord(ch))

        sorted_list = sorted(list(num_st))
        # Reconstruct the deque
        sorted_deque = deque(sorted_list)

        for idx, ch in enumerate(ch_list):
            if not ch:
                ch_list[idx] = chr(sorted_deque.popleft())

        return "".join(ch_list)
            