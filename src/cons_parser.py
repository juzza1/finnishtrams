import re

class ZoomInfo:
    def __init__(self):
        self.frames = None
        self.render_args = None
        self.src = None

class SpriteDef:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.zlevel_info = {}
        self.png_count = 0

    def __getitem__(self, zlevel):
        assert zlevel in {'z1', 'z4'} # Change in the future
        if zlevel not in self.zlevel_info:
            self.zlevel_info[zlevel] = ZoomInfo()
        return self.zlevel_info[zlevel]

    def output_spriteset(self):
        spriteset_out = ['spriteset({}) {{'.format(self.name)]
        png_name = self.make_8bpp()
        if self.length.isdigit():
            for i in range(0, 8):
                spriteset_out.append(
                    '[0, 0, 0, 0, 0, 0, {}]'.format(png_name))
        else:
            spriteset_out.append(
                '[0, 0, 0, 0, 0, 0, {}]'.format(png_name))
        return '\n'.join(spriteset_out) + ' }'

    def output_alternative_sprites(self):
        alt_out = ['alternative_sprites({}) {{'.format(self.name)]
        if self.length.isdigit():
            for i in range(0, 8):
                alt_out.append(
                    '[0, 0, 0, 0, 0, 0, {}]'.format(self.make_32bpp()))
        else:
            alt_out.append('[0, 0, 0, 0, 0, 0, {}]'.format(self.make_32bpp()))
        return '\n'.join(alt_out) + ' }'

    def output_spriteset_and_alt(self):
        return self.output_spriteset() + '\n' \
               + self.output_alternative_sprites()

    def output_make_rules(self):
        pass

class Parser:
    def __init__(self, cons):
        self.cons = cons
        self.veh_id = 'piss'
        self.sprite_defs = []
        self.parse_sprs()
        print([i.zlevel_info for i in self.sprite_defs])

    def add_sprite_def(self, name, **kwargs):
        # Disallow duplicates
        assert name not in {sprd.name for sprd in self.sprite_defs}
        spr_def = SpriteDef(name, **kwargs)
        self.sprite_defs.append(spr_def)
        return spr_def

    def parse_sprs(self):
        count = 1
        srcs = {s[0]: s[1] for s in re.findall(
                r'^(z\d) (\w+.(?:xcf|blend));', self.cons, re.MULTILINE)}
        sprs = re.findall(r'spr (\w+)\((\w+)\) \{(.+?)\}',
                          self.cons, re.DOTALL)
        for spr in sprs:
            sprite_def = self.add_sprite_def(name=spr[0], length=spr[1])
            zdefs = spr[2].split(';')[:-1] # Ignore last empty split
            for zd in zdefs:
                sprite_def[z].src = srcs[zlevel]
                spl = zd.split(':')
                z = spl[0].strip() # Zoom level
                render_info = spl[1].split(',')
                sprite_def[z].layers = render_info[0].split()
                if '.xcf' in srcs[zlevel]:
                    sprite_def[z].render_args = \
                        [a.strip() for a in render_info[1:]] \
                        if len(render_info) > 1 else None
                elif '.blend' in srcs[zlevel]:
                    sprite_def[z].frames = render_info[1].split()
                    sprite_def[z].render_args = \
                        [a.strip() for a in render_info[2:]] \
                        if len(render_info) > 2 else None
