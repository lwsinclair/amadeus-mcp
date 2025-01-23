from mcp.server.fastmcp import FastMCP
from amadeus import Client
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('amadeus_mcp.log')
    ]
)
logger = logging.getLogger('amadeus_mcp')

mcp = FastMCP("amadeus-flight-search")

amadeus = Client(
    client_id=os.getenv('AMADEUS_API_KEY'),
    client_secret=os.getenv('AMADEUS_API_SECRET'),
    hostname='test'  # Use test environment
)

@mcp.tool()
async def search_flights(origin: str, destination: str, date: str) -> str:
    """Search for flights using the Amadeus API."""
    try:
        logger.info(f"Searching flights: {origin} to {destination} on {date}")
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=1,
            currencyCode="USD"
        )
        
        flights = []
        for offer in response.data[:5]:
            segments = offer['itineraries'][0]['segments']
            for segment in segments:
                flights.append(
                    f"Flight: {segment['carrierCode']} {segment['number']}\n"
                    f"From: {segment['departure']['iataCode']}\n"
                    f"To: {segment['arrival']['iataCode']}\n"
                    f"Departure: {segment['departure']['at']}\n"
                    f"Arrival: {segment['arrival']['at']}\n"
                    f"Price: ${float(offer['price']['total']):.2f}\n"
                )
        
        return "\n---\n".join(flights) if flights else "No flights found"
        
    except Exception as e:
        logger.error(f"Error searching flights: {str(e)}")
        return f"Error searching flights: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')