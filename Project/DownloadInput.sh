echo "Which day is it?: "
read Day
mkdir Day$Day
touch Day$Day/main.py Day$Day/test.txt

Session=$(cat ./.cookie)
echo $Session

curl "https://adventofcode.com/2021/day/$Day/input" --cookie "session=$Session" > Day$Day/input.txt
