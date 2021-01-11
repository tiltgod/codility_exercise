from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        for i in range(len(agents)):
            if agents[i].load >= 3:
                agents.pop(agents[i])
        return agents

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented

class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented
