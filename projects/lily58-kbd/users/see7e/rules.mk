# ifeq ($(strip $(OLED_DRIVER_ENABLE)), yes)
#     SRC += oled_setup.c
# 	SRC += ocean_dream.c

# 	ifdef OCEAN_DREAM_ENABLE
# 		ifeq ($(strip $(OCEAN_DREAM_ENABLE)), yes)
# 			OPT_DEFS += -DOCEAN_DREAM_ENABLE
#     	endif
# 	endif
# 	ifndef OCEAN_DREAM_ENABLE
# 		OPT_DEFS += -DOCEAN_DREAM_ENABLE
# 	endif

# 	ifdef LUNA_ENABLE
# 		ifeq ($(strip $(LUNA_ENABLE)), yes)
# 			SRC += luna.c
# 			OPT_DEFS += -DLUNA_ENABLE
# 		endif
# 	endif
# 	ifndef LUNA_ENABLE
# 		SRC += luna.c
# 		OPT_DEFS += -DLUNA_ENABLE
# 	endif
# endif

SRC += $(USER_PATH)/oled_setup.c
SRC += $(USER_PATH)/ocean_dream.c

OPT_DEFS += -DOCEAN_DREAM_ENABLE
