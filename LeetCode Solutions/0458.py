class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        pigs_needed = 0
        while (rounds + 1) ** pigs_needed < buckets:
            pigs_needed += 1
        return pigs_needed
def main():
    sol = Solution()
    print(sol.poorPigs(4, 15, 15))
    print(sol.poorPigs(4, 15, 30))
    print(sol.poorPigs(1000, 15, 30))
if __name__ == "__main__":
    main()
