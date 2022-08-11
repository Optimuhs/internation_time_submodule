from datetime import datetime

from disnake.ext import commands


class InternationalTime(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """ discord member time
    short time = t
    short date = d
    long date = D
    long date with short time = f
    long date with day of week and short time = F
    relative = R

    <t:1653142980:R>


utc_timezone = commands.option_enum(
        {-12, -11, -10, -9, -8, -7, -6, -5, -4 -, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
    "-12", "-11", "-10", "-9", "-8", "-7", "-6", "-5", "-4" , "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"


    """
    utc_timezone = commands.option_enum(
        {"-3": -3, "-2": -2, "-1": -1, "0": 0, "1": 1, "2": 2, "3": 3})

    @commands.slash_command(
        description="create a timestamp to use in messages, so everybody gets to see dates and times in their local time")
    async def date(self, inter, day: int, month: int,
                   UTC: utc_timezone = -2, hours: commands.Range[0, 24] = 24, minutes: commands.Range[0, 60] = 0,
                   type: str = "X", year: int = 0):
        now = datetime.utcnow()
        print(str(now.tzinfo))

        aware_now = now.astimezone()
        server_utc_offset = aware_now.tzinfo.utcoffset(aware_now).seconds
        server_utc = int(server_utc_offset / 3600)

        print(str(aware_now.tzinfo))
        print(str(aware_now.tzinfo.utcoffset(aware_now)))
        print(str(aware_now.tzinfo.dst(aware_now)))
        print(server_utc)

        if type == "X":
            if hours == 24:
                type = "D"
                hours = 12
            else:
                type = "F"

        if year == 0:
            year = now.year

        print(str(hours))
        hours = hours + UTC + server_utc
        print(str(hours))
        print(str(day))
        if hours > 23:
            hours = hours - 24
            day = day - 1
        elif hours < 0:
            hours = hours + 24
            day = day - 1
        print(str(hours))
        print(str(day))
        date_time = datetime(year, month, day, hours, minutes)
        ts = str(int(date_time.timestamp()))
        await inter.response.send_message("copy/paste this              \<t:" + ts + ":" + type + ">" +
                                          "\nit will show as this         " + "<t:" + ts + ":" + type + ">" +
                                          "\n(date & time in viewer's timezone)")


def setup(bot: commands.Bot):
    bot.add_cog(InternationalTime(bot))
