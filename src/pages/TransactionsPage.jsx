import React from 'react';
import { useAuth } from '../context/AuthContext';
import { formatCurrency } from '../utils/formatters';

const TransactionsPage = ({ transactions = [] }) => {
  const { user } = useAuth();
  const currency = user?.currency || 'INR';

  return (
    <div className="transactions-page p-6">
      <h1 className="text-2xl font-bold mb-4">Transactions</h1>
      <div className="bg-white shadow rounded-lg overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Amount</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {transactions.map((tx, idx) => (
              <tr key={idx}>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{tx.description}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-950">
                  {formatCurrency(tx.amount, currency)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TransactionsPage;
