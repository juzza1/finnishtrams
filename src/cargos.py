import generic_functions as gen

class Cargos(object):

    def __init__(self, cargos, **kwargs):
        self.cargos = cargos.replace('"', '')
        self.cargos = gen.to_list(self.cargos)

    def out(self, allowed_cargos):
        self.allowed_cargos = allowed_cargos
        return ', '.join(
                    gen.substr_lists(self.cargos, self.allowed_cargos))

    def write_cargotable(self, path):
        with open(path, 'wab') as f:
            f.write("cargotable {\n")
            f.write('    %s' % ', '.join(self.cargos))
            f.write("\n}")
