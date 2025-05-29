# Product trend analysist back-end

Repository ini berisi kode untuk layanan back-end pada proyek product trend analysist

#### Persiapan

- Tools :

  - python : 3.12.7
  - pip : 25.1.1
  - mysql : 10.4.32
  - xampp : 3.3.0

- Setup environtment

  - Download python melalui [link](https://www.python.org/downloads/) berikut
  - Install pip melalui [panduan](https://packaging.python.org/en/latest/tutorials/installing-packages/) berikut
  - Install xampp yang menyertakan mysql di dalamnya, melalui [link](https://www.apachefriends.org/download.html) berikut
  - (Opsional) Aktifkan environtment pip atau conda jika menggunakan anaconda package manager. Langkah ini dapat dilewati jika ingin menjalankan proyek tanpa environtment, namun sangat disarankan agar tidak terjadi konflik dengan library lain pada komputer anda. Jika menggunakan pip, maka perintahnya adalah sebagai berikut

  ```bash
  pipenv install #buat pip environment
  pipenv shell #mengaktifkan pip environtment
  ```

  - Install dependecies menggunakan perintah

  ```
  pip install -r requirements.txt
  ```

  - Buka xampp dan jalankan mysql dan apache
  - Buka mysql workspace pada browser melalui link : localhost:[port-apache]/phpmyadmin. _port-apache disesuaikan dengan port pada lokal komputer_
  - Import file db.sql melalui menu import pada mysql workspace
  - Buka terminal lalu jalankan proyek dengan perintah

  ```bash
  python ./main.py
  ```

  - Buka alamat localhost:5000 pada browser <br>
    _note : jika terjadi konflik dengan port 5000, ganti dengan port lain yang tersedia dengan mengupdate kode berikut_

  ```python
  if __name__ == '__main__':
  app.run(debug=True, port=[port]) # ganti [port] dengan port yang tersedia
  ```

  - Proyek siap digunakan
