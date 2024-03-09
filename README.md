# Readme

i
### Environments

- [Python](https://www.python.org/): 3.12
- [tiktoken](https://pypi.org/project/tiktoken/): 0.6.0
- [python-dotenv](https://pypi.org/project/python-dotenv/): 1.0.1
- [numpy](https://numpy.org/): 1.26.4
- [matplotlib](https://matplotlib.org/): 3.8.3
- [openai](https://pypi.org/project/openai/): 1.13.3
- [sentence-transformers](https://pypi.org/project/sentence-transformers/): 2.5.1

### Installation

1. Installing packages

   ```bash
   poetry install
   ```

### Usage

#### Start deployment server



### Basic Branch Operation Rules

- Work is branched from each latest branch
- Delete working branches after merging
- Review as much as possible (have someone do it for you)
- Build, deploy, etc. are discussed separately.

### Branch Naming Rules

| Branch Name | Description | Supplemental |
| ---------------------------- | ---------------- | ---- |
| main | latest release | dev/main | latest for development
| dev/main | latest for development | hotfix/{module name}/{subject}
| hotfix/{module name}/{subject matter} | sandbox/{anything} | test code, etc. |

### Commit message

Please refer to the following template for the commit message.

````plaintext
🐞 Bugs and Performance
#🐛 :bug: bug fixes.
#🚑 :ambulance: fix a critical bug
#🚀 :rocket: performance improvements
#💻 Code quality and style
#👍 :+1: feature improvements
#♻️ :recycle: refactoring
#👕 :shirt: Lint error fixes and code style fixes

🎨 UI/UX and design
#✨ :sparkles: add new features
#🎨 :art: design changes only

🛠️ Development Tools and Settings.
#🚧 :construction: WIP (Work in Progress)
#⚙ :gear: config change
#📦 :package: add new dependency
#🆙 :up: update dependency packages, etc.

documentation and comments.
#📝 :memo: fix wording
#📚 :books: documentation
#💡 :bulb: add new ideas and comments

🛡️ security
#👮 :op: security-related improvements

🧪 testing and CI.
#💚 :green_heart: fix/improve testing and CI

🗂️ file and folder manipulation.
#📂 :file_folder: Folder manipulation
#🚚 :truck: file movement

#📊 :log: logging and tracking
#💢 :anger: conflicts
#🔊 :loud_sound: add log
#🔇 :mute: log deleted.
#📈 :chart_with_upwards_trend: add analytics or tracking code

💡 Other.
#🧐 :monocle_face: code reading and questions.
#🍻 :beers: code that was fun to write.
#🙈 :see_no_evil: .gitignore addition.
#🛠️ :hammer_and_wrench: bug fixes and basic problem solving
```
