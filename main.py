from scraper import Scraper
from export import Export
# Searched offer type, type parameter from the right side of equal sign
# Apartment = mieszkanie
# Studio apartment = kawalerka
# House = dom
# Investments = inwestycja
# Rooms = pokoj
# Plots = dzialka
# Commercial premises = lokal
# Halls and warehouses = haleimagazyny
# Garages = garaz

type_of_search = "kawalerka"


# Offer type
# Rent = wynajem
# Sale = sprzedaz
offer_type = "wynajem"

# Price from
price_range_from = "1500"
# Price to
price_range_to = "2500"

# City name
city = "warszawa"


# In what range from the city
# 0 means show offers only from exact city
# Accepted parameters (in km)
# 0 5 10 15 25 50 75
radius = "0"

# If not relevant, leave blank
# Square footage from
square_footage_from = ""
# Square footage to
square_footage_to = ""

URL = f"https://www.otodom.pl/pl/oferty/{offer_type}" \
      f"/{type_of_search}" \
      f"/{city}" \
      f"?distanceRadius={radius}" \
      f"&priceMin={price_range_from}" \
      f"&priceMax={price_range_to}" \
      f"&areaMin={square_footage_from}" \
      f"&areaMax={square_footage_to}" \
      f"&by=DEFAULT&direction=DESC&viewType=listing&limit=72"

print(URL)
scraper = Scraper(URL, type_of_search)
data = scraper.scrape()
export = Export(data, type_of_search)
export.to_excel()
