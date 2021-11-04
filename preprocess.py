import csv
import re


def read_csv(filepath, keep_header=False):
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        raw = [r for r in reader]

        if not keep_header:
            return raw[1:]

        return raw


def process_groceries(raw_data, no_repeat=True):
    transactions = [
        [
            item.strip() for item in r[1].strip(' {}').split(',')
        ] for r in raw_data]
    if no_repeat:
        transactions = [list(set(t)) for t in transactions]

    return transactions


def read_sessions(filepath):
    with open(filepath, encoding='utf-8') as f:
        return [r.strip() for r in f.readlines() if r != '`']


# CMD = 0
# FLAG = 1
# ARGS = 2
# JOINMETA = 3
# ENDMETA = 4
# PAIRMETA = 5
# SOF = 6
# EOF = 7


# def parse_token(token):
#     if token == '**SOF**':
#         return SOF
#     if token == '**EOF**':
#         return EOF
#     if token.isalpha():
#         return CMD
#     if token[0] == '-':
#         return FLAG
#     if re.match('<[1-9]\d*>', token):
#         return ARGS
#     if re.match(r'^[<>\|\$#;\\]|(&&).*$', token):
#         return JOINMETA
#     if re.match(r'[\[\]`\(\)]', token):
#         return PAIRMETA

#     # else regard as end
#     return ENDMETA


# def process_sessions(raw_data):
#     sessions = []
#     sess = []
#     line = []
#     pair_stack = []
#     continuing = False
#     for r in raw_data:
#         token = parse_token(r)
#         if token == SOF:
#             # a new session
#             sess = []
#         elif token == EOF:
#             # end of session
#             if len(line != 0):
#                 sess.append(' '.join(line))
#             if len(sess) != 0:
#                 sessions.append(sess)
#         else:
#             if token == CMD:
#                 # a new cmd
#                 if continuing:
#                     line.append(r)
#                     continuing = False
#                 else:
#                     # a new line
#                     sess.append(' '.join(line))
#                     line = []
#             elif token == FLAG or token == ARGS or token == ENDMETA:
#                 line.append(r)
#             elif

#     return sessions


def is_cmd(tok):
    return len(tok) > 0 and tok[0] != '-' and re.search('[a-zA-Z]', tok) is not None


def process_sessions(raw_data, cmd_only=False, no_repeat=True):
    sessions = []
    sess = []
    for r in raw_data:
        if r == "**SOF**":
            # a new session
            sess = []
        elif r == "**EOF**":
            # end of session
            if len(sess) != 0:
                sessions.append(sess)
        else:
            if cmd_only and not is_cmd(r):
                continue
            if no_repeat and r in sess:
                continue
            sess.append(r)

    return sessions


if __name__ == '__main__':
    # test read csv
    print('========== raed csv test start ==========')
    gro_raw = read_csv('./dataset/GroceryStore/Groceries.csv')
    print(len(gro_raw))
    # for r in gro_raw:
    #     print(r)
    print(gro_raw[:5])
    print('========== read csv test finish ==========')

    # test process groceries
    print('========== process groceries start ==========')
    tra = process_groceries(gro_raw)
    print(len(tra))
    # for t in tra:
    #     print(t)
    print(tra[:5])
    print("========== process groceries finish ==========")

    # test read all lines
    print('========== read sessions start ==========')
    sess_raw = read_sessions('./dataset/UNIX_usage/USER0/sanitized_all.981115184025')
    print(len(sess_raw))
    # for r in sess_raw:
    #     print(r)
    print(sess_raw[:5])
    print('========== read sessions finish ==========')

    # test process sessions
    print('========== process sessions start ==========')
    sess = process_sessions(sess_raw, True)
    print(len(sess))
    # for s in sess:
    #     print(s)
    print(sess[:5])
    print('========== process sessions finish ==========')


