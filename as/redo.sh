echo $1
echo "deleting all data w/o booting server..."
rm db*;
echo "remaking migrations for $1.."
if [[ -e $1/migrations ]]; then
	echo "**before**"
	ls $1/migrations
	echo "**removing**"
	rm -rf $1/migrations/000*
	ls $1/migrations
fi
echo "**makemigrations**"
python manage.py makemigrations $1
ls $1/migrations
echo "**migrating**"
python manage.py migrate
bash ~/projects/dollars/as/django/bootserver.sh
