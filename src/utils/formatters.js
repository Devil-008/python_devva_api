export const formatCurrency = (amount, currency) => {
  const symbols = {
    'INR': '₹',
    'USD': '$',
    'EUR': '€',
    'GBP': '£',
    'CAD': '$',
    'AUD': '$',
    'JPY': '¥'
  };
  const symbol = symbols[currency] || '₹';
  return `${symbol}${amount.toLocaleString()}`;
};