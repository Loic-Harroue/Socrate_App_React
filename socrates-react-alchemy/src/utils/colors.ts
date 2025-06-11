
export interface Color {
  color: string;
  label: string;
  hexa: string;
  red: number;
  green: number;
  blue: number;
}

const NB_COLORS_AS_VOS = 16;
const NB_COLORS = 874;

const COLORS: Color[] = [
  {
    color: 'red',
    label: "Red",
    hexa: "#ff0000",
    red: 255,
    green: 0,
    blue: 0
  },
  {
    color: 'green_color_wheel_x11_green',
    label: "Green (Color Wheel) (X11 Green)",
    hexa: "#00ff00",
    red: 0,
    green: 255,
    blue: 0
  },
  {
    color: 'blue',
    label: "Blue",
    hexa: "#0000ff",
    red: 0,
    green: 0,
    blue: 255
  },
  // Adding more blue variations since you mentioned using mainly blue
  {
    color: 'navy_blue',
    label: "Navy Blue",
    hexa: "#000080",
    red: 0,
    green: 0,
    blue: 128
  },
  {
    color: 'royal_blue',
    label: "Royal Blue",
    hexa: "#4169e1",
    red: 65,
    green: 105,
    blue: 225
  },
  {
    color: 'steel_blue',
    label: "Steel Blue",
    hexa: "#4682b4",
    red: 70,
    green: 130,
    blue: 180
  },
  {
    color: 'dodger_blue',
    label: "Dodger Blue",
    hexa: "#1e90ff",
    red: 30,
    green: 144,
    blue: 255
  },
  {
    color: 'deep_sky_blue',
    label: "Deep Sky Blue",
    hexa: "#00bfff",
    red: 0,
    green: 191,
    blue: 255
  },
  {
    color: 'sky_blue',
    label: "Sky Blue",
    hexa: "#87ceeb",
    red: 135,
    green: 206,
    blue: 235
  },
  {
    color: 'light_sky_blue',
    label: "Light Sky Blue",
    hexa: "#87cefa",
    red: 135,
    green: 206,
    blue: 250
  },
  {
    color: 'powder_blue',
    label: "Powder Blue",
    hexa: "#b0e0e6",
    red: 176,
    green: 224,
    blue: 230
  },
  {
    color: 'light_blue',
    label: "Light Blue",
    hexa: "#add8e6",
    red: 173,
    green: 216,
    blue: 230
  },
  {
    color: 'alice_blue',
    label: "Alice Blue",
    hexa: "#f0f8ff",
    red: 240,
    green: 248,
    blue: 255
  },
  {
    color: 'cornflower_blue',
    label: "Cornflower Blue",
    hexa: "#6495ed",
    red: 100,
    green: 149,
    blue: 237
  },
  {
    color: 'medium_slate_blue',
    label: "Medium Slate Blue",
    hexa: "#7b68ee",
    red: 123,
    green: 104,
    blue: 238
  },
  {
    color: 'slate_blue',
    label: "Slate Blue",
    hexa: "#6a5acd",
    red: 106,
    green: 90,
    blue: 205
  }
];

export function getClustersColors(nbClusters: number): Color[] {
  if (nbClusters <= NB_COLORS_AS_VOS) {
    return COLORS.slice(0, nbClusters);
  } else {
    const colors = COLORS.slice(0, NB_COLORS_AS_VOS);
    for (let i = NB_COLORS_AS_VOS; i < nbClusters; i++) {
      const randomIndex = Math.floor(Math.random() * (NB_COLORS - NB_COLORS_AS_VOS)) + NB_COLORS_AS_VOS;
      // Since we don't have all 874 colors, we'll cycle through our available colors
      colors.push(COLORS[Math.floor(Math.random() * COLORS.length)]);
    }
    return colors;
  }
}

export { COLORS };
