from craigslist import CraigslistHousing
from slackclient import SlackClient
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
import time
import settings

engine = create_engine("sqlite:///listings.db", echo=False)

Base = declarative_base()

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    geotag = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    name = Column(String)
    price = Column(Float)
    location = Column(String)
    cl_id = Column(Integer, unique=True)
    area = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_listing(result, price):
    return Listing(
            link=result["url"],
            created=parse(result["datetime"]),
            name=result["name"],
            price=price,
            location=result["where"],
            cl_id=result["id"],
            area=result["area"]
        )


def query_for_listing(result):
    return session.query(Listing).filter_by(cl_id=result["id"]).first()


def extract_price(result):
    price = 0
    try:
        price = float(result["price"].replace("$", ""))
    except Exception:
        pass

    return price

def check_in_box(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False

def filter_results(results):
    filtered_results=[]

    for result in results:
        listing = query_for_listing(result)
        if listing is None:
            if result["where"]:
                for hood in settings.NEIGHBORHOODS:
                    if hood in result["where"].lower():
                        result["area"] = result["where"]
                        filtered_results.append(result)

            price = extract_price(result)
            listing = create_listing(result, price)

            session.add(listing)
            session.commit()

    filtered_results = {r['url']:r for r in filtered_results}.values()
    return filtered_results

def init_craigslist():
    return CraigslistHousing(
        site=settings.CRAIGSLIST_SITE,
        area='sfc',
        category=settings.CRAIGSLIST_HOUSING_SECTION,
        filters={
            'max_price':settings.MAX_PRICE,
            'min_price':settings.MIN_PRICE,
            'min_bedrooms':4,
            'max_bedrooms':5,
            'min_bathrooms':1,
            'max_bathrooms':4
        }
    )

def post_to_slack(sc, result):
        desc = "{0} | {1} | {2} | <{3}>".format(
            result["area"], result["price"], result["name"], result["url"])

        print desc

        sc.api_call(
            "chat.postMessage", channel=settings.SLACK_CHANNEL, text=desc,
            username='aptbot', icon_emoji=':robot_face:'
        )


def scrape():

    cl = init_craigslist()

    results = cl.get_results(sort_by='newest', geotagged=True, limit=200)

    filtered_results = filter_results(results)

    sc = SlackClient(settings.SLACK_TOKEN)

    for result in filtered_results:
        post_to_slack(sc, result)
