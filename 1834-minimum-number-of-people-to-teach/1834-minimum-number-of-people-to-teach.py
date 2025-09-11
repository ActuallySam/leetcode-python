class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need = set()

        for u1, u2 in friendships:
            u1 -= 1
            u2 -= 1
            can_communicate = False

            for l1 in languages[u1]:
                if l1 in languages[u2]:
                    can_communicate = True
                    break
            
            if not can_communicate:
                need.add(u1)
                need.add(u2)
        
        ans = len(languages) + 1
        for language in range(1, n + 1):
            count = 0
            for user in need:
                if language not in languages[user]:
                    count += 1
            ans = min(ans, count)

        return ans