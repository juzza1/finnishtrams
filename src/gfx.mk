XCFP := xcf2png
XCFP_FLAGS := --autocrop --background \\\#FFFFFF --dissolve --output

build/test_4.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 4
build/test_6.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 6
build/test_6a.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 6_arti
build/test_8.png: src/gfx/xcf/vehs/testveh.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 8
build/arctic_front.png: src/gfx/xcf/vehs/arctic.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg front cat
build/arctic_middle.png: src/gfx/xcf/vehs/arctic.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg middle
build/arctic_rear.png: src/gfx/xcf/vehs/arctic.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg rear
