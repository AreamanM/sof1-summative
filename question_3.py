TRUMP_SUIT_RANKING = {
    "Jack": 20, "9": 14, "Ace": 11, "10": 10,
    "King": 4, "Queen": 3, "8": 0, "7": 0,
}

NON_TRUMP_SUIT_RANKING = {
    "Jack": 2, "9": 0, "Ace": 11, "10": 10,
    "King": 4, "Queen": 3, "8": 0, "7": 0,
}

VALID_SUITS = {"Spades", "Diamonds", "Hearts", "Clubs"}


def trick_score(trick: set[tuple[str, str]], trump_suit: str) -> int:
    """Calculate the score of a trick.
    
    Args:
     trick: A list of cards of length 4.
     trump_suit: The suit that will use a different points system
       for calculation of points for a given `trick`.

    Returns:
      The score of the specificed trick.

    Raises:
      TypeError: If `trump_suit` is not a valid suit.
      ValueError: If `trump_suit` is not a valid suit or an invalid
        card is in `trick`.
    """
    if trump_suit not in VALID_SUITS:
        raise TypeError(f"Invalid trump suit: {trump_suit}.")

    if len(trick) != 4:
        raise ValueError("Expected 4 cards in trick.")

    total_score = 0
    for rank, suit in trick:

        if suit not in VALID_SUITS:
            raise ValueError(f"Invalid suit: {suit}.")

        if TRUMP_SUIT_RANKING.get(rank) == None:
            raise ValueError(f"Invalid rank: {rank}.")
        
        total_score += compute_score_for_card((rank, suit), trump_suit)

    return total_score


def compute_score_for_card(card: tuple[str, str], trump_suit: str) -> int:
    """Calculate the score for a card.
    
    Args:
     card: A tuple containing its rank and suit in order.
     trump_suit: The suit that will use a different points system
       for calculation of points for a given `card`.

    Returns:
      The score of the specificed card.
    """
    rank, suit = card
    if suit == trump_suit:
        return TRUMP_SUIT_RANKING[rank]
    return NON_TRUMP_SUIT_RANKING[rank]
