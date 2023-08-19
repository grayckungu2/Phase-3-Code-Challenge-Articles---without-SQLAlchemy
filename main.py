import sys
import os

# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.Author import Author 
from lib.Article import Article
from lib.Magazine import Magazine

# Create instances of Magazine
magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Fashion Magazine", "Fashion")

# Print magazine names
print(magazine1.name())  
print(magazine2.name()) 

# Create instances of Author
author1 = Author("Krystal mark")
author2 = Author("Lacie kui")

print(author1.name())  
print(author2.name()) 

# Create instances of Article
article1 = Article(author1, magazine1, "Python Programming")
article2 = Article(author2, magazine2, "Fashion Trends")

print(article1.title())  
print(article2.title())  

# Add articles to authors
author1.add_article(magazine1, "Introduction to Python")
author1.add_article(magazine2, "Dangers of Love")
author2.add_article(magazine1, "Special Needs")

print([article.title() for article in author1.articles()] or "No articles")  
print([article.title() for article in author2.articles()] or "No articles")  

# Print magazines of authors
print([magazine.name() for magazine in author1.magazines()] or "No magazines")  
print([magazine.name() for magazine in author2.magazines()] or "No magazines")  

# Print contributing authors of magazines
contributing_authors1 = [author.name() for author in magazine1.contributing_authors()]
contributing_authors2 = [author.name() for author in magazine2.contributing_authors()]

print(contributing_authors1 or "No contributors")  
print(contributing_authors2 or "No contributors")  

# Print list of all magazines
print([magazine.name() for magazine in Magazine.all()] or "No magazines")  

# Find magazine by name
magazine_found = Magazine.find_by_name("Tech Magazine")
if magazine_found:
    print(magazine_found.name())
else:
    print("Magazine not found")

# Print article titles of all magazines
print([article.title() for article in Magazine.article_titles()] or "No articles") 

# Print contributing authors of magazines
print(contributing_authors1 or "No contributors")  
print(contributing_authors2 or "No contributors")

