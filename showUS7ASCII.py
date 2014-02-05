import os
import logging
import cx_Oracle

log = logging.getLogger("main")

def get_connection():
    host = "dev01"
    port = 1521
    tns_name = "..."
    user = "..."
    pwd = '...'
    try:
        tns_name = cx_Oracle.makedsn(host, port, tns_name)
        connection = cx_Oracle.Connection(user=user, password=pwd, dsn=tns_name)
    except Exception as e:
        log.error("%s" %(e))
        return

    return connection


def test_nls(nls_lang=None):
    print (">>> run test_nls for %s" %(nls_lang))
    if nls_lang:
        os.environ["NLS_LANG"] = nls_lang
    os.environ["ORA_NCHAR_LITERAL_REPLACE"] = "TRUE"

    connection = get_connection()
    cursor = connection.cursor()
    print("version=%s\nencoding=%s\tnencoding=%s\tmaxBytesPerCharacter=%s" %(connection.version, connection.encoding,
            connection.nencoding, connection.maxBytesPerCharacter))

    cursor.execute("SELECT USERENV ('language') FROM DUAL")
    for result in cursor:
        print("%s" %(result))

    cursor.execute("select ANSWER from SECURITY_HINTS where USERID = '...'")
    for rawValue in cursor:
        print("query returned [%s]" % (rawValue))
        answer = rawValue[0]
    str = ""
    for iterating_var in answer:
        str = ("%s [%d]" % (str, ord(iterating_var)))

    print ("str %s" %(str))

    cursor.close()
    connection.close()

if __name__ == '__main__':
    test_nls()
    test_nls(".AL32UTF8")
    test_nls("ENGLISH_UNITED KINGDOM.US7ASCII")