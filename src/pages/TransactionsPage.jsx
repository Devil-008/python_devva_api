import React, { useState, useEffect } from 'react';
import { getTransactions } from '../services/transactionService';

export const TransactionsPage = () => {
  const [data, setData] = useState({ transactions: [], pagination: {} });
  const [params, setParams] = useState({ page: 1, per_page: 10, q: '', sort_by: 'transaction_date', sort_order: 'desc' });

  useEffect(() => {
    const handler = setTimeout(async () => {
      const result = await getTransactions(params);
      setData(result);
    }, 300);
    return () => clearTimeout(handler);
  }, [params]);

  return (
    <div>
      <input placeholder="Search notes..." onChange={(e) => setParams({...params, q: e.target.value})} />
      <table>
        <thead>
          <tr>
            <th onClick={() => setParams({...params, sort_by: 'transaction_date', sort_order: params.sort_order === 'asc' ? 'desc' : 'asc'})}>Date</th>
            <th>Category</th>
            <th>Type</th>
            <th>Payment Method</th>
            <th onClick={() => setParams({...params, sort_by: 'amount', sort_order: params.sort_order === 'asc' ? 'desc' : 'asc'})}>Amount</th>
            <th>Note</th>
          </tr>
        </thead>
        <tbody>{data.transactions.map(t => <tr key={t.id}><td>{t.transaction_date}</td><td><span style={{backgroundColor: t.category_color}}>{t.category_name}</span></td><td>{t.type}</td><td>{t.payment_method}</td><td>{t.amount}</td><td>{t.note}</td></tr>)}</tbody>
      </table>
    </div>
  );
};