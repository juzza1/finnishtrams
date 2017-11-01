XCFP := xcf2png
XCFP_FLAGS := --autocrop --background \\\#FFFFFF --dissolve --output

build/test_8.png:
	$(XCFP) $(XCFP_FLAGS) $@ src/gfx/xcf/testveh.xcf bg 8
build/test_4.png:
	$(XCFP) $(XCFP_FLAGS) $@ src/gfx/xcf/testveh.xcf bg 4
