import argparse

def format_line(line):
    '''
    Warning: this adds a newline add the end
    '''
    stripped_line = line.lstrip().rstrip()
    section_begin = (stripped_line == 'Show') or (stripped_line == 'Hide')
    if len(stripped_line) is 0 or stripped_line.startswith('#') or section_begin:
        return stripped_line
    return '\t%s' % stripped_line

def format_filter_file(file_path):
    new_content = str()
    with open(file_path) as filter_file:
        for line in filter_file.readlines():
            new_content += format_line(line) + '\n'
    return new_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-i', '--in_place', type=bool, default=True)
    parser.add_argument('-o', '--out', default=None)
    args = parser.parse_args()
    new_content = format_filter_file(args.path)
    new_file_name = args.path if args.in_place else "%s.formatted" % (args.path) if args.out is None else args.out
    with open(new_file_name, 'w+') as outfile:
        outfile.write(new_content)