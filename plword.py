#!/Users/jeff/.pyenv/shims/python

def plword(string):
    pl_string = ''
    for char in string:
        if char in ('a','e','i','o','u'):
            pl_string = string + 'way'
        else:
            string_list = list(string)
            first_letter = string_list[0]
            string_list.pop(0)
            string_list.append(first_letter)
            string_list.append('ay')
            pl_string = ''.join(string_list)
        break
    return pl_string

def main():
    print(plword('jeff'))
    print(plword('apple'))

if __name__ == '__main__':
    main()
