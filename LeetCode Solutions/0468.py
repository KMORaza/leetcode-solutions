import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(ipv4):
            parts = ipv4.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if len(part) > 1 and part[0] == '0':
                    return False
                if not (0 <= int(part) <= 255):
                    return False
            return True
        def is_valid_ipv6(ipv6):
            parts = ipv6.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) < 1 or len(part) > 4:
                    return False
                if not all(c in '0123456789abcdefABCDEF' for c in part):
                    return False
            return True
        if '.' in queryIP:
            if is_valid_ipv4(queryIP):
                return "IPv4"
        elif ':' in queryIP:
            if is_valid_ipv6(queryIP):
                return "IPv6"
        return "Neither"
