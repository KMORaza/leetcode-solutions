class Solution:
    def digArtifacts(self, grid_size: int, treasures: list[list[int]], digs: list[list[int]]) -> int:
        excavated_sites = set()
        for site in digs:
            excavated_sites.add(self.generate_key(site[0], site[1]))
        return sum(1 for item in treasures if self.is_extractable(item, excavated_sites))
    def generate_key(self, x: int, y: int) -> int:
        return (x << 16) | y
    def is_extractable(self, item: list[int], excavated_sites: set) -> bool:
        for row in range(item[0], item[2] + 1):
            for col in range(item[1], item[3] + 1):
                if self.generate_key(row, col) not in excavated_sites:
                    return False
        return True