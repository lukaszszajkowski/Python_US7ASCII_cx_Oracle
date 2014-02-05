import os
import logging
import cx_Oracle
import binascii


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


def updateWE8MSWIN1252asUS7ASCI():
    print (">>> run updateWE8MSWIN1252asUS7ASCI ")

    #os.environ["NLS_LANG"] = "ENGLISH_UNITED KINGDOM.US7ASCII"
    connection = get_connection()

    cursor = connection.cursor()

    answer = "Ła£ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷"
    answer_hex = []
    lost_characters = []
    ext_message = ". All characters saved."
    for ch in answer:
        if ord(ch) <= 255:
            answer_hex.append(format(ord(ch), 'X'))
        else:
            lost_characters.append(ch)
            ext_message = ", but some characters were lost: %s" %(', '.join(lost_characters))

    answer_hex = ''.join(answer_hex)
    print ("answer_hex %s" %answer_hex)

    user_id = '...'
    cursor.execute("UPDATE WW_SECURITY_HINTS SET ANSWER = UTL_RAW.CAST_TO_VARCHAR2(hextoraw('%s')) WHERE USERID = '%s'"
                   %(answer_hex, user_id))
    connection.commit()

    print("Data %s saved %s" %(answer, ext_message))
    cursor.close()
    connection.close()


def readWE8MSWIN1252asUS7ASCI():
    print (">>> run readWE8MSWIN1252asUS7ASCI ")
    connection = get_connection()

    #os.environ["NLS_LANG"] = "ENGLISH_UNITED KINGDOM.US7ASCII"
    print("version=%s\nencoding=%s\tnencoding=%s\tmaxBytesPerCharacter=%s" % (connection.version, connection.encoding,
                                                                              connection.nencoding,
                                                                              connection.maxBytesPerCharacter))
    cursor = connection.cursor()

    cursor.execute("SELECT USERENV ('language') FROM DUAL")
    for result in cursor:
        print("%s" % (result))

    cursor.execute(
        "select rawtohex(utl_raw.cast_to_raw(ANSWER)) from ww_security_hints where userid = '...'")
    for rawValue in cursor:
        answer = ''.join(['%c' % iterating_var for iterating_var in binascii.unhexlify(rawValue[0])])

    print('answer = %s' % answer)

    characters = []
    for character in answer:
        characters.append("[%d][%c]" %(ord(character), character))
    print("Debug %s" % (', '.join(characters)))

    cursor.close()
    connection.close()


if __name__ == '__main__':
    readWE8MSWIN1252asUS7ASCI()
    updateWE8MSWIN1252asUS7ASCI()
