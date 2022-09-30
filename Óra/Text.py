def main():
    pass
    title = "Howl's Moving Castle"
    gerne = "Japanese Animation"
    author = "Miyazaki Hayao"
    date = 2004
    rating = 8.2
    mainc = "Sophie"
    maincJob = "hatmaker"
    mins = 119
    originall = "Japanese"
    text = "{title} is a {gerne} film, written by {author}.\nThe film was produced in {date}. It's IMDB rating is {rating}.\nThe main character's name {mainc} is who is a {maincJob}\nThe film is {mins} long.\nThe original language is {originall}"
    print(text.format(title = title,gerne = gerne,author = author,date = date,rating = rating,mainc = mainc,maincJob = maincJob,mins = mins,originall = originall))

if __name__ == "__main__":
    main()