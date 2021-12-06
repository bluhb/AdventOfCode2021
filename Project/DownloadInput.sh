echo "Which day is it?: "
read Day
mkdir Day$Day
touch Day$Day/main.py Day$Day/test.txt
cp timer.py Day$Day/
echo "from timer import time" > Day$Day/main.py

Session=$(cat ./.cookie)

curl "https://adventofcode.com/2021/day/$Day/input" --cookie "session=$Session" > Day$Day/input.txt
