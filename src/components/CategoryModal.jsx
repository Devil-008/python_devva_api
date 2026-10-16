import React, { useState } from 'react';

export const CategoryModal = ({ isOpen, category, onClose, onSave }) => {
  const [name, setName] = useState(category?.name || '');
  const [type, setType] = useState(category?.type || 'expense');
  const [color, setColor] = useState(category?.color || '#3B82F6');

  if (!isOpen) return null;

  return (
    <div className="modal">
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Category Name" />
      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>
      <button onClick={() => onSave({ name, type, color })}>Save</button>
      <button onClick={onClose}>Cancel</button>
    </div>
  );
};