record1 = """{"customer": {"last": "Ross", "first": "Bob"}}"""
record2 = """{"customer": {"entity": "Steve's Painting Co."}}"""


import json
from dataclasses import dataclass


@dataclass
class PersonCustomer:
    first_name: str
    last_name: str


@dataclass
class BusinessCustomer:
    company_name: str


def deserialize_if(data):
    record = json.loads(data)

    if "customer" in record:
        inner = record["customer"]

        if "last" in inner and "first" in inner:
            return PersonCustomer(inner["first"], inner["last"])
        elif "entity" in inner:
            return BusinessCustomer(inner["entity"])

    raise ValueError("Unknown record type")


print(deserialize_if(record1))
print(deserialize_if(record2))


def deserialize_match(data):
    record = json.loads(data)

    match record:
        case {"customer": {"last": last, "first": first}}:
            return PersonCustomer(first, last)
        case {"customer": {"entity": company}}:
            return BusinessCustomer(company)
        case _:
            raise ValueError("Unknown record type")


print(deserialize_match(record1))
print(deserialize_match(record2))
