# code-exercise

## Local Process validation

Based on user josevalim, user is public user meaning no auth is required however you should validate you can hit the users GitHub API address using a curl command: 
    `curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/users/josevalim`

Then focus on gathering events with another curl command:
    `curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/users/josevalim/events`

The steps above will be sure you can pull all the required info from the machine you are using. 

## Local Testing

Now to run python,** all tested on python3 (if previous version of python installed please remove "3").**

Please clone the whole repo to your machine

`git clone https://github.com/almcfarlane1878/code-exercise.git`

To avoid installing Python packages system-wide on consuming users machine, or pipeline in later step plesae use a virtual environment:
    
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate (could be path/to/venv_/**Scripts**_/activate if on windows)
    python3 -m pip install -r requirements.txt
    python3 app.py
    

## GitHub Actions

If the consuming users do not want to clone files or run Python, you can find a GitHub action in this repo. Select "Actions" tab above to trigger script without needing any infra or local setup.

    `1 - Open Actions Tab `
    `2 - Select "Python Application" workflow`
    `3 - Select "Run Workflow" -> "Main" branch`
    `4 - Open the manually trigger run,
    `5 - select "Run script" step, answer will be provided ![image](https://github.com/almcfarlane1878/code-exercise/assets/54910866/48c5fa76-aa5f-4d9e-aea8-28d2e1cac82c)`
   

## Future enhancements 
1 - Include token for auth (to ensure script works for users who are not public"
2 - Replace URL as var to pull other apis from github if needed
3 - Instead of hard-coded increments, could make a dictory and multiply at the end += 4, maybe something like - https://stackoverflow.com/questions/34693927/multiple-increment-operators-on-the-same-line-python#:~:text=You%20can%20create%20special%20function%20for%20it%3A%20def,value2%2C%20value3%20%3D%20inc%20%28value4%2C%20value1%2C%20value2%2C%20value3%29

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
