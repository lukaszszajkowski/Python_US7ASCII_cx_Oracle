Python_US7ASCII_cx_Oracle
=========================

Problem with displaying national characters from “ENGLISH_UNITED KINGDOM.US7ASCII” Oracle 11 database using Python cx_Oracle 5.1.2 and "NLS_LANG" environment variable.


In Oracle 11 Database I created SECURITY_HINTS.ANSWER="£aÀÁÂÃÄÅÆÇÈ".
Now when using cx_Oracle and default NLS_LANG and I get "¿a¿¿¿¿¿¿¿¿¿"
and when usinx NLS_LANG="ENGLISH_UNITED KINGDOM.US7ASCII" I get
"UnicodeDecodeError: 'ascii' codec can't decode byte 0xa3 in position 0: ordinal not in range(128)"

see log below.

How to display SECURITY_HINTS.ANSWER as "£aÀÁÂÃÄÅÆÇÈ" ??



```
run test_nls for None
version=11.1.0.7.0
encoding=WINDOWS-1252	nencoding=WINDOWS-1252	maxBytesPerCharacter=1
ENGLISH_UNITED KINGDOM.US7ASCII
query returned [¿a¿¿¿¿¿¿¿¿¿]
str  [191] [97] [191] [191] [191] [191] [191] [191] [191] [191] [191


run test_nls for .AL32UTF8
version=11.1.0.7.0
encoding=UTF-8	nencoding=UTF-8	maxBytesPerCharacter=4
AMERICAN_AMERICA.US7ASCII
query returned [�a���������]
str  [65533] [97] [65533] [65533] [65533] [65533] [65533] [65533] [65533] [65533] [65533]

run test_nls for ENGLISH_UNITED KINGDOM.US7ASCII
version=11.1.0.7.0
encoding=US-ASCII	nencoding=US-ASCII	maxBytesPerCharacter=1
ENGLISH_UNITED KINGDOM.US7ASCII
Traceback (most recent call last):
  File "C:/dev/tmp/Python_US7ASCII_cx_Oracle/showUS7ASCII.py", line 71, in <module>
    test_nls("ENGLISH_UNITED KINGDOM.US7ASCII")
  File "C:/dev/tmp/Python_US7ASCII_cx_Oracle/showUS7ASCII.py", line 55, in test_nls
    for rawValue in cursor:
UnicodeDecodeError: 'ascii' codec can't decode byte 0xa3 in position 0: ordinal not in range(128)
```
