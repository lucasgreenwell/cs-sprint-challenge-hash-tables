#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    destinations = {}
    sources = {}
    route = [None] * length
    for ticket in tickets:
        if ticket.source is "NONE":
            route[0] = ticket.destination
        elif ticket.destination is None:
            route[length - 1] = ticket.source
        destinations[ticket.source] = ticket.destination
        sources[ticket.destination] = ticket.source
    place_we_are = route[0]
    for index in range(length):
        route[index] = place_we_are
        if place_we_are in destinations:
            place_we_are = destinations[place_we_are]
    return route
