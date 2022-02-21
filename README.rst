Config Required
----------
- Install ``Python >= 3.8``: `Python <https://www.python.org/downloads/release/python-382/>`_:
- Install ``Oracle Client``: `cx_Oracle <https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#installing-cx-oracle-on-linux>`_:

Quickstart
----------

First, Setup venv python `Document Setup <https://docs.python.org/3.9/library/venv.html>`_: ::

    python -m venv venv

    Windows:
    - Cmd: .\venv\Scripts\activate
    Linux:
    - Terminal: source venv/bin/active

Then run the following commands to bootstrap your environment with ``PIP``: ::

    Windows:
    - cmd: python -m pip install -r requirements/local_windowns.txt
    Linux:
    - Terminal: sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
    - Terminal: pip install -r requirements/local_debian.txt

Then create ``.env`` file (or copy and modify ``.env.example.yaml``) in project root and set environment variables for application: ::

    Windows:
    - cmd: copy env.example.yaml .env
    Linux:
    - Terminal: cp env.example.yaml .env

Then Install ``pre-commit``: ::

    Windows:
    - cmd: pre-commit install

    Linux:
    - Terminal: pre-commit install


To run the web application in debug use::

    Develop:
    - uvicorn --env-file .env app.main:app --port {port} --reload
    Deloy:
    - gunicorn app.main:app -k uvicorn.workers.UvicornWorker

    Lưu ý:
    - Config worker, port, host trong file gunicorn.conf.py




Project structure
-----------------

Files related to application are in the ``app`` directories.
Application parts are::

    .
    ├── app
    │   ├── api
    │   │   └── v1
    │   │       ├── controllers
    │   │       ├── dependencies
    │   │       ├── endpoints
    │   │       └── schemas
    │   ├── repositories
    │   ├── settings
    │   ├── third_party
    │   │   ├── mongo
    │   │   ├── oracle
    │   │   │   └── models
    │   │   └── services
    │   └── utils
    ├── backup
    │   └── oracle
    └── requirements

Rules commit git
-----------------

Structure: ``[type] (issues) : descriptions``

Example:  [add] (#31) : thêm function validate tài sản đảm bảo

``git commit -m "Title" -m "Descriptions"``

Example: git commit -m "[add] (#31) thêm function validate tài sản đảm bảo"



Refer:

- `How to Write a Git Commit Message <https://chris.beams.io/posts/git-commit/>`_

- `Git commit message convention that you can follow! <https://dev.to/i5han3/git-commit-message-convention-that-you-can-follow-1709>`_

Type:
    - feat: A new feature
    - fix: A bug fix
    - docs: Documentation related changes
    - refactor: A code that neither fix bug nor adds a feature. (eg: You can use this when there is semantic changes like renaming a variable/ function name
    - perf: A code that improves performance
    - merge: Merge branch to branch
    - revert: Revert git
    - conflict: Fix conflict

Rules create branch
-----------------

Structure: ``[develop]/[Module]/[#issues]_[name]``

Example:  develop/ktt/#72_create_model

- Module: Giai đoạn phát triển project
    - `Tham khảo <https://git.minerva.vn/scb-los/los_be/-/wikis/issues>`_

- Issues: Số id công việc được giao

- Name: mô tả ngắn công việc

Báo cáo tiến độ task
-----------------

Structure: ``#<ten> <yyyy/mm/dd> <project> <id_issue> <mô tả ngắn tiến độ>``

Example:  #phuongnd 2021/08/04   LOS  #0 Review & support code , merge 6 step


Refer project
-----------------

- `Tài liệu <https://git.minerva.vn/scb-los/los_be/-/wikis/Wiki>`_

- `Cách sử dụng issues <https://git.minerva.vn/scb-los/los_be/-/wikis/Issues-Description>`_



Run test
-----------------

- Change all database setting to TEST environment
- Run following command: ::


    pytest --color=yes -s -v --show-capture=no

- Exclude internal_credit_rating: ::

    pytest --color=yes -s -v --show-capture=no --ignore=tests/normal_loan/internal_credit_rating


