<img src="https://raw.githubusercontent.com/DNArchery/DNArchery/main/assets/dnarchery-logo.png" alt="dnarchery logo" width="250" align="right">

# `MailMan Web` 🧬

> A free and open-source web application for senting mass emails with multiple attachments.

The core goal of the project is to be a good easy tool to sent mass emails (Read [Goals](#goals))

Built with ❤️ at [**FOSSHack 3.0**](https://fossunited.org/fosshack/2023)!

<p align="left">
    <img src="https://img.shields.io/badge/version-0.1.0-blue.svg" title="version" alt="version">
    <a href="https://github.com/dnarchery/dnarchery/blob/master/LICENSE"><img alt="github license" src="https://img.shields.io/github/license/dnarchery/dnarchery.svg"></a>
</p>

## Table of Contents

- [Goals](#goals)
- [Features](#features)
- [Installation](#installation)
- [Citations & Acknowledgments](#citations--acknowledgements)
- [Contribution](#contribution)
- [License](#license)
- [Project Progress](#faq)

## Goals

- First goal is to make sent mass emails.

## Features

- The core of the utility is exposed as a Webservice API (Django backend)
- **Performance** - Processing large FASTA files/DNA sequences are pretty fast as most of them utilize vectorized or parallelized 

## Requirements
- Python 3.10.0
- Django 4.1.2
- djangorestframework 3.14.0

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

after this setup `.env` file which helps to store credentials of project

```
cd mailman-web
```


```
touch .gitignore
```

## Contribution

As stated in the goals section, one of our primary goal is to provide a low barrier contributing opportunity to the bioinformatics open-source space. If you want to add more DNA sequencing/alignment/conversion algorithms, you can browse to `src -> core ->` and chose which part you want to extend. Every super module in the tree have the same structure, a `utils.rs` file which contain all functions, you can add a new function and implement it as an exposed actix-web endpoint in the `src -> api -> endpoints.rs` and that's it.

**Ways to contribute:**

- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word

## License

Licensed under the MIT License, see <a href="./LICENCE.md">LICENSE</a> for more information.

## Citations & Acknowledgements
This project wouldn't exist without these resources (libraries/blogs):

- [python](https://github.com/python)
- [django](https://github.com/django)

## FAQ

**_FOSSHack Questionnaire:_**

Q. What was the initial stage of the project?

> The idea of the project is to create a utility tool for senting mass emails.
>
> the initial stage was just implementing the core feature which is sent mass emails with attachments
>


Q. What stage is it in now?

> The Project is complete.it is an mvp stage now.

Q. How did you get there?

> Authors of the project face some manual emailing issues which kills lots of time so we taught to solve this headache when we solve it lots of people enquired about this and said to implement mail attachments too.
>

Q. What is working/not working?

> The backend is stable and works according to the feature.

---