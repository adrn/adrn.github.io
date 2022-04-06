adrian.pw
=========

Source code for my website and blog.

The `main` branch contains the built website, code is in the branch `source`.

Commands
--------

Use the environment `conda activate adrn.github.io`.

Use `make devserver` to start a development server to generate the pages and
serve them locally at http://localhost:8000 - `make stopserver` will stop the
server.

Use `make publish` to build the production site.

Use `make github` to make the production site and push to the `gh-pages` branch.

Use `make pubs github` to regenerate the publication list and push.
