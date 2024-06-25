from difflib import get_close_matches,SequenceMatcher

def closeMatches(patterns,word):
    print(get_close_matches(word,patterns))

if __name__ == '__main__':
    word = 'monkey'
    patterns = ['money','apple','kevin','monkey']
    closeMatches(patterns,word)
