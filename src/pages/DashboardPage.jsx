import React from 'react';
import { useAuth } from '../context/AuthContext';
import { formatCurrency } from '../utils/formatters';

const DashboardPage = ({ metrics = { total: 0 } }) => {
  const { user } = useAuth();
  const currency = user?.currency || 'INR';

  return (
    <div className="dashboard-page p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-sm font-medium text-gray-500">Total Balance</h2>
        <p className="text-3xl font-bold text-gray-900 mt-2">
          {formatCurrency(metrics.total, currency)}
        </p>
      </div>
    </div>
  );
};

export default DashboardPage;
