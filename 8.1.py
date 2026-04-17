"""1. Удалите ключи ["name", "salary"] из sample_dict.
sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
     "salary": 8000,
    "city": "New york"
}

print("до удаления: ", sample_dict)

sample_dict.pop('name')
sample_dict.pop('salary')

print("после удалеения: ", sample_dict)
