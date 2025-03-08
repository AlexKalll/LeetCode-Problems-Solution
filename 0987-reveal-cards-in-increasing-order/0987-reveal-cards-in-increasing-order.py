class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        q = deque()

        for card in deck:
            if q:
                curr = q.pop()
                q.appendleft(curr)
            
            q.appendleft(card)

        return list(q)