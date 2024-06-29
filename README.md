# code-exercise

## Local Testing

Based on user josevalim, user is public user so no auth required if replacing with another user be sure you can auth with a simple curl command.
    `curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/users/josevalim`

Then focus on gathering advice
    `curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/users/josevalim/events`

Steps above will be sure you can pull all the required info from the machine you are on

Now to run python, all tested on python3 (if previous verision please remove "3").
To avoid installing Python packages system-wide on consuming users machine, or pipeline in later step plesae use a virtual environment:
    
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install -r requirements.txt

## GitHub Actions

There is a GitHub action in this repo, select actions tab above to trigger script without needing any infra or local setup.
    `1 - Open Actions Tab `
    `2 - Select "Python Application" workflow`
    `3 - Select "Run Workflow" -> "Main" branch`
    `4 - Open the manually trigger run, select "Run script" step, answer will be provided`

## Future enhancements 
1 - Include token for Auth
2 - Replace URL as var to pull other apis from github
3 - Instead of hard-coded increments, could make a dictory and multipy at the end += 4, maybe something like - https://stackoverflow.com/questions/34693927/multiple-increment-operators-on-the-same-line-python#:~:text=You%20can%20create%20special%20function%20for%20it%3A%20def,value2%2C%20value3%20%3D%20inc%20%28value4%2C%20value1%2C%20value2%2C%20value3%29

4 - instead  of this big list of event types vars, dictoarys and scores, could dyanmicallly pull this?
    #EventTypes
    pull_request_event = "PullRequestEvent"
    push_event_type = "PushEvent"
    issue_comment_event = "IssueCommentEvent"

    #Scores
    score = {}
    other_events={}
    push_event_score = 0
    pull_request_event_score = 0
    issue_comment_event = 0

5 - run python test tools as part of PR / Merge
6 - Push to lambda (not enough value now, GitHub action can run the script well enough)

## Citation
https://docs.github.com/en/rest?apiVersion=2022-11-28
https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28
https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
https://stackoverflow.com/questions/22160424/how-to-add-multiple-values-to-a-list-in-one-line-in-python
