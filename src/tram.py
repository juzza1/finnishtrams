from string import Template

from cargos import Cargos
import generic_functions as gen

class Tram(object):
    
    def __init__(self, kwargs, cargos):
        """Initialize values from spreadsheet"""
        self.name = kwargs.get('name')
        self.num_id = kwargs.get('num_id')
        self.long_name = kwargs.get('long_name')
        self.feature = kwargs.get('feature')
        self.climates = kwargs.get('climates', 'all')
        self.intr = kwargs.get('intr', '0')
        self.model_life = kwargs.get('model_life', 'VEHICLE_NEVER_EXPIRES')
        self.vehicle_life = kwargs.get('vehicle_life', '255')
        self.reliability_decay = kwargs.get('reliability_decay', '20')
        self.allow_cargo = kwargs.get('allow_cargo')
        self.allow_cargo_class = kwargs.get('allow_cargo_class')
        self.disallow_cargo_class = kwargs.get('disallow_cargo_class')
        self.loading_speed = kwargs.get('load_speed', '5')
        self.cost_factor = kwargs.get('cost_factor', '0')
        self.run_cost_factor = kwargs.get('run_cost_factor', '0')
        self.cargo_age = kwargs.get('cargo_age')
        self.speed = kwargs.get('speed', '0 km/h')
        self.flags = kwargs.get('flags')
        self.run_cost_base = kwargs.get('run_cost_base')
        self.power = kwargs.get('power', '0 hpM')
        self.weight = kwargs.get('weight', '1 ton')
        self.te_coef = kwargs.get('te_coef', '0.3')
        self.air_drag = kwargs.get('air_drag')
        self.real_livery = kwargs.get('real_livery')
        self.refit_livery = kwargs.get('refit_livery')
        self.capacity = kwargs.get('capacity', '0')
        self.length = gen.to_list(kwargs.get('length', '8'))
        self.visual_eff = kwargs.get('visual_eff')
        self.visual_eff_offset = gen.to_list(kwargs.get('visual_eff_offset', '0'))
        self.articulated_id = gen.to_list(kwargs.get('articulated_id'))
        self.sprite_src = gen.to_list(kwargs.get('sprite_src'))
        self.sprite_row = gen.to_list(kwargs.get('sprite_row', '0'))

        self.flags = self.parse_flags()
        self.visual_eff = self.parse_visual()

        # Init disallowed cargos
        self.disallow_cargo = cargos.out(gen.to_list(self.allow_cargo))

    def parse_flags(self):
        """Parse misc. flags"""
        self.outflags = []
        self.ottdflags = [
            'ROADVEH_FLAG_TRAM',
            'ROADVEH_FLAG_2CC',
            'ROADVEH_FLAG_AUTOREFIT',
            'ROADVEH_FLAG_NO_BREAKDOWN_SMOKE'
            ]
        self.flags = gen.to_list(self.flags)
        self.flags = gen.to_upper(self.flags)
        for i in self.flags:
            for j in self.ottdflags:
                if i in j:
                    self.outflags.append(j)
        # Convert this list into a string, flags separated by a comma and space 
        return ', '.join(self.outflags)

    def parse_visual(self):
        """Parse visual effect"""
        self.outvisuals = []
        self.ottdvisuals = [
            'VISUAL_EFFECT_DEFAULT',
            'VISUAL_EFFECT_STEAM',
            'VISUAL_EFFECT_DIESEL',
            'VISUAL_EFFECT_ELECTRIC',
            'VISUAL_EFFECT_DISABLE'
            ]
        self.visual_eff = gen.to_list(self.visual_eff) 
        self.visual_eff = gen.to_upper(self.visual_eff) 
        for i in self.visual_eff:
            for j in self.ottdvisuals:
                if i == '0':
                    self.outvisuals.append(self.ottdvisuals[4])
                    break
                elif i in j:
                    self.outvisuals.append(j)
                    break
                else:
                    continue
        return self.outvisuals

    def sprites_out(self, f, gfxpath):
        """Write & parse spritesets and spritegroups"""
        # Purchase window sprite
        f.write((
                 'spriteset(spriteset_{0}_purchase, "{1}{0}_loaded.png") {{ '
                 'template_purchase() }}\n'
                ).format(self.name, gfxpath))

        # Spritesets and groups for each articulated part
        for i, (l, s, r) in enumerate(zip(self.length, self.sprite_src,
                                          self.sprite_row)):
            spr = (
                   'spriteset(spriteset_{0}_{6}_{2}, "{1}{4}_{6}.png") {{ '
                   'template_tram({3}, {5}) }}\n'
                  )
            sprgrp = (
                      'spritegroup spritegroup_{0}_{1} {{\n'
                      'loading: spriteset_{0}_loading_{1};\n'
                      'loaded: spriteset_{0}_loaded_{1};\n'
                      '}}\n'
                     )
            f.write(spr.format(self.name, gfxpath, i, l, s, r, 'loaded'))
            f.write(spr.format(self.name, gfxpath, i, l, s, r, 'loading'))
            f.write(sprgrp.format(self.name, i))

        # Gfx switch only needed for articulated vehicle
        if self.length > 1:
            f.write(('switch(FEAT_ROADVEH, SELF, switch_{0}_gfx, '
                     'position_in_vehid_chain) {{\n').format(self.name))

            for i, l in enumerate(self.length):
                f.write('{1}: spritegroup_{0}_{1};\n'.format(self.name, i))

            f.write('}\n')

        # Recolouring switches, hardcoded for now
        recols = ['2cc', 'real', 'rand_2cc', 'rand_1cc', 'rainbow']

        for i, col in enumerate(recols):
            f.write((
                     'switch(FEAT_ROADVEH, SELF, switch_{0}_recolour_def_{1}, '
                     'cargo_subtype) {{\n'
                    ).format(self.name, col))
            for j, liv in enumerate(self.refit_livery):
                f.write('switch_{0}_refit_{1}').format(self.name, liv)

        f.write((
                 'switch(FEAT_ROADVEH, SELF, switch_{0}_recolour, '
                 'param_default_livery) {{\n'
                ).format(self.name))

        for i, col in enumerate(recols):
            f.write('{1}: switch_{0}_recolour_def_{2};\n'.format(
                    self.name, i, col))

        f.write('}\n')

    def props_out(self, f):
        """Replace values in python template string. Some values in lists need
        to be inserted as separate keywords, because template string doesn't
        seem to support slice indices
        """

        self.props_temp = Template(
            'item(FEAT_ROADVEHS, item_${name}, ${num_id}) {\n'

            'property {\n'

            'name: string(STR_NAME_${name});\n'
            'climates_available: ${climates};\n'
            'introduction_date: date(${intr}, 01, 01);\n'
            'model_life: ${model_life};\n'
            'vehicle_life: ${vehicle_life};\n'
            'reliability_decay: ${reliability_decay};\n'
            'refittable_cargo_classes: bitmask(${allow_cargo_class});\n'
            'non_refittable_cargo_classes: bitmask(${disallow_cargo_class});\n'
            'cargo_allow_refit: [${allow_cargo}];\n'
            'cargo_disallow_refit: [${disallow_cargo}];\n'
            'loading_speed: ${loading_speed};\n'
            'cost_factor: ${cost_factor};\n'
            'running_cost_factor: ${run_cost_factor};\n'
            'cargo_age_period: ${cargo_age};\n'

            'sprite_id: SPRITE_ID_NEW_ROADVEH;\n'
            'speed: ${speed};\n'
            'misc_flags: bitmask(${flags});\n'
            'refit_cost: 0;\n'
            'running_cost_base: ${run_cost_base};\n'
            'power: ${power};\n'
            'weight: ${weight};\n'
            'tractive_effort_coefficient: ${te_coef};\n'
            'air_drag_coefficient: ${air_drag};\n'
            '//default_cargo_type: ;\n'
            'cargo_capacity: 1;\n'
            'visual_effect: visual_effect(${visual_eff}, ${visual_eff_offset});\n'
            'length: ${length};\n'

            '}\n'

            '}\n'
        )
        f.write(self.props_temp.substitute(
            self.__dict__,
            visual_eff=self.visual_eff[0],
            visual_eff_offset=self.visual_eff_offset[0],
            length=self.length[0]
        ))

    def graphs_out(self, f):
        f.write('graphics {\n')
        f.write('cargo_capacity: {0};\n'.format(
            int(round(int(self.capacity) / len(self.length)))))
        f.write((
                'purchase: spriteset_{0}_purchase;\n'
                'colour_mapping: switch_{0}_recolour;\n'
                ).format(self.name))
        if len(self.length) == 1:
            f.write('default: spritegroup_{0};\n'.format(self.name))
        else:
            f.write(('default: switch_{0}_gfx;\n'
                     'length: switch_{0}_length;\n'
                     'articulated_part: switch_{0}_articulated;\n'
                     'visual_effect: switch_{0}_visual:\n'
                    ).format(self.name))
        f.write('}\n')

    def all_out(self, buildpath, gfxpath):
        with open(buildpath % self.name, 'wb') as f:
            self.sprites_out(f, gfxpath)
            self.props_out(f)
            self.graphs_out(f)
