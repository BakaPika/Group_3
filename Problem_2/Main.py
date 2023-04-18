from collections import Counter
from YoutubeTags import videotags
import webbrowser

link = "https://www.youtube.com/watch?v=-0fUAaeDnQM&ab_channel=TechBurner" # Use https / http Links
variable_name = videotags(link)
resultant_variable_name = variable_name.replace(",", "")
print(resultant_variable_name)

split_it = resultant_variable_name.split()
print(split_it)

Counter = Counter(split_it)

print(Counter)

index = list(Counter.keys())

query = index[0], index[1], index[3]
SEARCH_QUERY = "+".join(query)
webbrowser.open(f"https://www.youtube.com/results?search_query={SEARCH_QUERY}")


