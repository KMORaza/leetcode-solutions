class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        def can_stamp(stamp_pos: int) -> bool:
            can_stamp = False
            for i in range(len(stamp)):
                if target[stamp_pos + i] != '*' and target[stamp_pos + i] != stamp[i]:
                    return False
                if target[stamp_pos + i] != '*':
                    can_stamp = True
            return can_stamp
        def stamp_at(stamp_pos: int) -> None:
            for i in range(len(stamp)):
                target[stamp_pos + i] = '*'
        stamp_len, target_len = len(stamp), len(target)
        target = list(target)
        result = []
        while True:
            stamped = False
            for i in range(target_len - stamp_len + 1):
                if can_stamp(i):
                    stamp_at(i)
                    result.append(i)
                    stamped = True
            if not stamped:
                break
        if all(c == '*' for c in target):
            return result[::-1]
        else:
            return []
