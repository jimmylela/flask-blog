
## Notes

Create GitHub repo <directory_name>, don't add README

$ mkdir <directory_name>
$ cd <directory_name>
$ python3 -m venv venv
$ source venv/bin/activate
$ git init
$ git branch -m main
$ cp ../README.md .
$ cp ../.gitignore .
$ git add -A
$ git commit -m "initial_commit"
$ git remote add origin https://github.com/jimmylela/<repo_name>.git
$ git push origin main


