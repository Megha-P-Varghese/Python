d= {'stud1' : {
    'name':'megha',
    'age' : 25,
    'marks' : {
    'physics' : 70,
    'english' : 90
    }
},
'stud2' : {
    'name' : 'jibi',
    'age' : 23,
    'marks' : {
        'physics' : 80,
        'english' : 90
    }
}

}
print(d.get('stud1').get('marks'))
d['stud1']
print(d['stud1'])
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.pop("year")
print(thisdict)
