import sys, os

with open('header.html', 'r') as file:
    header = file.read()

with open('content.html', 'r') as file:
    content = file.read()

with open('footer.html', 'r') as file:
    footer = file.read()

# empty list to sort pages
page_lst = []

# create index.html
with open('index.html', 'w') as index:
    index.write(header + '\n\n')
    index.write(content + '\n\n')

    # write pages
    for file in os.listdir('pages/'):
        page_lst.append(file)

    # sort list
    page_lst.sort()

    # write to file
    for page in page_lst:
        index.write(open('pages/' + page, 'r').read() + '\n\n')

    index.write(footer)