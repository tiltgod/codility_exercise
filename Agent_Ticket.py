from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        raise NotImplemented


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented
