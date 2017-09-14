import datetime
from os import path, getcwd
import ads

up_one_dir = path.abspath(path.join(getcwd(), '..'))
if not path.exists(path.join(up_one_dir, 'scripts')):
    raise RuntimeError("generate_pubs.py must be run from inside the scripts "
                       "directory.")

pubs_path = path.join(up_one_dir, 'content', 'extra', 'pubs.rst')

def parse_authors(paper, max_authors):
    names = []
    for a in paper.author:
        last, others = a.split(', ')
        others = ['{0}.'.format(o[0]) for o in others.split()]
        name = "{first} {last}".format(first=' '.join(others), last=last)
        if 'Price-Whelan' in name:
            name = '<span class=apw>{0}</span>'.format(name)

        names.append(name)

        if len(names) >= max_authors:
            names.append('<i>et al.</i>')
            break

    return names

def main():
    # We grab all papers where I'm first or second author

    # Only include papers in these journals:
    include_journals = ['arxiv', 'apj', 'aj', 'mnras']

    # Maximum number of recent papers to show
    max_papers = 10

    # How many authors to show before et al.?
    max_authors = 4

    # Get recent papers
    papers = ads.SearchQuery(author="price-whelan",
                             database="astronomy",
                             sort="date")

    show_papers = []
    for paper in papers:
        # Skip papers not in our included journals
        if not any([any([include in x.lower()
                         for include in include_journals])
                    for x in paper.identifier]):
            continue

        for author in paper.author[:max_authors]:
            if 'price-whelan' in author.lower():
                break
        else: # not in first three authors
            continue

        # Check the publication date, make sure it's within a year
        try:
            y, m, d = paper.pubdate.split('-')
            y = int(y)
            m = max(int(m), 1)
            d = max(int(d), 1)

        except:
            print("Failed to get date for paper: {0}".format(paper.title))
            continue

        date = datetime.date(y, m, d)
        dt = datetime.datetime.now().date() - date

        if dt.days > 365: # skip papers more than a year old
            continue

        show_papers.append((y, paper))

        if len(show_papers) >= max_papers:
            break

    # Now we construct the restructured text format:
    text = ".. raw:: html\n\n"
    text += "\t<ul>\n"

    # text_blob = "* `{title} <{url}>`_\n{authors}" # ReST
    _text_blob = ("\t\t<li><a href='{url}' class='paper-title'>{title}</a>"
                  "<br/><span class='paper-authors'>{authors}</span></li>\n")

    for year, paper in show_papers:
        authors = parse_authors(paper, max_authors=max_authors)
        authors = ", ".join(authors) + " ({0})".format(year)

        if paper.doi is None:
            url = "http://arxiv.org/pdf/{0}".format(paper.identifier[0]) # why?
        else:
            url = "https://doi.org/{0}".format(paper.doi[0]) # why?
        text += _text_blob.format(title=paper.title[0], # why?
                                  authors=authors,
                                  url=url)

    text += "\t</ul>\n"

    with open(pubs_path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    main()
