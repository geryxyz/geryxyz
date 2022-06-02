import pdb
from ui import *
from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://54.86.9.156:36381", 
    auth=basic_auth("neo4j", "rides-spots-punches"))
session = driver.session()

cypher_query = '''
MATCH (n)
RETURN id(n) AS id
LIMIT $limit
'''

results = session.run(cypher_query,
  parameters={"limit": 10})

#]
def getAll(query, property, parameters={}):
	values = []
	for record in session.run(query, parameters=parameters):
		values.append(record[property])
	return values

def get_liked_genre():
	return get_genre_of('Inception')

def get_movies():
	query = '''
	match (m:Movie)
	return m.title as title
	'''
	return getAll(query, 'title')

def get_genre_of(title):
	query = '''
	match (liked:Movie {title: $title})-[:IN_GENRE]->(likedGenre:Genre)
	return likedGenre.name as name
	'''
	return getAll(query, 'name', parameters={'title': title})

def get_sets():
	query = '''
	match (liked:Movie {title: "Inception"})-[:IN_GENRE]->(genre:Genre)<-[:IN_GENRE]-(other:Movie)
	with liked, other, collect(genre.name) as intersection
	match (liked)-[:IN_GENRE]->(likedGenre:Genre)
	with liked, other, collect(likedGenre.name) as likedGenres, intersection
	match (other)-[:IN_GENRE]->(otherGenre:Genre)
	return liked.title as liked, other.title as other, likedGenres, intersection, collect(otherGenre.name) as otherGenres

	'''
	return session.run(query)

def jaccard_slow():
	likedGenres = set(get_liked_genre())
	similarMovies = []
	for title in get_movies()[:50]:
		otherGenres = set(get_genre_of(title))
		intersection = likedGenres & otherGenres
		union = likedGenres | otherGenres
		similarity = len(intersection) / len(union)
		entry = (title, similarity)
		info("similarity of %s is %f" % entry)
		similarMovies.append(entry)
	return similarMovies

def jaccard():
	similarMovies = []
	for db_entry in get_sets():
		likedGenres = set(db_entry['likedGenres'])
		otherGenres = set(db_entry['otherGenres'])
		otherTitle = db_entry['other']
		intersection = likedGenres & otherGenres
		union = likedGenres | otherGenres
		similarity = len(intersection) / len(union)
		item = (otherTitle, similarity)
		#info("similarity of %s is %f" % item)
		similarMovies.append(item)
	return similarMovies

def recommend():
	similarMovies = jaccard()
	similarMovies.sort(key=lambda entry: entry[1], reverse=True)
	return similarMovies[:10]

if __name__ == '__main__':
	info("The top 10 movies you should watch:")
	for i, entry in enumerate(recommend()):
		info("   %dth %s" % (i+1, entry[0]))