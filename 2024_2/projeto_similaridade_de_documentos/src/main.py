from data_loader import read_documents
from search import search_by_keyword, search_by_similarity

def main():
    filepath = '../data/wikipedia_good_articles_video_games.txt'
    docs = read_documents(filepath)

    # Select title to search
    keywords = input('Enter the keywords to search (separated by space): ')

    index = 0
    titles = []
    for doc in docs:
        titles.append(doc['title'])
    title_scores = search_by_keyword(titles, keywords, top_n=-1)
    print('Titles found:')
    for title_index, score in title_scores:
        # Must have at least 1 keyword in the title
        if score < 1:
            break
        print(f'{index}:\t{titles[title_index]}')
        index += 1
    
    title_index = int(input('Enter the index of the title to search: '))
    query_doc = docs[title_scores[title_index][0]]
    query_title = query_doc['title']
    query_text = query_doc['text']

    texts = []
    for doc in docs:
        texts.append(doc['text'])
    similarities = search_by_similarity(texts, query_text, top_n=5)

    print(f'Search results for "{query_title}":')
    for text_index, similarity in similarities:
        print(f'{titles[text_index]}: {similarity:.2f}')

if __name__ == '__main__':
    main()