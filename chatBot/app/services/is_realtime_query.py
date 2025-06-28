
  #check This query is related to real_estate or not
def is_realtime_query(query: str) -> bool:
 
    realtime_keywords = [
    "latest", "now", "today", "current", "breaking",
    "real-time", "live", "trending", "today's",
    "up-to-date", "just in", "fresh", "new", "recent",
    "as of now", "as of today", "real time", "this moment",
    "updated", "update", "latest update", "currently"]

    query_list = []
    word = ''
    for char in query:
        if char.isalnum():
            word += char
        else:
            if word:
                query_list.append(word.lower())
                word = ''

    if word:
        query_list.append(word.lower())

    for word in query_list:
        if word in realtime_keywords:
            return True

    return False
