class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_hour, login_minute = map(int, loginTime.split(':'))
        logout_hour, logout_minute = map(int, logoutTime.split(':'))
        login_minutes = login_hour * 60 + login_minute
        logout_minutes = logout_hour * 60 + logout_minute
        if logout_minutes < login_minutes:
            logout_minutes += 24 * 60
        login_minutes = (login_minutes + 14) // 15 * 15
        if login_minutes > logout_minutes:
            return 0
        return (logout_minutes - login_minutes) // 15
