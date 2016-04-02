echo "remaking migrations for main.."
echo "**before**"
ls main/migrations
rm -rf main/migrations/0001*
echo "**removing**"
ls main/migrations
python manage.py makemigrations
echo "**makemigrations**"
ls main/migrations
bash ~/projects/got_moves/as/django/reset_db.sh