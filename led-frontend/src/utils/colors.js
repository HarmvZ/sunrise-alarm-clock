export const rgbToArray = (rgb) => {
  return rgb.split(/^rgb\(|,|\)$/).filter(v => v !== '').map(v => Number.parseInt(v.trim()));
};
export const arrayToRgb = (arr) => {
  return `rgb(${arr[0]}, ${arr[1]}, ${arr[2]})`;
};
