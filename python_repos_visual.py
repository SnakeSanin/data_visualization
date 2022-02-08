"""

This project uses the github API
to get a list of the most rated projects by stars for the python language and builds a bar chart

"""

import requests  # import requests this module provides a convenient means to request information from websites
from plotly.graph_objects import Bar  # import a class for building a bar chart
from plotly import offline  # import the module offline to display the map

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # API call url stored in url variable
headers = {'Accept': 'application/vnd.github.v3+json'}  # GitHub is using the third version
# API, so headers are defined to call the API
r = requests.get(url, headers=headers)  # the requests module is used to call
print(f'Status code: {r.status_code}')  # prints the value of status_code
# so we can verify that the call was processed successfully


response_dict = r.json()  # API returns information in JSON format, so the program uses the json() method
repo_dicts = response_dict['items']  # to get a first idea of the information returned for each
# repository, the program retrieves the first element from repo_dicts and saves it in repo_dict
repo_links, stars, labels = [], [], []  # create empty lists for our data
for repo_dict in repo_dicts:  # loop through all dictionaries in repo_dicts
    repo_name = repo_dict['name']  # to get a first idea of the information returned for each repository,
    # the program retrieves the first element from repo_dicts and saves it in repo_dict
    repo_url = repo_dict['html_url']  # we extract the project url from repo_dict
    # and assign it to temporary variable repo_url
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  # project link is generated
    # For this using an HTML anchor tag of the form <a href='URL'>link text</a>
    repo_links.append(repo_link)  # link is attached to the repo_links list
    stars.append(repo_dict['stargazers_count'])  # number of stars join the list

    owner = repo_dict['owner']['login']  # extract the owner's nickname
    description = repo_dict['description']  # extract project description
    label = f"{owner}<br />{description}"  # plotly allows you to use HTML markup in text elements,
    # so we'll generate text for the label with a line break (<br />)
    # between the project owner's name and the description
    labels.append(label)  # the label is stored in the labels list

data = [{  # the list data is defined and contains a dictionary

    'type': 'bar',  # type chart
    'x': repo_links,  # values by x axis contains links to the project
    'y': stars,  # value by y axis contains the number of stars
    'hovertext': labels,  # value extracts labels
    'marker': {  # the marker settings affect the appearance of the columns
        'color': 'rgb(60, 100, 150)',  # assign columns blue color
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}  # specify they should have a gray border 1.5 pixels thick.
    },
    'opacity': 0.6  # columns are set to opacity 0.6
}]

my_layout = {  # chart layout is defined using a dictionary
    'title': 'Most-Starred Python Projects on Girhub',  # the title of the entire chart
    'titlefont': {'size': 28},  # general title font size diagrams
    'xaxis': {'title': 'Repository',  # name of axis x
              'titlefont': {'size': 24},  # size of font title
              'tickfont': {'size': 14}  # size of font tick marks
              },
    'yaxis': {'title': 'Stars',  # name of axis y
              'titlefont': {'size': 24},  # size of font title
              'tickfont': {'size': 14}  # size of font tick marks
              }
}

fig = {'data': data, 'layout': my_layout}   # create a dictionary named fig containing data and layout
offline.plot(fig, filename='python_repos.html')  # fig is passed to the plot()
# function with a meaningful filename to output the data
