import asyncio
import os
from collections import defaultdict

import aiohttp
from bs4 import BeautifulSoup

BASE_URL = 'https://www.conjugacao.com.br'


async def get_url_pagina_verbos(session, url):
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'html.parser')
        a_href_soup = soup.find('ul', {'class': 'word-list'}).find_all('a')
        return [f'{BASE_URL}{a_href["href"]}' for a_href in a_href_soup]


async def get_verbos(session, url):
    print(f'Buscando url: {url}')
    async with session.get(url) as response:
        conteudo = await response.text()
        print(f'Extraindo verbos da url: {url}')
        soup = BeautifulSoup(conteudo, 'html.parser')
        spans = soup.find_all('span', {'class': 'f'})
        return [span.text.lower() for span in spans]


async def busque():
    print('Buscando urls...')
    async with aiohttp.ClientSession() as session:
        tasks_urls = [asyncio.create_task(get_url_pagina_verbos(session, f'{BASE_URL}/verbos-populares/{pagina}'))
                      for pagina in range(1, 51)]
        urls_agrupadas = await asyncio.gather(*tasks_urls)

        tasks_verbos = [asyncio.create_task(get_verbos(session, url)) for grupo in urls_agrupadas for url in grupo]
        return await asyncio.gather(*tasks_verbos)


if __name__ == '__main__':
    arquivos_agrupados = defaultdict(list)
    diretorio = 'verbos'
    verbos_agrupados = asyncio.run(busque())
    print('Agrupando verbos...')
    for grupo in verbos_agrupados:
        for verbo in grupo:
            key = verbo[:2]
            arquivos_agrupados[key].append(verbo)

    print('Salvando verbos...')
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    for nome_arquivo, verbos in arquivos_agrupados.items():
        verbos.sort()
        with open(f'{diretorio}/{nome_arquivo}.txt', 'w') as f:
            f.write("\n".join(verbos))
