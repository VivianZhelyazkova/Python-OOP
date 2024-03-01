from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people: List[Person] = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([f'{x.name} {x.surname}' for x in self.people])}"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.people):
            raise StopIteration
        current_person = self.people[self.index]
        current_index = self.index
        self.index += 1
        return f"Person {current_index}: {current_person.name} {current_person.surname}"

    def __getitem__(self, key):
        current_person = self.people[key]
        return f"Person {key}: {current_person.name} {current_person.surname}"


