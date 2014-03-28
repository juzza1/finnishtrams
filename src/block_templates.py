def spriteset(name, spec, path, template, length=None, row=None):
    """Spriteset template"""
    spriteset = (
                 'spriteset(spriteset_{0}_{1}, "{2}") {{ {3}'
                ).format(name, spec, path, template, length, row)
    if length and row:
        spriteset += '({0}, {1}) '.format(length, row)
    else:
        spriteset += '() '
    spriteset += '}\n'
    return spriteset

def spritegroup(name, spec, loading_name, loaded_name):
    spritegroup = (
                   'spritegroup spritegroup_{0}_{1} {{\n'
                   'loading: spriteset_{0}_{2};\n'
                   'loaded: spriteset_{0}_{3};\n'
                  ).format(name, spec, loading_name, loaded_name)
    spritegroup += '}\n'
    return spritegroup

def switch(feature_in, scope_in, name, expression, range_value, def_value):
    """Switch template"""
    features = ['FEAT_TRAINS', 'FEAT_ROADVEHS', 'FEAT_SHIPS', 'FEAT_AIRCRAFT']
    for feature in features:
        if feature_in.upper() in feature:
            feature_out = feature

    scopes = ['SELF', 'PARENT']
    for scope in scopes:
        if scope_in.upper() in scope:
            scope_out = scope

    switch = 'switch(switch_{0}, {1}, {2}, {3}) {{\n'.format(
            feature_out, scope_out, name, expression)
    for i in range_value:
        switch += '{0}: {1};\n'.format(range_value[0], range_value[1])
    switch += '{0};\n'.format(def_value)
    switch += '}\n'
    return switch
