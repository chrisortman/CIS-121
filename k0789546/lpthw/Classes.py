class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
word = ["Happy birhtday to you","I don't want to get sued",
                    "So I'll stop right there"]     
word2 = ["They rally around the family",
                        "With pockets full of shells"]
happy_bday = Song(word)
                    
bulls_on_parade = Song(word2)
                        
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()