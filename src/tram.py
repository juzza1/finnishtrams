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
        # Convert this list into a string, flags separated by a comma and space 
        flagsout = ', '.join(outflags)
        return flagsout

    def ConsistInfo(self, *args):
        """Parse length and misc. info for each part in articulated consist.
        Returns a list of lists. This function can only handle integers. Check
        function call to see what values are passed onto this function."""
        consinfo = []
        for index, arg in enumerate(args):
            partinfo = []
            arg = Listify(arg)
            arg = Intify(arg)
            consinfo.append(arg)
        # Now we have a list of lists. We need to reorganize this
        # Get consist length from first list
        length = len(consinfo[0])
        cons = []
        for enum, i in enumerate(range(length)):
            part = []
            for j in consinfo:
                part.append(j[enum])
            cons.append(part)
        # Length of this list = the amount of parts in the consist
        print length
        return cons

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
        self.lengths = kwargs.get('lengths', '8')
        self.refit_gfx = kwargs.get('refit_gfx', '')
        self.visual_sfx_type = kwargs.get('visual_sfx_type', 'disable')
        self.visual_sfx_enabled = kwargs.get('visual_sfx_enabled', '0')
        self.visual_sfx_offset = kwargs.get('visual_sfx_offset', '0')
        self.sprite_rows = kwargs.get('sprite_rows', '0')
        self.recolor = kwargs.get('recolor', '')
        # Parse consist info. Length is len(consinfo)
        self.consinfo = self.ConsistInfo(self.lengths,
                                         self.visual_sfx_enabled,
                                         self.visual_sfx_offset,
                                         self.sprite_rows)
        # Properties which require parsing
        self.misc_flags = self.ParseFlags(self.flags)
        # Capacity is (capacity from csv / number of parts in consist)
        self.cargo_capacity =int(round(int(self.capacity) / len(self.consinfo)))
        self.visual_effect = 0
        # Length property is taken from first element of consist info
        self.length = self.consinfo[0][0]

        # More values, calculated & not in tracking table

        print self.consinfo
