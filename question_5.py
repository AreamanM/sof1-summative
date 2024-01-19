import copy


class GameObject:
    """Represents an object in the French game Bazar Bizzare.

    Attributes:
      shape: Shape of the object.
      colour: Colour of the object.
    """

    def __init__(self, shape: str, colour: str) -> None:
        """Initialises GameObject with the specified shape and colour."""
        self._shape = shape
        self._colour = colour
        pass

    @property
    def shape(self):
        return self._shape

    @property
    def colour(self):
        return self._colour

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GameObject):
            return NotImplemented
        return self.shape == other.shape and self.colour == other.colour

    def __hash__(self) -> int:
        return hash((self.shape, self.colour))

    def __repr__(self) -> str:
        return f"({self.shape}, {self.colour})"


class GameCard:
    """Represents a card in the French game Bazar Bizzare.

    Attributes:
      content: List of 2 elements containing 2 objects on the card.
    """

    def __init__(self, obj1: GameObject, obj2: GameObject) -> None:
        """Initialises GameCard with the specified objects."""
        self._content = [copy.copy(obj1), copy.copy(obj2)]

    @property
    def content(self):
        return copy.deepcopy(self._content)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GameCard):
            return NotImplemented
        return self.content[0] in other.content and self.content[1] in other.content

    def __hash__(self) -> int:
        return hash((self.content[0], self.content[1]))

    def __repr__(self) -> str:
        # wrote this for debugging
        return f"<{self.content[0]}, {self.content[1]}>"


class CardDeck:
    """Represents a deck of cards in the French game Bazar Bizzare."""

    def __init__(self, pieces: list[GameObject]) -> None:
        """Initialises CardDeck with the specified wooden pieces.

        Arguments:
          pieces:
            list of pieces containing between 3 and 5 elements
            where no 2 objects share the same colour or shape.
        """
        if len(pieces) > 5 or len(pieces) < 3:
            raise ValueError("Expected between 3 and 5 objects.")

        # ensure there are no duplicates
        for i, obj1 in enumerate(pieces):
            for j, obj2 in enumerate(pieces):
                if i == j:
                    continue
                if obj1.colour == obj2.colour or obj1.shape == obj2.shape:
                    raise ValueError("All objects are not unique.")
        
        self._pieces = pieces


    def generate_deck(self):
        """Generate a possible list of cards for the deck."""
        valid_cards = []

        colours = list(map(lambda x: x.colour, self._pieces))
        shapes = list(map(lambda x: x.shape, self._pieces))

        all_possible_cards = []
        # generate all possible cards
        #
        # this is terribly inefficient and should never make it to
        # production
        for s1 in shapes:
            for s2 in shapes:
                if s1 == s2:
                    continue
                for c1 in colours:
                    obj1 = GameObject(s1, c1) 
                    for c2 in colours:
                        if c1 == c2:
                            continue
                        obj2 = GameObject(s2, c2) 
                        card = GameCard(obj1, obj2)
                        all_possible_cards.append(card)

        # extract valid cards from all possible cards
        #
        # this part is what is likely wrong in my solution
        for card in all_possible_cards:
            obj1, obj2 = card.content
            if obj1 in self._pieces and obj2 not in self._pieces:
                if obj1.colour != obj2.colour and obj2.shape != obj1.shape:
                    valid_cards.append(card)
            elif obj1 not in self._pieces and obj2 in self._pieces:
                if obj1.colour != obj2.colour and obj2.shape != obj1.shape:
                    valid_cards.append(card)
            elif obj1 not in self._pieces and obj2 not in self._pieces:
                if obj1.colour != obj2.colour and obj2.shape != obj1.shape:
                    valid_cards.append(card)

        # finally, remove duplicates
        for i, c1 in enumerate(valid_cards.copy()):
            for j, c2 in enumerate(valid_cards.copy()):
                if i == j:
                    continue
                if c1.content[0] == c2.content[1] and c1.content[1] == c2.content[0]:
                    valid_cards.remove(c1)


        return valid_cards
