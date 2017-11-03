XCFP := xcf2png
XCFP_FLAGS := --autocrop --background \\\#FFFFFF --dissolve --output

build/test_4.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 4
build/test4_6w.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 4_6w
build/test_6.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 6
build/test_6a.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 6_arti
build/test_8.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 8
build/test8_6w.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 8_6w

build/mlnrviii_front.png: src/gfx/xcf/vehs/mlnrviii.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 1 panto
build/mlnrviii_front_open.png: src/gfx/xcf/vehs/mlnrviii.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 1 doors_1 panto
build/mlnrviii_middle.png: src/gfx/xcf/vehs/mlnrviii.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2
build/mlnrviii_middle_open.png: src/gfx/xcf/vehs/mlnrviii.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2 doors_2
build/mlnrviii_rear.png: src/gfx/xcf/vehs/mlnrviii.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 3
build/mlnrviii_rear_open.png: src/gfx/xcf/vehs/mlnrviii.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 3 doors_3
