# utils/actor.py
class Actor:
    def __init__(self, name: str):
        self.name = name
        self.abilities = {}

    def can(self, ability):
        self.abilities[ability.__class__.__name__] = ability
        return self

    def ability_to(self, ability_cls):
        return self.abilities[ability_cls.__name__]

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)

    def should_see_that(self, question):
        assert question.answered_by(self)
