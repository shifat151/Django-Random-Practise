from django.core.management import BaseCommand
from faker import Faker, providers
from modelPrac.models import Musician, Concert, Album
from django.db.models import Max, Min


albums=[
    'Justice To All',
    'Behind The Scene Mate/s',
    'Suffering Is Optional',
    'Typical of Friends',
    'A dance to my sorrows',
    'Cheerful giving',
    'Holy Life',
    'The Grand Creator',
    'Disconnected',
    'Love has no ending',
    'A Poison To My Heart',
    'The Beauty Of Life',
    'Plight of a widow',
    'It Was Too Good To Be True',
    'Its An Old Story',
    'Fearing God',
    'the little things',
    'Be Strong & Courageous',
    'Underestimated By Many',
    'Talents',
    'My Hidden Pain',
    'You Were A True Friend'
]

concerts=[
    'Annual Sin',
    'Annual Wonderland',
    'Boogie Horizon',
    'Boogie Paradise',
    'Danceex',
    'Dance Paradise',
    'Festivscape',
    'Festival Oasis',
    'Fest Invasion',
    'Fest Kingdom',
    'Fest VIP',
    'Gala Jungle',
    'Gala Temple',
    'Gigscape',
    'Gig Glory'
    'Midsummer Splendour',
    'Music Dreamland',
    'Music Heritage',
    'Party Playground',
    'Venue Beast'
]



class Provider(providers.BaseProvider):
    def album_names(self):
        return self.random_element(albums)
    def concert_names(self):
        return self.random_element(concerts)



class Command(BaseCommand):
    help="Command Information"

    def handle(self, *args, **kwargs):
        fake=Faker()
        fake.add_provider(Provider)

        for _ in range(15):
            f_name=fake.first_name()
            l_name=fake.unique.last_name()
            Musician.objects.create(first_name=f_name, last_name=l_name)
        
        max_id_dict=Musician.objects.aggregate(Max('id'))
        max=list(max_id_dict.values())[0]
        min_id_dict=Musician.objects.aggregate(Min('id'))
        min=list(min_id_dict.values())[0]

        for _ in range(0, len(albums)):
            album_name=fake.unique.album_names()
            date=fake.date()
            Album.objects.create(name=album_name, 
            release_date=date,
            artist_id=fake.random_element(elements=tuple(range(min, max)))
            )
        for _ in range(0, len(concerts)):
            concert_name=fake.unique.concert_names()
            concert_location=fake.city()
            artists_id=fake.random_choices(elements=tuple(range(min, max)))
            c1=Concert.objects.create(
                name=concert_name,
                location=concert_location,
            )
            for i in artists_id:
                m1=Musician.objects.get(pk=i)
                c1.artists.add(m1)





