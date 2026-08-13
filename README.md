# GitHub User Activity CLI

A simple command-line application built with Python that uses the GitHub API to fetch and display recent activity from a GitHub user.

This project was created to practice working with APIs, JSON data, loops, conditional statements, user input, and command-line applications.

## Features

* Enter any GitHub username.
* Fetch recent GitHub activity using the GitHub API.
* Display event types.
* Display repository information.
* Display event payload information.
* Continue checking other users without restarting the program.
* Clear the terminal before starting another search.

## Requirements

* Python 3.x
* `requests` library
* Internet connection

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/github-user-activity.git
cd github-user-activity
```

Install the required Python package:

```bash
pip install requests
```

## Usage

Run the Python program:

```bash
python main.py
```

The program will display:

```text
== GitHub User Activity ==
Github Username:
identify github account [type or repo or payload]:
```

Enter a GitHub username and choose what information you want to see.

### Type

Enter:

```text
type
```

This displays the type of each GitHub event.

Example:

```text
PushEvent
CreateEvent
IssuesEvent
WatchEvent
```

### Repo

Enter:

```text
repo
```

This displays the repository information associated with each event.

### Payload

Enter:

```text
payload
```

This displays the payload data associated with each event.

Payload information can contain additional details about what happened during the event.

## How It Works

The program sends a request to the GitHub Events API:

```python
URL = f"https://api.github.com/users/{githubUsername}/events"
r = requests.get(URL)
events = r.json()
```

The API returns JSON data containing the user's recent public GitHub events.

The program then loops through the events and displays the requested information:

```python
if options == "type".lower():
    for event in events:
        print(event["type"])
```

The program supports three options:

* `type` — displays the event type.
* `repo` — displays repository information.
* `payload` — displays event payload information.

## Technologies Used

* Python
* Requests
* GitHub REST API
* JSON
* Command Line Interface (CLI)

## What I Learned

Through this project, I practiced:

* Making HTTP requests with Python.
* Using an API.
* Working with JSON data.
* Accessing values inside Python dictionaries.
* Using `for` loops.
* Using `if`/`elif`/`else` statements.
* Getting input from users.
* Creating a simple CLI application.
* Handling invalid commands.
* Repeating a program with a `while` loop.

## Future Improvements

Possible improvements for this project include:

* Add error handling for usernames that don't exist.
* Handle GitHub API errors.
* Display cleaner repository names.
* Create readable messages for different event types.
* Add more command options.
* Add an option to quit the program.
* Make the program work on both Windows and Linux/macOS terminal commands.

## Project Goal

The goal of this project is to build a simple CLI that allows a user to retrieve and inspect recent GitHub activity from the terminal while practicing fundamental Python programming and API concepts.
