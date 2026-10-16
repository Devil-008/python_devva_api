# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.

## Changelog & Recent Updates

### EXP-104 - User Profile & Currency Preference Management

```
### User Story
> **As a** registered user,  
> **I want to** update my profile details (name, preferred currency, and theme preference) from the Settings page,  
> **So that** my transaction records and dashboard financial metrics display using my preferred currency formatting across the entire app.

### Background / Context
- **Backend Gap**: The `User` database model (`app/models/user.py`) stores `currency` (default: `'INR'`) and `theme` (default: `'light'`), but lacks an API route to update these preferences. `app/routes/auth.py` only handles registration, login, logout, password change

**Acceptance Criteria:**
AC 1 (Update Profile Details)**: Given an authenticated user on `/settings`, when they modify their name or currency and click "Save Changes", then the backend persists the update via `PUT /api/v1/auth/profile` and a success banner is displayed.
  AC 2 (Validation & Error Handling)**: Given an empty name or unsupported currency code, when the user submits, then the backend rejects the request with

## Changelog & Recent Updates

### EXP-104 - User Profile & Currency Preference Management

```
### User Story
> **As a** registered user,  
> **I want to** update my profile details (name, preferred currency, and theme preference) from the Settings page,  
> **So that** my transaction records and dashboard financial metrics display using my preferred currency formatting across the entire app.

### Background / Context
- **Backend Gap**: The `User` database model (`app/models/user.py`) stores `currency` (default: `'INR'`) and `theme` (default: `'light'`), but lacks an API route to update these preferences. `app/routes/auth.py` only handles registration, login, logout, password change

**Acceptance Criteria:**
AC 1 (Update Profile Details)**: Given an authenticated user on `/settings`, when they modify their name or currency and click "Save Changes", then the backend persists the update via `PUT /api/v1/auth/profile` and a success banner is displayed.
  AC 2 (Validation & Error Handling)**: Given an empty name or unsupported currency code, when the user submits, then the backend rejects the request with

## Changelog & Recent Updates

### EXP-104 - User Profile & Currency Preference Management

```
### User Story
> **As a** registered user,  
> **I want to** update my profile details (name, preferred currency, and theme preference) from the Settings page,  
> **So that** my transaction records and dashboard financial metrics display using my preferred currency formatting across the entire app.

### Background / Context
- **Backend Gap**: The `User` database model (`app/models/user.py`) stores `currency` (default: `'INR'`) and `theme` (default: `'light'`), but lacks an API route to update these preferences. `app/routes/auth.py` only handles registration, login, logout, password change

**Acceptance Criteria:**
AC 1 (Update Profile Details)**: Given an authenticated user on `/settings`, when they modify their name or currency and click "Save Changes", then the backend persists the update via `PUT /api/v1/auth/profile` and a success banner is displayed.
  AC 2 (Validation & Error Handling)**: Given an empty name or unsupported currency code, when the user submits, then the backend rejects the request with
