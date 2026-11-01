import datetime
import json

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
    def __init__(self, *, word, id, deck_id, pos_tag, meanings, phonetics, examples, familiarity = 0, times_seen = 0, times_correct = 0, times_wrong = 0, last_review = None, date_added = None):
        """Main Class for a Word"""

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
        self.__familiarity = familiarity
        self.__times_seen = times_seen
        self.__times_correct = times_correct
        self.__times_wrong = times_wrong
        self.__last_reviewed = datetime.datetime.fromisoformat(last_review) if last_review else None
        self.__date_added = datetime.datetime.fromisoformat(date_added) if date_added else datetime.datetime.now()

    def __repr__(self):
        return f"""
        Word: {self._word}
        ID: {self._id}, Deck ID: {self._deck_id}
        Phonetics: {self.__phonetics}, POS Tag: {self.__pos_tag}
        Meanings --- {self.__meanings}
        Examples --- {self.__examples}
        Current familiarity: {self.__familiarity}, Date Added: {self.__date_added}
        """

    def to_dict(self):
        """This method returns the dictionary format of word object. Basially the key value arrangement"""
        return {
                "id": self._id,
                "word": self._word,
                "deck_id": self._deck_id,
                "pos_tag": self.__pos_tag,
                "meanings": self.__meanings,
                "phonetics": self.__phonetics,
                "examples": self.__examples,
                "familiarity": self.__familiarity,
                "times_seen": self.__times_seen,
                "times_correct": self.__times_correct,
                "times_wrong": self.__times_wrong,
                "last_review": self.__last_reviewed.isoformat(),
                "date_added": self.__date_added.isoformat()
                }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


can = Word(id=1, deck_id=1, word='can', meanings=["sb's ability to do sth"], phonetics=None,pos_tag='modal',  examples=["He can lift 100Kgs of weight"])
print(can)


that_word = can.to_dict()

print(that_word)

print('------------------------------')

print(Word.from_dict(that_word))


json.dumps(that_word)
