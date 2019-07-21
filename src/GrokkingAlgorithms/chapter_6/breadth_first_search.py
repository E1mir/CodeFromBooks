from collections import deque

# graph = {
#     "you": ["alice", "bob", "claire", ],
#     "bob": ["anuj", "peggy", ],
#     "alice": ["peggy", ],
#     "claire": ["thom", "jonny", ],
#     "anuj": [],
#     "peggy": [],
#     "thom": [],
#     "jonny": []
# }


graph = dict()
graph["you"] = ["alice", "bob", "claire", ]
graph["bob"] = ["anuj", "peggy", ]
graph["alice"] = ["peggy", ]
graph["claire"] = ["thom", "jonny", ]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("{} is a mango seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    breadth_first_search("you")
