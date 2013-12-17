def Listify(string):
    "Convert a comma-separated string to a list"
    return string.split(',')

def Intify(list_):
    "Convert each element of a list into an integer"
    return map(int, list_)
    
def Upper(list_):
    "Convert each string in a list to uppercase"
    return map(str.upper, list_)

class Tram(object):
    
    def ParseFlags(self, inflags):
        "Parse misc. flags"
        outflags = []
        ottdflags = [
            'ROADVEH_FLAG_TRAM' ,
            'ROADVEH_FLAG_2CC',
            'ROADVEH_FLAG_AUTOREFIT',
            'ROADVEH_FLAG_NO_BREAKDOWN_SMOKE']
        if inflags == '0':
            outflags = 0
        else:
            inflags = Listify(inflags)
            inflags = Upper(inflags)
            for i in inflags:
                for j in ottdflags:
                    if i in j:
                        outflags.append(j)
        return outflags

    def __init__(self, **kwargs):
        "Get values from csv"
        self.num_id = kwargs.get('num_id')
        # These properties don't need any additional parsing
        self.name = kwargs.get('name')
        self.intr = kwargs.get('intr', '0')
        self.model_life = kwargs.get('model_life', 'VEHICLE_NEVER_EXPIRES')
        self.vehicle_life = kwargs.get('vehicle_life', '255')
        self.reliability_decay = kwargs.get('reliability_decay', '20')
        self.loading_speed = kwargs.get('load_speed', '5')
        self.cost_factor = kwargs.get('cost_factor', '0')
        self.running_cost_factor = kwargs.get('run_cost_factor', '0')
        self.speed = kwargs.get('speed', '100 km/h')
        self.power = kwargs.get('power', '100 hpM')
        self.weight = kwargs.get('weight', '1 ton')
        self.te_coef = kwargs.get('te_coef', '0.3')
        # Additional values
        self.long_name = kwargs.get('long_name', '')
        self.flags = kwargs.get('flags', '')
        self.capacity = kwargs.get('capacity', '0')
        self.cons_lengths = kwargs.get('length', '8')
        self.refit_gfx = kwargs.get('refit_gfx', '')
        self.visual_sfx_type = kwargs.get('visual_sfx_type', 'disable')
        self.visual_sfx_pos = kwargs.get('visual_sfx_pos', '0')
        self.visual_sfx_offset = kwargs.get('visual_sfx_offset', '0')
        self.sprite_rows = kwargs.get('sprite_rows', '0')
        self.recolor = kwargs.get('recolor', '')
        # Properties which require parsing
        self.misc_flags = self.ParseFlags(self.flags)
        self.cargo_capacity = 0
        self.visual_effect = 0
        self.length = 0

#        print self.misc_flags
