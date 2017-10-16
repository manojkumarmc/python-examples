
Install dependencies
---------------------
  yum install zlib zlib-devel openssl openssl-devel 

Install Python 3.6 from source 
------------------------------
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz

./configure \
--with-zlib \
--prefix=/usr/local \
--enable-shared \
--enable-unicode=ucs4 \
LD_LIBRARY_PATH=/usr/local/lib64/python363/config

make && make altinstall && make commoninstall

ln -sf /usr/local/lib/libpython3.6m.so /usr/lib64/libpython3.6m.so.1.0


Install Python 2.7 from source
------------------------------
wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz

./configure \
--with-zlib \
--prefix=/usr/local \
--enable-shared \
--enable-unicode=ucs4 \
LD_LIBRARY_PATH=/usr/local/lib64/python2714/config

make && make altinstall && make commoninstall

ln -sf /usr/local/lib/libpython2.7m.so /usr/lib64/libpython2.7m.so.1.0




