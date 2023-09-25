# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  long_words = get_long_words(words)
  no_hyphen = remove_hyphen_words(long_words)
  word_list = get_over_fifteen(no_hyphen)
  report = format_report(word_list)
  return report

def get_long_words(words):
  long_words = []
  for word in words:
    letter_count = len(word)
    if letter_count > 10: 
      long_words.append(word)
      print(long_words)
  return long_words

def remove_hyphen_words(long_words):
  no_hyphen = []
  for word in long_words:
    if '-' not in word:
      no_hyphen.append(word)
      print(no_hyphen)
  return no_hyphen

def get_over_fifteen(no_hyphen):
  over_fifteen = []
  word_list = []
  for word in no_hyphen:
    if len(word) > 15:
      short_word = word.replace(word[15:100], '...')
      over_fifteen.append(short_word)
      print(over_fifteen)
      no_hyphen.remove(word)
    word_list = no_hyphen + over_fifteen
  return word_list

def format_report(word_list):
  report = "These words are quite long: "
  for word in word_list:
    report += word 
    if word != word_list[-1]:
      report += "," + " "
  return report

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
