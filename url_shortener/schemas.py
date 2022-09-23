# by Richi Rod AKA @richionline / falken20
# url_shortener/schemas.py

# Base models for API request and response bodies

from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str  # to store the URL that your shortened URL forwards to


class URL(URLBase):
    is_active: bool  # to deactivate shortened URLs
    clicks: int  # count how many times a shortened URL has been visited

    class Config:
        orm_mode: bool = True  # to work with a database model


class URLInfo(URL):
    #  You could also add the two strings url and admin_url to URL. But by
    # adding url and admin_url to the URLInfo subclass, you can use the data
    # in your API without storing it in your database.
    url: str
    admin_url: str
