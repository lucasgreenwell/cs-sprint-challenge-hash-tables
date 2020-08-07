#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = [None] * length
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
        if ticket.source is None:
            route[0] = ticket.destination
        elif ticket.destination is None:
            route[length - 1] = ticket.source

    return route
