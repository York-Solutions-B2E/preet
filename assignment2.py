stopwords=["the","is" ,"at","which"]
def text_analyzer(input_text):
     words=input_text.split()
     num_words=len(words)
     longest_word = max(words, key=len)
     word_counts = {}
     for word in words:
          if word.lower() not in stopwords:
               word_counts[word]=word_counts.get(word,0) +1

     return num_words, longest_word, word_counts

input_text=("the city where she is living now is Arden Hills")
result=text_analyzer(input_text)
print(result)


     

    
