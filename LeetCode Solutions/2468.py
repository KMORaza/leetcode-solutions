class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)

        def can_split(k):
            if k == 0:
                return False
            suffix_len = len(str(k)) + 3
            if suffix_len >= limit:
                return False

            total_available = 0
            digits = len(str(k))

            for d in range(1, digits + 1):
                start = 10 ** (d - 1) if d > 1 else 1
                end = min(10 ** d - 1, k)
                if start > end:
                    break
                suffix_per_part = d + len(str(k)) + 3
                if suffix_per_part >= limit:
                    return False
                total_available += (end - start + 1) * (limit - suffix_per_part)

            return total_available >= n

        for parts in range(1, n + 1):
            if can_split(parts):
                result = []
                msg_idx = 0
                for i in range(1, parts + 1):
                    suffix = f"<{i}/{parts}>"
                    available = limit - len(suffix)
                    segment = message[msg_idx:msg_idx + available]
                    result.append(segment + suffix)
                    msg_idx += available
                    if msg_idx >= n:
                        break
                return result

        return []