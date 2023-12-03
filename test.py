""" git test & time op. """
from datetime import datetime, timezone

print("test python")

__utctime__ = datetime.now(tz=timezone.utc)
__loctime__ = __utctime__.astimezone(datetime.utcnow().astimezone().tzinfo)
print(f'{"ORGformat":<10}:', __utctime__)
print(f'{"isoformat":<10}:', __utctime__.isoformat())
print(f'{"loacl"    :<10}:', __loctime__)
print(f'{"iso loacl":<10}:', __loctime__.isoformat())
