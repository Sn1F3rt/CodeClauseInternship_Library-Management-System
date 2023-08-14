# Library Management System

> Library Management System implemented using Flask as my second golden project for the CodeClause internship.


## Table of Contents

- [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Setup](#setup)
- [Running](#running)
- [CLI Commands](#cli-commands)
- [License](#license)


## Installation

### Prerequisites

The prerequisites are as follows:

* `python3` (tested on **v3.11.2**)
* `git`

### Setup

1. Clone the GitHub repository:

    ```shell
    git clone https://github.com/Sn1F3rt/CodeClauseInternship_Library-Management-System
    ```

2. Install the dependencies:

    ```shell
    python -m pip install -r requirements.txt
    ```

3. Create a file called `.env` with the following contents (replace them with the actual database credentials):

    ```
    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=databaseuser
    DB_PASS=supersecretpassword
    DB_NAME=databasename
    ```
    

## Running

You can run the application using the CLI:

```shell
flask run
```


## CLI Commands

- `flask add_librarian username`\
  CLI command to give admin privileges to a user. Note that `username` has to be a valid existing user.
  
- `flask rm_librarian username`\
  CLI command to revoke admin privileges from a user. Note that `username` has to be a valid existing user.
  

## License

[Creative Commons Zero v1.0 Universal](LICENSE)

Copyright &copy; 2023 Sayan Bhattacharyya