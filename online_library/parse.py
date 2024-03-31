import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from datetime import datetime
import os



HEADERS = {'User-Agent': UserAgent().random}
TRASH = './temporary files'

async def main(search: str):
    search = search.replace(' ', '+').lower()
    BASE_URL = f'https://flibusta.su/booksearch/?ask={search}'
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            request = await aiohttp.StreamReader.read(response.content)
            soup = BS(request, 'html.parser')
            items = soup.find_all('div', class_="desc")
            lenth = len(items)
            #items = items[0:5] if lenth > 5 else items
            books = []
            for item in items:
                title = item.find('div', class_='book_name').find('a',).text.strip()
                author = item.find('span', class_='author').find('a',).text.strip()
                img = item.find('div', class_='cover').find('img')
                img = f'https://flibusta.su{img["src"]}'
                url = item.find('div', class_='cover').find('a').get('href')
                url = f'https://flibusta.su{url}'
                obj = {
                    'title': title, 'author': author, 'img': img, 'url': url
                }
                books.append(obj)
            return books


async def download_book(link: str):
    async with (aiohttp.ClientSession() as session):
        async with session.get(link, headers=HEADERS) as response:
            request = await aiohttp.StreamReader.read(response.content)
            soup = BS(request, 'html.parser')
            book = soup.find('div', class_="page_wrapper")
            book = book.find('div', class_="content")
            book = book.find('div', class_="container")
            book = book.find('div', class_="b_block_two")
            book = book.find('div', class_="b_block_center")
            book = book.find('div', class_="b_biblio_book")
            description_text = book.find('div', class_="b_biblio_book_annotation").find_all('p', )
            files = book.find('div', class_="b_download").find_all('span', class_="link")
            fb2, epub = files[:2]
            book = book.find('div', class_="b_biblio_book_top")
            title = book.find('div', class_="book_name").find('h1', ).text.strip()  # title
            author = book.find('div', class_="row author").find('span', class_="row_content").find('a', )
            author_url = author.get('href')  # author url
            author = author.text.strip()  # author
            description = soup.find('div', class_="book_desc")
            year = description.find('div', class_="row year_public").find('span',
                                                                          class_="row_content").text.strip()  # year
            try:
                seria = description.find('div', class_="row series").find('span', class_="row_content").find(
                    'a', ).text.strip()  # seria
                seria = False if seria in [None, '', ' '] else seria
            except:
                seria = False
            tags = description.find('div', class_="row tags").find('span', class_='row_content').find_all('a')  # tags
            img = book.find('div', class_="book_left").find('div', class_="book_img").find('img')  # img
            ###
            year = int(year[:4])
            tags2 = [t.text.strip() for t in tags]
            tags = tags2
            img = f'https://flibusta.su{img["src"]}'
            description_text = '\n'.join(list(map(lambda x: x.text.strip(), description_text[:-1])))
            fb2 = f"https://flibusta.su/book{fb2.get('onclick')[18:-10]}"
            epub = f"https://flibusta.su/book{epub.get('onclick')[18:-10]}"
        data = {
            'title': title, 'author': author, 'year': year, 'seria': seria, 'tags': tags,
            'description': description_text, 'author_url': f"https://flibusta.su{author_url}"
        }
        download_files = [img]
        for file_url in [fb2, epub]:
            async with session.get(file_url, headers=HEADERS) as response:
                request = await aiohttp.StreamReader.read(response.content)
                soup = BS(request, 'html.parser')
                book = soup.find('div', class_="page_wrapper").find('div', class_="content").find('div',
                                                                                                  class_="container")
                book = book.find('div', class_="b_block_two").find('div', class_="b_block_center")
                book = book.find('div', class_="b_biblio_book").find('div', class_="b_biblio_book_top")
                file_url = book.find('div', class_="book_desc").find('div', class_='b_download_progress_txt').find(
                    'a', )
                file_url = file_url.get('href')
                download_files.append(file_url)
        file_ind = 0
        typesf = []
        for ft in download_files:
            if ft.find('jpg') != -1:
                typesf.append('jpg')
            elif ft.find('zip') != -1:
                typesf.append('zip')
            elif ft.find('epub') != -1:
                typesf.append('epub')
            elif ft.find('fb2') != -1:
                typesf.append('fb2')
            elif ft.find('jpeg') != -1:
                typesf.append('jpeg')
            else:
                typesf.append('zip')
        #folder = str(datetime.now())[:19].replace(' ', '_').replace(':', '-')
        def relocate():
            import string
            import random as rnd
            file_path = ''
            for _ in range(6):
                file_path += string.ascii_lowercase[rnd.randint(0, len(string.ascii_lowercase) - 1)]
                file_path += str(rnd.randint(0, 9))
            return file_path
        folder = relocate()
        os.mkdir(f'media/books/{str(datetime.now().year)}/{folder}')
        for f_url in download_files:
            async with session.get(f_url, headers=HEADERS) as response:
                request = await aiohttp.StreamReader.read(response.content)
                file_d = f'media/books/{str(datetime.now().year)}/{folder}/{file_ind}.{typesf[file_ind]}'
                with open(f'{file_d}', 'wb') as file:
                    file.write(request)
                if file_ind == 0:
                    ft_ = 'img'
                elif file_ind == 1:
                    ft_ = 'fb2'
                else:
                    ft_ = 'epub'
                data = {**data, f'{ft_}': file_d[6:]}
                file_ind += 1
        return data

async def author_parse(link: str):
    async with (aiohttp.ClientSession() as session):
        async with session.get(link, headers=HEADERS) as response:
            request = await aiohttp.StreamReader.read(response.content)
            soup = BS(request, 'html.parser')
            page = soup.find('div', class_="page_wrapper").find('div', class_="content")
            page = page.find('div', class_="container").find('div', class_="b_block_two")
            page = page.find('div', class_="b_block_center").find('div', class_="b_desc")
            author_fio = page.find('h1', ).text.strip()
            page = page.find('div', class_='b_author')
            img = page.find('div', class_='cover__authors').find('img')
            bio = page.find('p',).text.strip()
            ###
            img = f'https://flibusta.su{img["src"]}'
            path_img = f'media/authors/avatar/' + author_fio.replace(' ', '_') + '.jpg'
            async with session.get(img, headers=HEADERS) as response:
                request = await aiohttp.StreamReader.read(response.content)
                with open(path_img, 'wb') as file:
                    file.write(request)

            data = {
                'author_fio': author_fio, 'bio': bio, 'img': path_img[6:]
            }
            return data