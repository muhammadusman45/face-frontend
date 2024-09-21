import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { PrimeReactProvider } from "primereact/api";
import "primereact/resources/themes/lara-light-cyan/theme.css";
// import "primereact/resources/themes/lara-light-indigo/theme.css";
// import 'primereact/resources/themes/bootstrap4-dark-blue/theme.css';
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <PrimeReactProvider >
      <App />
    </PrimeReactProvider>
  </React.StrictMode>
);
