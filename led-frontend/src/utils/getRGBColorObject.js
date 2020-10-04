export default (color) => {
  const pattern = /rgb\(|\)/g;
  const [r, g, b] = color.replace(pattern, '').split(',');
  return { r, g, b };
};
