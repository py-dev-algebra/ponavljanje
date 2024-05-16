from typing import List, Dict


class Address:
    def __init__(self, 
                 street: str,
                 postal_code: str,
                 city: str,
                 country: str) -> None:
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return f'{self.street}\n{self.postal_code} {self.city}\n{self.country}'
    
    def __repr__(self) -> str:
        return f'{self.street}\n{self.postal_code} {self.city}\n{self.country}'