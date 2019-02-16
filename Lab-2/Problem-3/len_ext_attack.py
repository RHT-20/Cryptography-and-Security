import pymd5


def solve():

    fp = open("3.3_query.txt", "r")
    query = fp.read()
    fp.close()
    print("query: " + query)

    token = query[query.index("=")+1: query.index("&")]
    message = query.replace("token="+token+"&", "")
    print("token: " + token)
    print("message: " + message)

    fp = open("3.3_command3.txt", "r")
    command3 = fp.read()
    fp.close()
    print("command3: " + command3)

    key_len = 8 # given in the question
    msg_len = len(message)
    padding = pymd5.padding((key_len + msg_len) * 8)
    pad_len = len(padding)
    count = (key_len + msg_len + pad_len) * 8
    md5_obj = pymd5.md5(command3, token.decode("hex"), count)
    new_token = md5_obj.hexdigest()
    print("new token: " + new_token)

    extended_query = "token=" + new_token + "&" + message + padding + command3
    print("extended query: " + extended_query)

    fp = open("solution33.txt", "w")
    fp.write(extended_query)
    fp.close()


def verify():

    key = raw_input("Secret key: ")
    query = raw_input("Query: ")
    append = raw_input("Command to extend: ")

    # token without append part
    md5_obj = pymd5.md5(key+query)
    token1 = md5_obj.hexdigest()

    key_len = len(key)
    qry_len = len(query)
    padding = pymd5.padding((key_len + qry_len) * 8)
    pad_len = len(padding)
    count = (key_len + qry_len + pad_len) * 8
    md5_obj = pymd5.md5(append, token1.decode("hex"), count)
    token1 = md5_obj.hexdigest()

    # token for the whole query
    md5_obj = pymd5.md5(key+query+padding+append)
    token2 = md5_obj.hexdigest()

    print("token1: " + token1)
    print("token2: " + token2)

    if token1 == token2:
        print("Token matches.")
    else:
        print("Token doesn't match.")


def main():
    solve()
    verify()


if __name__ == main():
    main()


"""
To verify:
SECRETkey
user=admin&command1=ListFiles&command2=NoOp
&command3=DeleteAllFiles
"""

# Run from Terminal:
# python2 len_ext_attack.py
