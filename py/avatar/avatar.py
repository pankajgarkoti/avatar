import random
import py_avataaars as pa  # this library makes and renders the avatars


def randomized_user_avatar(random_string):

    # we use python dictionaries to map integers to avatar attributes
    # this makes it possible for us to use randint() to randomly
    # choose the attributes. further, the dictionaries will be reused when
    # the request will contain the attributes from an avatar make interface (to be implemented)

    filename = random_string + '.png'

    skin_color = {
        1: pa.SkinColor.TANNED,
        2: pa.SkinColor.YELLOW,
        3: pa.SkinColor.PALE,
        4: pa.SkinColor.LIGHT,
        5: pa.SkinColor.BROWN,
        6: pa.SkinColor.DARK_BROWN,
    }

    hair_color = {
        1: pa.HairColor.AUBURN,
        2: pa.HairColor.BLACK,
        3: pa.HairColor.BLONDE,
        4: pa.HairColor.BLONDE_GOLDEN,
        5: pa.HairColor.BROWN,
        6: pa.HairColor.BROWN_DARK,
        7: pa.HairColor.PASTEL_PINK,
        8: pa.HairColor.PLATINUM,
        9: pa.HairColor.RED,
        10: pa.HairColor.SILVER_GRAY,
    }

    top_type = {
        1: pa.TopType.NO_HAIR,
        2: pa.TopType.EYE_PATCH,
        3: pa.TopType.HAT,
        4: pa.TopType.WINTER_HAT1,
        5: pa.TopType.WINTER_HAT2,
        6: pa.TopType.WINTER_HAT3,
        7: pa.TopType.WINTER_HAT4,
        8: pa.TopType.LONG_HAIR_BIG_HAIR,
        9: pa.TopType.LONG_HAIR_BOB,
        10: pa.TopType.LONG_HAIR_BUN,
        11: pa.TopType.LONG_HAIR_CURLY,
        12: pa.TopType.LONG_HAIR_CURVY,
        13: pa.TopType.LONG_HAIR_DREADS,
        14: pa.TopType.LONG_HAIR_FRIDA,
        15: pa.TopType.LONG_HAIR_FRO,
        16: pa.TopType.LONG_HAIR_FRO_BAND,
        17: pa.TopType.LONG_HAIR_NOT_TOO_LONG,
        18: pa.TopType.LONG_HAIR_SHAVED_SIDES,
        19: pa.TopType.LONG_HAIR_MIA_WALLACE,
        20: pa.TopType.LONG_HAIR_STRAIGHT,
        21: pa.TopType.LONG_HAIR_STRAIGHT2,
        22: pa.TopType.LONG_HAIR_STRAIGHT_STRAND,
        23: pa.TopType.SHORT_HAIR_DREADS_01,
        24: pa.TopType.SHORT_HAIR_DREADS_02,
        25: pa.TopType.SHORT_HAIR_FRIZZLE,
        26: pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
        27: pa.TopType.SHORT_HAIR_SHORT_CURLY,
        28: pa.TopType.SHORT_HAIR_SHORT_FLAT,
        29: pa.TopType.SHORT_HAIR_SHORT_ROUND,
        30: pa.TopType.SHORT_HAIR_SHORT_WAVED,
        31: pa.TopType.SHORT_HAIR_SIDES,
        32: pa.TopType.SHORT_HAIR_THE_CAESAR,
        33: pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART,
    }

    facial_hair_type = {
        1: pa.FacialHairType.DEFAULT,
        2: pa.FacialHairType.BEARD_MEDIUM,
        3: pa.FacialHairType.BEARD_LIGHT,
        4: pa.FacialHairType.BEARD_MAJESTIC,
        5: pa.FacialHairType.MOUSTACHE_FANCY,
        6: pa.FacialHairType.MOUSTACHE_MAGNUM,
    }

    cloth_type = {
        1: pa.ClotheType.BLAZER_SHIRT,
        2: pa.ClotheType.BLAZER_SWEATER,
        3: pa.ClotheType.COLLAR_SWEATER,
        4: pa.ClotheType.GRAPHIC_SHIRT,
        5: pa.ClotheType.HOODIE,
        6: pa.ClotheType.OVERALL,
        7: pa.ClotheType.SHIRT_CREW_NECK,
        8: pa.ClotheType.SHIRT_SCOOP_NECK,
        9: pa.ClotheType.SHIRT_V_NECK,

    }

    cloth_graphic_type = {
        1: pa.ClotheGraphicType.BAT,
        2: pa.ClotheGraphicType.CUMBIA,
        3: pa.ClotheGraphicType.DEER,
        4: pa.ClotheGraphicType.DIAMOND,
        5: pa.ClotheGraphicType.HOLA,
        6: pa.ClotheGraphicType.PIZZA,
        7: pa.ClotheGraphicType.RESIST,
        8: pa.ClotheGraphicType.SELENA,
        9: pa.ClotheGraphicType.BEAR,
        10: pa.ClotheGraphicType.SKULL_OUTLINE,
        11: pa.ClotheGraphicType.SKULL,
    }

    color = {
        1: pa.Color.BLACK,
        2: pa.Color.BLUE_01,
        3: pa.Color.BLUE_02,
        4: pa.Color.BLUE_03,
        5: pa.Color.GRAY_01,
        6: pa.Color.GRAY_02,
        7: pa.Color.HEATHER,
        8: pa.Color.PASTEL_BLUE,
        9: pa.Color.PASTEL_GREEN,
        10: pa.Color.PASTEL_ORANGE,
        11: pa.Color.PASTEL_RED,
        12: pa.Color.PASTEL_YELLOW,
        13: pa.Color.PINK,
        14: pa.Color.RED,
        15: pa.Color.WHITE,
    }  # the color attributes will also be used in hat color.

    mouth_type = {
        1: pa.MouthType.DEFAULT,
        2: pa.MouthType.CONCERNED,
        3: pa.MouthType.DISBELIEF,
        4: pa.MouthType.SMILE,
        5: pa.MouthType.SAD,
        6: pa.MouthType.SERIOUS,
        7: pa.MouthType.TONGUE,
        8: pa.MouthType.TWINKLE,
    }

    eyes_type = {
        1: pa.EyesType.DEFAULT,
        2: pa.EyesType.CLOSE,
        3: pa.EyesType.CRY,
        4: pa.EyesType.DIZZY,
        5: pa.EyesType.EYE_ROLL,
        6: pa.EyesType.HAPPY,
        7: pa.EyesType.HEARTS,
        8: pa.EyesType.SIDE,
        9: pa.EyesType.SQUINT,
        10: pa.EyesType.SURPRISED,
        11: pa.EyesType.WINK,
        12: pa.EyesType.WINK_WACKY,
    }

    eyebrow_type = {
        1: pa.EyebrowType.DEFAULT,
        2: pa.EyebrowType.DEFAULT_NATURAL,
        3: pa.EyebrowType.ANGRY,
        4: pa.EyebrowType.ANGRY_NATURAL,
        5: pa.EyebrowType.FLAT_NATURAL,
        6: pa.EyebrowType.RAISED_EXCITED,
        7: pa.EyebrowType.RAISED_EXCITED_NATURAL,
        8: pa.EyebrowType.SAD_CONCERNED,
        9: pa.EyebrowType.SAD_CONCERNED_NATURAL,
        10: pa.EyebrowType.UNI_BROW_NATURAL,
        11: pa.EyebrowType.UP_DOWN,
        13: pa.EyebrowType.UP_DOWN_NATURAL,
        14: pa.EyebrowType.FROWN_NATURAL,
    }

    accessories_type = {
        1: pa.AccessoriesType.DEFAULT,
        2: pa.AccessoriesType.KURT,
        3: pa.AccessoriesType.PRESCRIPTION_01,
        4: pa.AccessoriesType.PRESCRIPTION_02,
        5: pa.AccessoriesType.ROUND,
        6: pa.AccessoriesType.SUNGLASSES,
        7: pa.AccessoriesType.WAYFARERS,
    }

    try:
        avatar = pa.PyAvataaar(
            style=pa.AvatarStyle.CIRCLE,
            background_color=color[random.randint(1, 15)],
            skin_color=skin_color[random.randint(1, 6)],
            hair_color=hair_color[random.randint(1, 10)],
            top_type=top_type[random.randint(1, 33)],
            #facial_hair_type=facial_hair_type[random.randint(1, 6)],
            facial_hair_color=hair_color[random.randint(1, 10)],
            hat_color=color[random.randint(1, 15)],
            clothe_type=cloth_type[random.randint(1, 9)],
            clothe_graphic_type=cloth_graphic_type[random.randint(1, 11)],
            clothe_color=color[random.randint(1, 15)],
            mouth_type=mouth_type[random.randint(1, 8)],
            eye_type=eyes_type[random.randint(1, 12)],
            eyebrow_type=eyebrow_type[random.randint(1, 14)],
            nose_type=pa.NoseType.DEFAULT,
            accessories_type=accessories_type[random.randint(1, 7)],
        )
        avatar.render_png_file(filename)
        return (True, filename)

    except Exception as exc:
        print(exc)
        return (False, None)