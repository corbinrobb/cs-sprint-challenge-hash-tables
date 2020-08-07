#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    d = {}
    route = []

    for ticket in tickets:
        d[ticket.source] = ticket.destination

    cur = d['NONE']

    while cur != 'NONE':
        route.append(cur)
        cur = d[cur]
    route.append("NONE")
    return route
