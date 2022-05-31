Sphinx Example
==============

Small example Python/Poetry project with a Sphinx website including Jupyter notebooks.

How to try it
-------------

Clone the project from GitHub:

```
$ git clone git@github.com:denisrosset/brent-level-3.git
```

Then initialize the Poetry virtual environment and install packages:

```
$ cd brent-level-3
$ python -m venv .venv
$ poetry install
```

Then verify the documentation building works:

```
$ pwd
/home/.../brent-level-3
$ poetry run make -C docs clean html
```

and then open the `docs/build/html/index.html` file in your browser.

On your GitHub
--------------

There is a `.github/workflows/build-docs.yml` file in this repository.

If you fork/clone this repository on your GitHub account, there is an action that will run
on every commit on the `main` branch, and will update the website on GitHub Pages.

This workflow will create and update a `gh-pages` branch on GitHub containing the html
files for the website.

Then go (as of March 2022) to the "Settings" tab on GitHub, on the "Pages" link in the
left list, then select "gh-pages" in the "Source" drop down and save.

Then something like

   Your site is ready to be published at https://YOURNAME.github.io/brent-level-3/ 

will be displayed; now you can put that link as your project website on the main
project page (in Edit repository details).
