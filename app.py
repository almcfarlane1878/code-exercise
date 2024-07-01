import requests

user = "josevalim"

url = f"https://api.github.com/users/{user}/events"
response = requests.get(url)
data = response.json()

#EventTypes
pull_request_event = "PullRequestEvent"
push_event_type = "PushEvent"
issue_comment_event = "IssueCommentEvent"
create_event_event = "CreateEvent"

#Scores
score = {}
other_events={}
pull_request_event_score = 0
push_event_score = 0
issue_comment_event_score = 0
create_event_score = 0

for item in data:
    event_type = item["type"]
    if event_type == pull_request_event:
        pull_request_event_score += 5
    elif event_type == push_event_type:
        push_event_score += 4
    elif event_type == issue_comment_event:
        issue_comment_event_score += 4
    elif event_type == create_event_event:
        create_event_score += 2
    else:
        if event_type in other_events:
            other_events[event_type] += 1
        else:
            other_events[event_type] = 1

event_scores = [pull_request_event_score, push_event_score, issue_comment_event_score, create_event_score]
other_events_score = sum(other_events.values())
total_score = sum(event_scores, other_events_score)

print(f"The user", user, "has a total scoe of", total_score)
