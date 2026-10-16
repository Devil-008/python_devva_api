import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';

const SettingsPage = () => {
  const { user, updateProfile } = useAuth();
  const [name, setName] = useState(user?.name || '');
  const [currency, setCurrency] = useState(user?.currency || 'INR');
  const [theme, setTheme] = useState(user?.theme || 'light');
  const [loading, setLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccessMessage('');
    setErrorMessage('');

    if (!name.trim()) {
      setErrorMessage('Name cannot be empty.');
      return;
    }

    setLoading(true);
    try {
      await updateProfile({ name: name.trim(), currency, theme });
      setSuccessMessage('Profile updated successfully.');
    } catch (err) {
      setErrorMessage(err.response?.data?.error || 'Failed to update profile.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="settings-page max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">Account Settings</h1>
      {successMessage && <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">{successMessage}</div>}
      {errorMessage && <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">{errorMessage}</div>}
      
      <form onSubmit={handleSubmit} className="bg-white shadow rounded-lg p-6 space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full border border-gray-300 rounded px-3 py-2"
            maxLength={100}
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <div className="flex items-center">
            <span className="w-full bg-gray-100 border border-gray-300 rounded px-3 py-2 text-gray-600">{user?.email}</span>
            <span className="ml-2 px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded">Verified</span>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Preferred Currency</label>
          <select
            value={currency}
            onChange={(e) => setCurrency(e.target.value)}
            className="w-full border border-gray-300 rounded px-3 py-2"
          >
            <option value="INR">INR (₹)</option>
            <option value="USD">USD ($)</option>
            <option value="EUR">EUR (€)</option>
            <option value="GBP">GBP (£)</option>
            <option value="CAD">CAD ($)</option>
            <option value="AUD">AUD ($)</option>
            <option value="JPY">JPY (¥)</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Theme Preference</label>
          <select
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
            className="w-full border border-gray-300 rounded px-3 py-2"
          >
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? 'Saving Changes...' : 'Save Changes'}
        </button>
      </form>
    </div>
  );
};

export default SettingsPage;
