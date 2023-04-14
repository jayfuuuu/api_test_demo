
from datetime import datetime
from typing import Any, Optional

from dateutil.relativedelta import relativedelta


class Time:

    @staticmethod
    def now() -> datetime:
        """Return the current datetime.

        Returns:
            datetime: Current datetime.
        """
        return datetime.now()

    @staticmethod
    def relative_time(
        time: Any = None, year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None,
        hour: Optional[int] = None, minute: Optional[int] = None, second: Optional[int] = None,
        microsecond: Optional[int] = None, years: int = 0, months: int = 0, days: int = 0, hours: int = 0,
        minutes: int = 0, seconds: int = 0, microseconds: int = 0
    ) -> datetime:
        """Return a datetime which applied the relativedelta.

        Args:
            time (Any, optional): Specified time. Defaults to Now.
            year (Optional[int], optional): Absolute year information. Defaults to None.
            month (Optional[int], optional): Absolute month information. Defaults to None.
            day (Optional[int], optional): Absolute day information. Defaults to None.
            hour (Optional[int], optional): Absolute hour information. Defaults to None.
            minute (Optional[int], optional): Absolute minute information. Defaults to None.
            second (Optional[int], optional): Absolute second information. Defaults to None.
            microsecond (Optional[int], optional): Absolute microsecond information. Defaults to None.
            years (int, optional): Relative year information. Defaults to 0.
            months (int, optional): Relative month information. Defaults to 0.
            days (int, optional): Relative day information. Defaults to 0.
            hours (int, optional): Relative hour information. Defaults to 0.
            minutes (int, optional): Relative minute information. Defaults to 0.
            seconds (int, optional): Relative second information. Defaults to 0.
            microseconds (int, optional): Relative microsecond information. Defaults to 0.

        Returns:
            datetime: Relative time.
        """
        given_time = time or datetime.now()
        delta = relativedelta(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            microseconds=microseconds
        )
        return given_time + delta
