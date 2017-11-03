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


build/a3.png: src/gfx/xcf/vehs/a3.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc panto
build/a3_open.png: src/gfx/xcf/vehs/a3.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc doors panto

build/a4.png: src/gfx/xcf/vehs/a4.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc panto
build/a4_open.png: src/gfx/xcf/vehs/a4.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc doors panto

build/a12.png: src/gfx/xcf/vehs/a12.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc panto
build/a12_open.png: src/gfx/xcf/vehs/a12.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc doors panto

build/hmiv.png: src/gfx/xcf/vehs/hmiv.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc panto
build/hmiv_open.png: src/gfx/xcf/vehs/hmiv.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2cc doors panto

build/horse_car.png: src/gfx/xcf/vehs/horse.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg car
build/horse_idle.png: src/gfx/xcf/vehs/horse.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg horse_idle
build/horse_anim1.png: src/gfx/xcf/vehs/horse.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg horse_anim_1
build/horse_anim2.png: src/gfx/xcf/vehs/horse.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg horse_anim_2
build/horse_anim3.png: src/gfx/xcf/vehs/horse.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg horse_anim_3

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

build/mlrvi_1.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 1 panto
build/mlrvi_1_open.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 1 doors_1 panto
build/mlrvi_2_4.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2_4
build/mlrvi_2_4_open.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 2_4 doors_2_4
build/mlrvi_3.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 3
build/mlrvi_5.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 5
build/mlrvi_5_open.png: src/gfx/xcf/vehs/mlrvi.xcf
	$(XCFP) $(XCFP_FLAGS) $@ $< bg 5 doors_5
