# This is readme for Skeleton Project

Silahkan kemudian untu mengubah nama project nya atau url nya disesuaikan saja, termasuk repo nya.
tapi ini adalah template awalnya.

Beberapa yang perlu di perhatikan adalah:

# Installation
1. Buatlah terlebih dahulu virtual env  -> virtualenv -p python3 venv, satu root dengan root folder project
2. kemudian aktifkan virtualenv -> source venv/bin/activate
3. kemudian masuk ke dalam folder project, install semua modules yg digunakan
   pip install -r requirements.txt

4. Jika nanti menambahkan satu atau banyak modules, catat kembali semua modules yg dipakai, pake
   pip freeze > requirements.txt

# Database
1. database default menggunakan sqlite3,
2. bisa multiple databases: tambahkan config di settings
3. jika ingin konek ke database yg sudah existing, buat app khusus utk database tersebut,
   lalu buatlah model yg sesuai dengan database tsb, gunakan perintah

   ## python manage.py inspectdb --database mydatabase > myapp/models.py

   (sumber : https://django-book.readthedocs.io/en/latest/chapter18.html)
   (https://stackoverflow.com/questions/37581885/django-using-more-than-one-database-with-inspectdb)

4. Untuk menggunakan database2 yg berbeda, gunakan command .using('mydatabase')
  misalkan Paymnet.objects.using('switching').all() --> artinya akan konek ke tabel payment di database switching
