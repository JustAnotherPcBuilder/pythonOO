from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary"""
    def __init__(self, path):
        self.words = []
        self.read_file(path)
        print( f'{len(self.words)} words read')

    def read_file(self, path):
        """Reads the lines of a specified path and places them into the words list"""
        with open(path, 'r') as file:
            for line in file:
                self.words.append(line.strip())
            
    def random(self):
        """Returns a random word from the word list"""
        return self.words[randint(0,len(self.words) - 1 )]

class RandomWordFinder(WordFinder):
    # def __init__(self, path):
    #     super().__init__(path)
    
    def read_file(self, path):
        """Reads lines from a file, but ignors comments (starting with #) and empty lines"""
        with open(path, 'r') as file:
            for line in file:
                splt = line.split('#')
                if len(splt) > 1:
                    #read words that are before comments, but not after in the same line
                    if splt[0]:
                        self.words.append(splt[0])
                else: 
                    #splt is just a single word; not a comment, just add if not empty line
                    if line.strip():
                        self.words.append(line.strip())