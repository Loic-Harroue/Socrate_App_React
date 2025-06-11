"""Gestion des couleurs pour les clusters.

Les 17 premières couleurs sont les mêmes que VOSviewer.
Les suivantes sont par ordre alphabétique.
Pour définir la liste des clusters, on prend les 17 premières
couleurs et on ajoute aléatoirement dans les suivantes
le nombre de couleurs complémentairement au nombre de clusters.
"""

import random


def get_clusters_colors(nb_clusters):
    """Retourne un tableau contenant les couleurs pour n clusters."""

    if nb_clusters <= NB_COLORS_AS_VOS:
        colors = COLORS[:nb_clusters]

    else:
        colors = COLORS[:NB_COLORS_AS_VOS]
        for i in range(NB_COLORS_AS_VOS, nb_clusters):
            colors.append(COLORS[random.randint(NB_COLORS_AS_VOS, NB_COLORS - 1)])

    return colors


NB_COLORS_AS_VOS = 16
NB_COLORS = 874
COLORS = [{
    'color': 'red',
    'label': "Red",
    'hexa': "#ff0000",
    'red': 255,
    'green': 0,
    'blue': 0
}, {
    'color': 'green_color_wheel_x11_green',
    'label': "Green (Color Wheel) (X11 Green)",
    'hexa': "#00ff00",
    'red': 0,
    'green': 255,
    'blue': 0
}, {
    'color': 'blue',
    'label': "Blue",
    'hexa': "#0000ff",
    'red': 0,
    'green': 0,
    'blue': 255
}, {
    'color': 'violet',
    'label': "Violet",
    'hexa': "#8f00ff",
    'red': 143,
    'green': 0,
    'blue': 255
}, {
    'color': 'cyan',
    'label': "Cyan",
    'hexa': "#00ffff",
    'red': 0,
    'green': 255,
    'blue': 255
}, {
    'color': 'orange_color_wheel',
    'label': "Orange (Color Wheel)",
    'hexa': "#ff7f00",
    'red': 255,
    'green': 127,
    'blue': 0
}, {
    'color': 'brown_traditional',
    'label': "Brown (Traditional)",
    'hexa': "#964b00",
    'red': 150,
    'green': 75,
    'blue': 0
}, {
    'color': 'rose',
    'label': "Rose",
    'hexa': "#ff007f",
    'red': 255,
    'green': 0,
    'blue': 127
}, {
    'color': 'light_red_ochre',
    'label': "Light Red Ochre",
    'hexa': "#e97451",
    'red': 233,
    'green': 116,
    'blue': 81
}, {
    'color': 'light_green',
    'label': "Light Green",
    'hexa': "#90ee90",
    'red': 144,
    'green': 238,
    'blue': 144
}, {
    'color': 'light_blue',
    'label': "Light Blue",
    'hexa': "#add8e6",
    'red': 173,
    'green': 216,
    'blue': 230
}, {
    'color': 'light_pastel_purple',
    'label': "Light Pastel Purple",
    'hexa': "#b19cd9",
    'red': 177,
    'green': 156,
    'blue': 217
}, {
    'color': 'light_cyan',
    'label': "Light Cyan",
    'hexa': "#e0ffff",
    'red': 224,
    'green': 255,
    'blue': 255
}, {
    'color': 'light_apricot',
    'label': "Light Apricot",
    'hexa': "#fdd5b1",
    'red': 253,
    'green': 213,
    'blue': 177
}, {
    'color': 'light_brown',
    'label': "Light Brown",
    'hexa': "#b5651d",
    'red': 181,
    'green': 101,
    'blue': 29
}, {
    'color': 'light_fuchsia_pink',
    'label': "Light Fuchsia Pink",
    'hexa': "#f984ef",
    'red': 249,
    'green': 132,
    'blue': 239
}, {
    'color': 'air_force_blue_raf',
    'label': "Air Force Blue (Raf)",
    'hexa': "#5d8aa8",
    'red': 93,
    'green': 138,
    'blue': 168
}, {
    'color': 'air_force_blue_usaf',
    'label': "Air Force Blue (Usaf)",
    'hexa': "#00308f",
    'red': 0,
    'green': 48,
    'blue': 143
}, {
    'color': 'air_superiority_blue',
    'label': "Air Superiority Blue",
    'hexa': "#72a0c1",
    'red': 114,
    'green': 160,
    'blue': 193
}, {
    'color': 'alabama_crimson',
    'label': "Alabama Crimson",
    'hexa': "#a32638",
    'red': 163,
    'green': 38,
    'blue': 56
}, {
    'color': 'alice_blue',
    'label': "Alice Blue",
    'hexa': "#f0f8ff",
    'red': 240,
    'green': 248,
    'blue': 255
}, {
    'color': 'alizarin_crimson',
    'label': "Alizarin Crimson",
    'hexa': "#e32636",
    'red': 227,
    'green': 38,
    'blue': 54
}, {
    'color': 'alloy_orange',
    'label': "Alloy Orange",
    'hexa': "#c46210",
    'red': 196,
    'green': 98,
    'blue': 16
}, {
    'color': 'almond',
    'label': "Almond",
    'hexa': "#efdecd",
    'red': 239,
    'green': 222,
    'blue': 205
}, {
    'color': 'amaranth',
    'label': "Amaranth",
    'hexa': "#e52b50",
    'red': 229,
    'green': 43,
    'blue': 80
}, {
    'color': 'amber',
    'label': "Amber",
    'hexa': "#ffbf00",
    'red': 255,
    'green': 191,
    'blue': 0
}, {
    'color': 'amber_sae_ece',
    'label': "Amber (Sae/Ece)",
    'hexa': "#ff7e00",
    'red': 255,
    'green': 126,
    'blue': 0
}, {
    'color': 'american_rose',
    'label': "American Rose",
    'hexa': "#ff033e",
    'red': 255,
    'green': 3,
    'blue': 62
}, {
    'color': 'amethyst',
    'label': "Amethyst",
    'hexa': "#9966cc",
    'red': 153,
    'green': 102,
    'blue': 204
}, {
    'color': 'android_green',
    'label': "Android Green",
    'hexa': "#a4c639",
    'red': 164,
    'green': 198,
    'blue': 57
}, {
    'color': 'anti_flash_white',
    'label': "Anti-Flash White",
    'hexa': "#f2f3f4",
    'red': 242,
    'green': 243,
    'blue': 244
}, {
    'color': 'antique_brass',
    'label': "Antique Brass",
    'hexa': "#cd9575",
    'red': 205,
    'green': 149,
    'blue': 117
}, {
    'color': 'antique_fuchsia',
    'label': "Antique Fuchsia",
    'hexa': "#915c83",
    'red': 145,
    'green': 92,
    'blue': 131
}, {
    'color': 'antique_ruby',
    'label': "Antique Ruby",
    'hexa': "#841b2d",
    'red': 132,
    'green': 27,
    'blue': 45
}, {
    'color': 'antique_white',
    'label': "Antique White",
    'hexa': "#faebd7",
    'red': 250,
    'green': 235,
    'blue': 215
}, {
    'color': 'ao_english',
    'label': "Ao (English)",
    'hexa': "#008000",
    'red': 0,
    'green': 128,
    'blue': 0
}, {
    'color': 'apple_green',
    'label': "Apple Green",
    'hexa': "#8db600",
    'red': 141,
    'green': 182,
    'blue': 0
}, {
    'color': 'apricot',
    'label': "Apricot",
    'hexa': "#fbceb1",
    'red': 251,
    'green': 206,
    'blue': 177
}, {
    'color': 'aqua',
    'label': "Aqua",
    'hexa': "#00ffff",
    'red': 0,
    'green': 255,
    'blue': 255
}, {
    'color': 'aquamarine',
    'label': "Aquamarine",
    'hexa': "#7fffd4",
    'red': 127,
    'green': 255,
    'blue': 212
}, {
    'color': 'army_green',
    'label': "Army Green",
    'hexa': "#4b5320",
    'red': 75,
    'green': 83,
    'blue': 32
}, {
    'color': 'arsenic',
    'label': "Arsenic",
    'hexa': "#3b444b",
    'red': 59,
    'green': 68,
    'blue': 75
}, {
    'color': 'arylide_yellow',
    'label': "Arylide Yellow",
    'hexa': "#e9d66b",
    'red': 233,
    'green': 214,
    'blue': 107
}, {
    'color': 'ash_grey',
    'label': "Ash Grey",
    'hexa': "#b2beb5",
    'red': 178,
    'green': 190,
    'blue': 181
}, {
    'color': 'asparagus',
    'label': "Asparagus",
    'hexa': "#87a96b",
    'red': 135,
    'green': 169,
    'blue': 107
}, {
    'color': 'atomic_tangerine',
    'label': "Atomic Tangerine",
    'hexa': "#ff9966",
    'red': 255,
    'green': 153,
    'blue': 102
}, {
    'color': 'auburn',
    'label': "Auburn",
    'hexa': "#a52a2a",
    'red': 165,
    'green': 42,
    'blue': 42
}, {
    'color': 'aureolin',
    'label': "Aureolin",
    'hexa': "#fdee00",
    'red': 253,
    'green': 238,
    'blue': 0
}, {
    'color': 'aurometalsaurus',
    'label': "Aurometalsaurus",
    'hexa': '#6e7f80',
    'red': 110,
    'green': 127,
    'blue': 128
}, {
    'color': 'avocado',
    'label': "Avocado",
    'hexa': '#568203',
    'red': 86,
    'green': 130,
    'blue': 3
}, {
    'color': 'azure',
    'label': "Azure",
    'hexa': '#007fff',
    'red': 0,
    'green': 127,
    'blue': 255
}, {
    'color': 'azure_mist_web',
    'label': "Azure Mist/Web",
    'hexa': '#f0ffff',
    'red': 240,
    'green': 255,
    'blue': 255
}, {
    'color': 'baby_blue',
    'label': "Baby Blue",
    'hexa': '#89cff0',
    'red': 137,
    'green': 207,
    'blue': 240
}, {
    'color': 'baby_blue_eyes',
    'label': "Baby Blue Eyes",
    'hexa': '#a1caf1',
    'red': 161,
    'green': 202,
    'blue': 241
}, {
    'color': 'baby_pink',
    'label': "Baby Pink",
    'hexa': '#f4c2c2',
    'red': 244,
    'green': 194,
    'blue': 194
}, {
    'color': 'ball_blue',
    'label': "Ball Blue",
    'hexa': '#21abcd',
    'red': 33,
    'green': 171,
    'blue': 205
}, {
    'color': 'banana_mania',
    'label': "Banana Mania",
    'hexa': '#fae7b5',
    'red': 250,
    'green': 231,
    'blue': 181
}, {
    'color': 'banana_yellow',
    'label': "Banana Yellow",
    'hexa': '#ffe135',
    'red': 255,
    'green': 225,
    'blue': 53
}, {
    'color': 'barn_red',
    'label': "Barn Red",
    'hexa': '#7c0a02',
    'red': 124,
    'green': 10,
    'blue': 2
}, {
    'color': 'battleship_grey',
    'label': "Battleship Grey",
    'hexa': '#848482',
    'red': 132,
    'green': 132,
    'blue': 130
}, {
    'color': 'bazaar',
    'label': "Bazaar",
    'hexa': '#98777b',
    'red': 152,
    'green': 119,
    'blue': 123
}, {
    'color': 'beau_blue',
    'label': "Beau Blue",
    'hexa': '#bcd4e6',
    'red': 188,
    'green': 212,
    'blue': 230
}, {
    'color': 'beaver',
    'label': "Beaver",
    'hexa': '#9f8170',
    'red': 159,
    'green': 129,
    'blue': 112
}, {
    'color': 'beige',
    'label': "Beige",
    'hexa': '#f5f5dc',
    'red': 245,
    'green': 245,
    'blue': 220
}, {
    'color': 'big_dip_o_ruby',
    'label': "Big Dip O’Ruby",
    'hexa': '#9c2542',
    'red': 156,
    'green': 37,
    'blue': 66
}, {
    'color': 'bisque',
    'label': "Bisque",
    'hexa': '#ffe4c4',
    'red': 255,
    'green': 228,
    'blue': 196
}, {
    'color': 'bistre',
    'label': "Bistre",
    'hexa': '#3d2b1f',
    'red': 61,
    'green': 43,
    'blue': 31
}, {
    'color': 'bittersweet',
    'label': "Bittersweet",
    'hexa': '#fe6f5e',
    'red': 254,
    'green': 111,
    'blue': 94
}, {
    'color': 'bittersweet_shimmer',
    'label': "Bittersweet Shimmer",
    'hexa': '#bf4f51',
    'red': 191,
    'green': 79,
    'blue': 81
}, {
    'color': 'black',
    'label': "Black",
    'hexa': '#000000',
    'red': 0,
    'green': 0,
    'blue': 0
}, {
    'color': 'black_bean',
    'label': "Black Bean",
    'hexa': '#3d0c02',
    'red': 61,
    'green': 12,
    'blue': 2
}, {
    'color': 'black_leather_jacket',
    'label': "Black Leather Jacket",
    'hexa': '#253529',
    'red': 37,
    'green': 53,
    'blue': 41
}, {
    'color': 'black_olive',
    'label': "Black Olive",
    'hexa': '#3b3c36',
    'red': 59,
    'green': 60,
    'blue': 54
}, {
    'color': 'blanched_almond',
    'label': "Blanched Almond",
    'hexa': '#ffebcd',
    'red': 255,
    'green': 235,
    'blue': 205
}, {
    'color': 'blast_off_bronze',
    'label': "Blast-Off Bronze",
    'hexa': '#a57164',
    'red': 165,
    'green': 113,
    'blue': 100
}, {
    'color': 'bleu_de_france',
    'label': "Bleu De France",
    'hexa': '#318ce7',
    'red': 49,
    'green': 140,
    'blue': 231
}, {
    'color': 'blizzard_blue',
    'label': "Blizzard Blue",
    'hexa': '#ace5ee',
    'red': 172,
    'green': 229,
    'blue': 238
}, {
    'color': 'blond',
    'label': "Blond",
    'hexa': '#faf0be',
    'red': 250,
    'green': 240,
    'blue': 190
}, {
    'color': 'blue_bell',
    'label': "Blue Bell",
    'hexa': '#a2a2d0',
    'red': 162,
    'green': 162,
    'blue': 208
}, {
    'color': 'blue_crayola',
    'label': "Blue (Crayola)",
    'hexa': '#1f75fe',
    'red': 31,
    'green': 117,
    'blue': 254
}, {
    'color': 'blue_gray',
    'label': "Blue Gray",
    'hexa': '#6699cc',
    'red': 102,
    'green': 153,
    'blue': 204
}, {
    'color': 'blue_green',
    'label': "Blue-Green",
    'hexa': '#0d98ba',
    'red': 13,
    'green': 152,
    'blue': 186
}, {
    'color': 'blue_munsell',
    'label': "Blue (Munsell)",
    'hexa': '#0093af',
    'red': 0,
    'green': 147,
    'blue': 175
}, {
    'color': 'blue_ncs',
    'label': "Blue (Ncs)",
    'hexa': '#0087bd',
    'red': 0,
    'green': 135,
    'blue': 189
}, {
    'color': 'blue_pigment',
    'label': "Blue (Pigment)",
    'hexa': '#333399',
    'red': 51,
    'green': 51,
    'blue': 153
}, {
    'color': 'blue_ryb',
    'label': "Blue (Ryb)",
    'hexa': '#0247fe',
    'red': 2,
    'green': 71,
    'blue': 254
}, {
    'color': 'blue_sapphire',
    'label': "Blue Sapphire",
    'hexa': '#126180',
    'red': 18,
    'green': 97,
    'blue': 128
}, {
    'color': 'blue_violet',
    'label': "Blue-Violet",
    'hexa': '#8a2be2',
    'red': 138,
    'green': 43,
    'blue': 226
}, {
    'color': 'blush',
    'label': "Blush",
    'hexa': '#de5d83',
    'red': 222,
    'green': 93,
    'blue': 131
}, {
    'color': 'bole',
    'label': "Bole",
    'hexa': '#79443b',
    'red': 121,
    'green': 68,
    'blue': 59
}, {
    'color': 'bondi_blue',
    'label': "Bondi Blue",
    'hexa': '#0095b6',
    'red': 0,
    'green': 149,
    'blue': 182
}, {
    'color': 'bone',
    'label': "Bone",
    'hexa': '#e3dac9',
    'red': 227,
    'green': 218,
    'blue': 201
}, {
    'color': 'boston_university_red',
    'label': "Boston University Red",
    'hexa': '#cc0000',
    'red': 204,
    'green': 0,
    'blue': 0
}, {
    'color': 'bottle_green',
    'label': "Bottle Green",
    'hexa': '#006a4e',
    'red': 0,
    'green': 106,
    'blue': 78
}, {
    'color': 'boysenberry',
    'label': "Boysenberry",
    'hexa': '#873260',
    'red': 135,
    'green': 50,
    'blue': 96
}, {
    'color': 'brandeis_blue',
    'label': "Brandeis Blue",
    'hexa': '#0070ff',
    'red': 0,
    'green': 112,
    'blue': 255
}, {
    'color': 'brass',
    'label': "Brass",
    'hexa': '#b5a642',
    'red': 181,
    'green': 166,
    'blue': 66
}, {
    'color': 'brick_red',
    'label': "Brick Red",
    'hexa': '#cb4154',
    'red': 203,
    'green': 65,
    'blue': 84
}, {
    'color': 'bright_cerulean',
    'label': "Bright Cerulean",
    'hexa': '#1dacd6',
    'red': 29,
    'green': 172,
    'blue': 214
}, {
    'color': 'bright_green',
    'label': "Bright Green",
    'hexa': '#66ff00',
    'red': 102,
    'green': 255,
    'blue': 0
}, {
    'color': 'bright_lavender',
    'label': "Bright Lavender",
    'hexa': '#bf94e4',
    'red': 191,
    'green': 148,
    'blue': 228
}, {
    'color': 'bright_maroon',
    'label': "Bright Maroon",
    'hexa': '#c32148',
    'red': 195,
    'green': 33,
    'blue': 72
}, {
    'color': 'bright_pink',
    'label': "Bright Pink",
    'hexa': '#ff007f',
    'red': 255,
    'green': 0,
    'blue': 127
}, {
    'color': 'bright_turquoise',
    'label': "Bright Turquoise",
    'hexa': '#08e8de',
    'red': 8,
    'green': 232,
    'blue': 222
}, {
    'color': 'bright_ube',
    'label': "Bright Ube",
    'hexa': '#d19fe8',
    'red': 209,
    'green': 159,
    'blue': 232
}, {
    'color': 'brilliant_lavender',
    'label': "Brilliant Lavender",
    'hexa': '#f4bbff',
    'red': 244,
    'green': 187,
    'blue': 255
}, {
    'color': 'brilliant_rose',
    'label': "Brilliant Rose",
    'hexa': '#ff55a3',
    'red': 255,
    'green': 85,
    'blue': 163
}, {
    'color': 'brink_pink',
    'label': "Brink Pink",
    'hexa': '#fb607f',
    'red': 251,
    'green': 96,
    'blue': 127
}, {
    'color': 'british_racing_green',
    'label': "British Racing Green",
    'hexa': '#004225',
    'red': 0,
    'green': 66,
    'blue': 37
}, {
    'color': 'bronze',
    'label': "Bronze",
    'hexa': '#cd7f32',
    'red': 205,
    'green': 127,
    'blue': 50
}, {
    'color': 'brown_traditional',
    'label': "Brown (Traditional)",
    'hexa': '#964b00',
    'red': 150,
    'green': 75,
    'blue': 0
}, {
    'color': 'brown_web',
    'label': "Brown (Web)",
    'hexa': '#a52a2a',
    'red': 165,
    'green': 42,
    'blue': 42
}, {
    'color': 'bubble_gum',
    'label': "Bubble Gum",
    'hexa': '#ffc1cc',
    'red': 255,
    'green': 193,
    'blue': 204
}, {
    'color': 'bubbles',
    'label': "Bubbles",
    'hexa': '#e7feff',
    'red': 231,
    'green': 254,
    'blue': 255
}, {
    'color': 'buff',
    'label': "Buff",
    'hexa': '#f0dc82',
    'red': 240,
    'green': 220,
    'blue': 130
}, {
    'color': 'bulgarian_rose',
    'label': "Bulgarian Rose",
    'hexa': '#480607',
    'red': 72,
    'green': 6,
    'blue': 7
}, {
    'color': 'burgundy',
    'label': "Burgundy",
    'hexa': '#800020',
    'red': 128,
    'green': 0,
    'blue': 32
}, {
    'color': 'burlywood',
    'label': "Burlywood",
    'hexa': '#deb887',
    'red': 222,
    'green': 184,
    'blue': 135
}, {
    'color': 'burnt_orange',
    'label': "Burnt Orange",
    'hexa': '#cc5500',
    'red': 204,
    'green': 85,
    'blue': 0
}, {
    'color': 'burnt_sienna',
    'label': "Burnt Sienna",
    'hexa': '#e97451',
    'red': 233,
    'green': 116,
    'blue': 81
}, {
    'color': 'burnt_umber',
    'label': "Burnt Umber",
    'hexa': '#8a3324',
    'red': 138,
    'green': 51,
    'blue': 36
}, {
    'color': 'byzantine',
    'label': "Byzantine",
    'hexa': '#bd33a4',
    'red': 189,
    'green': 51,
    'blue': 164
}, {
    'color': 'byzantium',
    'label': "Byzantium",
    'hexa': '#702963',
    'red': 112,
    'green': 41,
    'blue': 99
}, {
    'color': 'cadet',
    'label': "Cadet",
    'hexa': '#536872',
    'red': 83,
    'green': 104,
    'blue': 114
}, {
    'color': 'cadet_blue',
    'label': "Cadet Blue",
    'hexa': '#5f9ea0',
    'red': 95,
    'green': 158,
    'blue': 160
}, {
    'color': 'cadet_grey',
    'label': "Cadet Grey",
    'hexa': '#91a3b0',
    'red': 145,
    'green': 163,
    'blue': 176
}, {
    'color': 'cadmium_green',
    'label': "Cadmium Green",
    'hexa': '#006b3c',
    'red': 0,
    'green': 107,
    'blue': 60
}, {
    'color': 'cadmium_orange',
    'label': "Cadmium Orange",
    'hexa': '#ed872d',
    'red': 237,
    'green': 135,
    'blue': 45
}, {
    'color': 'cadmium_red',
    'label': "Cadmium Red",
    'hexa': '#e30022',
    'red': 227,
    'green': 0,
    'blue': 34
}, {
    'color': 'cadmium_yellow',
    'label': "Cadmium Yellow",
    'hexa': '#fff600',
    'red': 255,
    'green': 246,
    'blue': 0
}, {
    'color': 'caf_au_lait',
    'label': "Café Au Lait",
    'hexa': '#a67b5b',
    'red': 166,
    'green': 123,
    'blue': 91
}, {
    'color': 'caf_noir',
    'label': "Café Noir",
    'hexa': '#4b3621',
    'red': 75,
    'green': 54,
    'blue': 33
}, {
    'color': 'cal_poly_green',
    'label': "Cal Poly Green",
    'hexa': '#1e4d2b',
    'red': 30,
    'green': 77,
    'blue': 43
}, {
    'color': 'cambridge_blue',
    'label': "Cambridge Blue",
    'hexa': '#a3c1ad',
    'red': 163,
    'green': 193,
    'blue': 173
}, {
    'color': 'camel',
    'label': "Camel",
    'hexa': '#c19a6b',
    'red': 193,
    'green': 154,
    'blue': 107
}, {
    'color': 'cameo_pink',
    'label': "Cameo Pink",
    'hexa': '#efbbcc',
    'red': 239,
    'green': 187,
    'blue': 204
}, {
    'color': 'camouflage_green',
    'label': "Camouflage Green",
    'hexa': '#78866b',
    'red': 120,
    'green': 134,
    'blue': 107
}, {
    'color': 'canary_yellow',
    'label': "Canary Yellow",
    'hexa': '#ffef00',
    'red': 255,
    'green': 239,
    'blue': 0
}, {
    'color': 'candy_apple_red',
    'label': "Candy Apple Red",
    'hexa': '#ff0800',
    'red': 255,
    'green': 8,
    'blue': 0
}, {
    'color': 'candy_pink',
    'label': "Candy Pink",
    'hexa': '#e4717a',
    'red': 228,
    'green': 113,
    'blue': 122
}, {
    'color': 'capri',
    'label': "Capri",
    'hexa': '#00bfff',
    'red': 0,
    'green': 191,
    'blue': 255
}, {
    'color': 'caput_mortuum',
    'label': "Caput Mortuum",
    'hexa': '#592720',
    'red': 89,
    'green': 39,
    'blue': 32
}, {
    'color': 'cardinal',
    'label': "Cardinal",
    'hexa': '#c41e3a',
    'red': 196,
    'green': 30,
    'blue': 58
}, {
    'color': 'caribbean_green',
    'label': "Caribbean Green",
    'hexa': '#00cc99',
    'red': 0,
    'green': 204,
    'blue': 153
}, {
    'color': 'carmine',
    'label': "Carmine",
    'hexa': '#960018',
    'red': 150,
    'green': 0,
    'blue': 24
}, {
    'color': 'carmine_m_p',
    'label': "Carmine (M&P)",
    'hexa': '#d70040',
    'red': 215,
    'green': 0,
    'blue': 64
}, {
    'color': 'carmine_pink',
    'label': "Carmine Pink",
    'hexa': '#eb4c42',
    'red': 235,
    'green': 76,
    'blue': 66
}, {
    'color': 'carmine_red',
    'label': "Carmine Red",
    'hexa': '#ff0038',
    'red': 255,
    'green': 0,
    'blue': 56
}, {
    'color': 'carnation_pink',
    'label': "Carnation Pink",
    'hexa': '#ffa6c9',
    'red': 255,
    'green': 166,
    'blue': 201
}, {
    'color': 'carnelian',
    'label': "Carnelian",
    'hexa': '#b31b1b',
    'red': 179,
    'green': 27,
    'blue': 27
}, {
    'color': 'carolina_blue',
    'label': "Carolina Blue",
    'hexa': '#99badd',
    'red': 153,
    'green': 186,
    'blue': 221
}, {
    'color': 'carrot_orange',
    'label': "Carrot Orange",
    'hexa': '#ed9121',
    'red': 237,
    'green': 145,
    'blue': 33
}, {
    'color': 'catalina_blue',
    'label': "Catalina Blue",
    'hexa': '#062a78',
    'red': 6,
    'green': 42,
    'blue': 120
}, {
    'color': 'ceil',
    'label': "Ceil",
    'hexa': '#92a1cf',
    'red': 146,
    'green': 161,
    'blue': 207
}, {
    'color': 'celadon',
    'label': "Celadon",
    'hexa': '#ace1af',
    'red': 172,
    'green': 225,
    'blue': 175
}, {
    'color': 'celadon_blue',
    'label': "Celadon Blue",
    'hexa': '#007ba7',
    'red': 0,
    'green': 123,
    'blue': 167
}, {
    'color': 'celadon_green',
    'label': "Celadon Green",
    'hexa': '#2f847c',
    'red': 47,
    'green': 132,
    'blue': 124
}, {
    'color': 'celeste_colour',
    'label': "Celeste (Colour)",
    'hexa': '#b2ffff',
    'red': 178,
    'green': 255,
    'blue': 255
}, {
    'color': 'celestial_blue',
    'label': "Celestial Blue",
    'hexa': '#4997d0',
    'red': 73,
    'green': 151,
    'blue': 208
}, {
    'color': 'cerise',
    'label': "Cerise",
    'hexa': '#de3163',
    'red': 222,
    'green': 49,
    'blue': 99
}, {
    'color': 'cerise_pink',
    'label': "Cerise Pink",
    'hexa': '#ec3b83',
    'red': 236,
    'green': 59,
    'blue': 131
}, {
    'color': 'cerulean',
    'label': "Cerulean",
    'hexa': '#007ba7',
    'red': 0,
    'green': 123,
    'blue': 167
}, {
    'color': 'cerulean_blue',
    'label': "Cerulean Blue",
    'hexa': '#2a52be',
    'red': 42,
    'green': 82,
    'blue': 190
}, {
    'color': 'cerulean_frost',
    'label': "Cerulean Frost",
    'hexa': '#6d9bc3',
    'red': 109,
    'green': 155,
    'blue': 195
}, {
    'color': 'cg_blue',
    'label': "Cg Blue",
    'hexa': '#007aa5',
    'red': 0,
    'green': 122,
    'blue': 165
}, {
    'color': 'cg_red',
    'label': "Cg Red",
    'hexa': '#e03c31',
    'red': 224,
    'green': 60,
    'blue': 49
}, {
    'color': 'chamoisee',
    'label': "Chamoisee",
    'hexa': '#a0785a',
    'red': 160,
    'green': 120,
    'blue': 90
}, {
    'color': 'champagne',
    'label': "Champagne",
    'hexa': '#fad6a5',
    'red': 250,
    'green': 214,
    'blue': 165
}, {
    'color': 'charcoal',
    'label': "Charcoal",
    'hexa': '#36454f',
    'red': 54,
    'green': 69,
    'blue': 79
}, {
    'color': 'charm_pink',
    'label': "Charm Pink",
    'hexa': '#e68fac',
    'red': 230,
    'green': 143,
    'blue': 172
}, {
    'color': 'chartreuse_traditional',
    'label': "Chartreuse (Traditional)",
    'hexa': '#dfff00',
    'red': 223,
    'green': 255,
    'blue': 0
}, {
    'color': 'chartreuse_web',
    'label': "Chartreuse (Web)",
    'hexa': '#7fff00',
    'red': 127,
    'green': 255,
    'blue': 0
}, {
    'color': 'cherry',
    'label': "Cherry",
    'hexa': '#de3163',
    'red': 222,
    'green': 49,
    'blue': 99
}, {
    'color': 'cherry_blossom_pink',
    'label': "Cherry Blossom Pink",
    'hexa': '#ffb7c5',
    'red': 255,
    'green': 183,
    'blue': 197
}, {
    'color': 'chestnut',
    'label': "Chestnut",
    'hexa': '#cd5c5c',
    'red': 205,
    'green': 92,
    'blue': 92
}, {
    'color': 'china_pink',
    'label': "China Pink",
    'hexa': '#de6fa1',
    'red': 222,
    'green': 111,
    'blue': 161
}, {
    'color': 'china_rose',
    'label': "China Rose",
    'hexa': '#a8516e',
    'red': 168,
    'green': 81,
    'blue': 110
}, {
    'color': 'chinese_red',
    'label': "Chinese Red",
    'hexa': '#aa381e',
    'red': 170,
    'green': 56,
    'blue': 30
}, {
    'color': 'chocolate_traditional',
    'label': "Chocolate (Traditional)",
    'hexa': '#7b3f00',
    'red': 123,
    'green': 63,
    'blue': 0
}, {
    'color': 'chocolate_web',
    'label': "Chocolate (Web)",
    'hexa': '#d2691e',
    'red': 210,
    'green': 105,
    'blue': 30
}, {
    'color': 'chrome_yellow',
    'label': "Chrome Yellow",
    'hexa': '#ffa700',
    'red': 255,
    'green': 167,
    'blue': 0
}, {
    'color': 'cinereous',
    'label': "Cinereous",
    'hexa': '#98817b',
    'red': 152,
    'green': 129,
    'blue': 123
}, {
    'color': 'cinnabar',
    'label': "Cinnabar",
    'hexa': '#e34234',
    'red': 227,
    'green': 66,
    'blue': 52
}, {
    'color': 'cinnamon',
    'label': "Cinnamon",
    'hexa': '#d2691e',
    'red': 210,
    'green': 105,
    'blue': 30
}, {
    'color': 'citrine',
    'label': "Citrine",
    'hexa': '#e4d00a',
    'red': 228,
    'green': 208,
    'blue': 10
}, {
    'color': 'classic_rose',
    'label': "Classic Rose",
    'hexa': '#fbcce7',
    'red': 251,
    'green': 204,
    'blue': 231
}, {
    'color': 'cobalt',
    'label': "Cobalt",
    'hexa': '#0047ab',
    'red': 0,
    'green': 71,
    'blue': 171
}, {
    'color': 'cocoa_brown',
    'label': "Cocoa Brown",
    'hexa': '#d2691e',
    'red': 210,
    'green': 105,
    'blue': 30
}, {
    'color': 'coffee',
    'label': "Coffee",
    'hexa': '#6f4e37',
    'red': 111,
    'green': 78,
    'blue': 55
}, {
    'color': 'columbia_blue',
    'label': "Columbia Blue",
    'hexa': '#9bddff',
    'red': 155,
    'green': 221,
    'blue': 255
}, {
    'color': 'congo_pink',
    'label': "Congo Pink",
    'hexa': '#f88379',
    'red': 248,
    'green': 131,
    'blue': 121
}, {
    'color': 'cool_black',
    'label': "Cool Black",
    'hexa': '#002e63',
    'red': 0,
    'green': 46,
    'blue': 99
}, {
    'color': 'cool_grey',
    'label': "Cool Grey",
    'hexa': '#8c92ac',
    'red': 140,
    'green': 146,
    'blue': 172
}, {
    'color': 'copper',
    'label': "Copper",
    'hexa': '#b87333',
    'red': 184,
    'green': 115,
    'blue': 51
}, {
    'color': 'copper_crayola',
    'label': "Copper (Crayola)",
    'hexa': '#da8a67',
    'red': 218,
    'green': 138,
    'blue': 103
}, {
    'color': 'copper_penny',
    'label': "Copper Penny",
    'hexa': '#ad6f69',
    'red': 173,
    'green': 111,
    'blue': 105
}, {
    'color': 'copper_red',
    'label': "Copper Red",
    'hexa': '#cb6d51',
    'red': 203,
    'green': 109,
    'blue': 81
}, {
    'color': 'copper_rose',
    'label': "Copper Rose",
    'hexa': '#996666',
    'red': 153,
    'green': 102,
    'blue': 102
}, {
    'color': 'coquelicot',
    'label': "Coquelicot",
    'hexa': '#ff3800',
    'red': 255,
    'green': 56,
    'blue': 0
}, {
    'color': 'coral',
    'label': "Coral",
    'hexa': '#ff7f50',
    'red': 255,
    'green': 127,
    'blue': 80
}, {
    'color': 'coral_pink',
    'label': "Coral Pink",
    'hexa': '#f88379',
    'red': 248,
    'green': 131,
    'blue': 121
}, {
    'color': 'coral_red',
    'label': "Coral Red",
    'hexa': '#ff4040',
    'red': 255,
    'green': 64,
    'blue': 64
}, {
    'color': 'cordovan',
    'label': "Cordovan",
    'hexa': '#893f45',
    'red': 137,
    'green': 63,
    'blue': 69
}, {
    'color': 'corn',
    'label': "Corn",
    'hexa': '#fbec5d',
    'red': 251,
    'green': 236,
    'blue': 93
}, {
    'color': 'cornell_red',
    'label': "Cornell Red",
    'hexa': '#b31b1b',
    'red': 179,
    'green': 27,
    'blue': 27
}, {
    'color': 'cornflower_blue',
    'label': "Cornflower Blue",
    'hexa': '#6495ed',
    'red': 100,
    'green': 149,
    'blue': 237
}, {
    'color': 'cornsilk',
    'label': "Cornsilk",
    'hexa': '#fff8dc',
    'red': 255,
    'green': 248,
    'blue': 220
}, {
    'color': 'cosmic_latte',
    'label': "Cosmic Latte",
    'hexa': '#fff8e7',
    'red': 255,
    'green': 248,
    'blue': 231
}, {
    'color': 'cotton_candy',
    'label': "Cotton Candy",
    'hexa': '#ffbcd9',
    'red': 255,
    'green': 188,
    'blue': 217
}, {
    'color': 'cream',
    'label': "Cream",
    'hexa': '#fffdd0',
    'red': 255,
    'green': 253,
    'blue': 208
}, {
    'color': 'crimson',
    'label': "Crimson",
    'hexa': '#dc143c',
    'red': 220,
    'green': 20,
    'blue': 60
}, {
    'color': 'crimson_glory',
    'label': "Crimson Glory",
    'hexa': '#be0032',
    'red': 190,
    'green': 0,
    'blue': 50
}, {
    'color': 'cyan_process',
    'label': "Cyan (Process)",
    'hexa': '#00b7eb',
    'red': 0,
    'green': 183,
    'blue': 235
}, {
    'color': 'daffodil',
    'label': "Daffodil",
    'hexa': '#ffff31',
    'red': 255,
    'green': 255,
    'blue': 49
}, {
    'color': 'dandelion',
    'label': "Dandelion",
    'hexa': '#f0e130',
    'red': 240,
    'green': 225,
    'blue': 48
}, {
    'color': 'dark_blue',
    'label': "Dark Blue",
    'hexa': '#00008b',
    'red': 0,
    'green': 0,
    'blue': 139
}, {
    'color': 'dark_brown',
    'label': "Dark Brown",
    'hexa': '#654321',
    'red': 101,
    'green': 67,
    'blue': 33
}, {
    'color': 'dark_byzantium',
    'label': "Dark Byzantium",
    'hexa': '#5d3954',
    'red': 93,
    'green': 57,
    'blue': 84
}, {
    'color': 'dark_candy_apple_red',
    'label': "Dark Candy Apple Red",
    'hexa': '#a40000',
    'red': 164,
    'green': 0,
    'blue': 0
}, {
    'color': 'dark_cerulean',
    'label': "Dark Cerulean",
    'hexa': '#08457e',
    'red': 8,
    'green': 69,
    'blue': 126
}, {
    'color': 'dark_chestnut',
    'label': "Dark Chestnut",
    'hexa': '#986960',
    'red': 152,
    'green': 105,
    'blue': 96
}, {
    'color': 'dark_coral',
    'label': "Dark Coral",
    'hexa': '#cd5b45',
    'red': 205,
    'green': 91,
    'blue': 69
}, {
    'color': 'dark_cyan',
    'label': "Dark Cyan",
    'hexa': '#008b8b',
    'red': 0,
    'green': 139,
    'blue': 139
}, {
    'color': 'dark_electric_blue',
    'label': "Dark Electric Blue",
    'hexa': '#536878',
    'red': 83,
    'green': 104,
    'blue': 120
}, {
    'color': 'dark_goldenrod',
    'label': "Dark Goldenrod",
    'hexa': '#b8860b',
    'red': 184,
    'green': 134,
    'blue': 11
}, {
    'color': 'dark_gray',
    'label': "Dark Gray",
    'hexa': '#a9a9a9',
    'red': 169,
    'green': 169,
    'blue': 169
}, {
    'color': 'dark_green',
    'label': "Dark Green",
    'hexa': '#013220',
    'red': 1,
    'green': 50,
    'blue': 32
}, {
    'color': 'dark_imperial_blue',
    'label': "Dark Imperial Blue",
    'hexa': '#00416a',
    'red': 0,
    'green': 65,
    'blue': 106
}, {
    'color': 'dark_jungle_green',
    'label': "Dark Jungle Green",
    'hexa': '#1a2421',
    'red': 26,
    'green': 36,
    'blue': 33
}, {
    'color': 'dark_khaki',
    'label': "Dark Khaki",
    'hexa': '#bdb76b',
    'red': 189,
    'green': 183,
    'blue': 107
}, {
    'color': 'dark_lava',
    'label': "Dark Lava",
    'hexa': '#483c32',
    'red': 72,
    'green': 60,
    'blue': 50
}, {
    'color': 'dark_lavender',
    'label': "Dark Lavender",
    'hexa': '#734f96',
    'red': 115,
    'green': 79,
    'blue': 150
}, {
    'color': 'dark_magenta',
    'label': "Dark Magenta",
    'hexa': '#8b008b',
    'red': 139,
    'green': 0,
    'blue': 139
}, {
    'color': 'dark_midnight_blue',
    'label': "Dark Midnight Blue",
    'hexa': '#003366',
    'red': 0,
    'green': 51,
    'blue': 102
}, {
    'color': 'dark_olive_green',
    'label': "Dark Olive Green",
    'hexa': '#556b2f',
    'red': 85,
    'green': 107,
    'blue': 47
}, {
    'color': 'dark_orange',
    'label': "Dark Orange",
    'hexa': '#ff8c00',
    'red': 255,
    'green': 140,
    'blue': 0
}, {
    'color': 'dark_orchid',
    'label': "Dark Orchid",
    'hexa': '#9932cc',
    'red': 153,
    'green': 50,
    'blue': 204
}, {
    'color': 'dark_pastel_blue',
    'label': "Dark Pastel Blue",
    'hexa': '#779ecb',
    'red': 119,
    'green': 158,
    'blue': 203
}, {
    'color': 'dark_pastel_green',
    'label': "Dark Pastel Green",
    'hexa': '#03c03c',
    'red': 3,
    'green': 192,
    'blue': 60
}, {
    'color': 'dark_pastel_purple',
    'label': "Dark Pastel Purple",
    'hexa': '#966fd6',
    'red': 150,
    'green': 111,
    'blue': 214
}, {
    'color': 'dark_pastel_red',
    'label': "Dark Pastel Red",
    'hexa': '#c23b22',
    'red': 194,
    'green': 59,
    'blue': 34
}, {
    'color': 'dark_pink',
    'label': "Dark Pink",
    'hexa': '#e75480',
    'red': 231,
    'green': 84,
    'blue': 128
}, {
    'color': 'dark_powder_blue',
    'label': "Dark Powder Blue",
    'hexa': '#003399',
    'red': 0,
    'green': 51,
    'blue': 153
}, {
    'color': 'dark_raspberry',
    'label': "Dark Raspberry",
    'hexa': '#872657',
    'red': 135,
    'green': 38,
    'blue': 87
}, {
    'color': 'dark_red',
    'label': "Dark Red",
    'hexa': '#8b0000',
    'red': 139,
    'green': 0,
    'blue': 0
}, {
    'color': 'dark_salmon',
    'label': "Dark Salmon",
    'hexa': '#e9967a',
    'red': 233,
    'green': 150,
    'blue': 122
}, {
    'color': 'dark_scarlet',
    'label': "Dark Scarlet",
    'hexa': '#560319',
    'red': 86,
    'green': 3,
    'blue': 25
}, {
    'color': 'dark_sea_green',
    'label': "Dark Sea Green",
    'hexa': '#8fbc8f',
    'red': 143,
    'green': 188,
    'blue': 143
}, {
    'color': 'dark_sienna',
    'label': "Dark Sienna",
    'hexa': '#3c1414',
    'red': 60,
    'green': 20,
    'blue': 20
}, {
    'color': 'dark_slate_blue',
    'label': "Dark Slate Blue",
    'hexa': '#483d8b',
    'red': 72,
    'green': 61,
    'blue': 139
}, {
    'color': 'dark_slate_gray',
    'label': "Dark Slate Gray",
    'hexa': '#2f4f4f',
    'red': 47,
    'green': 79,
    'blue': 79
}, {
    'color': 'dark_spring_green',
    'label': "Dark Spring Green",
    'hexa': '#177245',
    'red': 23,
    'green': 114,
    'blue': 69
}, {
    'color': 'dark_tan',
    'label': "Dark Tan",
    'hexa': '#918151',
    'red': 145,
    'green': 129,
    'blue': 81
}, {
    'color': 'dark_tangerine',
    'label': "Dark Tangerine",
    'hexa': '#ffa812',
    'red': 255,
    'green': 168,
    'blue': 18
}, {
    'color': 'dark_taupe',
    'label': "Dark Taupe",
    'hexa': '#483c32',
    'red': 72,
    'green': 60,
    'blue': 50
}, {
    'color': 'dark_terra_cotta',
    'label': "Dark Terra Cotta",
    'hexa': '#cc4e5c',
    'red': 204,
    'green': 78,
    'blue': 92
}, {
    'color': 'dark_turquoise',
    'label': "Dark Turquoise",
    'hexa': '#00ced1',
    'red': 0,
    'green': 206,
    'blue': 209
}, {
    'color': 'dark_violet',
    'label': "Dark Violet",
    'hexa': '#9400d3',
    'red': 148,
    'green': 0,
    'blue': 211
}, {
    'color': 'dark_yellow',
    'label': "Dark Yellow",
    'hexa': '#9b870c',
    'red': 155,
    'green': 135,
    'blue': 12
}, {
    'color': 'dartmouth_green',
    'label': "Dartmouth Green",
    'hexa': '#00703c',
    'red': 0,
    'green': 112,
    'blue': 60
}, {
    'color': 'davy_s_grey',
    'label': "Davy'S Grey",
    'hexa': '#555555',
    'red': 85,
    'green': 85,
    'blue': 85
}, {
    'color': 'debian_red',
    'label': "Debian Red",
    'hexa': '#d70a53',
    'red': 215,
    'green': 10,
    'blue': 83
}, {
    'color': 'deep_carmine',
    'label': "Deep Carmine",
    'hexa': '#a9203e',
    'red': 169,
    'green': 32,
    'blue': 62
}, {
    'color': 'deep_carmine_pink',
    'label': "Deep Carmine Pink",
    'hexa': '#ef3038',
    'red': 239,
    'green': 48,
    'blue': 56
}, {
    'color': 'deep_carrot_orange',
    'label': "Deep Carrot Orange",
    'hexa': '#e9692c',
    'red': 233,
    'green': 105,
    'blue': 44
}, {
    'color': 'deep_cerise',
    'label': "Deep Cerise",
    'hexa': '#da3287',
    'red': 218,
    'green': 50,
    'blue': 135
}, {
    'color': 'deep_champagne',
    'label': "Deep Champagne",
    'hexa': '#fad6a5',
    'red': 250,
    'green': 214,
    'blue': 165
}, {
    'color': 'deep_chestnut',
    'label': "Deep Chestnut",
    'hexa': '#b94e48',
    'red': 185,
    'green': 78,
    'blue': 72
}, {
    'color': 'deep_coffee',
    'label': "Deep Coffee",
    'hexa': '#704241',
    'red': 112,
    'green': 66,
    'blue': 65
}, {
    'color': 'deep_fuchsia',
    'label': "Deep Fuchsia",
    'hexa': '#c154c1',
    'red': 193,
    'green': 84,
    'blue': 193
}, {
    'color': 'deep_jungle_green',
    'label': "Deep Jungle Green",
    'hexa': '#004b49',
    'red': 0,
    'green': 75,
    'blue': 73
}, {
    'color': 'deep_lilac',
    'label': "Deep Lilac",
    'hexa': '#9955bb',
    'red': 153,
    'green': 85,
    'blue': 187
}, {
    'color': 'deep_magenta',
    'label': "Deep Magenta",
    'hexa': '#cc00cc',
    'red': 204,
    'green': 0,
    'blue': 204
}, {
    'color': 'deep_peach',
    'label': "Deep Peach",
    'hexa': '#ffcba4',
    'red': 255,
    'green': 203,
    'blue': 164
}, {
    'color': 'deep_pink',
    'label': "Deep Pink",
    'hexa': '#ff1493',
    'red': 255,
    'green': 20,
    'blue': 147
}, {
    'color': 'deep_ruby',
    'label': "Deep Ruby",
    'hexa': '#843f5b',
    'red': 132,
    'green': 63,
    'blue': 91
}, {
    'color': 'deep_saffron',
    'label': "Deep Saffron",
    'hexa': '#ff9933',
    'red': 255,
    'green': 153,
    'blue': 51
}, {
    'color': 'deep_sky_blue',
    'label': "Deep Sky Blue",
    'hexa': '#00bfff',
    'red': 0,
    'green': 191,
    'blue': 255
}, {
    'color': 'deep_tuscan_red',
    'label': "Deep Tuscan Red",
    'hexa': '#66424d',
    'red': 102,
    'green': 66,
    'blue': 77
}, {
    'color': 'denim',
    'label': "Denim",
    'hexa': '#1560bd',
    'red': 21,
    'green': 96,
    'blue': 189
}, {
    'color': 'desert',
    'label': "Desert",
    'hexa': '#c19a6b',
    'red': 193,
    'green': 154,
    'blue': 107
}, {
    'color': 'desert_sand',
    'label': "Desert Sand",
    'hexa': '#edc9af',
    'red': 237,
    'green': 201,
    'blue': 175
}, {
    'color': 'dim_gray',
    'label': "Dim Gray",
    'hexa': '#696969',
    'red': 105,
    'green': 105,
    'blue': 105
}, {
    'color': 'dodger_blue',
    'label': "Dodger Blue",
    'hexa': '#1e90ff',
    'red': 30,
    'green': 144,
    'blue': 255
}, {
    'color': 'dogwood_rose',
    'label': "Dogwood Rose",
    'hexa': '#d71868',
    'red': 215,
    'green': 24,
    'blue': 104
}, {
    'color': 'dollar_bill',
    'label': "Dollar Bill",
    'hexa': '#85bb65',
    'red': 133,
    'green': 187,
    'blue': 101
}, {
    'color': 'drab',
    'label': "Drab",
    'hexa': '#967117',
    'red': 150,
    'green': 113,
    'blue': 23
}, {
    'color': 'duke_blue',
    'label': "Duke Blue",
    'hexa': '#00009c',
    'red': 0,
    'green': 0,
    'blue': 156
}, {
    'color': 'earth_yellow',
    'label': "Earth Yellow",
    'hexa': '#e1a95f',
    'red': 225,
    'green': 169,
    'blue': 95
}, {
    'color': 'ebony',
    'label': "Ebony",
    'hexa': '#555d50',
    'red': 85,
    'green': 93,
    'blue': 80
}, {
    'color': 'ecru',
    'label': "Ecru",
    'hexa': '#c2b280',
    'red': 194,
    'green': 178,
    'blue': 128
}, {
    'color': 'eggplant',
    'label': "Eggplant",
    'hexa': '#614051',
    'red': 97,
    'green': 64,
    'blue': 81
}, {
    'color': 'eggshell',
    'label': "Eggshell",
    'hexa': '#f0ead6',
    'red': 240,
    'green': 234,
    'blue': 214
}, {
    'color': 'egyptian_blue',
    'label': "Egyptian Blue",
    'hexa': '#1034a6',
    'red': 16,
    'green': 52,
    'blue': 166
}, {
    'color': 'electric_blue',
    'label': "Electric Blue",
    'hexa': '#7df9ff',
    'red': 125,
    'green': 249,
    'blue': 255
}, {
    'color': 'electric_crimson',
    'label': "Electric Crimson",
    'hexa': '#ff003f',
    'red': 255,
    'green': 0,
    'blue': 63
}, {
    'color': 'electric_cyan',
    'label': "Electric Cyan",
    'hexa': '#00ffff',
    'red': 0,
    'green': 255,
    'blue': 255
}, {
    'color': 'electric_green',
    'label': "Electric Green",
    'hexa': '#00ff00',
    'red': 0,
    'green': 255,
    'blue': 0
}, {
    'color': 'electric_indigo',
    'label': "Electric Indigo",
    'hexa': '#6f00ff',
    'red': 111,
    'green': 0,
    'blue': 255
}, {
    'color': 'electric_lavender',
    'label': "Electric Lavender",
    'hexa': '#f4bbff',
    'red': 244,
    'green': 187,
    'blue': 255
}, {
    'color': 'electric_lime',
    'label': "Electric Lime",
    'hexa': '#ccff00',
    'red': 204,
    'green': 255,
    'blue': 0
}, {
    'color': 'electric_purple',
    'label': "Electric Purple",
    'hexa': '#bf00ff',
    'red': 191,
    'green': 0,
    'blue': 255
}, {
    'color': 'electric_ultramarine',
    'label': "Electric Ultramarine",
    'hexa': '#3f00ff',
    'red': 63,
    'green': 0,
    'blue': 255
}, {
    'color': 'electric_violet',
    'label': "Electric Violet",
    'hexa': '#8f00ff',
    'red': 143,
    'green': 0,
    'blue': 255
}, {
    'color': 'electric_yellow',
    'label': "Electric Yellow",
    'hexa': '#ffff00',
    'red': 255,
    'green': 255,
    'blue': 0
}, {
    'color': 'emerald',
    'label': "Emerald",
    'hexa': '#50c878',
    'red': 80,
    'green': 200,
    'blue': 120
}, {
    'color': 'english_lavender',
    'label': "English Lavender",
    'hexa': '#b48395',
    'red': 180,
    'green': 131,
    'blue': 149
}, {
    'color': 'eton_blue',
    'label': "Eton Blue",
    'hexa': '#96c8a2',
    'red': 150,
    'green': 200,
    'blue': 162
}, {
    'color': 'fallow',
    'label': "Fallow",
    'hexa': '#c19a6b',
    'red': 193,
    'green': 154,
    'blue': 107
}, {
    'color': 'falu_red',
    'label': "Falu Red",
    'hexa': '#801818',
    'red': 128,
    'green': 24,
    'blue': 24
}, {
    'color': 'fandango',
    'label': "Fandango",
    'hexa': '#b53389',
    'red': 181,
    'green': 51,
    'blue': 137
}, {
    'color': 'fashion_fuchsia',
    'label': "Fashion Fuchsia",
    'hexa': '#f400a1',
    'red': 244,
    'green': 0,
    'blue': 161
}, {
    'color': 'fawn',
    'label': "Fawn",
    'hexa': '#e5aa70',
    'red': 229,
    'green': 170,
    'blue': 112
}, {
    'color': 'feldgrau',
    'label': "Feldgrau",
    'hexa': '#4d5d53',
    'red': 77,
    'green': 93,
    'blue': 83
}, {
    'color': 'fern_green',
    'label': "Fern Green",
    'hexa': '#4f7942',
    'red': 79,
    'green': 121,
    'blue': 66
}, {
    'color': 'ferrari_red',
    'label': "Ferrari Red",
    'hexa': '#ff2800',
    'red': 255,
    'green': 40,
    'blue': 0
}, {
    'color': 'field_drab',
    'label': "Field Drab",
    'hexa': '#6c541e',
    'red': 108,
    'green': 84,
    'blue': 30
}, {
    'color': 'fire_engine_red',
    'label': "Fire Engine Red",
    'hexa': '#ce2029',
    'red': 206,
    'green': 32,
    'blue': 41
}, {
    'color': 'firebrick',
    'label': "Firebrick",
    'hexa': '#b22222',
    'red': 178,
    'green': 34,
    'blue': 34
}, {
    'color': 'flame',
    'label': "Flame",
    'hexa': '#e25822',
    'red': 226,
    'green': 88,
    'blue': 34
}, {
    'color': 'flamingo_pink',
    'label': "Flamingo Pink",
    'hexa': '#fc8eac',
    'red': 252,
    'green': 142,
    'blue': 172
}, {
    'color': 'flavescent',
    'label': "Flavescent",
    'hexa': '#f7e98e',
    'red': 247,
    'green': 233,
    'blue': 142
}, {
    'color': 'flax',
    'label': "Flax",
    'hexa': '#eedc82',
    'red': 238,
    'green': 220,
    'blue': 130
}, {
    'color': 'floral_white',
    'label': "Floral White",
    'hexa': '#fffaf0',
    'red': 255,
    'green': 250,
    'blue': 240
}, {
    'color': 'fluorescent_orange',
    'label': "Fluorescent Orange",
    'hexa': '#ffbf00',
    'red': 255,
    'green': 191,
    'blue': 0
}, {
    'color': 'fluorescent_pink',
    'label': "Fluorescent Pink",
    'hexa': '#ff1493',
    'red': 255,
    'green': 20,
    'blue': 147
}, {
    'color': 'fluorescent_yellow',
    'label': "Fluorescent Yellow",
    'hexa': '#ccff00',
    'red': 204,
    'green': 255,
    'blue': 0
}, {
    'color': 'folly',
    'label': "Folly",
    'hexa': '#ff004f',
    'red': 255,
    'green': 0,
    'blue': 79
}, {
    'color': 'forest_green_traditional',
    'label': "Forest Green (Traditional)",
    'hexa': '#014421',
    'red': 1,
    'green': 68,
    'blue': 33
}, {
    'color': 'forest_green_web',
    'label': "Forest Green (Web)",
    'hexa': '#228b22',
    'red': 34,
    'green': 139,
    'blue': 34
}, {
    'color': 'french_beige',
    'label': "French Beige",
    'hexa': '#a67b5b',
    'red': 166,
    'green': 123,
    'blue': 91
}, {
    'color': 'french_blue',
    'label': "French Blue",
    'hexa': '#0072bb',
    'red': 0,
    'green': 114,
    'blue': 187
}, {
    'color': 'french_lilac',
    'label': "French Lilac",
    'hexa': '#86608e',
    'red': 134,
    'green': 96,
    'blue': 142
}, {
    'color': 'french_lime',
    'label': "French Lime",
    'hexa': '#ccff00',
    'red': 204,
    'green': 255,
    'blue': 0
}, {
    'color': 'french_raspberry',
    'label': "French Raspberry",
    'hexa': '#c72c48',
    'red': 199,
    'green': 44,
    'blue': 72
}, {
    'color': 'french_rose',
    'label': "French Rose",
    'hexa': '#f64a8a',
    'red': 246,
    'green': 74,
    'blue': 138
}, {
    'color': 'fuchsia',
    'label': "Fuchsia",
    'hexa': '#ff00ff',
    'red': 255,
    'green': 0,
    'blue': 255
}, {
    'color': 'fuchsia_crayola',
    'label': "Fuchsia (Crayola)",
    'hexa': '#c154c1',
    'red': 193,
    'green': 84,
    'blue': 193
}, {
    'color': 'fuchsia_pink',
    'label': "Fuchsia Pink",
    'hexa': '#ff77ff',
    'red': 255,
    'green': 119,
    'blue': 255
}, {
    'color': 'fuchsia_rose',
    'label': "Fuchsia Rose",
    'hexa': '#c74375',
    'red': 199,
    'green': 67,
    'blue': 117
}, {
    'color': 'fulvous',
    'label': "Fulvous",
    'hexa': '#e48400',
    'red': 228,
    'green': 132,
    'blue': 0
}, {
    'color': 'fuzzy_wuzzy',
    'label': "Fuzzy Wuzzy",
    'hexa': '#cc6666',
    'red': 204,
    'green': 102,
    'blue': 102
}, {
    'color': 'gainsboro',
    'label': "Gainsboro",
    'hexa': '#dcdcdc',
    'red': 220,
    'green': 220,
    'blue': 220
}, {
    'color': 'gamboge',
    'label': "Gamboge",
    'hexa': '#e49b0f',
    'red': 228,
    'green': 155,
    'blue': 15
}, {
    'color': 'ghost_white',
    'label': "Ghost White",
    'hexa': '#f8f8ff',
    'red': 248,
    'green': 248,
    'blue': 255
}, {
    'color': 'ginger',
    'label': "Ginger",
    'hexa': '#b06500',
    'red': 176,
    'green': 101,
    'blue': 0
}, {
    'color': 'glaucous',
    'label': "Glaucous",
    'hexa': '#6082b6',
    'red': 96,
    'green': 130,
    'blue': 182
}, {
    'color': 'glitter',
    'label': "Glitter",
    'hexa': '#e6e8fa',
    'red': 230,
    'green': 232,
    'blue': 250
}, {
    'color': 'gold_metallic',
    'label': "Gold (Metallic)",
    'hexa': '#d4af37',
    'red': 212,
    'green': 175,
    'blue': 55
}, {
    'color': 'gold_web_golden',
    'label': "Gold (Web) (Golden)",
    'hexa': '#ffd700',
    'red': 255,
    'green': 215,
    'blue': 0
}, {
    'color': 'golden_brown',
    'label': "Golden Brown",
    'hexa': '#996515',
    'red': 153,
    'green': 101,
    'blue': 21
}, {
    'color': 'golden_poppy',
    'label': "Golden Poppy",
    'hexa': '#fcc200',
    'red': 252,
    'green': 194,
    'blue': 0
}, {
    'color': 'golden_yellow',
    'label': "Golden Yellow",
    'hexa': '#ffdf00',
    'red': 255,
    'green': 223,
    'blue': 0
}, {
    'color': 'goldenrod',
    'label': "Goldenrod",
    'hexa': '#daa520',
    'red': 218,
    'green': 165,
    'blue': 32
}, {
    'color': 'granny_smith_apple',
    'label': "Granny Smith Apple",
    'hexa': '#a8e4a0',
    'red': 168,
    'green': 228,
    'blue': 160
}, {
    'color': 'gray',
    'label': "Gray",
    'hexa': '#808080',
    'red': 128,
    'green': 128,
    'blue': 128
}, {
    'color': 'gray_asparagus',
    'label': "Gray-Asparagus",
    'hexa': '#465945',
    'red': 70,
    'green': 89,
    'blue': 69
}, {
    'color': 'gray_html_css_gray',
    'label': "Gray (Html/Css Gray)",
    'hexa': '#808080',
    'red': 128,
    'green': 128,
    'blue': 128
}, {
    'color': 'gray_x11_gray',
    'label': "Gray (X11 Gray)",
    'hexa': '#bebebe',
    'red': 190,
    'green': 190,
    'blue': 190
}, {
    'color': 'green_crayola',
    'label': "Green (Crayola)",
    'hexa': '#1cac78',
    'red': 28,
    'green': 172,
    'blue': 120
}, {
    'color': 'green_html_css_green',
    'label': "Green (Html/Css Green)",
    'hexa': '#008000',
    'red': 0,
    'green': 128,
    'blue': 0
}, {
    'color': 'green_munsell',
    'label': "Green (Munsell)",
    'hexa': '#00a877',
    'red': 0,
    'green': 168,
    'blue': 119
}, {
    'color': 'green_ncs',
    'label': "Green (Ncs)",
    'hexa': '#009f6b',
    'red': 0,
    'green': 159,
    'blue': 107
}, {
    'color': 'green_pigment',
    'label': "Green (Pigment)",
    'hexa': '#00a550',
    'red': 0,
    'green': 165,
    'blue': 80
}, {
    'color': 'green_ryb',
    'label': "Green (Ryb)",
    'hexa': '#66b032',
    'red': 102,
    'green': 176,
    'blue': 50
}, {
    'color': 'green_yellow',
    'label': "Green-Yellow",
    'hexa': '#adff2f',
    'red': 173,
    'green': 255,
    'blue': 47
}, {
    'color': 'grullo',
    'label': "Grullo",
    'hexa': '#a99a86',
    'red': 169,
    'green': 154,
    'blue': 134
}, {
    'color': 'guppie_green',
    'label': "Guppie Green",
    'hexa': '#00ff7f',
    'red': 0,
    'green': 255,
    'blue': 127
}, {
    'color': 'halay_be',
    'label': "Halayà úBe",
    'hexa': '#663854',
    'red': 102,
    'green': 56,
    'blue': 84
}, {
    'color': 'han_blue',
    'label': "Han Blue",
    'hexa': '#446ccf',
    'red': 68,
    'green': 108,
    'blue': 207
}, {
    'color': 'han_purple',
    'label': "Han Purple",
    'hexa': '#5218fa',
    'red': 82,
    'green': 24,
    'blue': 250
}, {
    'color': 'hansa_yellow',
    'label': "Hansa Yellow",
    'hexa': '#e9d66b',
    'red': 233,
    'green': 214,
    'blue': 107
}, {
    'color': 'harlequin',
    'label': "Harlequin",
    'hexa': '#3fff00',
    'red': 63,
    'green': 255,
    'blue': 0
}, {
    'color': 'harvard_crimson',
    'label': "Harvard Crimson",
    'hexa': '#c90016',
    'red': 201,
    'green': 0,
    'blue': 22
}, {
    'color': 'harvest_gold',
    'label': "Harvest Gold",
    'hexa': '#da9100',
    'red': 218,
    'green': 145,
    'blue': 0
}, {
    'color': 'heart_gold',
    'label': "Heart Gold",
    'hexa': '#808000',
    'red': 128,
    'green': 128,
    'blue': 0
}, {
    'color': 'heliotrope',
    'label': "Heliotrope",
    'hexa': '#df73ff',
    'red': 223,
    'green': 115,
    'blue': 255
}, {
    'color': 'hollywood_cerise',
    'label': "Hollywood Cerise",
    'hexa': '#f400a1',
    'red': 244,
    'green': 0,
    'blue': 161
}, {
    'color': 'honeydew',
    'label': "Honeydew",
    'hexa': '#f0fff0',
    'red': 240,
    'green': 255,
    'blue': 240
}, {
    'color': 'honolulu_blue',
    'label': "Honolulu Blue",
    'hexa': '#007fbf',
    'red': 0,
    'green': 127,
    'blue': 191
}, {
    'color': 'hooker_s_green',
    'label': "Hooker'S Green",
    'hexa': '#49796b',
    'red': 73,
    'green': 121,
    'blue': 107
}, {
    'color': 'hot_magenta',
    'label': "Hot Magenta",
    'hexa': '#ff1dce',
    'red': 255,
    'green': 29,
    'blue': 206
}, {
    'color': 'hot_pink',
    'label': "Hot Pink",
    'hexa': '#ff69b4',
    'red': 255,
    'green': 105,
    'blue': 180
}, {
    'color': 'hunter_green',
    'label': "Hunter Green",
    'hexa': '#355e3b',
    'red': 53,
    'green': 94,
    'blue': 59
}, {
    'color': 'iceberg',
    'label': "Iceberg",
    'hexa': '#71a6d2',
    'red': 113,
    'green': 166,
    'blue': 210
}, {
    'color': 'icterine',
    'label': "Icterine",
    'hexa': '#fcf75e',
    'red': 252,
    'green': 247,
    'blue': 94
}, {
    'color': 'imperial_blue',
    'label': "Imperial Blue",
    'hexa': '#002395',
    'red': 0,
    'green': 35,
    'blue': 149
}, {
    'color': 'inchworm',
    'label': "Inchworm",
    'hexa': '#b2ec5d',
    'red': 178,
    'green': 236,
    'blue': 93
}, {
    'color': 'india_green',
    'label': "India Green",
    'hexa': '#138808',
    'red': 19,
    'green': 136,
    'blue': 8
}, {
    'color': 'indian_red',
    'label': "Indian Red",
    'hexa': '#cd5c5c',
    'red': 205,
    'green': 92,
    'blue': 92
}, {
    'color': 'indian_yellow',
    'label': "Indian Yellow",
    'hexa': '#e3a857',
    'red': 227,
    'green': 168,
    'blue': 87
}, {
    'color': 'indigo',
    'label': "Indigo",
    'hexa': '#6f00ff',
    'red': 111,
    'green': 0,
    'blue': 255
}, {
    'color': 'indigo_dye',
    'label': "Indigo (Dye)",
    'hexa': '#00416a',
    'red': 0,
    'green': 65,
    'blue': 106
}, {
    'color': 'indigo_web',
    'label': "Indigo (Web)",
    'hexa': '#4b0082',
    'red': 75,
    'green': 0,
    'blue': 130
}, {
    'color': 'international_klein_blue',
    'label': "International Klein Blue",
    'hexa': '#002fa7',
    'red': 0,
    'green': 47,
    'blue': 167
}, {
    'color': 'international_orange_aerospace',
    'label': "International Orange (Aerospace)",
    'hexa': '#ff4f00',
    'red': 255,
    'green': 79,
    'blue': 0
}, {
    'color': 'international_orange_engineering',
    'label': "International Orange (Engineering)",
    'hexa': '#ba160c',
    'red': 186,
    'green': 22,
    'blue': 12
}, {
    'color': 'international_orange_golden_gate_bridge',
    'label': "International Orange (Golden Gate Bridge)",
    'hexa': '#c0362c',
    'red': 192,
    'green': 54,
    'blue': 44
}, {
    'color': 'iris',
    'label': "Iris",
    'hexa': '#5a4fcf',
    'red': 90,
    'green': 79,
    'blue': 207
}, {
    'color': 'isabelline',
    'label': "Isabelline",
    'hexa': '#f4f0ec',
    'red': 244,
    'green': 240,
    'blue': 236
}, {
    'color': 'islamic_green',
    'label': "Islamic Green",
    'hexa': '#009000',
    'red': 0,
    'green': 144,
    'blue': 0
}, {
    'color': 'ivory',
    'label': "Ivory",
    'hexa': '#fffff0',
    'red': 255,
    'green': 255,
    'blue': 240
}, {
    'color': 'jade',
    'label': "Jade",
    'hexa': '#00a86b',
    'red': 0,
    'green': 168,
    'blue': 107
}, {
    'color': 'jasmine',
    'label': "Jasmine",
    'hexa': '#f8de7e',
    'red': 248,
    'green': 222,
    'blue': 126
}, {
    'color': 'jasper',
    'label': "Jasper",
    'hexa': '#d73b3e',
    'red': 215,
    'green': 59,
    'blue': 62
}, {
    'color': 'jazzberry_jam',
    'label': "Jazzberry Jam",
    'hexa': '#a50b5e',
    'red': 165,
    'green': 11,
    'blue': 94
}, {
    'color': 'jet',
    'label': "Jet",
    'hexa': '#343434',
    'red': 52,
    'green': 52,
    'blue': 52
}, {
    'color': 'jonquil',
    'label': "Jonquil",
    'hexa': '#fada5e',
    'red': 250,
    'green': 218,
    'blue': 94
}, {
    'color': 'june_bud',
    'label': "June Bud",
    'hexa': '#bdda57',
    'red': 189,
    'green': 218,
    'blue': 87
}, {
    'color': 'jungle_green',
    'label': "Jungle Green",
    'hexa': '#29ab87',
    'red': 41,
    'green': 171,
    'blue': 135
}, {
    'color': 'kelly_green',
    'label': "Kelly Green",
    'hexa': '#4cbb17',
    'red': 76,
    'green': 187,
    'blue': 23
}, {
    'color': 'kenyan_copper',
    'label': "Kenyan Copper",
    'hexa': '#7c1c05',
    'red': 124,
    'green': 28,
    'blue': 5
}, {
    'color': 'khaki_html_css_khaki',
    'label': "Khaki (Html/Css) (Khaki)",
    'hexa': '#c3b091',
    'red': 195,
    'green': 176,
    'blue': 145
}, {
    'color': 'khaki_x11_light_khaki',
    'label': "Khaki (X11) (Light Khaki)",
    'hexa': '#f0e68c',
    'red': 240,
    'green': 230,
    'blue': 140
}, {
    'color': 'ku_crimson',
    'label': "Ku Crimson",
    'hexa': '#e8000d',
    'red': 232,
    'green': 0,
    'blue': 13
}, {
    'color': 'la_salle_green',
    'label': "La Salle Green",
    'hexa': '#087830',
    'red': 8,
    'green': 120,
    'blue': 48
}, {
    'color': 'languid_lavender',
    'label': "Languid Lavender",
    'hexa': '#d6cadd',
    'red': 214,
    'green': 202,
    'blue': 221
}, {
    'color': 'lapis_lazuli',
    'label': "Lapis Lazuli",
    'hexa': '#26619c',
    'red': 38,
    'green': 97,
    'blue': 156
}, {
    'color': 'laser_lemon',
    'label': "Laser Lemon",
    'hexa': '#fefe22',
    'red': 254,
    'green': 254,
    'blue': 34
}, {
    'color': 'laurel_green',
    'label': "Laurel Green",
    'hexa': '#a9ba9d',
    'red': 169,
    'green': 186,
    'blue': 157
}, {
    'color': 'lava',
    'label': "Lava",
    'hexa': '#cf1020',
    'red': 207,
    'green': 16,
    'blue': 32
}, {
    'color': 'lavender_blue',
    'label': "Lavender Blue",
    'hexa': '#ccccff',
    'red': 204,
    'green': 204,
    'blue': 255
}, {
    'color': 'lavender_blush',
    'label': "Lavender Blush",
    'hexa': '#fff0f5',
    'red': 255,
    'green': 240,
    'blue': 245
}, {
    'color': 'lavender_floral',
    'label': "Lavender (Floral)",
    'hexa': '#b57edc',
    'red': 181,
    'green': 126,
    'blue': 220
}, {
    'color': 'lavender_gray',
    'label': "Lavender Gray",
    'hexa': '#c4c3d0',
    'red': 196,
    'green': 195,
    'blue': 208
}, {
    'color': 'lavender_indigo',
    'label': "Lavender Indigo",
    'hexa': '#9457eb',
    'red': 148,
    'green': 87,
    'blue': 235
}, {
    'color': 'lavender_magenta',
    'label': "Lavender Magenta",
    'hexa': '#ee82ee',
    'red': 238,
    'green': 130,
    'blue': 238
}, {
    'color': 'lavender_mist',
    'label': "Lavender Mist",
    'hexa': '#e6e6fa',
    'red': 230,
    'green': 230,
    'blue': 250
}, {
    'color': 'lavender_pink',
    'label': "Lavender Pink",
    'hexa': '#fbaed2',
    'red': 251,
    'green': 174,
    'blue': 210
}, {
    'color': 'lavender_purple',
    'label': "Lavender Purple",
    'hexa': '#967bb6',
    'red': 150,
    'green': 123,
    'blue': 182
}, {
    'color': 'lavender_rose',
    'label': "Lavender Rose",
    'hexa': '#fba0e3',
    'red': 251,
    'green': 160,
    'blue': 227
}, {
    'color': 'lavender_web',
    'label': "Lavender (Web)",
    'hexa': '#e6e6fa',
    'red': 230,
    'green': 230,
    'blue': 250
}, {
    'color': 'lawn_green',
    'label': "Lawn Green",
    'hexa': '#7cfc00',
    'red': 124,
    'green': 252,
    'blue': 0
}, {
    'color': 'lemon',
    'label': "Lemon",
    'hexa': '#fff700',
    'red': 255,
    'green': 247,
    'blue': 0
}, {
    'color': 'lemon_chiffon',
    'label': "Lemon Chiffon",
    'hexa': '#fffacd',
    'red': 255,
    'green': 250,
    'blue': 205
}, {
    'color': 'lemon_lime',
    'label': "Lemon Lime",
    'hexa': '#e3ff00',
    'red': 227,
    'green': 255,
    'blue': 0
}, {
    'color': 'licorice',
    'label': "Licorice",
    'hexa': '#1a1110',
    'red': 26,
    'green': 17,
    'blue': 16
}, {
    'color': 'light_apricot',
    'label': "Light Apricot",
    'hexa': '#fdd5b1',
    'red': 253,
    'green': 213,
    'blue': 177
}, {
    'color': 'light_blue',
    'label': "Light Blue",
    'hexa': '#add8e6',
    'red': 173,
    'green': 216,
    'blue': 230
}, {
    'color': 'light_brown',
    'label': "Light Brown",
    'hexa': '#b5651d',
    'red': 181,
    'green': 101,
    'blue': 29
}, {
    'color': 'light_carmine_pink',
    'label': "Light Carmine Pink",
    'hexa': '#e66771',
    'red': 230,
    'green': 103,
    'blue': 113
}, {
    'color': 'light_coral',
    'label': "Light Coral",
    'hexa': '#f08080',
    'red': 240,
    'green': 128,
    'blue': 128
}, {
    'color': 'light_cornflower_blue',
    'label': "Light Cornflower Blue",
    'hexa': '#93ccea',
    'red': 147,
    'green': 204,
    'blue': 234
}, {
    'color': 'light_crimson',
    'label': "Light Crimson",
    'hexa': '#f56991',
    'red': 245,
    'green': 105,
    'blue': 145
}, {
    'color': 'light_cyan',
    'label': "Light Cyan",
    'hexa': '#e0ffff',
    'red': 224,
    'green': 255,
    'blue': 255
}, {
    'color': 'light_fuchsia_pink',
    'label': "Light Fuchsia Pink",
    'hexa': '#f984ef',
    'red': 249,
    'green': 132,
    'blue': 239
}, {
    'color': 'light_goldenrod_yellow',
    'label': "Light Goldenrod Yellow",
    'hexa': '#fafad2',
    'red': 250,
    'green': 250,
    'blue': 210
}, {
    'color': 'light_gray',
    'label': "Light Gray",
    'hexa': '#d3d3d3',
    'red': 211,
    'green': 211,
    'blue': 211
}, {
    'color': 'light_green',
    'label': "Light Green",
    'hexa': '#90ee90',
    'red': 144,
    'green': 238,
    'blue': 144
}, {
    'color': 'light_khaki',
    'label': "Light Khaki",
    'hexa': '#f0e68c',
    'red': 240,
    'green': 230,
    'blue': 140
}, {
    'color': 'light_pastel_purple',
    'label': "Light Pastel Purple",
    'hexa': '#b19cd9',
    'red': 177,
    'green': 156,
    'blue': 217
}, {
    'color': 'light_pink',
    'label': "Light Pink",
    'hexa': '#ffb6c1',
    'red': 255,
    'green': 182,
    'blue': 193
}, {
    'color': 'light_red_ochre',
    'label': "Light Red Ochre",
    'hexa': '#e97451',
    'red': 233,
    'green': 116,
    'blue': 81
}, {
    'color': 'light_salmon',
    'label': "Light Salmon",
    'hexa': '#ffa07a',
    'red': 255,
    'green': 160,
    'blue': 122
}, {
    'color': 'light_salmon_pink',
    'label': "Light Salmon Pink",
    'hexa': '#f99',
    'red': 255,
    'green': 153,
    'blue': 153
}, {
    'color': 'light_sea_green',
    'label': "Light Sea Green",
    'hexa': '#20b2aa',
    'red': 32,
    'green': 178,
    'blue': 170
}, {
    'color': 'light_sky_blue',
    'label': "Light Sky Blue",
    'hexa': '#87cefa',
    'red': 135,
    'green': 206,
    'blue': 250
}, {
    'color': 'light_slate_gray',
    'label': "Light Slate Gray",
    'hexa': '#778899',
    'red': 119,
    'green': 136,
    'blue': 153
}, {
    'color': 'light_taupe',
    'label': "Light Taupe",
    'hexa': '#b38b6d',
    'red': 179,
    'green': 139,
    'blue': 109
}, {
    'color': 'light_thulian_pink',
    'label': "Light Thulian Pink",
    'hexa': '#e68fac',
    'red': 230,
    'green': 143,
    'blue': 172
}, {
    'color': 'light_yellow',
    'label': "Light Yellow",
    'hexa': '#ffffe0',
    'red': 255,
    'green': 255,
    'blue': 224
}, {
    'color': 'lilac',
    'label': "Lilac",
    'hexa': '#c8a2c8',
    'red': 200,
    'green': 162,
    'blue': 200
}, {
    'color': 'lime_color_wheel',
    'label': "Lime (Color Wheel)",
    'hexa': '#bfff00',
    'red': 191,
    'green': 255,
    'blue': 0
}, {
    'color': 'lime_green',
    'label': "Lime Green",
    'hexa': '#32cd32',
    'red': 50,
    'green': 205,
    'blue': 50
}, {
    'color': 'lime_web_x11_green',
    'label': "Lime (Web) (X11 Green)",
    'hexa': '#00ff00',
    'red': 0,
    'green': 255,
    'blue': 0
}, {
    'color': 'limerick',
    'label': "Limerick",
    'hexa': '#9dc209',
    'red': 157,
    'green': 194,
    'blue': 9
}, {
    'color': 'lincoln_green',
    'label': "Lincoln Green",
    'hexa': '#195905',
    'red': 25,
    'green': 89,
    'blue': 5
}, {
    'color': 'linen',
    'label': "Linen",
    'hexa': '#faf0e6',
    'red': 250,
    'green': 240,
    'blue': 230
}, {
    'color': 'lion',
    'label': "Lion",
    'hexa': '#c19a6b',
    'red': 193,
    'green': 154,
    'blue': 107
}, {
    'color': 'little_boy_blue',
    'label': "Little Boy Blue",
    'hexa': '#6ca0dc',
    'red': 108,
    'green': 160,
    'blue': 220
}, {
    'color': 'liver',
    'label': "Liver",
    'hexa': '#534b4f',
    'red': 83,
    'green': 75,
    'blue': 79
}, {
    'color': 'lust',
    'label': "Lust",
    'hexa': '#e62020',
    'red': 230,
    'green': 32,
    'blue': 32
}, {
    'color': 'magenta',
    'label': "Magenta",
    'hexa': '#ff00ff',
    'red': 255,
    'green': 0,
    'blue': 255
}, {
    'color': 'magenta_dye',
    'label': "Magenta (Dye)",
    'hexa': '#ca1f7b',
    'red': 202,
    'green': 31,
    'blue': 123
}, {
    'color': 'magenta_process',
    'label': "Magenta (Process)",
    'hexa': '#ff0090',
    'red': 255,
    'green': 0,
    'blue': 144
}, {
    'color': 'magic_mint',
    'label': "Magic Mint",
    'hexa': '#aaf0d1',
    'red': 170,
    'green': 240,
    'blue': 209
}, {
    'color': 'magnolia',
    'label': "Magnolia",
    'hexa': '#f8f4ff',
    'red': 248,
    'green': 244,
    'blue': 255
}, {
    'color': 'mahogany',
    'label': "Mahogany",
    'hexa': '#c04000',
    'red': 192,
    'green': 64,
    'blue': 0
}, {
    'color': 'maize',
    'label': "Maize",
    'hexa': '#fbec5d',
    'red': 251,
    'green': 236,
    'blue': 93
}, {
    'color': 'majorelle_blue',
    'label': "Majorelle Blue",
    'hexa': '#6050dc',
    'red': 96,
    'green': 80,
    'blue': 220
}, {
    'color': 'malachite',
    'label': "Malachite",
    'hexa': '#0bda51',
    'red': 11,
    'green': 218,
    'blue': 81
}, {
    'color': 'manatee',
    'label': "Manatee",
    'hexa': '#979aaa',
    'red': 151,
    'green': 154,
    'blue': 170
}, {
    'color': 'mango_tango',
    'label': "Mango Tango",
    'hexa': '#ff8243',
    'red': 255,
    'green': 130,
    'blue': 67
}, {
    'color': 'mantis',
    'label': "Mantis",
    'hexa': '#74c365',
    'red': 116,
    'green': 195,
    'blue': 101
}, {
    'color': 'mardi_gras',
    'label': "Mardi Gras",
    'hexa': '#880085',
    'red': 136,
    'green': 0,
    'blue': 133
}, {
    'color': 'maroon_crayola',
    'label': "Maroon (Crayola)",
    'hexa': '#c32148',
    'red': 195,
    'green': 33,
    'blue': 72
}, {
    'color': 'maroon_html_css',
    'label': "Maroon (Html/Css)",
    'hexa': '#800000',
    'red': 128,
    'green': 0,
    'blue': 0
}, {
    'color': 'maroon_x11',
    'label': "Maroon (X11)",
    'hexa': '#b03060',
    'red': 176,
    'green': 48,
    'blue': 96
}, {
    'color': 'mauve',
    'label': "Mauve",
    'hexa': '#e0b0ff',
    'red': 224,
    'green': 176,
    'blue': 255
}, {
    'color': 'mauve_taupe',
    'label': "Mauve Taupe",
    'hexa': '#915f6d',
    'red': 145,
    'green': 95,
    'blue': 109
}, {
    'color': 'mauvelous',
    'label': "Mauvelous",
    'hexa': '#ef98aa',
    'red': 239,
    'green': 152,
    'blue': 170
}, {
    'color': 'maya_blue',
    'label': "Maya Blue",
    'hexa': '#73c2fb',
    'red': 115,
    'green': 194,
    'blue': 251
}, {
    'color': 'meat_brown',
    'label': "Meat Brown",
    'hexa': '#e5b73b',
    'red': 229,
    'green': 183,
    'blue': 59
}, {
    'color': 'medium_aquamarine',
    'label': "Medium Aquamarine",
    'hexa': '#66ddaa',
    'red': 102,
    'green': 221,
    'blue': 170
}, {
    'color': 'medium_blue',
    'label': "Medium Blue",
    'hexa': '#0000cd',
    'red': 0,
    'green': 0,
    'blue': 205
}, {
    'color': 'medium_candy_apple_red',
    'label': "Medium Candy Apple Red",
    'hexa': '#e2062c',
    'red': 226,
    'green': 6,
    'blue': 44
}, {
    'color': 'medium_carmine',
    'label': "Medium Carmine",
    'hexa': '#af4035',
    'red': 175,
    'green': 64,
    'blue': 53
}, {
    'color': 'medium_champagne',
    'label': "Medium Champagne",
    'hexa': '#f3e5ab',
    'red': 243,
    'green': 229,
    'blue': 171
}, {
    'color': 'medium_electric_blue',
    'label': "Medium Electric Blue",
    'hexa': '#035096',
    'red': 3,
    'green': 80,
    'blue': 150
}, {
    'color': 'medium_jungle_green',
    'label': "Medium Jungle Green",
    'hexa': '#1c352d',
    'red': 28,
    'green': 53,
    'blue': 45
}, {
    'color': 'medium_lavender_magenta',
    'label': "Medium Lavender Magenta",
    'hexa': '#dda0dd',
    'red': 221,
    'green': 160,
    'blue': 221
}, {
    'color': 'medium_orchid',
    'label': "Medium Orchid",
    'hexa': '#ba55d3',
    'red': 186,
    'green': 85,
    'blue': 211
}, {
    'color': 'medium_persian_blue',
    'label': "Medium Persian Blue",
    'hexa': '#0067a5',
    'red': 0,
    'green': 103,
    'blue': 165
}, {
    'color': 'medium_purple',
    'label': "Medium Purple",
    'hexa': '#9370db',
    'red': 147,
    'green': 112,
    'blue': 219
}, {
    'color': 'medium_red_violet',
    'label': "Medium Red-Violet",
    'hexa': '#bb3385',
    'red': 187,
    'green': 51,
    'blue': 133
}, {
    'color': 'medium_ruby',
    'label': "Medium Ruby",
    'hexa': '#aa4069',
    'red': 170,
    'green': 64,
    'blue': 105
}, {
    'color': 'medium_sea_green',
    'label': "Medium Sea Green",
    'hexa': '#3cb371',
    'red': 60,
    'green': 179,
    'blue': 113
}, {
    'color': 'medium_slate_blue',
    'label': "Medium Slate Blue",
    'hexa': '#7b68ee',
    'red': 123,
    'green': 104,
    'blue': 238
}, {
    'color': 'medium_spring_bud',
    'label': "Medium Spring Bud",
    'hexa': '#c9dc87',
    'red': 201,
    'green': 220,
    'blue': 135
}, {
    'color': 'medium_spring_green',
    'label': "Medium Spring Green",
    'hexa': '#00fa9a',
    'red': 0,
    'green': 250,
    'blue': 154
}, {
    'color': 'medium_taupe',
    'label': "Medium Taupe",
    'hexa': '#674c47',
    'red': 103,
    'green': 76,
    'blue': 71
}, {
    'color': 'medium_turquoise',
    'label': "Medium Turquoise",
    'hexa': '#48d1cc',
    'red': 72,
    'green': 209,
    'blue': 204
}, {
    'color': 'medium_tuscan_red',
    'label': "Medium Tuscan Red",
    'hexa': '#79443b',
    'red': 121,
    'green': 68,
    'blue': 59
}, {
    'color': 'medium_vermilion',
    'label': "Medium Vermilion",
    'hexa': '#d9603b',
    'red': 217,
    'green': 96,
    'blue': 59
}, {
    'color': 'medium_violet_red',
    'label': "Medium Violet-Red",
    'hexa': '#c71585',
    'red': 199,
    'green': 21,
    'blue': 133
}, {
    'color': 'mellow_apricot',
    'label': "Mellow Apricot",
    'hexa': '#f8b878',
    'red': 248,
    'green': 184,
    'blue': 120
}, {
    'color': 'mellow_yellow',
    'label': "Mellow Yellow",
    'hexa': '#f8de7e',
    'red': 248,
    'green': 222,
    'blue': 126
}, {
    'color': 'melon',
    'label': "Melon",
    'hexa': '#fdbcb4',
    'red': 253,
    'green': 188,
    'blue': 180
}, {
    'color': 'midnight_blue',
    'label': "Midnight Blue",
    'hexa': '#191970',
    'red': 25,
    'green': 25,
    'blue': 112
}, {
    'color': 'midnight_green_eagle_green',
    'label': "Midnight Green (Eagle Green)",
    'hexa': '#004953',
    'red': 0,
    'green': 73,
    'blue': 83
}, {
    'color': 'mikado_yellow',
    'label': "Mikado Yellow",
    'hexa': '#ffc40c',
    'red': 255,
    'green': 196,
    'blue': 12
}, {
    'color': 'mint',
    'label': "Mint",
    'hexa': '#3eb489',
    'red': 62,
    'green': 180,
    'blue': 137
}, {
    'color': 'mint_cream',
    'label': "Mint Cream",
    'hexa': '#f5fffa',
    'red': 245,
    'green': 255,
    'blue': 250
}, {
    'color': 'mint_green',
    'label': "Mint Green",
    'hexa': '#98ff98',
    'red': 152,
    'green': 255,
    'blue': 152
}, {
    'color': 'misty_rose',
    'label': "Misty Rose",
    'hexa': '#ffe4e1',
    'red': 255,
    'green': 228,
    'blue': 225
}, {
    'color': 'moccasin',
    'label': "Moccasin",
    'hexa': '#faebd7',
    'red': 250,
    'green': 235,
    'blue': 215
}, {
    'color': 'mode_beige',
    'label': "Mode Beige",
    'hexa': '#967117',
    'red': 150,
    'green': 113,
    'blue': 23
}, {
    'color': 'moonstone_blue',
    'label': "Moonstone Blue",
    'hexa': '#73a9c2',
    'red': 115,
    'green': 169,
    'blue': 194
}, {
    'color': 'mordant_red_19',
    'label': "Mordant Red 19",
    'hexa': '#ae0c00',
    'red': 174,
    'green': 12,
    'blue': 0
}, {
    'color': 'moss_green',
    'label': "Moss Green",
    'hexa': '#addfad',
    'red': 173,
    'green': 223,
    'blue': 173
}, {
    'color': 'mountain_meadow',
    'label': "Mountain Meadow",
    'hexa': '#30ba8f',
    'red': 48,
    'green': 186,
    'blue': 143
}, {
    'color': 'mountbatten_pink',
    'label': "Mountbatten Pink",
    'hexa': '#997a8d',
    'red': 153,
    'green': 122,
    'blue': 141
}, {
    'color': 'msu_green',
    'label': "Msu Green",
    'hexa': '#18453b',
    'red': 24,
    'green': 69,
    'blue': 59
}, {
    'color': 'mulberry',
    'label': "Mulberry",
    'hexa': '#c54b8c',
    'red': 197,
    'green': 75,
    'blue': 140
}, {
    'color': 'mustard',
    'label': "Mustard",
    'hexa': '#ffdb58',
    'red': 255,
    'green': 219,
    'blue': 88
}, {
    'color': 'myrtle',
    'label': "Myrtle",
    'hexa': '#21421e',
    'red': 33,
    'green': 66,
    'blue': 30
}, {
    'color': 'nadeshiko_pink',
    'label': "Nadeshiko Pink",
    'hexa': '#f6adc6',
    'red': 246,
    'green': 173,
    'blue': 198
}, {
    'color': 'napier_green',
    'label': "Napier Green",
    'hexa': '#2a8000',
    'red': 42,
    'green': 128,
    'blue': 0
}, {
    'color': 'naples_yellow',
    'label': "Naples Yellow",
    'hexa': '#fada5e',
    'red': 250,
    'green': 218,
    'blue': 94
}, {
    'color': 'navajo_white',
    'label': "Navajo White",
    'hexa': '#ffdead',
    'red': 255,
    'green': 222,
    'blue': 173
}, {
    'color': 'navy_blue',
    'label': "Navy Blue",
    'hexa': '#000080',
    'red': 0,
    'green': 0,
    'blue': 128
}, {
    'color': 'neon_carrot',
    'label': "Neon Carrot",
    'hexa': '#ffa343',
    'red': 255,
    'green': 163,
    'blue': 67
}, {
    'color': 'neon_fuchsia',
    'label': "Neon Fuchsia",
    'hexa': '#fe4164',
    'red': 254,
    'green': 65,
    'blue': 100
}, {
    'color': 'neon_green',
    'label': "Neon Green",
    'hexa': '#39ff14',
    'red': 57,
    'green': 255,
    'blue': 20
}, {
    'color': 'new_york_pink',
    'label': "New York Pink",
    'hexa': '#d7837f',
    'red': 215,
    'green': 131,
    'blue': 127
}, {
    'color': 'non_photo_blue',
    'label': "Non-Photo Blue",
    'hexa': '#a4dded',
    'red': 164,
    'green': 221,
    'blue': 237
}, {
    'color': 'north_texas_green',
    'label': "North Texas Green",
    'hexa': '#059033',
    'red': 5,
    'green': 144,
    'blue': 51
}, {
    'color': 'ocean_boat_blue',
    'label': "Ocean Boat Blue",
    'hexa': '#0077be',
    'red': 0,
    'green': 119,
    'blue': 190
}, {
    'color': 'ochre',
    'label': "Ochre",
    'hexa': '#cc7722',
    'red': 204,
    'green': 119,
    'blue': 34
}, {
    'color': 'office_green',
    'label': "Office Green",
    'hexa': '#008000',
    'red': 0,
    'green': 128,
    'blue': 0
}, {
    'color': 'old_gold',
    'label': "Old Gold",
    'hexa': '#cfb53b',
    'red': 207,
    'green': 181,
    'blue': 59
}, {
    'color': 'old_lace',
    'label': "Old Lace",
    'hexa': '#fdf5e6',
    'red': 253,
    'green': 245,
    'blue': 230
}, {
    'color': 'old_lavender',
    'label': "Old Lavender",
    'hexa': '#796878',
    'red': 121,
    'green': 104,
    'blue': 120
}, {
    'color': 'old_mauve',
    'label': "Old Mauve",
    'hexa': '#673147',
    'red': 103,
    'green': 49,
    'blue': 71
}, {
    'color': 'old_rose',
    'label': "Old Rose",
    'hexa': '#c08081',
    'red': 192,
    'green': 128,
    'blue': 129
}, {
    'color': 'olive',
    'label': "Olive",
    'hexa': '#808000',
    'red': 128,
    'green': 128,
    'blue': 0
}, {
    'color': 'olive_drab_7',
    'label': "Olive Drab #7",
    'hexa': '#3c341f',
    'red': 60,
    'green': 52,
    'blue': 31
}, {
    'color': 'olive_drab_web_olive_drab_3',
    'label': "Olive Drab (Web) (Olive Drab #3)",
    'hexa': '#6b8e23',
    'red': 107,
    'green': 142,
    'blue': 35
}, {
    'color': 'olivine',
    'label': "Olivine",
    'hexa': '#9ab973',
    'red': 154,
    'green': 185,
    'blue': 115
}, {
    'color': 'onyx',
    'label': "Onyx",
    'hexa': '#353839',
    'red': 53,
    'green': 56,
    'blue': 57
}, {
    'color': 'opera_mauve',
    'label': "Opera Mauve",
    'hexa': '#b784a7',
    'red': 183,
    'green': 132,
    'blue': 167
}, {
    'color': 'orange_peel',
    'label': "Orange Peel",
    'hexa': '#ff9f00',
    'red': 255,
    'green': 159,
    'blue': 0
}, {
    'color': 'orange_red',
    'label': "Orange-Red",
    'hexa': '#ff4500',
    'red': 255,
    'green': 69,
    'blue': 0
}, {
    'color': 'orange_ryb',
    'label': "Orange (Ryb)",
    'hexa': '#fb9902',
    'red': 251,
    'green': 153,
    'blue': 2
}, {
    'color': 'orange_web_color',
    'label': "Orange (Web Color)",
    'hexa': '#ffa500',
    'red': 255,
    'green': 165,
    'blue': 0
}, {
    'color': 'orchid',
    'label': "Orchid",
    'hexa': '#da70d6',
    'red': 218,
    'green': 112,
    'blue': 214
}, {
    'color': 'otter_brown',
    'label': "Otter Brown",
    'hexa': '#654321',
    'red': 101,
    'green': 67,
    'blue': 33
}, {
    'color': 'ou_crimson_red',
    'label': "Ou Crimson Red",
    'hexa': '#990000',
    'red': 153,
    'green': 0,
    'blue': 0
}, {
    'color': 'outer_space',
    'label': "Outer Space",
    'hexa': '#414a4c',
    'red': 65,
    'green': 74,
    'blue': 76
}, {
    'color': 'outrageous_orange',
    'label': "Outrageous Orange",
    'hexa': '#ff6e4a',
    'red': 255,
    'green': 110,
    'blue': 74
}, {
    'color': 'oxford_blue',
    'label': "Oxford Blue",
    'hexa': '#002147',
    'red': 0,
    'green': 33,
    'blue': 71
}, {
    'color': 'pakistan_green',
    'label': "Pakistan Green",
    'hexa': '#006600',
    'red': 0,
    'green': 102,
    'blue': 0
}, {
    'color': 'palatinate_blue',
    'label': "Palatinate Blue",
    'hexa': '#273be2',
    'red': 39,
    'green': 59,
    'blue': 226
}, {
    'color': 'palatinate_purple',
    'label': "Palatinate Purple",
    'hexa': '#682860',
    'red': 104,
    'green': 40,
    'blue': 96
}, {
    'color': 'pale_aqua',
    'label': "Pale Aqua",
    'hexa': '#bcd4e6',
    'red': 188,
    'green': 212,
    'blue': 230
}, {
    'color': 'pale_blue',
    'label': "Pale Blue",
    'hexa': '#afeeee',
    'red': 175,
    'green': 238,
    'blue': 238
}, {
    'color': 'pale_brown',
    'label': "Pale Brown",
    'hexa': '#987654',
    'red': 152,
    'green': 118,
    'blue': 84
}, {
    'color': 'pale_carmine',
    'label': "Pale Carmine",
    'hexa': '#af4035',
    'red': 175,
    'green': 64,
    'blue': 53
}, {
    'color': 'pale_cerulean',
    'label': "Pale Cerulean",
    'hexa': '#9bc4e2',
    'red': 155,
    'green': 196,
    'blue': 226
}, {
    'color': 'pale_chestnut',
    'label': "Pale Chestnut",
    'hexa': '#ddadaf',
    'red': 221,
    'green': 173,
    'blue': 175
}, {
    'color': 'pale_copper',
    'label': "Pale Copper",
    'hexa': '#da8a67',
    'red': 218,
    'green': 138,
    'blue': 103
}, {
    'color': 'pale_cornflower_blue',
    'label': "Pale Cornflower Blue",
    'hexa': '#abcdef',
    'red': 171,
    'green': 205,
    'blue': 239
}, {
    'color': 'pale_gold',
    'label': "Pale Gold",
    'hexa': '#e6be8a',
    'red': 230,
    'green': 190,
    'blue': 138
}, {
    'color': 'pale_goldenrod',
    'label': "Pale Goldenrod",
    'hexa': '#eee8aa',
    'red': 238,
    'green': 232,
    'blue': 170
}, {
    'color': 'pale_green',
    'label': "Pale Green",
    'hexa': '#98fb98',
    'red': 152,
    'green': 251,
    'blue': 152
}, {
    'color': 'pale_lavender',
    'label': "Pale Lavender",
    'hexa': '#dcd0ff',
    'red': 220,
    'green': 208,
    'blue': 255
}, {
    'color': 'pale_magenta',
    'label': "Pale Magenta",
    'hexa': '#f984e5',
    'red': 249,
    'green': 132,
    'blue': 229
}, {
    'color': 'pale_pink',
    'label': "Pale Pink",
    'hexa': '#fadadd',
    'red': 250,
    'green': 218,
    'blue': 221
}, {
    'color': 'pale_plum',
    'label': "Pale Plum",
    'hexa': '#dda0dd',
    'red': 221,
    'green': 160,
    'blue': 221
}, {
    'color': 'pale_red_violet',
    'label': "Pale Red-Violet",
    'hexa': '#db7093',
    'red': 219,
    'green': 112,
    'blue': 147
}, {
    'color': 'pale_robin_egg_blue',
    'label': "Pale Robin Egg Blue",
    'hexa': '#96ded1',
    'red': 150,
    'green': 222,
    'blue': 209
}, {
    'color': 'pale_silver',
    'label': "Pale Silver",
    'hexa': '#c9c0bb',
    'red': 201,
    'green': 192,
    'blue': 187
}, {
    'color': 'pale_spring_bud',
    'label': "Pale Spring Bud",
    'hexa': '#ecebbd',
    'red': 236,
    'green': 235,
    'blue': 189
}, {
    'color': 'pale_taupe',
    'label': "Pale Taupe",
    'hexa': '#bc987e',
    'red': 188,
    'green': 152,
    'blue': 126
}, {
    'color': 'pale_violet_red',
    'label': "Pale Violet-Red",
    'hexa': '#db7093',
    'red': 219,
    'green': 112,
    'blue': 147
}, {
    'color': 'pansy_purple',
    'label': "Pansy Purple",
    'hexa': '#78184a',
    'red': 120,
    'green': 24,
    'blue': 74
}, {
    'color': 'papaya_whip',
    'label': "Papaya Whip",
    'hexa': '#ffefd5',
    'red': 255,
    'green': 239,
    'blue': 213
}, {
    'color': 'paris_green',
    'label': "Paris Green",
    'hexa': '#50c878',
    'red': 80,
    'green': 200,
    'blue': 120
}, {
    'color': 'pastel_blue',
    'label': "Pastel Blue",
    'hexa': '#aec6cf',
    'red': 174,
    'green': 198,
    'blue': 207
}, {
    'color': 'pastel_brown',
    'label': "Pastel Brown",
    'hexa': '#836953',
    'red': 131,
    'green': 105,
    'blue': 83
}, {
    'color': 'pastel_gray',
    'label': "Pastel Gray",
    'hexa': '#cfcfc4',
    'red': 207,
    'green': 207,
    'blue': 196
}, {
    'color': 'pastel_green',
    'label': "Pastel Green",
    'hexa': '#77dd77',
    'red': 119,
    'green': 221,
    'blue': 119
}, {
    'color': 'pastel_magenta',
    'label': "Pastel Magenta",
    'hexa': '#f49ac2',
    'red': 244,
    'green': 154,
    'blue': 194
}, {
    'color': 'pastel_orange',
    'label': "Pastel Orange",
    'hexa': '#ffb347',
    'red': 255,
    'green': 179,
    'blue': 71
}, {
    'color': 'pastel_pink',
    'label': "Pastel Pink",
    'hexa': '#dea5a4',
    'red': 222,
    'green': 165,
    'blue': 164
}, {
    'color': 'pastel_purple',
    'label': "Pastel Purple",
    'hexa': '#b39eb5',
    'red': 179,
    'green': 158,
    'blue': 181
}, {
    'color': 'pastel_red',
    'label': "Pastel Red",
    'hexa': '#ff6961',
    'red': 255,
    'green': 105,
    'blue': 97
}, {
    'color': 'pastel_violet',
    'label': "Pastel Violet",
    'hexa': '#cb99c9',
    'red': 203,
    'green': 153,
    'blue': 201
}, {
    'color': 'pastel_yellow',
    'label': "Pastel Yellow",
    'hexa': '#fdfd96',
    'red': 253,
    'green': 253,
    'blue': 150
}, {
    'color': 'patriarch',
    'label': "Patriarch",
    'hexa': '#800080',
    'red': 128,
    'green': 0,
    'blue': 128
}, {
    'color': 'payne_s_grey',
    'label': "Payne'S Grey",
    'hexa': '#536878',
    'red': 83,
    'green': 104,
    'blue': 120
}, {
    'color': 'peach',
    'label': "Peach",
    'hexa': '#ffe5b4',
    'red': 255,
    'green': 229,
    'blue': 180
}, {
    'color': 'peach_crayola',
    'label': "Peach (Crayola)",
    'hexa': '#ffcba4',
    'red': 255,
    'green': 203,
    'blue': 164
}, {
    'color': 'peach_orange',
    'label': "Peach-Orange",
    'hexa': '#ffcc99',
    'red': 255,
    'green': 204,
    'blue': 153
}, {
    'color': 'peach_puff',
    'label': "Peach Puff",
    'hexa': '#ffdab9',
    'red': 255,
    'green': 218,
    'blue': 185
}, {
    'color': 'peach_yellow',
    'label': "Peach-Yellow",
    'hexa': '#fadfad',
    'red': 250,
    'green': 223,
    'blue': 173
}, {
    'color': 'pear',
    'label': "Pear",
    'hexa': '#d1e231',
    'red': 209,
    'green': 226,
    'blue': 49
}, {
    'color': 'pearl',
    'label': "Pearl",
    'hexa': '#eae0c8',
    'red': 234,
    'green': 224,
    'blue': 200
}, {
    'color': 'pearl_aqua',
    'label': "Pearl Aqua",
    'hexa': '#88d8c0',
    'red': 136,
    'green': 216,
    'blue': 192
}, {
    'color': 'pearly_purple',
    'label': "Pearly Purple",
    'hexa': '#b768a2',
    'red': 183,
    'green': 104,
    'blue': 162
}, {
    'color': 'peridot',
    'label': "Peridot",
    'hexa': '#e6e200',
    'red': 230,
    'green': 226,
    'blue': 0
}, {
    'color': 'periwinkle',
    'label': "Periwinkle",
    'hexa': '#ccccff',
    'red': 204,
    'green': 204,
    'blue': 255
}, {
    'color': 'persian_blue',
    'label': "Persian Blue",
    'hexa': '#1c39bb',
    'red': 28,
    'green': 57,
    'blue': 187
}, {
    'color': 'persian_green',
    'label': "Persian Green",
    'hexa': '#00a693',
    'red': 0,
    'green': 166,
    'blue': 147
}, {
    'color': 'persian_indigo',
    'label': "Persian Indigo",
    'hexa': '#32127a',
    'red': 50,
    'green': 18,
    'blue': 122
}, {
    'color': 'persian_orange',
    'label': "Persian Orange",
    'hexa': '#d99058',
    'red': 217,
    'green': 144,
    'blue': 88
}, {
    'color': 'persian_pink',
    'label': "Persian Pink",
    'hexa': '#f77fbe',
    'red': 247,
    'green': 127,
    'blue': 190
}, {
    'color': 'persian_plum',
    'label': "Persian Plum",
    'hexa': '#701c1c',
    'red': 112,
    'green': 28,
    'blue': 28
}, {
    'color': 'persian_red',
    'label': "Persian Red",
    'hexa': '#cc3333',
    'red': 204,
    'green': 51,
    'blue': 51
}, {
    'color': 'persian_rose',
    'label': "Persian Rose",
    'hexa': '#fe28a2',
    'red': 254,
    'green': 40,
    'blue': 162
}, {
    'color': 'persimmon',
    'label': "Persimmon",
    'hexa': '#ec5800',
    'red': 236,
    'green': 88,
    'blue': 0
}, {
    'color': 'peru',
    'label': "Peru",
    'hexa': '#cd853f',
    'red': 205,
    'green': 133,
    'blue': 63
}, {
    'color': 'phlox',
    'label': "Phlox",
    'hexa': '#df00ff',
    'red': 223,
    'green': 0,
    'blue': 255
}, {
    'color': 'phthalo_blue',
    'label': "Phthalo Blue",
    'hexa': '#000f89',
    'red': 0,
    'green': 15,
    'blue': 137
}, {
    'color': 'phthalo_green',
    'label': "Phthalo Green",
    'hexa': '#123524',
    'red': 18,
    'green': 53,
    'blue': 36
}, {
    'color': 'piggy_pink',
    'label': "Piggy Pink",
    'hexa': '#fddde6',
    'red': 253,
    'green': 221,
    'blue': 230
}, {
    'color': 'pine_green',
    'label': "Pine Green",
    'hexa': '#01796f',
    'red': 1,
    'green': 121,
    'blue': 111
}, {
    'color': 'pink',
    'label': "Pink",
    'hexa': '#ffc0cb',
    'red': 255,
    'green': 192,
    'blue': 203
}, {
    'color': 'pink_lace',
    'label': "Pink Lace",
    'hexa': '#ffddf4',
    'red': 255,
    'green': 221,
    'blue': 244
}, {
    'color': 'pink_orange',
    'label': "Pink-Orange",
    'hexa': '#ff9966',
    'red': 255,
    'green': 153,
    'blue': 102
}, {
    'color': 'pink_pearl',
    'label': "Pink Pearl",
    'hexa': '#e7accf',
    'red': 231,
    'green': 172,
    'blue': 207
}, {
    'color': 'pink_sherbet',
    'label': "Pink Sherbet",
    'hexa': '#f78fa7',
    'red': 247,
    'green': 143,
    'blue': 167
}, {
    'color': 'pistachio',
    'label': "Pistachio",
    'hexa': '#93c572',
    'red': 147,
    'green': 197,
    'blue': 114
}, {
    'color': 'platinum',
    'label': "Platinum",
    'hexa': '#e5e4e2',
    'red': 229,
    'green': 228,
    'blue': 226
}, {
    'color': 'plum_traditional',
    'label': "Plum (Traditional)",
    'hexa': '#8e4585',
    'red': 142,
    'green': 69,
    'blue': 133
}, {
    'color': 'plum_web',
    'label': "Plum (Web)",
    'hexa': '#dda0dd',
    'red': 221,
    'green': 160,
    'blue': 221
}, {
    'color': 'portland_orange',
    'label': "Portland Orange",
    'hexa': '#ff5a36',
    'red': 255,
    'green': 90,
    'blue': 54
}, {
    'color': 'powder_blue_web',
    'label': "Powder Blue (Web)",
    'hexa': '#b0e0e6',
    'red': 176,
    'green': 224,
    'blue': 230
}, {
    'color': 'princeton_orange',
    'label': "Princeton Orange",
    'hexa': '#ff8f00',
    'red': 255,
    'green': 143,
    'blue': 0
}, {
    'color': 'prune',
    'label': "Prune",
    'hexa': '#701c1c',
    'red': 112,
    'green': 28,
    'blue': 28
}, {
    'color': 'prussian_blue',
    'label': "Prussian Blue",
    'hexa': '#003153',
    'red': 0,
    'green': 49,
    'blue': 83
}, {
    'color': 'psychedelic_purple',
    'label': "Psychedelic Purple",
    'hexa': '#df00ff',
    'red': 223,
    'green': 0,
    'blue': 255
}, {
    'color': 'puce',
    'label': "Puce",
    'hexa': '#cc8899',
    'red': 204,
    'green': 136,
    'blue': 153
}, {
    'color': 'pumpkin',
    'label': "Pumpkin",
    'hexa': '#ff7518',
    'red': 255,
    'green': 117,
    'blue': 24
}, {
    'color': 'purple_heart',
    'label': "Purple Heart",
    'hexa': '#69359c',
    'red': 105,
    'green': 53,
    'blue': 156
}, {
    'color': 'purple_html_css',
    'label': "Purple (Html/Css)",
    'hexa': '#800080',
    'red': 128,
    'green': 0,
    'blue': 128
}, {
    'color': 'purple_mountain_majesty',
    'label': "Purple Mountain Majesty",
    'hexa': '#9678b6',
    'red': 150,
    'green': 120,
    'blue': 182
}, {
    'color': 'purple_munsell',
    'label': "Purple (Munsell)",
    'hexa': '#9f00c5',
    'red': 159,
    'green': 0,
    'blue': 197
}, {
    'color': 'purple_pizzazz',
    'label': "Purple Pizzazz",
    'hexa': '#fe4eda',
    'red': 254,
    'green': 78,
    'blue': 218
}, {
    'color': 'purple_taupe',
    'label': "Purple Taupe",
    'hexa': '#50404d',
    'red': 80,
    'green': 64,
    'blue': 77
}, {
    'color': 'purple_x11',
    'label': "Purple (X11)",
    'hexa': '#a020f0',
    'red': 160,
    'green': 32,
    'blue': 240
}, {
    'color': 'quartz',
    'label': "Quartz",
    'hexa': '#51484f',
    'red': 81,
    'green': 72,
    'blue': 79
}, {
    'color': 'rackley',
    'label': "Rackley",
    'hexa': '#5d8aa8',
    'red': 93,
    'green': 138,
    'blue': 168
}, {
    'color': 'radical_red',
    'label': "Radical Red",
    'hexa': '#ff355e',
    'red': 255,
    'green': 53,
    'blue': 94
}, {
    'color': 'rajah',
    'label': "Rajah",
    'hexa': '#fbab60',
    'red': 251,
    'green': 171,
    'blue': 96
}, {
    'color': 'raspberry',
    'label': "Raspberry",
    'hexa': '#e30b5d',
    'red': 227,
    'green': 11,
    'blue': 93
}, {
    'color': 'raspberry_glace',
    'label': "Raspberry Glace",
    'hexa': '#915f6d',
    'red': 145,
    'green': 95,
    'blue': 109
}, {
    'color': 'raspberry_pink',
    'label': "Raspberry Pink",
    'hexa': '#e25098',
    'red': 226,
    'green': 80,
    'blue': 152
}, {
    'color': 'raspberry_rose',
    'label': "Raspberry Rose",
    'hexa': '#b3446c',
    'red': 179,
    'green': 68,
    'blue': 108
}, {
    'color': 'raw_umber',
    'label': "Raw Umber",
    'hexa': '#826644',
    'red': 130,
    'green': 102,
    'blue': 68
}, {
    'color': 'razzle_dazzle_rose',
    'label': "Razzle Dazzle Rose",
    'hexa': '#f3c',
    'red': 255,
    'green': 51,
    'blue': 204
}, {
    'color': 'razzmatazz',
    'label': "Razzmatazz",
    'hexa': '#e3256b',
    'red': 227,
    'green': 37,
    'blue': 107
}, {
    'color': 'red_brown',
    'label': "Red-Brown",
    'hexa': '#a52a2a',
    'red': 165,
    'green': 42,
    'blue': 42
}, {
    'color': 'red_devil',
    'label': "Red Devil",
    'hexa': '#860111',
    'red': 134,
    'green': 1,
    'blue': 17
}, {
    'color': 'red_munsell',
    'label': "Red (Munsell)",
    'hexa': '#f2003c',
    'red': 242,
    'green': 0,
    'blue': 60
}, {
    'color': 'red_ncs',
    'label': "Red (Ncs)",
    'hexa': '#c40233',
    'red': 196,
    'green': 2,
    'blue': 51
}, {
    'color': 'red_orange',
    'label': "Red-Orange",
    'hexa': '#ff5349',
    'red': 255,
    'green': 83,
    'blue': 73
}, {
    'color': 'red_pigment',
    'label': "Red (Pigment)",
    'hexa': '#ed1c24',
    'red': 237,
    'green': 28,
    'blue': 36
}, {
    'color': 'red_ryb',
    'label': "Red (Ryb)",
    'hexa': '#fe2712',
    'red': 254,
    'green': 39,
    'blue': 18
}, {
    'color': 'red_violet',
    'label': "Red-Violet",
    'hexa': '#c71585',
    'red': 199,
    'green': 21,
    'blue': 133
}, {
    'color': 'redwood',
    'label': "Redwood",
    'hexa': '#ab4e52',
    'red': 171,
    'green': 78,
    'blue': 82
}, {
    'color': 'regalia',
    'label': "Regalia",
    'hexa': '#522d80',
    'red': 82,
    'green': 45,
    'blue': 128
}, {
    'color': 'resolution_blue',
    'label': "Resolution Blue",
    'hexa': '#002387',
    'red': 0,
    'green': 35,
    'blue': 135
}, {
    'color': 'rich_black',
    'label': "Rich Black",
    'hexa': '#004040',
    'red': 0,
    'green': 64,
    'blue': 64
}, {
    'color': 'rich_brilliant_lavender',
    'label': "Rich Brilliant Lavender",
    'hexa': '#f1a7fe',
    'red': 241,
    'green': 167,
    'blue': 254
}, {
    'color': 'rich_carmine',
    'label': "Rich Carmine",
    'hexa': '#d70040',
    'red': 215,
    'green': 0,
    'blue': 64
}, {
    'color': 'rich_electric_blue',
    'label': "Rich Electric Blue",
    'hexa': '#0892d0',
    'red': 8,
    'green': 146,
    'blue': 208
}, {
    'color': 'rich_lavender',
    'label': "Rich Lavender",
    'hexa': '#a76bcf',
    'red': 167,
    'green': 107,
    'blue': 207
}, {
    'color': 'rich_lilac',
    'label': "Rich Lilac",
    'hexa': '#b666d2',
    'red': 182,
    'green': 102,
    'blue': 210
}, {
    'color': 'rich_maroon',
    'label': "Rich Maroon",
    'hexa': '#b03060',
    'red': 176,
    'green': 48,
    'blue': 96
}, {
    'color': 'rifle_green',
    'label': "Rifle Green",
    'hexa': '#414833',
    'red': 65,
    'green': 72,
    'blue': 51
}, {
    'color': 'robin_egg_blue',
    'label': "Robin Egg Blue",
    'hexa': '#0cc',
    'red': 0,
    'green': 204,
    'blue': 204
}, {
    'color': 'rose',
    'label': "Rose",
    'hexa': '#ff007f',
    'red': 255,
    'green': 0,
    'blue': 127
}, {
    'color': 'rose_bonbon',
    'label': "Rose Bonbon",
    'hexa': '#f9429e',
    'red': 249,
    'green': 66,
    'blue': 158
}, {
    'color': 'rose_ebony',
    'label': "Rose Ebony",
    'hexa': '#674846',
    'red': 103,
    'green': 72,
    'blue': 70
}, {
    'color': 'rose_gold',
    'label': "Rose Gold",
    'hexa': '#b76e79',
    'red': 183,
    'green': 110,
    'blue': 121
}, {
    'color': 'rose_madder',
    'label': "Rose Madder",
    'hexa': '#e32636',
    'red': 227,
    'green': 38,
    'blue': 54
}, {
    'color': 'rose_pink',
    'label': "Rose Pink",
    'hexa': '#f6c',
    'red': 255,
    'green': 102,
    'blue': 204
}, {
    'color': 'rose_quartz',
    'label': "Rose Quartz",
    'hexa': '#aa98a9',
    'red': 170,
    'green': 152,
    'blue': 169
}, {
    'color': 'rose_taupe',
    'label': "Rose Taupe",
    'hexa': '#905d5d',
    'red': 144,
    'green': 93,
    'blue': 93
}, {
    'color': 'rose_vale',
    'label': "Rose Vale",
    'hexa': '#ab4e52',
    'red': 171,
    'green': 78,
    'blue': 82
}, {
    'color': 'rosewood',
    'label': "Rosewood",
    'hexa': '#65000b',
    'red': 101,
    'green': 0,
    'blue': 11
}, {
    'color': 'rosso_corsa',
    'label': "Rosso Corsa",
    'hexa': '#d40000',
    'red': 212,
    'green': 0,
    'blue': 0
}, {
    'color': 'rosy_brown',
    'label': "Rosy Brown",
    'hexa': '#bc8f8f',
    'red': 188,
    'green': 143,
    'blue': 143
}, {
    'color': 'royal_azure',
    'label': "Royal Azure",
    'hexa': '#0038a8',
    'red': 0,
    'green': 56,
    'blue': 168
}, {
    'color': 'royal_blue_traditional',
    'label': "Royal Blue (Traditional)",
    'hexa': '#002366',
    'red': 0,
    'green': 35,
    'blue': 102
}, {
    'color': 'royal_blue_web',
    'label': "Royal Blue (Web)",
    'hexa': '#4169e1',
    'red': 65,
    'green': 105,
    'blue': 225
}, {
    'color': 'royal_fuchsia',
    'label': "Royal Fuchsia",
    'hexa': '#ca2c92',
    'red': 202,
    'green': 44,
    'blue': 146
}, {
    'color': 'royal_purple',
    'label': "Royal Purple",
    'hexa': '#7851a9',
    'red': 120,
    'green': 81,
    'blue': 169
}, {
    'color': 'royal_yellow',
    'label': "Royal Yellow",
    'hexa': '#fada5e',
    'red': 250,
    'green': 218,
    'blue': 94
}, {
    'color': 'rubine_red',
    'label': "Rubine Red",
    'hexa': '#d10056',
    'red': 209,
    'green': 0,
    'blue': 86
}, {
    'color': 'ruby',
    'label': "Ruby",
    'hexa': '#e0115f',
    'red': 224,
    'green': 17,
    'blue': 95
}, {
    'color': 'ruby_red',
    'label': "Ruby Red",
    'hexa': '#9b111e',
    'red': 155,
    'green': 17,
    'blue': 30
}, {
    'color': 'ruddy',
    'label': "Ruddy",
    'hexa': '#ff0028',
    'red': 255,
    'green': 0,
    'blue': 40
}, {
    'color': 'ruddy_brown',
    'label': "Ruddy Brown",
    'hexa': '#bb6528',
    'red': 187,
    'green': 101,
    'blue': 40
}, {
    'color': 'ruddy_pink',
    'label': "Ruddy Pink",
    'hexa': '#e18e96',
    'red': 225,
    'green': 142,
    'blue': 150
}, {
    'color': 'rufous',
    'label': "Rufous",
    'hexa': '#a81c07',
    'red': 168,
    'green': 28,
    'blue': 7
}, {
    'color': 'russet',
    'label': "Russet",
    'hexa': '#80461b',
    'red': 128,
    'green': 70,
    'blue': 27
}, {
    'color': 'rust',
    'label': "Rust",
    'hexa': '#b7410e',
    'red': 183,
    'green': 65,
    'blue': 14
}, {
    'color': 'rusty_red',
    'label': "Rusty Red",
    'hexa': '#da2c43',
    'red': 218,
    'green': 44,
    'blue': 67
}, {
    'color': 'sacramento_state_green',
    'label': "Sacramento State Green",
    'hexa': '#00563f',
    'red': 0,
    'green': 86,
    'blue': 63
}, {
    'color': 'saddle_brown',
    'label': "Saddle Brown",
    'hexa': '#8b4513',
    'red': 139,
    'green': 69,
    'blue': 19
}, {
    'color': 'safety_orange_blaze_orange',
    'label': "Safety Orange (Blaze Orange)",
    'hexa': '#ff6700',
    'red': 255,
    'green': 103,
    'blue': 0
}, {
    'color': 'saffron',
    'label': "Saffron",
    'hexa': '#f4c430',
    'red': 244,
    'green': 196,
    'blue': 48
}, {
    'color': 'salmon',
    'label': "Salmon",
    'hexa': '#ff8c69',
    'red': 255,
    'green': 140,
    'blue': 105
}, {
    'color': 'salmon_pink',
    'label': "Salmon Pink",
    'hexa': '#ff91a4',
    'red': 255,
    'green': 145,
    'blue': 164
}, {
    'color': 'sand',
    'label': "Sand",
    'hexa': '#c2b280',
    'red': 194,
    'green': 178,
    'blue': 128
}, {
    'color': 'sand_dune',
    'label': "Sand Dune",
    'hexa': '#967117',
    'red': 150,
    'green': 113,
    'blue': 23
}, {
    'color': 'sandstorm',
    'label': "Sandstorm",
    'hexa': '#ecd540',
    'red': 236,
    'green': 213,
    'blue': 64
}, {
    'color': 'sandy_brown',
    'label': "Sandy Brown",
    'hexa': '#f4a460',
    'red': 244,
    'green': 164,
    'blue': 96
}, {
    'color': 'sandy_taupe',
    'label': "Sandy Taupe",
    'hexa': '#967117',
    'red': 150,
    'green': 113,
    'blue': 23
}, {
    'color': 'sangria',
    'label': "Sangria",
    'hexa': '#92000a',
    'red': 146,
    'green': 0,
    'blue': 10
}, {
    'color': 'sap_green',
    'label': "Sap Green",
    'hexa': '#507d2a',
    'red': 80,
    'green': 125,
    'blue': 42
}, {
    'color': 'sapphire',
    'label': "Sapphire",
    'hexa': '#0f52ba',
    'red': 15,
    'green': 82,
    'blue': 186
}, {
    'color': 'sapphire_blue',
    'label': "Sapphire Blue",
    'hexa': '#0067a5',
    'red': 0,
    'green': 103,
    'blue': 165
}, {
    'color': 'satin_sheen_gold',
    'label': "Satin Sheen Gold",
    'hexa': '#cba135',
    'red': 203,
    'green': 161,
    'blue': 53
}, {
    'color': 'scarlet',
    'label': "Scarlet",
    'hexa': '#ff2400',
    'red': 255,
    'green': 36,
    'blue': 0
}, {
    'color': 'scarlet_crayola',
    'label': "Scarlet (Crayola)",
    'hexa': '#fd0e35',
    'red': 253,
    'green': 14,
    'blue': 53
}, {
    'color': 'school_bus_yellow',
    'label': "School Bus Yellow",
    'hexa': '#ffd800',
    'red': 255,
    'green': 216,
    'blue': 0
}, {
    'color': 'screamin_green',
    'label': "Screamin' Green",
    'hexa': '#76ff7a',
    'red': 118,
    'green': 255,
    'blue': 122
}, {
    'color': 'sea_blue',
    'label': "Sea Blue",
    'hexa': '#006994',
    'red': 0,
    'green': 105,
    'blue': 148
}, {
    'color': 'sea_green',
    'label': "Sea Green",
    'hexa': '#2e8b57',
    'red': 46,
    'green': 139,
    'blue': 87
}, {
    'color': 'seal_brown',
    'label': "Seal Brown",
    'hexa': '#321414',
    'red': 50,
    'green': 20,
    'blue': 20
}, {
    'color': 'seashell',
    'label': "Seashell",
    'hexa': '#fff5ee',
    'red': 255,
    'green': 245,
    'blue': 238
}, {
    'color': 'selective_yellow',
    'label': "Selective Yellow",
    'hexa': '#ffba00',
    'red': 255,
    'green': 186,
    'blue': 0
}, {
    'color': 'sepia',
    'label': "Sepia",
    'hexa': '#704214',
    'red': 112,
    'green': 66,
    'blue': 20
}, {
    'color': 'shadow',
    'label': "Shadow",
    'hexa': '#8a795d',
    'red': 138,
    'green': 121,
    'blue': 93
}, {
    'color': 'shamrock_green',
    'label': "Shamrock Green",
    'hexa': '#009e60',
    'red': 0,
    'green': 158,
    'blue': 96
}, {
    'color': 'shocking_pink',
    'label': "Shocking Pink",
    'hexa': '#fc0fc0',
    'red': 252,
    'green': 15,
    'blue': 192
}, {
    'color': 'shocking_pink_crayola',
    'label': "Shocking Pink (Crayola)",
    'hexa': '#ff6fff',
    'red': 255,
    'green': 111,
    'blue': 255
}, {
    'color': 'sienna',
    'label': "Sienna",
    'hexa': '#882d17',
    'red': 136,
    'green': 45,
    'blue': 23
}, {
    'color': 'silver',
    'label': "Silver",
    'hexa': '#c0c0c0',
    'red': 192,
    'green': 192,
    'blue': 192
}, {
    'color': 'sinopia',
    'label': "Sinopia",
    'hexa': '#cb410b',
    'red': 203,
    'green': 65,
    'blue': 11
}, {
    'color': 'skobeloff',
    'label': "Skobeloff",
    'hexa': '#007474',
    'red': 0,
    'green': 116,
    'blue': 116
}, {
    'color': 'sky_blue',
    'label': "Sky Blue",
    'hexa': '#87ceeb',
    'red': 135,
    'green': 206,
    'blue': 235
}, {
    'color': 'sky_magenta',
    'label': "Sky Magenta",
    'hexa': '#cf71af',
    'red': 207,
    'green': 113,
    'blue': 175
}, {
    'color': 'slate_blue',
    'label': "Slate Blue",
    'hexa': '#6a5acd',
    'red': 106,
    'green': 90,
    'blue': 205
}, {
    'color': 'slate_gray',
    'label': "Slate Gray",
    'hexa': '#708090',
    'red': 112,
    'green': 128,
    'blue': 144
}, {
    'color': 'smalt_dark_powder_blue',
    'label': "Smalt (Dark Powder Blue)",
    'hexa': '#003399',
    'red': 0,
    'green': 51,
    'blue': 153
}, {
    'color': 'smokey_topaz',
    'label': "Smokey Topaz",
    'hexa': '#933d41',
    'red': 147,
    'green': 61,
    'blue': 65
}, {
    'color': 'smoky_black',
    'label': "Smoky Black",
    'hexa': '#100c08',
    'red': 16,
    'green': 12,
    'blue': 8
}, {
    'color': 'snow',
    'label': "Snow",
    'hexa': '#fffafa',
    'red': 255,
    'green': 250,
    'blue': 250
}, {
    'color': 'spiro_disco_ball',
    'label': "Spiro Disco Ball",
    'hexa': '#0fc0fc',
    'red': 15,
    'green': 192,
    'blue': 252
}, {
    'color': 'spring_bud',
    'label': "Spring Bud",
    'hexa': '#a7fc00',
    'red': 167,
    'green': 252,
    'blue': 0
}, {
    'color': 'spring_green',
    'label': "Spring Green",
    'hexa': '#00ff7f',
    'red': 0,
    'green': 255,
    'blue': 127
}, {
    'color': 'st_patrick_s_blue',
    'label': "St. Patrick'S Blue",
    'hexa': '#23297a',
    'red': 35,
    'green': 41,
    'blue': 122
}, {
    'color': 'steel_blue',
    'label': "Steel Blue",
    'hexa': '#4682b4',
    'red': 70,
    'green': 130,
    'blue': 180
}, {
    'color': 'stil_de_grain_yellow',
    'label': "Stil De Grain Yellow",
    'hexa': '#fada5e',
    'red': 250,
    'green': 218,
    'blue': 94
}, {
    'color': 'stizza',
    'label': "Stizza",
    'hexa': '#990000',
    'red': 153,
    'green': 0,
    'blue': 0
}, {
    'color': 'stormcloud',
    'label': "Stormcloud",
    'hexa': '#4f666a',
    'red': 79,
    'green': 102,
    'blue': 106
}, {
    'color': 'straw',
    'label': "Straw",
    'hexa': '#e4d96f',
    'red': 228,
    'green': 217,
    'blue': 111
}, {
    'color': 'sunglow',
    'label': "Sunglow",
    'hexa': '#ffcc33',
    'red': 255,
    'green': 204,
    'blue': 51
}, {
    'color': 'sunset',
    'label': "Sunset",
    'hexa': '#fad6a5',
    'red': 250,
    'green': 214,
    'blue': 165
}, {
    'color': 'tan',
    'label': "Tan",
    'hexa': '#d2b48c',
    'red': 210,
    'green': 180,
    'blue': 140
}, {
    'color': 'tangelo',
    'label': "Tangelo",
    'hexa': '#f94d00',
    'red': 249,
    'green': 77,
    'blue': 0
}, {
    'color': 'tangerine',
    'label': "Tangerine",
    'hexa': '#f28500',
    'red': 242,
    'green': 133,
    'blue': 0
}, {
    'color': 'tangerine_yellow',
    'label': "Tangerine Yellow",
    'hexa': '#ffcc00',
    'red': 255,
    'green': 204,
    'blue': 0
}, {
    'color': 'tango_pink',
    'label': "Tango Pink",
    'hexa': '#e4717a',
    'red': 228,
    'green': 113,
    'blue': 122
}, {
    'color': 'taupe',
    'label': "Taupe",
    'hexa': '#483c32',
    'red': 72,
    'green': 60,
    'blue': 50
}, {
    'color': 'taupe_gray',
    'label': "Taupe Gray",
    'hexa': '#8b8589',
    'red': 139,
    'green': 133,
    'blue': 137
}, {
    'color': 'tea_green',
    'label': "Tea Green",
    'hexa': '#d0f0c0',
    'red': 208,
    'green': 240,
    'blue': 192
}, {
    'color': 'tea_rose_orange',
    'label': "Tea Rose (Orange)",
    'hexa': '#f88379',
    'red': 248,
    'green': 131,
    'blue': 121
}, {
    'color': 'tea_rose_rose',
    'label': "Tea Rose (Rose)",
    'hexa': '#f4c2c2',
    'red': 244,
    'green': 194,
    'blue': 194
}, {
    'color': 'teal',
    'label': "Teal",
    'hexa': '#008080',
    'red': 0,
    'green': 128,
    'blue': 128
}, {
    'color': 'teal_blue',
    'label': "Teal Blue",
    'hexa': '#367588',
    'red': 54,
    'green': 117,
    'blue': 136
}, {
    'color': 'teal_green',
    'label': "Teal Green",
    'hexa': '#00827f',
    'red': 0,
    'green': 130,
    'blue': 127
}, {
    'color': 'telemagenta',
    'label': "Telemagenta",
    'hexa': '#cf3476',
    'red': 207,
    'green': 52,
    'blue': 118
}, {
    'color': 'tenn_tawny',
    'label': "Tenné (Tawny)",
    'hexa': '#cd5700',
    'red': 205,
    'green': 87,
    'blue': 0
}, {
    'color': 'terra_cotta',
    'label': "Terra Cotta",
    'hexa': '#e2725b',
    'red': 226,
    'green': 114,
    'blue': 91
}, {
    'color': 'thistle',
    'label': "Thistle",
    'hexa': '#d8bfd8',
    'red': 216,
    'green': 191,
    'blue': 216
}, {
    'color': 'thulian_pink',
    'label': "Thulian Pink",
    'hexa': '#de6fa1',
    'red': 222,
    'green': 111,
    'blue': 161
}, {
    'color': 'tickle_me_pink',
    'label': "Tickle Me Pink",
    'hexa': '#fc89ac',
    'red': 252,
    'green': 137,
    'blue': 172
}, {
    'color': 'tiffany_blue',
    'label': "Tiffany Blue",
    'hexa': '#0abab5',
    'red': 10,
    'green': 186,
    'blue': 181
}, {
    'color': 'tiger_s_eye',
    'label': "Tiger'S Eye",
    'hexa': '#e08d3c',
    'red': 224,
    'green': 141,
    'blue': 60
}, {
    'color': 'timberwolf',
    'label': "Timberwolf",
    'hexa': '#dbd7d2',
    'red': 219,
    'green': 215,
    'blue': 210
}, {
    'color': 'titanium_yellow',
    'label': "Titanium Yellow",
    'hexa': '#eee600',
    'red': 238,
    'green': 230,
    'blue': 0
}, {
    'color': 'tomato',
    'label': "Tomato",
    'hexa': '#ff6347',
    'red': 255,
    'green': 99,
    'blue': 71
}, {
    'color': 'toolbox',
    'label': "Toolbox",
    'hexa': '#746cc0',
    'red': 116,
    'green': 108,
    'blue': 192
}, {
    'color': 'topaz',
    'label': "Topaz",
    'hexa': '#ffc87c',
    'red': 255,
    'green': 200,
    'blue': 124
}, {
    'color': 'tractor_red',
    'label': "Tractor Red",
    'hexa': '#fd0e35',
    'red': 253,
    'green': 14,
    'blue': 53
}, {
    'color': 'trolley_grey',
    'label': "Trolley Grey",
    'hexa': '#808080',
    'red': 128,
    'green': 128,
    'blue': 128
}, {
    'color': 'tropical_rain_forest',
    'label': "Tropical Rain Forest",
    'hexa': '#00755e',
    'red': 0,
    'green': 117,
    'blue': 94
}, {
    'color': 'true_blue',
    'label': "True Blue",
    'hexa': '#0073cf',
    'red': 0,
    'green': 115,
    'blue': 207
}, {
    'color': 'tufts_blue',
    'label': "Tufts Blue",
    'hexa': '#417dc1',
    'red': 65,
    'green': 125,
    'blue': 193
}, {
    'color': 'tumbleweed',
    'label': "Tumbleweed",
    'hexa': '#deaa88',
    'red': 222,
    'green': 170,
    'blue': 136
}, {
    'color': 'turkish_rose',
    'label': "Turkish Rose",
    'hexa': '#b57281',
    'red': 181,
    'green': 114,
    'blue': 129
}, {
    'color': 'turquoise',
    'label': "Turquoise",
    'hexa': '#30d5c8',
    'red': 48,
    'green': 213,
    'blue': 200
}, {
    'color': 'turquoise_blue',
    'label': "Turquoise Blue",
    'hexa': '#00ffef',
    'red': 0,
    'green': 255,
    'blue': 239
}, {
    'color': 'turquoise_green',
    'label': "Turquoise Green",
    'hexa': '#a0d6b4',
    'red': 160,
    'green': 214,
    'blue': 180
}, {
    'color': 'tuscan_red',
    'label': "Tuscan Red",
    'hexa': '#7c4848',
    'red': 124,
    'green': 72,
    'blue': 72
}, {
    'color': 'twilight_lavender',
    'label': "Twilight Lavender",
    'hexa': '#8a496b',
    'red': 138,
    'green': 73,
    'blue': 107
}, {
    'color': 'tyrian_purple',
    'label': "Tyrian Purple",
    'hexa': '#66023c',
    'red': 102,
    'green': 2,
    'blue': 60
}, {
    'color': 'ua_blue',
    'label': "Ua Blue",
    'hexa': '#0033aa',
    'red': 0,
    'green': 51,
    'blue': 170
}, {
    'color': 'ua_red',
    'label': "Ua Red",
    'hexa': '#d9004c',
    'red': 217,
    'green': 0,
    'blue': 76
}, {
    'color': 'ube',
    'label': "Ube",
    'hexa': '#8878c3',
    'red': 136,
    'green': 120,
    'blue': 195
}, {
    'color': 'ucla_blue',
    'label': "Ucla Blue",
    'hexa': '#536895',
    'red': 83,
    'green': 104,
    'blue': 149
}, {
    'color': 'ucla_gold',
    'label': "Ucla Gold",
    'hexa': '#ffb300',
    'red': 255,
    'green': 179,
    'blue': 0
}, {
    'color': 'ufo_green',
    'label': "Ufo Green",
    'hexa': '#3cd070',
    'red': 60,
    'green': 208,
    'blue': 112
}, {
    'color': 'ultra_pink',
    'label': "Ultra Pink",
    'hexa': '#ff6fff',
    'red': 255,
    'green': 111,
    'blue': 255
}, {
    'color': 'ultramarine',
    'label': "Ultramarine",
    'hexa': '#120a8f',
    'red': 18,
    'green': 10,
    'blue': 143
}, {
    'color': 'ultramarine_blue',
    'label': "Ultramarine Blue",
    'hexa': '#4166f5',
    'red': 65,
    'green': 102,
    'blue': 245
}, {
    'color': 'umber',
    'label': "Umber",
    'hexa': '#635147',
    'red': 99,
    'green': 81,
    'blue': 71
}, {
    'color': 'unbleached_silk',
    'label': "Unbleached Silk",
    'hexa': '#ffddca',
    'red': 255,
    'green': 221,
    'blue': 202
}, {
    'color': 'united_nations_blue',
    'label': "United Nations Blue",
    'hexa': '#5b92e5',
    'red': 91,
    'green': 146,
    'blue': 229
}, {
    'color': 'university_of_california_gold',
    'label': "University Of California Gold",
    'hexa': '#b78727',
    'red': 183,
    'green': 135,
    'blue': 39
}, {
    'color': 'unmellow_yellow',
    'label': "Unmellow Yellow",
    'hexa': '#ffff66',
    'red': 255,
    'green': 255,
    'blue': 102
}, {
    'color': 'up_forest_green',
    'label': "Up Forest Green",
    'hexa': '#014421',
    'red': 1,
    'green': 68,
    'blue': 33
}, {
    'color': 'up_maroon',
    'label': "Up Maroon",
    'hexa': '#7b1113',
    'red': 123,
    'green': 17,
    'blue': 19
}, {
    'color': 'upsdell_red',
    'label': "Upsdell Red",
    'hexa': '#ae2029',
    'red': 174,
    'green': 32,
    'blue': 41
}, {
    'color': 'urobilin',
    'label': "Urobilin",
    'hexa': '#e1ad21',
    'red': 225,
    'green': 173,
    'blue': 33
}, {
    'color': 'usafa_blue',
    'label': "Usafa Blue",
    'hexa': '#004f98',
    'red': 0,
    'green': 79,
    'blue': 152
}, {
    'color': 'usc_cardinal',
    'label': "Usc Cardinal",
    'hexa': '#990000',
    'red': 153,
    'green': 0,
    'blue': 0
}, {
    'color': 'usc_gold',
    'label': "Usc Gold",
    'hexa': '#ffcc00',
    'red': 255,
    'green': 204,
    'blue': 0
}, {
    'color': 'utah_crimson',
    'label': "Utah Crimson",
    'hexa': '#d3003f',
    'red': 211,
    'green': 0,
    'blue': 63
}, {
    'color': 'vanilla',
    'label': "Vanilla",
    'hexa': '#f3e5ab',
    'red': 243,
    'green': 229,
    'blue': 171
}, {
    'color': 'vegas_gold',
    'label': "Vegas Gold",
    'hexa': '#c5b358',
    'red': 197,
    'green': 179,
    'blue': 88
}, {
    'color': 'venetian_red',
    'label': "Venetian Red",
    'hexa': '#c80815',
    'red': 200,
    'green': 8,
    'blue': 21
}, {
    'color': 'verdigris',
    'label': "Verdigris",
    'hexa': '#43b3ae',
    'red': 67,
    'green': 179,
    'blue': 174
}, {
    'color': 'vermilion_cinnabar',
    'label': "Vermilion (Cinnabar)",
    'hexa': '#e34234',
    'red': 227,
    'green': 66,
    'blue': 52
}, {
    'color': 'vermilion_plochere',
    'label': "Vermilion (Plochere)",
    'hexa': '#d9603b',
    'red': 217,
    'green': 96,
    'blue': 59
}, {
    'color': 'veronica',
    'label': "Veronica",
    'hexa': '#a020f0',
    'red': 160,
    'green': 32,
    'blue': 240
}, {
    'color': 'violet_blue',
    'label': "Violet-Blue",
    'hexa': '#324ab2',
    'red': 50,
    'green': 74,
    'blue': 178
}, {
    'color': 'violet_color_wheel',
    'label': "Violet (Color Wheel)",
    'hexa': '#7f00ff',
    'red': 127,
    'green': 0,
    'blue': 255
}, {
    'color': 'violet_ryb',
    'label': "Violet (Ryb)",
    'hexa': '#8601af',
    'red': 134,
    'green': 1,
    'blue': 175
}, {
    'color': 'violet_web',
    'label': "Violet (Web)",
    'hexa': '#ee82ee',
    'red': 238,
    'green': 130,
    'blue': 238
}, {
    'color': 'viridian',
    'label': "Viridian",
    'hexa': '#40826d',
    'red': 64,
    'green': 130,
    'blue': 109
}, {
    'color': 'vivid_auburn',
    'label': "Vivid Auburn",
    'hexa': '#922724',
    'red': 146,
    'green': 39,
    'blue': 36
}, {
    'color': 'vivid_burgundy',
    'label': "Vivid Burgundy",
    'hexa': '#9f1d35',
    'red': 159,
    'green': 29,
    'blue': 53
}, {
    'color': 'vivid_cerise',
    'label': "Vivid Cerise",
    'hexa': '#da1d81',
    'red': 218,
    'green': 29,
    'blue': 129
}, {
    'color': 'vivid_tangerine',
    'label': "Vivid Tangerine",
    'hexa': '#ffa089',
    'red': 255,
    'green': 160,
    'blue': 137
}, {
    'color': 'vivid_violet',
    'label': "Vivid Violet",
    'hexa': '#9f00ff',
    'red': 159,
    'green': 0,
    'blue': 255
}, {
    'color': 'warm_black',
    'label': "Warm Black",
    'hexa': '#004242',
    'red': 0,
    'green': 66,
    'blue': 66
}, {
    'color': 'waterspout',
    'label': "Waterspout",
    'hexa': '#a4f4f9',
    'red': 164,
    'green': 244,
    'blue': 249
}, {
    'color': 'wenge',
    'label': "Wenge",
    'hexa': '#645452',
    'red': 100,
    'green': 84,
    'blue': 82
}, {
    'color': 'wheat',
    'label': "Wheat",
    'hexa': '#f5deb3',
    'red': 245,
    'green': 222,
    'blue': 179
}, {
    'color': 'white',
    'label': "White",
    'hexa': '#ffffff',
    'red': 255,
    'green': 255,
    'blue': 255
}, {
    'color': 'white_smoke',
    'label': "White Smoke",
    'hexa': '#f5f5f5',
    'red': 245,
    'green': 245,
    'blue': 245
}, {
    'color': 'wild_blue_yonder',
    'label': "Wild Blue Yonder",
    'hexa': '#a2add0',
    'red': 162,
    'green': 173,
    'blue': 208
}, {
    'color': 'wild_strawberry',
    'label': "Wild Strawberry",
    'hexa': '#ff43a4',
    'red': 255,
    'green': 67,
    'blue': 164
}, {
    'color': 'wild_watermelon',
    'label': "Wild Watermelon",
    'hexa': '#fc6c85',
    'red': 252,
    'green': 108,
    'blue': 133
}, {
    'color': 'wine',
    'label': "Wine",
    'hexa': '#722f37',
    'red': 114,
    'green': 47,
    'blue': 55
}, {
    'color': 'wine_dregs',
    'label': "Wine Dregs",
    'hexa': '#673147',
    'red': 103,
    'green': 49,
    'blue': 71
}, {
    'color': 'wisteria',
    'label': "Wisteria",
    'hexa': '#c9a0dc',
    'red': 201,
    'green': 160,
    'blue': 220
}, {
    'color': 'wood_brown',
    'label': "Wood Brown",
    'hexa': '#c19a6b',
    'red': 193,
    'green': 154,
    'blue': 107
}, {
    'color': 'xanadu',
    'label': "Xanadu",
    'hexa': '#738678',
    'red': 115,
    'green': 134,
    'blue': 120
}, {
    'color': 'yale_blue',
    'label': "Yale Blue",
    'hexa': '#0f4d92',
    'red': 15,
    'green': 77,
    'blue': 146
}, {
    'color': 'yellow_green',
    'label': "Yellow-Green",
    'hexa': '#9acd32',
    'red': 154,
    'green': 205,
    'blue': 50
}, {
    'color': 'yellow_munsell',
    'label': "Yellow (Munsell)",
    'hexa': '#efcc00',
    'red': 239,
    'green': 204,
    'blue': 0
}, {
    'color': 'yellow_ncs',
    'label': "Yellow (Ncs)",
    'hexa': '#ffd300',
    'red': 255,
    'green': 211,
    'blue': 0
}, {
    'color': 'yellow_orange',
    'label': "Yellow Orange",
    'hexa': '#ffae42',
    'red': 255,
    'green': 174,
    'blue': 66
}, {
    'color': 'yellow_process',
    'label': "Yellow (Process)",
    'hexa': '#ffef00',
    'red': 255,
    'green': 239,
    'blue': 0
}, {
    'color': 'yellow_ryb',
    'label': "Yellow (Ryb)",
    'hexa': '#fefe33',
    'red': 254,
    'green': 254,
    'blue': 51
}, {
    'color': 'zaffre',
    'label': "Zaffre",
    'hexa': '#0014a8',
    'red': 0,
    'green': 20,
    'blue': 168
}, {
    'color': 'zinnwaldite_brown',
    'label': "Zinnwaldite Brown",
    'hexa': '#2c1608',
    'red': 44,
    'green': 22,
    'blue': 8
}]
