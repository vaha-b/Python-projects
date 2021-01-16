def tallest_people(**kwargs):
    max_key = max(kwargs, key=kwargs.get)
    sort = sorted(kwargs.items())

    print(sort)


people = {"Jackie": 176, "Wilson": 185, "Saersha": 165, "Roman": 185, "Abram": 169
          }

tallest_people(**people)
