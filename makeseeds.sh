python manage.py dumpdata committee --output committee/seeds.json --indent=2;
python manage.py dumpdata events --output events/seeds.json --indent=2;
python manage.py dumpdata training --output training/seeds.json --indent=2;
python manage.py dumpdata photos --output photos/seeds.json --indent=2;