class Article:
    # class variable all which is an empty list and will store all instances of the Article class
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        # appends the current instance 'self' to the class variable 'all' so that each instance of Article is stored in the list
        Article.all.append(self)
    # created properties for author, magazine and title so they can be accessed as attributes rather than methods
    # created setter methods for author and magazine to change value of attributes and change to new value if it is an instance of the Author or Magazine class

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
        
            self._author = new_author
            
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
                
    @property
    def title(self):
        return self._title
    
    # created setter method for title, which changes the value of the title attribute. 
    # if not hasattr(self, "title"): checks to see if this instance already has a title attribute so that title is only set once
    # if isinstance(new_title, str): checks that new_title is a string
    # if 5<= len(new_title) <= 50: makes it so that the title string must be between 5 and 50 characters long
    # Author and Magazine classes are constructed similarly to meet their own requirements
    @title.setter
    def title(self, new_title):
        if not hasattr(self, "title"):
            if isinstance(new_title, str):
                if 5<= len(new_title) <= 50:
                    self._title = new_title
    
                    
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, "name"):
            if isinstance(new_name, str):
                self._name = new_name

    # returns a list of articles by iterating over Article.all and returning those which match the current Author instance
    def articles(self):
        return [article for article in Article.all if self == article.author]
    
    # returns a list of magazines after iterating over the list of articles authored by the current instance of Author 
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    #creates a new Article object for the current author('self')
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    #iterates over the list of magazines of the current author, extracts the category of each magazine and returns a list of categories. {} = set, so this list is also a set with unique categories. 
    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None
        

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    # makes sure new_name is between 2 and 16 characters long
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            # checks to make sure length of new_category isn't an empty string
            if len(new_category):
                self._category = new_category
        
    # iterates over Articles.all and returns a list of articles belonging to the current magazine instance
    def articles(self):
        return [article for article in Article.all if self == article.magazine]
    
    # iterates over the list of articles belonging to current magazine instance and returns a list that is a set with unique author objects. 
    def contributors(self):
        return list({article.author for article in self.articles()})
    
    # returns a list of titles belonging to current magazine instance, and if none returnes None
    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None
    # created a dict {} named authors to take in authors as keys and the number of articles they contributed as values
    # list_of_authors = [] is an empty list that will store authors who have contributed more than one article to the magazine
    # for loop iterates over each article in the current magazine instance, then if they are already in the authors dictionary it increments their value by 1,
    # and if they are not already in the authors dictionary it gives them a key value of 1, representing the number of articles contributed
    # if authors in the authors list have a value equal or greater than 2, they are appended to the list_of_authors
    # last if else statement checks to see if there are any authors in the list_of_authors and returns that list, otherwise returns None if empty
    def contributing_authors(self):
        authors= {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else: 
                authors[article.author] = 1  
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author)
        if (list_of_authors):
            return list_of_authors
        else:
            return None
