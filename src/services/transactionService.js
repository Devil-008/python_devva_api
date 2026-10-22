export const getTransactions = async (params) => {
  const queryString = new URLSearchParams(params).toString();
  const response = await fetch(`/api/v1/transactions?${queryString}`);
  if (!response.ok) throw new Error('Failed to fetch');
  return await response.json();
};