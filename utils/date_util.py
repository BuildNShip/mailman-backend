from datetime import datetime

import pytz


class DateUtil:

    @staticmethod
    def format_time(date_time: datetime) -> datetime:
        """
        Format and parse a datetime object.

        Parameters:
        - date_time (datetime): Input datetime object.

        Returns:
        - datetime: Parsed datetime object.
        """
        formatted_time = date_time.strftime("%Y-%m-%d %H:%M:%S%z")
        return datetime.strptime(formatted_time, "%Y-%m-%d %H:%M:%S%z")

    @staticmethod
    def get_current_utc_time() -> datetime:
        """
        Get the current UTC time as a formatted datetime object.

        Returns:
        - datetime: Current UTC time.
        """
        local_now = datetime.now(pytz.timezone("UTC"))
        return DateUtil.format_time(local_now)

    @staticmethod
    def get_user_timezone(request) -> pytz.timezone:
        """
        Get the user's timezone based on the request headers.

        Parameters:
        - request: Request object containing headers.

        Returns:
        - pytz.timezone: User's timezone.
        """
        default_timezone = pytz.timezone('UTC')

        user_timezone_str = request.headers.get('timezone')

        if user_timezone_str:
            try:
                user_timezone = pytz.timezone(user_timezone_str)
            except pytz.UnknownTimeZoneError:
                user_timezone = default_timezone
        else:
            user_timezone = default_timezone

        return user_timezone

    @staticmethod
    def format_timezone(timezone: str, date_time: datetime) -> str:
        """
        Format a datetime object in the user's timezone.

        Parameters:
        - request: Request object containing headers.
        - date_time (datetime): Input datetime object.

        Returns:
        - str: Formatted datetime string in the user's timezone.
        """
        return date_time.astimezone(timezone).strftime('%Y-%m-%d %I:%M %p')
