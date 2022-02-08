"""

In this project, we use the hacker news site API to get the output of the top 5 most popular articles.

"""


from operator import itemgetter  # operator.itemgetter(n) constructs a callable that assumes a
# n iterable object (e.g. list, tuple, set) as input, and fetches the n-th element out of it.
import requests   # import requests this module provides a convenient means to request information from websites

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'  # creates an API call
r = requests.get(url)  # get the answer and store it in a variable
print(f"Status code: {r.status_code}")  # display response status

submission_ids = r.json()  # the response text is converted to a Python list,
# which stored in the variable submission_ids.
submission_dicts = []   # creates an empty list named submission_dicts to store dictionaries
for submission_id in submission_ids[:5]:  # the program sorts through the identifiers of the 5 most popular articles
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"  # issues a new API call for each article,
    # generating a URL with the current value submission_id
    r = requests.get(url)  # get the answer and store it in a variable
    print(f"id: {submission_id}\tstatus: {r.status_code}")  # display response status
    # so we can check if it was processed successfully
    response_dict = r.json()  # this variable stores the data received earlier

    submission_dict = {  # dictionary is created for the currently processed article
        'title': response_dict['title'],  # stores the title of the article
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",  # a link to the page with its discussion
        'comments': response_dict.get('descendants'),  # the number comments on the article
    }
    submission_dicts.append(submission_dict)  # each element of submission_dict is attached to list submission_dicts

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)  # it is required to sort the
# list of dictionaries by the number of comments. To do this, we use the itemgetter() function from
# operator module. We pass the 'comments' key to this function and it retrieves
# the value associated with the given key from each dictionary in the list. Function
# sorted() then uses that value to sort the list. We sort
# list in reverse order so that the publications with the most commentaries were in the first place.

for submission_dict in submission_dicts:  # we iterate over the elements
    print(f"\nTitle: {submission_dict['title']}")  # output title
    print(f"Discussion link: {submission_dict['hn_link']}")  # output link to talk page
    print(f"Comments: {submission_dict['comments']}")  # output current number of comments
