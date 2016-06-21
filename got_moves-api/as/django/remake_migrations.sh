echo "remaking migrations for $1.."
echo "**before**"
ls $1/migrations
echo "**removing**"
rm -rf $1/migrations/0001*
ls $1/migrations
echo "**makemigrations**"
python manage.py makemigrations $1
ls $1/migrations
