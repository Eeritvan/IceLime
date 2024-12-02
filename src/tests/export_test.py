from entities.book import Book
from entities.article import Article
from export import Bibtex
import unittest

txt = '''@book{book13,
    author = {1324},
    title = {123},
    year = {123},
    publisher = {123},
    editor = {123},
    volume = {123},
    number = {123},
    pages = {123},
    month = {123},
    note = {123}
}


@book{book11,
    author = {1324},
    title = {123},
    year = {123},
    publisher = {123},
    editor = {123},
    volume = {123},
    number = {123},
    pages = {123},
    month = {123},
    note = {123}
}


'''


txt2 = '''@article{article2,
    author = {Jack Back},
    title = {Chocko Iland},
    year = {2017},
    journal = {New Journal},
    volume = {2},
    number = {23},
    pages = {14}
}


'''

class TestStatisticsService(unittest.TestCase):
    def test_exports_bibtex_book(self):
        
        kirja = Book("13","1324","123","123","123","123","123","123","123","123","123")

        kirja2 = Book("11","1324","123","123","123","123","123","123","123","123","123")

        bibtex = Bibtex()
        bibtex.create_book_bibtex([kirja])

        bibtex.create_book_bibtex([kirja2])

        with open("src/bibtex.bib","r",encoding= 'utf-8') as file:

            text = file.read()

        self.assertEqual(txt == text,True)

    def test_exports_bibtex_article(self):

        article = Article("2","Jack Back","Chocko Iland","New Journal","2017",  "2", "23","14")

        bibtex = Bibtex()
        bibtex.create_article_bibtex([article])

        with open("src/bibtex.bib","r",encoding= 'utf-8') as file:

            text = file.read()

        self.assertEqual(txt2 == text,True)