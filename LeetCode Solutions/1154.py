class Solution:
    def dayOfYear(self, date: str) -> int:
        from datetime import datetime
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        year = date_obj.year
        day_of_year = date_obj.timetuple().tm_yday
        return day_of_year
