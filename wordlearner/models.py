import datetime

# Custom Error classes --- start
class Error(Exception):
    pass

class MeaningException(Error):
    pass
class IdException(Error):
    pass
class DeckIdException(Error):
    pass
class WordException(Error):
    pass
class ExampleException(Error):
    pass

# Custom Error Classes ---- End

# Word Class 
class Word:
    def __init__(self, *, word, id, deck_id, pos_tag, meanings, phonetics, examples):
        if id is None or id < 1: raise IdException('Id of Word should be a Positive number')
        elif deck_id is None or deck_id < 1: raise DeckIdException('The given Deck ID should be a Positive number')
        elif not word: raise WordException('Cannot Create Word Object without specifying the word itself!')
        elif not meanings: raise MeaningException('Enter at Least One meaning for the word')
        elif not examples: raise ExampleException('Enter at Least One example Sentence for the word')
        if not phonetics: phonetics = ''
        if not pos_tag: pos_tag = ''

        self._id = id
        self._word = word
        self._deck_id = deck_id
        self.__pos_tag = pos_tag
        self.__meanings = meanings
        self.__phonetics = phonetics
        self.__examples = examples
        self.__familiarity = 0
        self.__times_seen = 0
        self.__times_correct = 0
        self.__times_wrong = 0
        self.__last_reviewed = None
        self.__date_added = datetime.datetime.now()

    def __repr__(self):
        return f"""
        Word: {self._word}
        ID: {self._id}, Deck ID: {self._deck_id}
        Phonetics: {self.__phonetics}, POS Tag: {self.__pos_tag}
        Meanings --- {self.__meanings}
        Examples --- {self.__examples}
        Current familiarity: {self.__familiarity}, Date Added: {self.__date_added}
        """


# can = Word(id=1, deck_id=1, word='can', meanings=["sb's ability to do sth"], phonetics=None,pos_tag='modal',  examples=["He can lift 100Kgs of weight"])
# print(can)
