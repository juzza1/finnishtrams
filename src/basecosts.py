def write_basecosts(costs, path):
    with open(path, 'wab') as f:
        f.write("basecost {\n")
        for row in costs:
            if 'PR' in row['id']:
                f.write('%s: %s;\n' % (row['id'], row['multiplier']))
            else:
                continue
        f.write('}')
#
