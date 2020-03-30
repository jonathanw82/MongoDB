##### MongoDB from the command line

cls == clears the terminal OR clear

insert link from mongo db

show collections == shows we are connected to out database

coll = db.myFirstMDB == assign the database to a variable

coll.insert({ first: 'jon', last: 'wheway', dob: '20/04/1982', gender: 'm', hair_color: 'brown', nationality: 'english', occupation: 's
oftware_developer'}); == inserts a result into our database.

coll.find() == will return all in the table

coll.find({gender:'f'}) == will return all records with the gender set to f

coll.find({gender:'f', nationality:'english'}) == return all records with gender f and nationality english

coll.find({gender: 'f', $or: [{nationality: 'american'}, {nationality: 'irish'}]}); to find all database entries with the female gender who are either Irish or American
The fiddly bit now is closing all of the braces in the correct order. So first, it's square brace, then curly brace, then regular bracket, and then our semicolon.

coll.find({gender: 'f', $or: [{nationality: 'american'}, {nationality: 'irish'}]}).sort({nationality: 1});
take off the semicolon. Then I'll do sort({ We're going to sort by nationality. 1 is for ascending. -1 is to sort descending. 

coll.update({nationality:'irish'}, {$set:{hair_color:'blue'}}); == the set keyword will update the first record with irish and replace the hair color to blue;

coll.update({nationality:'irish'}, {$set:{hair_color:'purle'}},{multi:true}); == the multi:true will update all the records with irish to hair color purple.

coll.remove({first: 'kate',last: 'bush'}); == will remove kate bush from the database.

coll.remove()  == ************ Warning! will remove all the data drom the database **************

##### Programmically using Python



first you must install 

pip3 install dnspython 

pip3 install pyMonogo ==  will install the Python 3 version of the pyMongo library

nano .bashrc  == will open the .bashrc hidden file in nano editor

echo $MONGO_URI  == will print back the uri string 

coll.insert(new_doc)  == will insert a single new_doc

coll.insert_many(new_docs)   == will insert many docs

coll.update_one({'first': 'martha'}, {'$set': {'gender': 'f'}})  == will update that field useing the set

'$set':

coll.update_many()  == will update many