class Solution:
    def isNStraightHand(self, hand, groupSize):
        frequency = Counter(hand)
        hand.sort()
        for card in hand:
            if frequency[card] > 0:
                for current_card in range(card, card + groupSize):
                    if frequency[current_card] <= 0:
                        return False
                    frequency[current_card] -= 1
        return True