"""Main code for demo cube

Intended operation:

- Post temp and pressure at set times from the hour, every hour
  - Allow bogus values to be posted for testing at other times
- Otherwise listen continuously for beacon messages and post them immediately
- Check for code updates once every hour
"""
