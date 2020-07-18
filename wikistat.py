from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding='utf8') as f:
        end_statistics = []
        soup = BeautifulSoup(f.read(), 'lxml')
        count = 0
        find_list = soup.find(name='div', id='bodyContent')
        finder = find_list.find_all(name='img')
        for image in finder:
            if image.name == 'img':
                try:
                    score = int(image['width'])
                    if score >= 200:
                        count += 1
                except KeyError:
                    continue
        end_statistics += [count]
        count = 0
        finder = find_list.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for header in finder:
            z = header.text.split()
            if z[0].startswith(('C', 'E', 'T')):
                count += 1

        end_statistics += [count]
        count = 1
        curr_count = 1
        finder = find_list.find_all('a')
        for href in finder:
            try:
                href['href']
            except KeyError:
                continue
            try:
                g = href.find_next('a')
                g['href']
                g.parent
                if g.parent == href.parent:
                    count += 1
                    if count > curr_count:
                        curr_count = count
                else:
                    count = 1
            except:
                continue
        end_statistics += [curr_count]
        count = 0
        finder = find_list.find_all(['ol', 'ul'])
        for lst in finder:
            if lst.name in ('ol', 'ul'):
                gen = [tag.name for tag in lst.parents]
                if 'ol' in gen or 'ul' in gen:
                    continue
                else:
                    count += 1
        end_statistics += [count]
        return end_statistics
