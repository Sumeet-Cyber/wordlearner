### Why choose hatchling over setuptools?
Because this is the first time I am building a python project with the intent to publish/share it online. I wanted to see how real world packages are built. And as I am just starting out, I wanted something easy to work with. Not everybody will agree with this, but I just wanted to keep the initial friction less. I do plan to get familiar with setuptools, as it is the one which legacy python packages use.

### Wrong Ans Penalty == Word Search Penalty
I always take these word lookups casually and think why should I remember when I can just look it up on internet. But the whole point of the app is to make user remember words and their meanings. So, I want the app to give a penalty on familiarity of the word user searches in the app. If the word is present in the app, then user should know its meaning, but the user is searching for the word means that he/she forgot the meaning, so, it is clear that word should appear more in quizzes.

### The Word Class
While creating the Word Class, I am presented with the choice of use a Plain class, or doing something more with dataclass. I choose the plain and simple option. While at first I researched about dataclass, I could see its many benefits, I also realized that it will similarly require more time and effort, which I am limited at the time.

### The starting index of decks and words
Both decks and index start with 1 and not 0, just a design choice and I will limit the number of words in a deck by 50.

### Attributes of Word Class
Okay, this can be confusing and I completely get it. Some Attributes of Word Class are private while others are protected. But the choice of which being private and others being protected doesn't seem to reflect any simple logic. Simply because I am inexperienced and for the time being, I would like to more forward. Once I get more familiar with which attributes need more attention and called the most, I will make necessary changes.
